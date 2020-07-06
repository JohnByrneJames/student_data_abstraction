# Abstraction

#### A concept related to the object oriented approach of programming.

Abstraction is another concept of OOP wherein the user is kept unaware of basic implementation of a function. <br>
property. The user is only able to view basic functionality whereas the internal details are hidden. <br>
The aim is to allow the user to know what they are doing but not how the work is being done. <br>
So for example, in an ATM the user just wants to access their money and carry out whatever they need to do, they do not care how the money is actually
counted or how much money is in the machine. They are free to use the object has a whole.

[**devops_student**](devops_student.py) **[Parent/ Base Class]** 
* **Attributes**
    * current_grade `private`
    * current_trainer `public`
* **Methods**
    * print `public`
    * print_details `abstract method`
    * change_current_grade `private` 

[**student_data**](student_data.py) **[Child/ Derived Class]**
* **Methods**
    * public_method `public`
    * private_method `private`

Some would say that Abstraction is very similar to Encapsulation, however there is one major difference :
* **Encapsulation** = Information hiding
* **Abstraction** = Implementation hiding

A common way to handle the complexity of a object is through something known as hierarchical abstraction.

A class that contains a abstract method is not allowed to made into an instance. It will raise
a TypeError: Can't instantiate abstract class AbsClass with the abstract method task. Here we actually inherit from
the ABC class, this allows us to set the base abstract class in our example which is the student_data class.

```python
John = DevOpsStudent(70, "Sharukh")
John.print_details()
John.print(100)

print(isinstance(John, StudentData))
```

Although we initialised the instance "John" through the DevOpsStudent class it is actually an instance of
the abstract class StudentData, this means that you cannot directly create an instance of StudentData instead you
must create an abstraction class in this case DevOpsStudent and that way you can access its functionality, without
knowing exactly how it is done. In this case how it gets the value we pass into print.