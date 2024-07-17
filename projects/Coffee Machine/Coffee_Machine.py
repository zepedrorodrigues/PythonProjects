import os
from os import system

inventory = {'water': 300,'milk':200,'coffee':100,'money':100.00}
drinks = [{'name':'espresso', 'water':50,'coffee':18,'milk':0,'price':1.5},{'name':'latte', 'water':200,'coffee':24,'milk':150,'price':2.5},{'name':'cappuccino','water':250,'coffee':24,'milk':100,'price':3}]

def machine():
    global drinks
    desire = input('What would you desire?').strip().lower()
    if desire == 'report':
        report()
        machine()
    elif desire == 'refill':
        refill()
        machine()
    else:
        for drink in drinks:
            if drink['name'] == desire:
                drink_choice(desire)
        return 'We have no such drink, sorry'
         
def drink_choice(name):
    for drink in drinks:
        if drink['name']== name:
            if check_inventory(name) == False:
                break
            else: payment_and_change(name)
    machine()

def report():
    print(f'Water:{inventory["water"]}mL\nMilk:{inventory["milk"]}mL\nCoffee:{inventory["coffee"]}g\nMoney:${inventory["money"]}')
    inp = input('')
    os.system('CLS')

def refill():
    global inventory
    water = int(input('How much water will you be adding (in mL)? ').strip())
    milk = int(input('How much milk will you be adding (in mL)? ').strip())
    coffee = int(input('How much coffee will you be adding (in g)? ').strip())
    money = float(input('How much money will you be adding (in $)? ').strip())
    inventory['water'] = inventory['water']+ water; inventory['coffee'] = inventory['coffee']+ coffee; inventory['milk'] = inventory['milk']+milk; inventory['money']=inventory['money']+money
    os.system('CLS')

def check_inventory(name):
    for drink in drinks:
        if drink['name'] == name and drink['water']<= inventory['water'] and drink['coffee']<= inventory['coffee'] and drink['milk'] <= inventory['milk']:
            inventory['coffee'] = inventory['coffee']-drink['coffee']
            inventory['milk']= inventory['milk']-drink['milk']
            inventory['water']= inventory['water']-drink['water']
            return True
    else:
        resources = []
        if drink['water'] > inventory['water']:
            resources.append('water')
        if drink['coffee'] > inventory['coffee']:
            resources.append('coffee')
        if drink['milk']>inventory['milk']:
            resources.append('milk')
        resources_missing = ''
        for resource in resources:
            if resources_missing == '':
                resources_missing = resources_missing + resource
            else:
                resources_missing = resources_missing + ' and ' +  resource
        print(f'not enough {resources_missing}, sorry')
        return False
          
def payment_and_change(name):
    for drink in drinks:
        global inventory
        if drink['name'] == name:
            print('Everything ready, let\'s proceed to payment')
            total = 0.25* int(input('How many quarters? ')) + 0.10 * int(input('How many dimes? ')) + 0.05* int(input('How many nickels? ')) + 0.01*int(input('How many pennies? '))
            if drink['price']>total:
                print('all ok till here')
                print('Not enough money, sorry!')
            elif drink['price'] == total:
                inventory['money'] = inventory['money'] + total
                print('Here\'s your drink, enjoy!')
            elif drink['price'] < total:
                change = round(total - drink['price'],2)
                inventory['money'] = inventory['money'] + drink['price']
                print(f'You get ${change} back. Here\'s your drink, enjoy!')

def __main__():
    machine()
    print('Hello world!')
if __name__ == '__main__':
    __main__()