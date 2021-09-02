machine_supply = {'water': 400, 'milk': 540, 'beans': 120, 'cups': 9, 'cash': 550}


def coffee_machine_status(machine_supply):
    print('The coffee machine has:\n{} of water\n{} of milk\n'
          '{} of coffee beans\n{} of disposable cups\n{} of money'.format(machine_supply['water'],
                                                                          machine_supply['milk'],
                                                                          machine_supply['beans'],
                                                                          machine_supply['cups'],
                                                                          machine_supply['cash']))


def substract_supply(supply, coffee):
    list = coffee
    supply['water'] -= list[0]
    supply['milk'] -= list[1]
    supply['beans'] -= list[2]
    supply['cups'] -= list[3]
    supply['cash'] += list[4]


def action_choice():
    while True:
        action = input('Write action (buy, fill, take, remaining, exit): ')
        if action == 'buy':
            buy_action(machine_supply)
        elif action == 'fill':
            fill_list = []
            fill_list.append(int(input('Write how many ml of water you want to add:')) * -1)
            fill_list.append(int(input('Write how many ml of milk you want to add:')) * -1)
            fill_list.append(int(input('Write how many grams of beans you want to add:')) * -1)
            fill_list.append(int(input('Write how many disposable cups you want to add:')) * -1)
            fill_list.append(0)
            substract_supply(machine_supply, fill_list)
        elif action == 'take':
            print('I gave you ${}'.format(machine_supply['cash']))
            machine_supply['cash'] = 0
        elif action == 'remaining':
            coffee_machine_status(machine_supply)
        elif action == 'exit':
            break
        else:
            print('Chose wrong action')

#  implement checking if there is enough resources to make coffee
def check_supply(choice):
    values = list(machine_supply.values())
    counter = 0
    if choice == '1':
        espr = ammount_for_coffee('1')
        for x in range(len(espr)):
            if values[x] >= espr[x]:
                counter += 1
        if counter == 5:
            return 1
        else:
            return 0

    elif choice == '2':
        latt = ammount_for_coffee('2')
        for x in range(len(latt)):
            if values[x] >= latt[x]:
                counter += 1
        if counter == 5:
             return 1
        else:
            return 0
    elif choice == '3':
        capp = ammount_for_coffee('3')
        for x in range(len(capp)):
            if values[x] >= capp[x]:
                counter += 1
        if counter == 5:
             return 1
        else:
            return 0

def ammount_for_coffee(number):
    if number == '1':
        espresso = [250, 0 , 16, 1, 4]
        return espresso
    elif number == '2':
        latte = [350, 75, 20, 1, 7]
        return latte
    elif number == '3':
        cappuccino = [200, 100, 12 ,1, 6]
        return cappuccino


def buy_action(supply):
    choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
    if choice == '1':
        check = check_supply(choice)
        if  check == 1:
            substract_supply(supply, ammount_for_coffee(choice))
            print('I have enough resources, making you a coffee!')
        else:
            print('Not enough')
    elif choice == '2':
        check = check_supply(choice)
        if check == 1:
            substract_supply(supply, ammount_for_coffee(choice))
            print('I have enough resources, making you a coffee!')
        else:
            print('Not enough')
    elif choice == '3':
        check = check_supply(choice)
        if check == 1:
            substract_supply(supply, ammount_for_coffee(choice))
            print('I have enough resources, making you a coffee!')
        else:
            print('Not enough')
    elif choice == 'back':
        return False
    else:
        print('We don\'t serve what you ordered')


def main():
    action_choice()


main()
