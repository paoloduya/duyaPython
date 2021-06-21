input('Full Name: ')
prelim = float(input('Prelim: '))
midterm = float(input('MidTerm: '))
semifinals = float(input('Semifinals: '))
finals = float(input('Finals: '))

total = prelim+midterm+semifinals+finals
ave = total / 4

if ave >=98 and ave<=100:
    print('With Highest Honors')
elif ave >=95 and ave <97:
    print('With High Honors')
elif ave >=90 and ave <94:
    print('With Honors')
elif ave >=75 and ave <89:
    print('Passed')
elif ave >=51 and ave <74:
    print('Failed')
else: print("Invalid")
