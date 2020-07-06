from abc import ABC, abstractmethod  # abstract helper class

class StudentData(ABC):  # subclass of ABC - this assigns StudentData as the abstract base class
    __current_grade = None  # This is a private attribute
    current_trainer = None

    def __init__(self, __current_grade, current_trainer):
        self.__current_grade = __current_grade
        self.current_trainer = current_trainer

    # normal method
    def print(self, x):
        print("Pass value : ", x)

    @abstractmethod  # An abstractmethod deceleration
    def print_details(self):
        return "We are inside the StudentData Print_details"

    def __change_current_grade(self):  # This is a private method
        new_grade = int(input("What grade have you achieved now [0 - 100]: "))
        print(new_grade.__str__() + " is your new grade.")
        __current_grade = new_grade

