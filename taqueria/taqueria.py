
def main():
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
    total_cost = 0.0

    while True:
        try:
            user_item = input("Item: ").strip().capitalize()

            #check if its inmenu or not , if its then need to update total_cost
            if user_input in menu:
                total_cost += menu[user_input]
                print(f"${total_cost:.2f}")
        except EOFError:
            print()  # To ensure the prompt moves to a new line after Ctrl-D
            break

main()










