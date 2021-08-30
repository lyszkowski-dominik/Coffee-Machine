machine_supply = {'water': 400, 'milk': 540, 'beans': 120, 'cups': 9, 'cash': 550}


def coffee_machine_status(machine_supply):
    print('The coffee machine has:\n{} of water\n{} of milk\n'
          '{} of coffee beans\n{} of disposable cups\n{} of money'.format(machine_supply['water'],
                                                                          machine_supply['milk'],
                                                                          machine_supply['beans'],
                                                                          machine_supply['cups'],
                                                                          machine_supply['cash']))


def substract_supply(supply, water, milk, beans, cups, cash):
    supply['water'] -= water
    supply['milk'] -= milk
    supply['beans'] -= beans
    supply['cups'] -= cups
    supply['cash'] += cash


def action_choice():
    while True:
        action = input('Write action (buy, fill, take, remaining, exit): ')
        if action == 'buy':
            buy_action(machine_supply)
        elif action == 'fill':
            w_to_fill = int(input('Write how many ml of water you want to add:'))
            m_to_fill = int(input('Write how many ml of milk you want to add:'))
            b_to_fill = int(input('Write how many grams of beans you want to add:'))
            c_to_fill = int(input('Write how many disposable cups you want to add:'))
            substract_supply(machine_supply, (w_to_fill * -1), (m_to_fill * -1), (b_to_fill * -1), (c_to_fill * -1), 0)
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
def check_supply():
    pass


def buy_action(supply):
    choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
    if choice == '1':
        substract_supply(supply, 250, 0, 16, 1, 4)
    elif choice == '2':
        substract_supply(supply, 350, 75, 20, 1, 7)
    elif choice == '3':
        substract_supply(supply, 200, 100, 12, 1, 6)
    elif choice == 'back':
        return False
    else:
        print('We don\'t serve what you ordered')


def main():
    action_choice()


main()
