def main():
    twitter = str(input("Twitter: "))
    tweet = shorten(twitter)
    print("Twttr:",tweet)

def shorten(tweet):
    twat = str(tweet)
    twat = twat.replace("a","")
    twat = twat.replace("A","")
    twat = twat.replace("e","")
    twat = twat.replace("E","")
    twat = twat.replace("i","")
    twat = twat.replace("I","")
    twat = twat.replace("o","")
    twat = twat.replace("O","")
    twat = twat.replace("u","")
    twat = twat.replace("U","")

    return twat
    #! aeiou

if __name__ == "__main__":
    main()
