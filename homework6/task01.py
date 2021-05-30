"""Task01 - Count instances"""


def instances_counter(cls):
    """Function which counts created instances
    or resets counter for class"""

    class CountInstances(cls):
        """Class which counts created instances
        or resets counter for another class"""

        if "count_inst" not in cls.__dict__:
            count_inst = 0

        def __init__(self, *args, **kwargs):
            """Counts created instances of the class-parent"""
            super().__init__(*args, **kwargs)
            self.__class__.count_inst += 1

        @classmethod
        def get_created_instances(cls):
            """Returns counter created instances of the class-parent"""
            return cls.count_inst

        @classmethod
        def reset_instances_counter(cls):
            """Resets counter created instances of the class-parent"""
            last_counter, cls.count_inst = cls.count_inst, 0
            return last_counter

    return CountInstances


@instances_counter
class User:
    pass


if __name__ == "__main__":
    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    print(User.get_created_instances())  # 3
    print(User.reset_instances_counter())  # 3
    print(User.get_created_instances())  # 0
