print('''Welcome to our Theme Park

These are the available rides:

1. Scenic River Cruise
2. Carnival Carousel
3. Jungle Adventure Water Splash
4. Downhill Mountain Run
5. The Regurgitator
''')

ride_number_text = input('Please enter the ride number you want:')
ride_number = int(ride_number_text)

while ride_number < 1 or ride_number > 5:
    print('There is no ride with that number')
    ride_number_text = input('Please enter the ride number you want:')
    ride_number = int(ride_number_text)

print('You have selected ride number:', ride_number)

if ride_number == 1:
    print('You have selected the Scenic River Cruise')
    print('There are no age limits for this ride')
else:
    # We need to get the age of the user
    age_text = input('Please enter your age:')
    age = int(age_text)

    if ride_number == 2:
        print('You have selected the Carnival Carousel')
        if age >= 3:
            print('You can go on the ride.')
        else:
            print('Sorry. You are too young.')

    if ride_number == 3:
        print('You have selected Jungle Adventure Water Splash')
        if age >= 6:
            print('You can go on the ride.')
        else:
            print('Sorry. You are too young.')

    if ride_number == 4:
        print('You have selected Downhill Mountain Run')
        if age >= 12:
            print('You can go on the ride.')
        else:
            print('Sorry. You are too young.')

    if ride_number == 5:
        print('You have selected The Regurgitator')
        if age >= 12:
            # Age is not too low
            if age > 70:
                # Age is too high
                print('Sorry. You are too old.')
            else:
                # Age is in the correct range
                print('You can go on the ride.')
        else:
            # Age is too low
            print('Sorry. You are too young.')
