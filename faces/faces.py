# Create function convert accept str as a input and converts

# creare var is is equal to input to get a str
def convert(input_str):
      # Replace :) with 🙂
    output_str = input_str.replace(':)', '🙂')
    # Replace :( with 🙁
    output_str = output_str.replace(':(', '🙁')
    return output_str


def main():

    user_input = input("Enter sentense with Emojis: ")
    result = convert(user_input)
    print(result)

