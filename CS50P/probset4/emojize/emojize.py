import emoji

def main():
    t = input("Input: ").strip()
    t = emoji.emojize(t,language="alias")
    print(t)


main()
