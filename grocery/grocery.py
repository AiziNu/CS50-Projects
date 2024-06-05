def main():
    import sys
    buy_list = {}

    while True:
        try:
             item = input().strip().lower()
             if item in buy_list:
                 buy_list[item] +=1
             else:
                 buy_list[item] +=1


