# Dictionaries are basically objects with key/value pairs

aircraft_ordinance = {
  'F-22 Raptor': ['AIM-120', 'AIM-9'],
  'F-14 Tomcat': ['AIM-9', 'AIM-7', 'AIM-54'],
  'F-4 Phantom': ['AIM-9', 'AIM-7']
}

weapon_names = {
  'AIM-9': 'Sidewinder',
  'AIM-7': 'Sparrow',
  'AIM-54': 'Phoenix',
  'AIM-120': 'AMRAAM'
}

print('The F-14 Tomcat carried the following weapons:')
for weapon in aircraft_ordinance['F-14 Tomcat']:
  print('% s % s' % (weapon, weapon_names[weapon]))

print('')

# Iterate

for aircraft in aircraft_ordinance:
  if 'AIM-120' in aircraft_ordinance[aircraft]:
    print('% s is a modern aircraft' % aircraft)
  else:
    print('% s is not a modern aircraft' % aircraft)