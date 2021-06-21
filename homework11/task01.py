"""Task01 - Metaclass"""


class SimplifiedEnum(type):
    """Metaclass removes duplications in variables declarations
    by setting them in '__keys'-attribute of class-inheritor"""

    def __new__(cls, name, bases, dct):
        cls_instance = super().__new__(cls, name, bases, dct)
        my_class = "_" + name + "__keys"
        for i in dct.get(my_class, []):
            setattr(cls, i, i)
        return cls_instance
