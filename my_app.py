class Person:
 
  def __init__(self, name, age):
    self.name=name
    self.age=age

  def walk(self):
    print(self.name + ' is walking..')

  def speak(self):
    print('Hello my name is ' + self.name + ' and I am '+ str(self.age) + ' years old')
    

john = Person('mostafa', 15)
mariam = Person('maryam', 22)
print (john.name + ' '+str(john.age))
print (mariam.name + ' '+str(mariam.age))
john.walk()
mariam.speak()


# age = 17
# is_adult = False

# def check_age(age):
#   if age>=18:
#       print ('Hello mok '+str(age))
#   else:
#       print('not')

# check_age(20)
# print()

# cars = ['bmw', 'tesla','fiat']
# print(len(cars))
# print(cars[0])
# print()
# for car in cars:
#     if car == 'bmw':
#       print(car.capitalize())
#     else:
#       print(car.upper())
