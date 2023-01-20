

class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    def __repr__(self):
        return self._name + ", has a salary of $" + str(self._salary)


class Manager(Employee):
    def __init__(self, name, salary, manager):
        super().__init__(name, salary)
        self._manager = manager
    def __repr__(self):
        return self._name + ", has a salary of $" + str(self._salary) + \
                ", and is an " + self._manager + " manager"


class Executive(Employee):
    def __init__(self, name, salary, executive):
        super().__init__(name, salary)
        self._executive = executive
    def __repr__(self):
        return self._name + ", has a salary of $" + str(self._salary) + \
                ", and is a " + self._executive + " executive"