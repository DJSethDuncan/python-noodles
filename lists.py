# A list is a container, which is an object that groups related objects together.
# A list is also a sequence; thus, the contained objects maintain a left-to-right positional order.
# Elements of the list can be accessed via indexing operations that specify the position of the desired element in the list.
# Each element in a list can be a different type such as strings, integers, floats, or even other lists.

# LISTS

fighters_list = ['F-22 Raptor', 'F-14 Tomcat', 'F-4 Phantom II']
print(fighters_list)

dna_list = list('atgagggtaccattg')
print(dna_list)

print('The best looking fighter is obviously the ' + fighters_list[1])

fighters_list.append('Dassault Rafale')
print(fighters_list)

rafale = fighters_list.pop()
print(rafale)                   # removed from list
print(fighters_list)            # list is missing rafale
fighters_list.append(rafale)    # add rafale back
print(fighters_list)            # list includes rafale again


# ITERATION

for fighter in fighters_list:
  print(fighter)

unsorted_list = [97, 23, 5, 87]
unsorted_list.sort()
print(unsorted_list)

nested_list = [[3, 99, 5], [78, 19, 3]]
for inner_list in nested_list:
  inner_list.sort()

print(nested_list)

# SLICING

american_fighters = fighters_list[1:4]
print(american_fighters)