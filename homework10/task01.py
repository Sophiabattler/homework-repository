import asyncio
import json
import operator
from datetime import datetime
from functools import reduce

import aiohttp
import requests
from bs4 import BeautifulSoup


class Company:
    def __init__(self):
        self._code = None
        self._name = None
        self._price = None
        self._p_e = None
        self._growth = None
        self._potential_profit = None

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def p_e(self):
        return self._p_e

    @p_e.setter
    def p_e(self, p_e):
        self._p_e = p_e

    @property
    def growth(self):
        return self._growth

    @growth.setter
    def growth(self, growth):
        self._growth = growth

    @property
    def potential_profit(self):
        return self._potential_profit

    @potential_profit.setter
    def potential_profit(self, potential_profit):
        self._potential_profit = potential_profit


all_companies = []

base_source_url = "https://markets.businessinsider.com{}"
c_b_url = "http://www.cbr.ru/scripts/XML_daily.asp?date_req={}"
s_and_p_url = "https://markets.businessinsider.com/index/components/s&p_500?p={}"


async def get_site_content(link):
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as response:
            text = await response.text()
            soup = BeautifulSoup(text, "html.parser")
    return soup


def dollar_rate():
    today_datetime = datetime.today().strftime("%d/%m/%Y")
    response = requests.get(c_b_url.format(today_datetime)).text
    soup = BeautifulSoup(response, "html.parser")
    rate = float(soup.find(id="R01235").value.text.replace(",", "."))
    return rate


async def main():

    # итерация по 10 стр
    for num_page in range(1, 11):
        companies_from_one_page = []
        main_page_soup = await get_site_content(s_and_p_url.format(num_page))
        table_body = main_page_soup.find("tbody", class_="table__tbody")
        table_rows = table_body.findAll("tr")

        # iteration through pages
        for row in table_rows:
            company = Company()
            # find company name
            header_column = row.find("td", class_="table__td table__td--big")
            company.name = header_column.find("a").contents[0]
            # find company growth
            all_columns = row.findAll("td", class_="table__td")
            growth_column = all_columns[-1]
            company.growth = float(growth_column.findAll("span")[-1].text[:-1])
            # find company price
            price_dollars = float(all_columns[1].contents[0].strip().replace(",", ""))
            company.price = round(price_dollars * dollar_rate(), 2)
            # go to the company page
            company_url = base_source_url.format(header_column.find("a").attrs["href"])
            # find company code, potential profit and p/e
            company_soup = await get_site_content(company_url)
            company_code_elements = company_soup.find(
                "span", class_="price-section__category"
            )
            company.code = (
                company_code_elements.find("span").contents[0].replace(",", "")
            )
            high = company_soup.find(string="52 Week High")
            week_high = (
                float(high.previous.previous.strip().replace(",", "")) if high else 0
            )
            low = company_soup.find(string="52 Week Low")
            week_low = (
                float(low.previous.previous.strip().replace(",", "")) if low else 0
            )
            company.potential_profit = (
                round((week_high - week_low) / week_low * 100, 3)
                if week_low and week_high
                else 0.0
            )
            p_e = company_soup.find_all(string="P/E Ratio")
            if len(p_e) > 1:
                company.p_e = float(p_e[1].previous.previous.strip().replace(",", ""))
            else:
                company.p_e = float("inf")

            companies_from_one_page.append(company)

        all_companies.append(companies_from_one_page)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
companies_glued_into_one_list = reduce(operator.concat, all_companies)


def top_10_high_price():
    """top 10 companies by highest price"""
    top = sorted(
        companies_glued_into_one_list, key=lambda company: company.price, reverse=True
    )[:11]
    return [
        {"code": company.code, "name": company.name, "price": company.price}
        for company in top
    ]


def top_10_low_p_e():
    """top 10 companies by lowest P/E"""
    top = sorted(companies_glued_into_one_list, key=lambda company: company.p_e)[:11]
    return [
        {"code": company.code, "name": company.name, "p/e": company.p_e}
        for company in top
    ]


def top_10_big_growth():
    """top 10 companies by biggest growth"""
    top = sorted(
        companies_glued_into_one_list, key=lambda company: company.growth, reverse=True
    )[:11]
    return [
        {
            "code": company.code,
            "name": company.name,
            "growth": "{}%".format(company.growth),
        }
        for company in top
    ]


def top_10_high_profit():
    """top 10 companies by highest profit"""
    top = sorted(
        companies_glued_into_one_list,
        key=lambda company: company.potential_profit,
        reverse=True,
    )[:11]
    return [
        {
            "code": company.code,
            "name": company.name,
            "potential_profit": "{}%".format(company.potential_profit),
        }
        for company in top
    ]


jsonData = json.dumps(top_10_high_price())
jsonData2 = json.dumps(top_10_low_p_e())
jsonData3 = json.dumps(top_10_big_growth())
jsonData4 = json.dumps(top_10_high_profit())


with open("most_expensive_shares.json", "w") as file:
    file.write(jsonData)

with open("lowest_p_e.json", "w") as file:
    file.write(jsonData2)

with open("highest_growth.json", "w") as file:
    file.write(jsonData3)

with open("most_profit.json", "w") as file:
    file.write(jsonData4)
