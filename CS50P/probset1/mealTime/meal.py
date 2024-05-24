def main():
    inputTime = input("What is the time? ") #?Get the input from the user
    ct = convert(inputTime) #*Call the convert function
    int(ct)

#*If statement to compare the values to determine whether or not the time is valid
#!breakfast between 7:00 and 8:00.
#!lunch between 12:00 and 13:00.
#!and dinner between 18:00 and 19:00.

    if ct >= 7 and ct <= 8:
        print("breakfast time")
    elif ct >= 12 and ct <= 13:
        print("lunch time")
    elif ct >= 18 and ct <= 19:
        print("dinner time")


def convert(time):
    tch,tcm = time.split(":")
    rth = int(tch)
    rtm = int(tcm)/60
    rtt = rth + rtm
    int(rtt)
    return rtt


if __name__ == "__main__":
    main()
