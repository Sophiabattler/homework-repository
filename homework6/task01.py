"""Task01 - Count instances"""


def instances_counter(cls):
    """Function which counts created instances
    or resets counter for class"""

    class CountInstances(cls):
        """Class which counts created instances
        or resets counter for another class"""

        if not hasattr(cls, "count_inst"):
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
