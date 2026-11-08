#1: Answer the following questions:

#a. What is duck typing, as explained in the video?
#Duck typing is a concept of polymorphism where the type or class of an object is less important than the methods or attributes it defines.

#b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
#The Car class needed to have a method with the exact same name like speak() or make_sound()) matching what the loop expected to call on the objects.

#2: Python Code
class Car:

  def move(self):
    print("The car drives on the road.")

class Boat:

  def move(self):
    print("The boat sails on water.")

class Drone:

  def move(self):
    print("The drone flies in the sky.")

def start_trip(vehicle):
  vehicle.move()

car = Car()
boat = Boat()
drone = Drone()

vehicles = [car, boat, drone]

for v in vehicles:
  start_trip(v)


#3:  How does the code in 2.2 demonstrate polymorphism?
#It demonstrates duck typing. The function start_trip() doesn't check the specific class of the vehicle object.
#It simply invokes the .move() method. Because Car, Boat, and Drone all independently implement a .move() method,
#Python successfully calls the correct version for whichever object is passed in.

