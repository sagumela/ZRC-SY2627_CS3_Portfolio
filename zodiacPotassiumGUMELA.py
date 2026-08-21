year = int(input("Enter your birth year: "))
if year < 1900:
    print("Invalid Year, it should not be earlier than 1900")
else:
    zodiac = ((year - 1900) % 12) + 1

    if zodiac == 1:
        print("Your Chinese Zodiac sign is a Rat")
    elif zodiac == 2:
        print("Your Chinese Zodiac sign is an Ox")
    elif zodiac == 3:
        print("Your Chinese Zodiac sign is a Tiger")
    elif zodiac == 4:
        print("Your Chinese Zodiac sign is a Rabbit")
    elif zodiac == 5:
        print("Your Chinese Zodiac sign is a Dragon")
    elif zodiac == 6:
        print("Your Chinese Zodiac sign is a Snake")
    elif zodiac == 7:
        print("Your Chinese Zodiac sign is a Horse")
    elif zodiac == 8:
        print("Your Chinese Zodiac sign is a Goat")
    elif zodiac == 9:
        print("Your Chinese Zodiac sign is a Monkey")
    elif zodiac == 10:
        print("Your Chinese Zodiac sign is a Rooster")
    elif zodiac == 11:
        print("Your Chinese Zodiac sign is a Dog")
    elif zodiac == 12:
        print("Your Chinese Zodiac sign is a Pig")