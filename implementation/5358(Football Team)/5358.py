try:
    while True :
        data = input()

        for datum in data:
            if datum == "e":
                print("i", end = "")
            elif datum == "i":
                print("e", end = "")
            elif datum == "E":
                print("I", end = "")
            elif datum == "I":
                print("E", end = "")
            else:
                print(datum, end = "")
                
        print()
except:
    exit(0)