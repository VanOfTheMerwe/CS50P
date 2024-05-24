def main():
    # Ass saved by Luke Melaia
    coke = 50

    while coke > 0:
        print("Amount Due:", coke)
        coins = int(input("Insert Coins: "))

        if coins == 25 or coins == 10 or coins == 5:
            coke -=coins

    print("Change Owed:", abs(coke))



if __name__ == "__main__":
    main()
