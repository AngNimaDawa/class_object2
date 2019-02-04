# #define class and create object
# class car:
# 	pass

# # #callable(car)
# c =  car()
# # print(c)
# # print(dir(c))
# # #all user defined class are instance of meta-class
# # print(isinstance(car,type)) #here type is metaclass and car is user defined class
# # print(isinstance(c,car)) #here c is instance of car
# b = car #here b is alias of
# d = b()
# print(b)
# print(d)
# e = d 
# print(e)

# # every user defined class is instance of meta-class 'type'
# class Car:
# 	pass

# class Bike:
# 	pass

# c = Car()
# print(isinstance(c, Car)) #true
# print(isinstance(c, Bike)) #false

# #add object attribute
# import sys 
# class Car:
#  	pass

# c = Car()
# print(c.__dict__)
# print(sys.getsizeof(c.__dict__))
# c.brand = 'honda'
# c.seat = [] #add list object in attribute of c
# c.name = 'ef30'
# c.type = 'petrol'
# c.color = 'white'
# print(c.__dict__)
# sys.getsizeof(c.__dict__)

# #add same attribute in different object ->brand in instance of car
# class Car:
# 	pass

# h = Car()
# h.brand = 'Honda' #setitem
# print(h.brand) #getitem
# y = Car()
# y.brand = 'Yahama'
# print(y.brand)
# print(y.__dict__,h.__dict__)


# #object initilization with init method
# class Car:
# 	def __init__(obj, value): #here init is not a constructor, its object initilizer
# 		obj.brand = value
# h = Car('Honda')	 
# y = Car('Yahama')
# print(h.brand, y.brand)


# #object initilization with init method
# class Car:
# 	def __init__(self, brand, color): #here init is not a constructor, its object initilizer
# 		self.brand = brand
# 		self.color = color
# h = Car('Honda', 'Red')	 
# y = Car('Yahama', 'white')
# print(h.brand, y.brand)
# print(h.color, y.color)

# class Car:
# 	def __init__(self, brand, model):
# 		self.brand = brand
# 		self.model = model
# 		self.status = False

# 	#user defined instance method
# 	def start(self): #always first attribute is instance itself
# 		self.status = True

# 	def stop(self): #always first attribute is instance itself
# 		self.status = False


# h = Car('Honda','m2o')
# y = Car('Yahama','e40')
# print('y:',y.__dict__)	
# print('h:',h.__dict__)	
# h.start()
# print('y:',y.__dict__)	
# print('h:',h.__dict__)
# h.stop()
# print('y:',y.__dict__)	
# print('h:',h.__dict__)

# from datetime import date
# dob = date(1997, 2, 3)
# print(dob)
# print(date.today())
# print(date.today() - dob)

# from datetime import date
# dob = date(1997, 2, 3)
# dob
# today = date.today()
# y = today.year - dob.year
# m = today.month - dob.month
# print(y, m)

# from datetime import date
# dob = date(1997, 6, 4)
# dob
# today = date.today()
# y = today.year - dob.year
# if today.month<dob.month:
# 	y -= 1
# 	m = today.month+ 12 - dob.month
# print(y,m)


# class AgeCalculator:
# 	def __init__(self, year, month, day):
# 		self.year = year
# 		self.month = month
# 		self.day = day

# 	def calculate(self):
# 		today = date.today()
# 		dob = date(self.year, self.month, self.day)
# 		age_delta = date.today() - dob

# #implement logic


# 		year, month, days = 27,11,24
# 		return(year, month, days)	


# yurika = AgeCalculator('1997','2','3')
# print(yurika.year, yurika.month, yurika.day)
# yurika.get_age()


# class Car:
# 	"""this is car class representing real word object
# 	c = Car('Honda')
# 	c.start()
# 	"""
# 	counter = 0
# 	def __init__(self, name, model=2018):
# 		self.name =name
# 		self.model =model
# 		self.status = 'stop'
# 		Car.counter += 1

# 	def start(self):
# 		"""change status of car object to start"""
# 		self.status = 'start'

# 	def stop(self):
# 		"""change status of car object to stop"""
# 		self.status = 'stop'

# c = Car('Honda')
# print(c.counter)
# y = Car('Yahama')
# c.counter += 5
# print(c.counter)
# print(y.counter)
# print(c.__dict__)


# #__private,_protected,public method and attribute
# class Employee:
	
# 	def __init__(self, name, age, post, salary):
# 		self.name =name
# 		self.age =age
# 		self._post =post #post is protected
# 		self.__salary=salary #salary is private 

# 	def get_salary(self):
# 		return self.__salary

# 	def set_salary(self,value):
# 		self.__salary = value


# 	def __repr__(self): #repr is method that represent object 
# 		return f'{self.name},age:{self.age},salary:{self.__salary}'

# 	def __str__(self): #repr is method that represent string 
# 		return f'{self.name},age:{self.age},salary:{self.__salary}'

# yurika = Employee('yurika',20,'SD',20000)
# alish = Employee('alice',21,'DD',30000)

# print(yurika._post)
# print(yurika._Employee__salary)
# print(yurika.__dict__)
# print(alish._post)
# print(alish._Employee__salary)
# print(alish.__dict__)

# print(alish.set_salary(80893)) # set and get are method
# print(alish.get_salary())

# print(alish.name) #get attribute
# alish.name = 'gafadi' #set attribute
# print(alish.name)

# # del alish.name #delete attribute
# print(alish)


# class Employee:
# 	def __init__(self,fname,lname):
# 		self.fname = fname
# 		self.lname = lname
# 		# self._email = fname+'.'+lname+'@hotmail.com'
# 		self.__generate_email() #private method

# 	def __generate_email(self):
# 		self._email = self.fname+'.'+self.lname+'@hotmail.com'

# 	def set_name(self,fname,lname=None):
# 		self.fname = fname
# 		if lname:
# 			self.lname = lname
# 		self.__generate_email()

# 	@property
# 	def emali(self):
# 		return self._email
	
# 	@email.setter
# 	def email(self, value):
# 		self._email = value

# 	@email.deleter
# 	def email(self):
# 		del self._email


# s = Employee('yurika','khanal')
# s.email = 'yuri@gmail.com'
# del s.email
# print(s.__dict__)



##instance method , static method, class method
import math
class Circle:
	"""
	"""
	counter = 0

	def __init__(self, radius):
		selfme or email address
Password .radius = radius
		#self.incerase_counter()

	def area(self):#instance method
		a = math.pi * self.radius **2
		b = round(a,5)
		return b

	@staticmethod
	def diameter(radius):
		return 2 * radius

	@classmethod
	def duplicate(cls, radius):
		return cls(radius)

	@classmethod
	def unit_circle(cls):
		#print(cls)
		return cls(1)

	def __repr__(self):
		return f'Circle(radius = {self.radius})'

c = Circle(5)
print(c)
print(c.area())
print(c.diameter(c.radius))
u = c.unit_circle()
c.radius = 4
print(u)
print(c)
