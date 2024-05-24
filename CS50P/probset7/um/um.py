import re

def main():
    print(count(input("Text: ")))

def count(ums):
    text = re.findall(r"\b([U-u]m)\b", ums)
    return len(text)

if __name__ == "__main__":
    main()

