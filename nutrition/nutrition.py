def main():
      # Dictionary containing fruits and their calorie values
      fruits= {
            "apple": 130,
            "avocado": 50,
            "banana": 110,
            "cantaloupe": 50,
            "grapefruit": 60,
            "grapes": 90,
            "honneydew melon": 50,
            "kiwifruit": 90,
            "lemon": 15,
            "lime": 20,
            "nectarine": 60,
            "orange": 80,
            "peach": 60,
            "pear": 100,
            "pineapple": 50,
            "plums": 70,
            "strawberries": 50,
            "sweet cherries": 100,
            "tangerine": 50,
            "watermelon": 80,

      }

      user_fruit = input("Fruit: ").strip().lower()

      # Output the number of calories if the fruit is in the dictionary
      if user_fruit in fruits:
            print(f"Callories: {fruits[user_fruit]}")
      else:
            return

main()





