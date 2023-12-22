# Basic class
class Time:
  def __init__(self):
    self.hours = 0
    self.minutes = 0

time1 = Time()
time1.hours = 7
time1.minutes = 30

time2 = Time()
time2.hours = 12
time2.hours = 45

print('% s hours and % s minutes' % (time1.hours, time1.minutes))
print('% s hours and % s minutes' % (time2.hours, time2.minutes))


# Instance methods (functions inside instances)
class Aircraft:
  def __init__(self):
    self.name = ""
    self.maxSpeedMPH = 0

  def print_name(self):
    print("Name: % s" % self.name)

  def print_speed(self):
    print("Max speed: % s" % self.maxSpeedMPH)

tomcat = Aircraft()
tomcat.name = "F-14 Tomcat"
tomcat.maxSpeedMPH = 1544

tomcat.print_name()
tomcat.print_speed()


# Class constructors
class Spaceship:
  def __init__(self, name, race, shipClass):
    self.name = name
    self.race = race
    self.shipClass = shipClass

  def print_ship_details(self):
    print("The % s is a % s class ship from the % s race." % (self.name, self.shipClass, self.race))

enterprise = Spaceship("Enterprise", "Human", "Galaxy")
enterprise.print_ship_details()


# Class customization - you can change some primitive methods to affect how the Class operates
class ElectricGuitar:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  
stratocaster = ElectricGuitar("Fender", "Stratocaster")
print(stratocaster) # outputs "<__main__.ElectricGuitar instance at {some address}}>"

class BassGuitar:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  
  def __str__(self):
    return("% s % s" % (self.brand, self.model))
  
jazzBass = BassGuitar("Fender", "Jazz Bass")
print(jazzBass) # outputs "Fender Jazz Bass"

# NOTE: You can overload comparisons like __lt__ (<) or __ge__ (>=) so doing comparisons across
# classes compares relevant properties or attributes of those classes
# kinda neat