#from scipy import stats
print("*******************************WELCOME TO THE GOD PROGRAM**************************************")
Entering = input("Press Enter to Start")
choice = int(input("Press 1 to run the aplhabetical order sorter...2 for array calculator...3 for armmstrong number...4 for Capitalizing a sentence... 5 to check whether a given array is monotonic or not... 6 to check whether a given date is valid or not... 7 to check whether a number is a harshad number or not... 8 to check the lcm of numbers... 9 to print a random meaningful word based on user input... 10 to check if an array is monotonic or not... 11 to print the multiplication table... 12 to check if a triangle is valid or not... 13 to get the union and intersection of two arrays... 14 to perform various calculations regarding velocity "))
word_list = []
if choice == 1:
    string = input("Enter the word you want to sort")
    while string == "":
        string = input("Enter your word again correctly")
        print("The Words which have been sorted are: ")
        word_list = string.split()
    for word in word_list:
        print(word, " ")
        string.sort()
        print(string)

elif choice == 2:
    #lmit of numbers
    limit = int(input("Enter the amount of numbers you need in  your array"))
    num_list = []
    #x = [1,2,3,4,5,6]
    x = 0
    y = 0
    #taking input
    for i in range(limit):
        num = int(input("Enter your number"))
        num_list.append(num)
    #the mean function
    def mean(c,div):
        div = int(len(num_list))
        for n in range(len(num_list)):
            c = c + num_list[n]
        result = c // div
        print(result, "is  your result")
#the  median function
    def median(n):
        if len(num_list) % 2 !=0:
            n = (len(num_list)-1)/2
            print("Your median number in the array is:", num_list[n])
        else:
            n = (len(num_list))/2
            print("Your median value is:", num_list[n], "&",num_list[n+1])
#the mode function
    def mode(lst):
        lst = stats.mode(num_list)
        print("mode value is ",lst)
#calling the functions
    mean()
    median()
    mode()

elif choice == 3:
    num = int(input("Enter the number you want to check"))
    num_retainer = num
    c = 0
    while num > 1: #This while loop will run until number doesn't become 1.
        c = c + (num % 10) ** 3 #c will store the value of the sum of the cubes of the digits of the numbers
        num = num // 10
    if c == num_retainer:
        print(num_retainer, "is an amstrong number")
    else:
        print(num_retainer, "not an amstrong number")
elif choice == 4:
    #Capitalize a sentence correctly in python.
    sentence = input("Enter a sentence: ")
    sentence = sentence.capitalize()
    print(sentence)
elif choice == 5:
    loop = int(input("Enter the number of  inputs you want...")) #taking the number limit input
    num_list = []
    num_list_increase = []

    for i in range(loop):
        num = int(input("Enter your number"))       #inputtng numbers 
        num_list.append(num) #appending numbers into array

    num_list_increase = sorted(num_list,reverse = False)  #sorting array

    print("Sorted array is..." , num_list_increase)

elif choice == 6:
    day = int(input("Enter the day of the month"))
    month = input("Enter the name of the month...")
    month= month.lower()

    year = int(input("Enter the year"))

    if month == "january"or month == "march" or month == "may" or month =="july" or month == "august"or month == "october" or month == "december":
        if day > 31 and day < 0:
            print("Date is not Valid")
    elif month == "february":
        if year % 4 == 0:
            if day > 29 or day <  0:
                print("Date is not Valid")
        else:
            if day > 28 or day < 0:
                print("Date is not valid")  
    elif month == "september" or month == "april" or month == "june" or  month == "november":
        if day > 30 or day < 0:
            print("Date is not valid")
    else:
        print("Date given is valid...")
        print(day,"/",month,"/",year)

elif choice == 7:
        a = int(input("Enter a number: ")) # taking the number from user
        c = a # storing the actual value of a in c
        sum_of_a = 0
        a = str(a)
        i = len(a)
        a = int(a)
        while i != 0:
            z = a % 10 # z stores the mod of a
            sum_of_a = sum_of_a + z # z adds itself to k
            a = a // 10 # a gets floor divided
            i -= 1
        if c % sum_of_a == 0: # checks if the sum of a is divisible by the original number
            print(c, "is a harshad number")
        else:
            print(c, "is not a harshad number")

elif choice == 8:
    def lcm(x, y):
        if x > y:
            greater = x
        else:
            greater = y

        while(True):
            if((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
                greater += 1

        return lcm

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("The L.C.M. is", lcm(num1, num2))

elif choice == 9:
    #array containing random words
    word_list = ["Air", "Well", "Marker", "Beautiful", "Beat", "Belle Deplhine", "Kill", "star", "Man",
            "Jerk", "Pond", "Beast", "Eminem", "Young", "Mojang", "Technical", "Rose",
            "Aesthetic", "Tired", "Game ", "Crawl", "Never", "Disrupt", "Level", "Base"]
#taking any 3 strings from the user
    x = input("Enter your random first string")
    y = input("Enter your random second string")
    z = input("Enter your random third string")
#Shortening strings down to just the first character
    x = x[0]
    y = y[0]
    z = z[0]
    i = 0

    for i in range(len(word_list)):
        if x in word_list[i] and y in word_list[i] and z in word_list[i]:
            print("Your word is...", word_list[i])
        else:
            print("Sed:( couldnt find a meaningful word for you maybe try giving a new set of strings??")

elif choice == 10:
    loop = int(input("Enter the number of  inputs you want...")) #taking the number limit input
    num_list = []
    num_list_increase = []
    num_list_decrease =[]

    for i in range(loop):
        num = int(input("Enter your number"))       #inputtng numbers 
        num_list.append(num) #appending numbers into array

    num_list_increase = sorted(num_list,reverse = False)        #sorting array
    num_list_decrease = sorted(num_list,reverse = True)

    if num_list_increase == num_list or num_list_decrease == num_list:
        print("Array is monotonic")
    else:
        print("Array is not monotonic")
elif choice == 11:
    a = int(input("Enter a number: ")) # taking input from user and storing in 'a'
    c = a
    i = 1 # loop and multiplication purposes
    while i <= 10:
        z = c * i # z stores the total value of the multiplication, i.e. 69 * 1 = 69 <--- z
        print(c, "x", i, "=", z)
        i += 1
elif choice == 12:
        a = (int(input("Enter first angle of the triangle: ")))
        b = (int(input("Enter second angle of the triangle: ")))
        c = (int(input("Enter third angle of the triangle: ")))

        d = a + b + c
        # as we know the sum of the angles of a triangle has to be 180 or the triangle cant be formed

        if d == 180:
            print("The triangle is possible")
        else:
            print("The triangle can't be formed")

elif choice == 13:
    print('''1. Final velocity
    2. Initial velocity
    3. Time
    4. Acceleration''')

    print("Enter what you find (eg. 1 or 2 or 3 or 4")
    n = int(input("Enter your choice"))

    if(n < 5 and n > 0):
        if(n == 1):
            u = (int(input("Enter your initial velocity: ")))
            a = (int(input("Enter your accelration: ")))
            t = (int(input("Enter your time: ")))

            v = u + a * t
            print (v)
        elif(n == 2):
            v = (int(input("Enter your final velocity: ")))
            a = (int(input("Enter your accelration: ")))
            t = (int(input("Enter your time: ")))

            u = v - a * t
            print(u)
        elif(n == 3):
            u = (int(input("Enter your initial velocity: ")))
            a = (int(input("Enter your accelration: ")))
            v = (int(input("Enter your final velocity: ")))

            t = (v - u)/a
            print (t)
        elif(n == 4):
            u = (int(input("Enter your initial velocity: ")))
            v = (int(input("Enter your final velocity: ")))
            t = (int(input("Enter your time: ")))

            a = (v-u)/t
            print (a)
    else:
        print("Enter a valid choice")

elif choice == 14:
    arr = []
    arr2 = []
    arInp1 = ""
    arInp2 = ""

    def aray_adder(arrc, arr, array_input):
        while arrc != 0:
            array_input = input("Enter your string: ")
            arr.append(array_input)
            arrc -= 1
    arrayc = int(input("How many keywords for first array? "))
    aray_adder(arrayc, arr, arInp1)
    arrayc2 = int(input("How many keywords for first array? "))
    aray_adder(arrayc2, arr2, arInp2)

    kws = len(arr) - 1
    while kws != -1:
        arr[kws] = str.upper(arr[kws])
        kws -= 1

    kws2 = len(arr2) - 1
    while kws2 != -1:
        arr2[kws2] = str.upper(arr2[kws2])
        kws2 -= 1

    def inception(arr, arr2):
        return list(set(arr) & set(arr2))

    print("Inception: ", inception(arr, arr2))
    arr.extend(arr2)
    print("Union: ",arr)
