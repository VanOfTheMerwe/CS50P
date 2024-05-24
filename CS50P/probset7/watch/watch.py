import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(yes):
    if result := re.search(r'.+src="https?://(?:www\.)?youtube\.com/embed/([a-z0-9A-Z]+)"',yes):
        return "https://youtu.be/" + result.group(1)


if __name__ == "__main__":
    main()
