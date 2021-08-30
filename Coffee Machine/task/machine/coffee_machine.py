print('Write how many ml of water the coffee machine has:')
has_water = int(input())
print('Write how many ml of milk the coffee machine has:')
has_milk = int(input())
print('Write how many grams of coffee beans the coffe machine has:')
has_beans = int(input())
print('Write how many cups of coffee you will need:')
cups_needed = int(input())

water = 200
milk = 50
beans = 15

water_for_cups = int(has_water / water)
milk_for_cups = int(has_milk / milk)
beans_for_cups = int(has_beans / beans)

can_do_cups = []
can_do_cups.append(water_for_cups)
can_do_cups.append(milk_for_cups)
can_do_cups.append(beans_for_cups)
how_many = 10000
for x in can_do_cups:
      if x < how_many:
            how_many = x
if how_many > cups_needed:
      print('Yes, I can make that amount of coffee (and even {} more than that)'.format(how_many - cups_needed))
elif how_many == cups_needed:
      print('Yes, I can make that amount of coffee')
else:
      print('No, I can make only {} cups of coffe'.format(how_many))