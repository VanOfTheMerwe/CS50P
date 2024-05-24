greet = input("Greeting: ").lower().strip().split()

if greet[0][0:5] == "hello":
    print("$0")
elif greet[0][0] == "h":
    print("$20")
else:
    print("$100")

#! Added lower to make the user input case insensitive

