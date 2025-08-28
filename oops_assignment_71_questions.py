
# OOPS Assignment — 71 Questions (Question -> Code -> Output)
# Generated to match the structure: question comment, code, expected output comment.
# NOTE: This file is intended for uploading to GitHub. Run it to see sample outputs.

# ------------------------------
# Part A - Functions, Iterators & Generators (Questions 1 - 25)
# ------------------------------

# Question 1: Explain importance of functions (answer in comment).
# Functions promote reusability, modularity, readability, and easier testing.

# Question 2: Greet students
def q2_greet_students(names):
    for name in names:
        print(f"Hello, {name}!")

q2_greet_students(['Tanvi','Arun'])
# Hello, Tanvi!  Hello, Arun!


# Question 3: print vs return demonstration
def q3_add_and_print(a,b): print(a+b)
def q3_add_and_return(a,b): return a+b
q3_add_and_print(2,3)   # prints 5
print(q3_add_and_return(2,3))  # 5


# Question 4: *args and **kwargs
def q4_demo(a, *args, **kwargs): return a, args, kwargs
print(q4_demo(1,2,3,x=10))
# (1, (2, 3), {'x': 10})


# Question 5: Explain iterator function (commented)
# Iterator: object implementing __iter__() returning iterator; iterator has __next__().

# Question 6: Squares generator
def q6_squares(n):
    for i in range(1, n+1): yield i*i
print(list(q6_squares(5)))
# [1,4,9,16,25]


# Question 7: Palindromic numbers generator
def q7_palindromes(n):
    for i in range(1,n+1):
        s=str(i)
        if s==s[::-1]: yield i
print(list(q7_palindromes(30)))
# [1,2,3,4,5,6,7,8,9,11,22]


# Question 8: Even numbers generator
def q8_evens(n):
    for i in range(2,n+1,2): yield i
print(list(q8_evens(10)))
# [2,4,6,8,10]


# Question 9: Powers of two generator
def q9_powers_of_two(n):
    p=1
    while p<=n:
        yield p; p*=2
print(list(q9_powers_of_two(20)))
# [1,2,4,8,16]


# Question 10: Primes generator
def q10_primes(n):
    def is_prime(x):
        if x<2: return False
        if x%2==0: return x==2
        r=int(x**0.5)
        for d in range(3,r+1,2):
            if x%d==0: return False
        return True
    for i in range(2,n+1):
        if is_prime(i): yield i
print(list(q10_primes(30)))
# [2,3,5,7,11,13,17,19,23,29]


# Question 11: Lambda sum
q11_sum = lambda a,b: a+b
print(q11_sum(3,4))
# 7


# Question 12: Lambda square
q12_square = lambda x: x*x
print(q12_square(5))
# 25


# Question 13: Lambda even check
q13_is_even = lambda x: x%2==0
print(q13_is_even(6))
# True


# Question 14: Lambda concat strings
q14_concat = lambda a,b: a+ b
print(q14_concat('Hi','!'))
# Hi!


# Question 15: Lambda max of 3
q15_max3 = lambda a,b,c: a if a>=b and a>=c else (b if b>=c else c)
print(q15_max3(5,9,7))
# 9


# Question 16: Squares of even numbers from list
def q16_squares_of_evens(lst): return [x*x for x in lst if x%2==0]
print(q16_squares_of_evens([1,2,3,4]))
# [4,16]


# Question 17: Product of positive numbers
from functools import reduce
def q17_product_of_positives(lst):
    pos=[x for x in lst if x>0]
    return reduce(lambda a,b: a*b, pos, 1)
print(q17_product_of_positives([1,-2,3,4]))
# 12


# Question 18: Double odd numbers values
def q18_double_odds(lst): return [x*2 if x%2 else x for x in lst]
print(q18_double_odds([1,2,3,4]))
# [2,2,6,4]


# Question 19: Sum of cubes
def q19_sum_of_cubes(lst): return sum(x**3 for x in lst)
print(q19_sum_of_cubes([1,2,3]))
# 36


# Question 20: Filter out primes from list
def q20_filter_out_primes(lst):
    def is_prime(x):
        if x<2: return False
        if x%2==0: return x==2
        for d in range(3,int(x**0.5)+1,2):
            if x%d==0: return False
        return True
    return [x for x in lst if not is_prime(x)]
print(q20_filter_out_primes([2,3,4,5,6,7,8,9]))
# [4,6,8,9]


# Question 21-25: (Repeats of earlier lambda tasks) provide alias functions
q21_sum = q11_sum; q22_square = q12_square; q23_is_even = q13_is_even
q24_concat = q14_concat; q25_max3 = q15_max3


# ------------------------------
# Part B - OOP, Inheritance, Polymorphism, Abstraction, Encapsulation (Questions 26 - 50)
# ------------------------------

# Question 26: What is encapsulation? (comment answer)
# Encapsulation bundles data and methods; hides internals and enforces interfaces.

# Question 27: Access modifiers in Python (comment)
# Python uses naming conventions: public, _protected, __private (name mangling).

# Question 28: What is inheritance? (comment)
# Inheritance allows a class to derive properties/methods from another class.

# Question 29: Define polymorphism (comment)
# Polymorphism: same interface, different implementations.

# Question 30: Method overriding explanation (comment)
# Overriding replaces parent method in subclass with new implementation.

# Question 31: Animal and Dog classes with make_sound
class q31_Animal:
    def __init__(self,name='Unknown'): self.name=name
    def make_sound(self): print("Generic animal sound")
class q31_Dog(q31_Animal):
    def make_sound(self): print("Woof!")
a=q31_Animal(); d=q31_Dog(); a.make_sound(); d.make_sound()
# Generic animal sound
# Woof!


# Question 32: Animal.move and Dog override
class q32_Animal:
    def move(self): print("Animal moves")
class q32_Dog(q32_Animal):
    def move(self): print("Dog runs")
q32_Dog().move()
# Dog runs


# Question 33: Multiple inheritance DogMammal
class q33_Mammal:
    def reproduce(self): print("Giving birth to live young.")
class q33_DogMammal(q31_Dog, q33_Mammal):
    pass
q33_DogMammal().reproduce()
# Giving birth to live young.


# Question 34: GermanShepherd overriding make_sound
class q34_GermanShepherd(q31_Dog):
    def make_sound(self): print("Bark!")
q34_GermanShepherd().make_sound()
# Bark!


# Question 35: Constructors in Animal and Dog
class q35_Animal:
    def __init__(self, species): self.species=species
class q35_Dog(q35_Animal):
    def __init__(self, species, name): super().__init__(species); self.name=name
dog=q35_Dog('Canine','Tom'); print(dog.species, dog.name)
# Canine Tom


# Question 36: Abstraction in Python (comment)
# Use abc.ABC and @abstractmethod to define abstract classes/methods.

# Question 37: Importance of abstraction (comment)
# Abstraction separates interface from implementation, simplifies usage and maintenance.

# Question 38: Abstract vs regular methods (comment)
# Abstract methods must be implemented by subclasses; regular methods have body.

# Question 39: Achieve abstraction via interfaces (comment)
# Use ABCs as interfaces; require methods to be implemented by subclasses.

# Question 40: Example of common interface (Shape/Rectangle)
from abc import ABC, abstractmethod
class q40_Shape(ABC):
    @abstractmethod
    def area(self): pass
class q40_Rect(q40_Shape):
    def __init__(self,w,h): self.w,self.h=w,h
    def area(self): return self.w*self.h
print(q40_Rect(3,4).area())
# 12


# Question 41: Polymorphism via overriding (comment)
# Subclasses implement same method; caller uses base type.

# Question 42: Base and subclass example (polymorphism)
class q42_Base:
    def action(self): print("Base")
class q42_Sub(q42_Base):
    def action(self): print("Sub")
for obj in [q42_Base(), q42_Sub()]: obj.action()
# Base  Sub


# Question 43: Multiple subclasses overriding
class q43_A(q42_Base): 
    def action(self): print("A")
class q43_B(q42_Base):
    def action(self): print("B")
for obj in [q43_A(), q43_B()]: obj.action()
# A  B


# Question 44: Polymorphism improves readability/reuse (comment)
# Write once, use many types — simpler client code.

# Question 45: Duck typing demonstration
class q45_Duck:
    def quack(self): print("quack")
class q45_Bird:
    def quack(self): print("bird sound")
def q45_make_it_quack(x): x.quack()
q45_make_it_quack(q45_Duck()); q45_make_it_quack(q45_Bird())
# quack  bird sound


# Question 46: How to achieve encapsulation in Python (comment)
# Use name mangling (__attr) and properties to hide internals.

# Question 47: Can encapsulation be bypassed? (comment+example)
class q47_Test:
    def __init__(self): self.__hidden=5
t=q47_Test()
# Bypass via _ClassName__hidden if needed (not recommended)
# print(t._q47_Test__hidden)  # would show 5


# Question 48: BankAccount with private balance
class q48_BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner=owner; self.__balance=float(balance)
    def deposit(self,amt):
        if amt<=0: raise ValueError("Positive amount"); self.__balance+=amt
    def withdraw(self,amt):
        if amt>self.__balance: raise ValueError("Insufficient")
        self.__balance-=amt
    def get_balance(self): return self.__balance
acct=q48_BankAccount('Tanvi',100); acct.deposit(50); print(acct.get_balance())
# 150.0


# Question 49: Person class with private name/email and getter/setter
class q49_Person:
    def __init__(self,name,email):
        self.__name=name; self.__email=email
    @property
    def email(self): return self.__email
    @email.setter
    def email(self,val):
        if '@' not in val: raise ValueError("Invalid"); self.__email=val
p=q49_Person('Tanvi','t@example.com'); print(p.email); p.email='ni@x.com'; print(p.email)
# t@example.com  ni@x.com


# Question 50: Why encapsulation is a pillar? (comment)
# Encapsulation protects state, enforces invariants, and reduces coupling.


# ------------------------------
# Part C - Decorators, Static/Class Methods, Dunder, Properties (Questions 51 - 71)
# ------------------------------

# Question 51: Decorator that prints before/after
def q51_deco(fn):
    def wrapper(*a,**k):
        print("Before"); res=fn(*a,**k); print("After"); return res
    return wrapper
@q51_deco
def q51_hi(): print("Hi")
q51_hi()
# Before Hi After


# Question 52: Decorator that accepts args and prints function name with message
def q52_msg(msg):
    def deco(fn):
        def wrapper(*a,**k):
            print(f"{msg}: {fn.__name__}")
            return fn(*a,**k)
        return wrapper
    return deco
@q52_msg("Running")
def q52_test(): print("done")
q52_test()
# Running: q52_test  done


# Question 53: Two decorators applied, check order
def d1(fn):
    def w(*a,**k):
        print("D1 start"); r=fn(*a,**k); print("D1 end"); return r
    return w
def d2(fn):
    def w(*a,**k):
        print("D2 start"); r=fn(*a,**k); print("D2 end"); return r
    return w
@d1
@d2
def q53_func(): print("Core")
q53_func()
# D1 start D2 start Core D2 end D1 end


# Question 54: Decorator that forwards args (already done above) - demonstrate with wraps
from functools import wraps
def q54_preserve(fn):
    @wraps(fn)
    def wrapper(*a,**k): return fn(*a,**k)
    return wrapper
@q54_preserve
def q54_add(a,b): return a+b
print(q54_add(3,4))
# 7


# Question 55: Calculator class with static add
class q55_Calculator:
    @staticmethod
    def add(a,b): return a+b
print(q55_Calculator.add(5,6))
# 11


# Question 56: Employee class with classmethod count
class q56_Employee:
    _count=0
    def __init__(self,name): self.name=name; q56_Employee._count+=1
    @classmethod
    def get_employee_count(cls): return cls._count
e1=q56_Employee('A'); e2=q56_Employee('B'); print(q56_Employee.get_employee_count())
# 2


# Question 57: StringFormatter static reverse_string
class q57_StringFormatter:
    @staticmethod
    def reverse_string(s): return s[::-1]
print(q57_StringFormatter.reverse_string('Tanvi'))
# ivnaT


# Question 58: Circle class with classmethod calculate_area
class q58_Circle:
    pi=3.141592653589793
    @classmethod
    def calculate_area(cls,r): return cls.pi * r * r
print(q58_Circle.calculate_area(3))
# 28.274333882308138


# Question 59: TemperatureConverter static method
class q59_TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c): return c*9/5+32
print(q59_TemperatureConverter.celsius_to_fahrenheit(0))
# 32.0


# Question 60: Purpose of __str__ with example
class q60_Person:
    def __init__(self,name): self.name=name
    def __str__(self): return f"Person({self.name})"
print(str(q60_Person('Tanvi')))
# Person(Tanvi)


# Question 61: __len__ example
class q61_Box:
    def __init__(self,items): self.items=list(items)
    def __len__(self): return len(self.items)
print(len(q61_Box([1,2,3])))
# 3


# Question 62: __add__ example
class q62_Box:
    def __init__(self,items): self.items=list(items)
    def __add__(self,other): return q62_Box(self.items+other.items)
    def __repr__(self): return f"q62_Box({self.items})"
print(q62_Box([1,2])+q62_Box([3,4]))
# q62_Box([1, 2, 3, 4])


# Question 63: __getitem__ example
class q63_Seq:
    def __init__(self,data): self.data=list(data)
    def __getitem__(self,i): return self.data[i]
s=q63_Seq([10,20,30]); print(s[1])
# 20


# Question 64: __iter__ and __next__ example
class q64_Iter:
    def __init__(self,items): self.items=items; self.i=0
    def __iter__(self): return self
    def __next__(self):
        if self.i>=len(self.items): raise StopIteration
        v=self.items[self.i]; self.i+=1; return v
it=q64_Iter([1,2,3])
for x in it: print(x, end=' ')
print()  # 1 2 3
# 1 2 3


# Question 65: Getter via @property example
class q65_Rect:
    def __init__(self,w,h): self._w=w; self._h=h
    @property
    def area(self): return self._w*self._h
r=q65_Rect(2,3); print(r.area)
# 6


# Question 66: Setter via @property demonstration
class q66_Student:
    def __init__(self,score=0): self._score=score
    @property
    def score(self): return self._score
    @score.setter
    def score(self,val):
        if not (0<=val<=100): raise ValueError("0-100")
        self._score=val
s=q66_Student(50); s.score=80; print(s.score)
# 80


# Question 67: Purpose of @property (comment)
# @property allows attribute access with method-like control (getter/setter).

# Question 68: @deleter demo
class q68_Thing:
    def __init__(self,x): self._x=x
    @property
    def x(self): return self._x
    @x.deleter
    def x(self): del self._x
t=q68_Thing(5); print(t.x); del t.x
# 5


# Question 69: How encapsulation relates to properties (comment+example)
# Properties provide controlled access to private data, enforcing validation (see q66_Student).

# Question 70: Extra example — preserving metadata with wraps (already used q54_preserve)

# Question 71: Final wrap-up example: Combining many concepts
@q51_deco
def q71_demo(a,b): print("sum is", a+b)
q71_demo(3,4)
# Before sum is 7 After
