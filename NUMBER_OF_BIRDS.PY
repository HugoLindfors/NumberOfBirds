while True:
    
    CURRENT_YEAR = 0
    START_NUMBER_OF_BIRDS = NUMBER_OF_BIRDS = float(input("HOW MANY BIRDS ARE THERE THIS YEAR? "))
    CHANGE_RATE = float(input("AT WHAT RATE ARE THEY IN/DECREASING? "))

    if CHANGE_RATE > 1:
        while (NUMBER_OF_BIRDS < 2 * START_NUMBER_OF_BIRDS):
            CURRENT_YEAR += 1
            NUMBER_OF_BIRDS *= CHANGE_RATE

        print("THE NUMBER OF BIRDS IS DOUBLED AFTER", CURRENT_YEAR, "YEARS")
        
    elif CHANGE_RATE < 1:
        while (NUMBER_OF_BIRDS > 0.5 * START_NUMBER_OF_BIRDS):
            CURRENT_YEAR += 1
            NUMBER_OF_BIRDS *= CHANGE_RATE

        print("THE NUMBER OF BIRDS IS HALVED AFTER", CURRENT_YEAR, "YEARS")