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