## craete var and get user input
file_name = input('Enter file. ').strip().lower()

# create conditions and return back
if file_name.endswith(".gif"):
    print("image/gif")
elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
    print("image/jpeg")
elif
