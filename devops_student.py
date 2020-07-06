from student_data import StudentData

class DevOpsStudent(StudentData):  # subclass to StudentData
    def __init__(self, current_grade, current_trainer):
        # super().__init__ is taking all the members of the parent class
        super().__init__(current_grade, current_trainer)
        self.__current_grade = current_grade  # Private attribute
        self.current_trainer = current_trainer  # Public attribute

    def public_method(self):  # public method
        return "This method is public, welcome!!"

    def __private_method(self):  # private method
        return "This method is private! I love cake! How are you seeing this?!"
