import re

def main():
    word = input("camelCase: ").strip()
    newword = convert_to_snake(word)
    print(newword)

# !def camelToSnake(camel):
#!     words = re.findall(r'[A-Z][a-z]*', camel)
# !    lowerWords = [word.lower() for word in words]
#  !   snakecase = "_".join(lowerWords)
#   !  return snakecase
# *better solution given by Paul Grobler

def convert_to_snake(word):
    snake_case = ''
    for c in word:
        if c.isupper():
            snake_case += '_'
            c = c.lower()
        snake_case += c
    return snake_case


if __name__ == "__main__":
    main()
