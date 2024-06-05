def main():
    import sys
    buy_list = {}

    while True:
        try:
             item = input().strip().lower()
             if item in buy_list:
                 buy_list[item] +=1
             else:
                 buy_list[item] =1
        except EOFError:
            print()  # To ensure the prompt moves to a new line after Ctrl-D
            break

    for item in sorted(buy_list):
        print(f"{buy_list[item]} {item.upper()}")

main()


