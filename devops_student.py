from student_data import StudentData

class DevOpsStudent(StudentData):  # subclass to StudentData
    def __init__(self, current_grade, current_trainer):
        # super().__init__ is taking all the members of the parent class
        super().__init__(current_grade, current_trainer)
        self.__current_grade = current_grade  # Private attribute
        self.current_trainer = current_trainer  # Public attribute

    def print_details(self):  # overridden method of abstractmethod from StudentData class
        return "We are inside the DevOpsStudent Print_details"


# object of test class created
John = DevOpsStudent(70, "Sharukh")
John.print_details()
John.print(100)
# It is in fact an instance of the studentData class and not the class it was instantiated from
print(isinstance(John, StudentData))


# This will throw a error because the task method inside the StudentData class is an abstract method and cannot
# be made into a instance. It raises a TypeError: Can't instantiate abstract class StudentData with abstract methods
# print_details
# >>> Alice = StudentData()
# >>> Alice.print_details()

