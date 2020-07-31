name = input("Enter your name: ")

def whoops(name):
    result = f"Whoops, {name} is not your name! Try again."
    return result

print(whoops(name))