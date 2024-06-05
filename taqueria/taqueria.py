menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    user_item = input("Item: ").strip().capitalize()
    total = get_item(user_item)

    total = 0
    while True:
        



def get_item(choose):

    if choose in menu:
        return menu[choose]
    else:
        pass


