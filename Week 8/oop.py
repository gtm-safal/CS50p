# def main():
#     student = get_student()
#     print(f"\nName: {student[0]}\nHome: {student[1]}")

# def get_student():
#     name = input("Name: ").strip().capitalize()
#     house = input("House: ").strip().capitalize()
#     return name, house  # Returns Tuple

class Students():
    def __init__ (self, n, h):
        try:
            if not n:
                raise ValueError
        except ValueError:
            student = get_student()
            n = student.name

        self.name = n
        self.house = h

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if not house:
            raise ValueError
        self._house = house

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError
        self._name = name

def main():
    student = get_student()
    print(student)
    print(type(student))

def get_student():
    name = input("Name: ").strip().capitalize()
    house = input("House: ").strip().capitalize()
    student = Students(name, house)
    print(type(student))

    return student


if __name__ == "__main__":
    main()


# class Students:

#     def __init__(self):
#         self.name = input("Name: ").strip()
#         self.marks1 = int(input("Marks1: "))
#         self.marks2 = int(input("Marks2: "))
#         self.marks3 = int(input("Marks3: "))
#     @property
#     def per(self):
#         return str(round((self.marks1 + self.marks2 + self.marks3) / 3, 2)) + "%"

# s1 = Students()
# print("Percentage:", s1.per)

# class Account:

#     def __init__(self, balance, acc):
#         self.balance = balance
#         self.acc = acc
#         print(f'{self} acc created successfully')

#     def debit(self, amt):
#         self.balance -= amt
#         print("Remaining Balance:", self.balance)

#     def credit(self, amt):
#         self.balance += amt
#         print("Remaining Balance:", self.balance)

#     def balance(self):
#         print("Balance:", self.balance)

# class Safal(Account):
#     ...

# me = Safal(10000, 12345)
# safal = Account(10000, '0x001')
# safal.debit(.01)
# safal.credit(99)

# class Animal:
#     def __init__(self, origin):
#         self.origin = origin

# class Human(Animal):
#     def __init__(self, name, origin):
#         self.name = name
#         super().__init__(origin)

# nepali = Human("Safal","Nepal")

# print(nepali.name, nepali.origin)

# class Complex:

#     def __init__(self, real, image):
#         self.real = real
#         self.image = image

#     def show(self):
#         return f"{self.real} + {self.image} i"

#     def __add__(self, num):
#         newReal = self.real + num.real
#         newImage = self.image + num.image
#         return Complex(newReal,newImage)

#     def __sub__(self, num):
#         newReal = self.real - num.real
#         newImage = self.image - num.image
#         return Complex(newReal, newImage)

#     def __str__(self):
#         return self.show()


# num1 = Complex(1, 3)
# print(num1)

# num2 = Complex(5, 6)
# print(num2)

# num3 = num1 + num2 #-->num3 = num1.__add__(num2)
# print(num3)

# num4 = num1 - num2
# print(num4)

# PI = 22/7
# class Circle:

#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return round(PI*self.radius**2, 2)

#     def perimeter(self):
#         return round(2*PI*self.radius, 2)

# circle1=Circle(5)
# print(circle1.area())
# print(circle1.perimeter())

# class Employee:
#     def __init__(self, department, role, salary):
#         self.department = department
#         self.role = role
#         self.salary = salary

#     def showDetails(self):
#         print(f"Department: {self.department}\nRole: {self.role}\nSalary: {self.salary:,}")


# class Engineer (Employee):

#     def __init__(self, name, age, depart, role, sal):
#         self.name = name
#         self.age = age
#         super().__init__(depart, role, sal)

#     def showDetails(self):
#         print(f"\nName: {self.name}\nAge: {self.age}")
#         super().showDetails()

# e1 = Engineer('Safal', 19, 'IT', 'AI', 1000000)
# e1.showDetails()


# class Order():

#     def __init__(self, item, price):
#         self.item = item
#         self.price = price

#     def __gt__(self, obj):
#         return self.price > obj.price


# o1 = Order('MO:MO', 50)
# o2 = Order('laphing', 70)

# if o1 > o2 :
#     print(o1.item, "is costier")

# else:
#     print(o2.item, "is costier")
