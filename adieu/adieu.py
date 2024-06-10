import inflect
import sys



def main():
    p = inflect.engine()

    #create initial name var
    names = []
    print("Enter names, one per line. ")

    #to handle errors we use try and exeptions
    try:
        while True:
             #get Input prompt
            name = input()
            names.append(name)
    except EOFError:
        pass

    #Check at lear one name has entered
    if not names:
        sys.exit("No manes has entered")

    formatted_names = p.join(names)
    print(f"Adieu, adieu, to {formatted_names}")

main()

