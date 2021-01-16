market = {"Egg": 1,
          "Toilet paper": 5,
          "Bread": 2.4,
          "Soap": 3,
          "Beans": 6,
          "Qristmas tree": 40}

print("Hello my friend, how are you?")
mood = input()

print("Great! me too... and your name is...?")
name = input()
print(f' Hello {name} I have been told that'
      f' you want to buy some stuff for the quarantine')
print("Here is what we have in our storage:")

for index, (key, cost) in enumerate(market.items()):
    print(f'{index}. {key} - {cost}$')

while True:
    product = input("please type what you need:")
    if product in market.keys():
        break
    else:
        print("I don't have that. please choose from the list...")

print("how many do you need?")
Quantity = int(input())
print(f'Total cost is {Quantity * market.get(product)} $')
print("Do you want to pay?")

while True:
    answer = input("Type Yes or No: ").lower()
    if answer == "yes":
        print("Thank you for the purchase")
        break
    elif answer == "no":
        quit()
    else:
        print("Please enter valid answer")
