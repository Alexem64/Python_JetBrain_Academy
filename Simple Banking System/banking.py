# Write your code here
import random


def check_card_number(card_number):
    if card_number not in all_cards_and_pins:
        all_cards_and_pins.append(card_number)
        return True
    return False


def luhn_alg(number):
    new_number_list = list(number)
    number_list = [int(x) for x in new_number_list[:]]
    print(number_list)
    counter = 0
    for x in number_list:
        if counter % 2 == 0:
            number_list[counter] = x * 2
        counter += 1
    print(number_list)
    #number_list = [x*2 if x % 2 == 0 else x for x in number_list]    #print(number_list)
    number_list = [x - 9 if x > 9 else x for x in number_list]
    print(number_list)
    checksum = 10 - (sum(number_list) % 10)
    print(sum(number_list, checksum))
    return checksum


def generate_card_number():
    bin = '400000'
    ain = str(random.randint(0, 999999999)).ljust(9, '0')
    checksum = str(luhn_alg(bin+ain))
    return bin+ain+checksum


def generate_pin():
    pin = str(random.randint(0, 9999)).ljust(4, '0')
    all_cards_and_pins.append(pin)
    return pin


def check_num_and_pin(card_number, pin):
    if card_number in all_cards_and_pins and pin == all_cards_and_pins[all_cards_and_pins.index(card_number)+1]:
        return True
    else:
        return False


def menu():
    exitflag = False
    while True:
        print("""1. Create an account\n2. Log into account\n0. Exit""")
        choice: str = input()
        print()
        if choice == '1':
            card_num = generate_card_number()
            while not check_card_number(card_num):
                card_num = generate_card_number()
            pin = generate_pin()
            print('Your card number:')
            print(card_num)
            print('Your card PIN:')
            print(pin)
            print()
            continue

        if choice == '2':
            card_num = input('Enter your card number:\n')
            pin = input('Enter your PIN:\n')

            if not check_num_and_pin(card_num, pin):
                print()
                print('Wrong card number or PIN!\n')
                continue
            else:
                print()
                print('You have successfully logged in!')
                while True:
                    print()
                    print("""1. Balance\n2. Log out\n0. Exit""")
                    subchoice = input()
                    if subchoice == '1':
                        print()
                        print('Balance: 0')
                        continue
                    elif subchoice == '2':
                        print()
                        print('You successfully logged out!\n')
                        break
                    elif subchoice == '0':
                        exitflag = True
                        break
                if exitflag:
                    print('\nBye!')
                    break
                else:
                    continue
        print('Bye!')
        break


all_cards_and_pins = []
menu()
#print(luhn_alg('400000757623120'))
