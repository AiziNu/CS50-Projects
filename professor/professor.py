import random



def main():
    # we initializing our var score and call our level function
    score = 0
    level = get_level()

    #loop and create var X and Y
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        prompt_try = 0


        #loop while propt is less than 3
        while prompt_try < 3:
            try:
                user_answer = int(input(f'{x} + {y} = '))
                if user_answer == correct_answer:
                    score +=1
                    break
                else:
                    print("EEE")
                    prompt_try += 1
            except ValueError:
                print("EEE")
                prompt_try += 1

        if prompt_try == 3:
            print(f"{x} + {y} = {correct_answer}")
    print(f'Score: {score}')





def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Invalid level. Please enter 1, 2, or 3.")
        except ValueError:
            print("Enter valid integer")


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)
    else:
        raise ValueError("Enter correct level. It must be 1, 2 or 3")


main()
