def main():
    greeting = input("Greeting: ").lower().strip()
    greetval = value(greeting)
    greetval = int(greetval)
    print(f"${greetval}")

def value(greeting):
    greeting = greeting.lower()
    if greeting[:5] == "hello":
        return(0)
    elif greeting[0][0] == "h":
        return(20)
    else:
        return(100)

if __name__ == "__main__":
    main()
