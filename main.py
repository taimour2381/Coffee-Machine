# Coffee Machine Project.

# The items that the coffee machine can dispense and their recipes are stored as a nested dictionary below.
resources = {
    "water": 1500,
    "milk": 600,
    "coffee": 0,
    "money": 0,
}
a = 0
order = ""


def resource_checker(consumer_choice):
    global a
    if resources['water'] < 50 and consumer_choice == 'E':
        print("Sorry, There is not enough water in the coffee machine's tank. Please add water!")
        a = 1
    if resources['coffee'] < 18 and consumer_choice == 'E':
        print("Sorry, There is not enough coffee in the coffee machine's tank. Please add coffee!")
        a = 1
    if resources['water'] < 200 and consumer_choice == 'L':
        print("Sorry, There is not enough water in the coffee machine's tank. Please add water!")
        a = 1
    if resources['coffee'] < 24 and (consumer_choice == 'L' or consumer_choice == 'C'):
        print("Sorry, There is not enough coffee in the coffee machine's tank. Please add coffee!")
        a = 1
    if resources['milk'] < 150 and consumer_choice == 'L':
        print("Sorry, There is not enough milk in the coffee machine's tank. Please add milk!")
        a = 1
    if resources['water'] < 250 and consumer_choice == 'C':
        print("Sorry, There is not enough water in the coffee machine's tank. Please add water!")
        a = 1
    if resources['milk'] < 100 and consumer_choice == 'C':
        print("Sorry, There is not enough milk in the coffee machine's tank. Please add milk!")
        a = 1
    return a


def administer_machine_resources():
    modify = input("Which resource do you want to modify? (water/milk/coffee): ")
    if modify == "water":
        print(f"There is currently {resources['water']} ml of water in the inventory.")
        add_water = int(input("The amount of water you want to add to the machine: (ml) "))
        if resources["water"] == 1500:
            print("The water tank of the machine is full and no more water can be added.")
        elif add_water > 1500 or (add_water + resources["water"]) > 1500:
            print("This is beyond machine's water tank capacity.")
        elif (add_water + resources["water"]) <= 1500:
            resources["water"] = resources["water"] + add_water
            print(f"The water has been replenished. the current water level is {resources['water']}ml.")
    if modify == "milk":
        print(f"There is currently {resources['milk']} ml of milk in the inventory.")
        add_milk = int(input("The amount of milk you want to add to the machine: (ml) "))
        if resources["milk"] == 600:
            print("The milk container of the machine is full and no more milk can be added.")
        elif add_milk > 600 or (add_milk + resources["milk"]) > 600:
            print("This is beyond machine's milk container capacity.")
        elif (add_milk + resources["milk"]) <= 600:
            resources["milk"] = resources["milk"] + add_milk
            print(f"The milk has been replenished. The current milk level is {resources['milk']}ml.")
    if modify == "coffee":
        print(f"There is currently {resources['coffee']} gm of coffee in the inventory.")
        add_coffee = int(input("The amount of coffee you want to add to the machine: (gm) "))
        if resources["coffee"] == 600:
            print("The coffee container of the machine is full and no more coffee can be added.")
        elif add_coffee > 600 or (add_coffee + resources["coffee"]) > 600:
            print("This is beyond machine's coffee container capacity.")
        elif (add_coffee + resources["coffee"]) <= 600:
            resources["coffee"] = resources["coffee"] + add_coffee
            print(f"The coffee has been replenished. The current coffee level is {resources['coffee']}gm.")


Power = "On"
while Power == "On":
    print("Welcome to Taimour's First Coffee Machine!")
    print("Do you want to administer the coffee machine resources or order something?")
    function = input("Press '1' for administration, '2' for ordering, '0' for powering off the Coffee machine: ")
    if function == '1':
        administer_machine_resources()
    elif function == '2':
        go = True
        while go:
            print("What would you like to have?")
            print("1.Press 'E' for Espresso($1.5).\n2. Press 'L' for Latte($2.5).")
            print("3. Press 'C' for Cappuccino($3.0).\nPress 'R' to view resources report.")
            order = input(": ")
            if resource_checker(order) == 0:
                go = False
        if order != 'R':
            print("Insert Coins")
            Penny = int(input("Pennies: "))
            Nickel = int(input("Nickels: "))
            Dime = int(input("Dimes: "))
            Quarter = int(input("Quarters: "))
            inserted_money = (Penny + (Nickel * 10) + (Dime * 20) + (Quarter * 25)) / 100
            print(f"You have inserted ${inserted_money}.")
            if inserted_money < 1.5:
                print("You have not provided enough money. Amount refunded.")

            elif order == "E" and inserted_money >= 1.5:
                resources['water'] = resources['water'] - 50
                resources['coffee'] = resources['coffee'] - 18
                resources['money'] = resources['money'] + 1.5
                refund_amount = round((inserted_money - 1.5) * 100)
                if refund_amount > 0:
                    print(f"Enjoy your cup of Espresso. Thank you for using Coffee Machine.")
                    print(f"{refund_amount}cents refunded.")

                else:
                    print("Enjoy your cup of Espresso. Thank you for using Coffee Machine.")

            elif order == "L" and inserted_money >= 2.5:
                resources['water'] = resources['water'] - 200
                resources['coffee'] = resources['coffee'] - 24
                resources['milk'] = resources['milk'] - 150
                resources['money'] = resources['money'] + 2.5
                refund_amount = round((inserted_money - 2.5) * 100)
                if refund_amount > 0:
                    print(f"Enjoy your cup of Latte. Thank you for using Coffee Machine.")
                    print(f"{refund_amount}cents refunded.")

                else:
                    print("Enjoy your cup of latte. Thank you for using Coffee Machine.")

            elif order == "C" and inserted_money >= 3.0:
                resources['water'] = resources['water'] - 250
                resources['coffee'] = resources['coffee'] - 24
                resources['milk'] = resources['milk'] - 100
                resources['money'] = resources['money'] + 3.0
                refund_amount = round((inserted_money - 3.0) * 100)
                if refund_amount > 0:
                    print(f"Enjoy your cup of Cappuccino. Thank you for using Coffee Machine.")
                    print(f"{refund_amount}cents refunded.")

                else:
                    print("Enjoy your cup of latte. Thank you for using Coffee Machine.")

        if order == "R":
            print(f"Coffee Machine's water level is {resources['water']} ml")
            print(f"Coffee Machine's milk level is {resources['milk']} ml")
            print(f"Coffee Machine has {resources['coffee']} gm of coffee.")
            print(f"There are ${resources['money']} in the Coffee Machine.)")

    elif function == '0':
        print("Coffee Machine is shutting down. Good Bye!")
        Power = "off"