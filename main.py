import pyodbc
import string
import secrets
from datetime import datetime

connection = pyodbc.connect('Driver={SQL Server};Server=server.sample.ca;uid=user123;pwd=password123')
print("Connection Successfully Established")  

userID = None

def login():
    global userID
    userID = input("Please enter your userID:")
    userIDCursor = connection.cursor()
    userIDCursor.execute("SELECT user_id FROM user_yelp")
    databaseUserIDs = userIDCursor.fetchone()

    while databaseUserIDs:
        if (userID == databaseUserIDs[0]):
            return True
        databaseUserIDs = userIDCursor.fetchone()
    return False

def displayFilters():
    print("Possible filtering options: ")
    print("1. Minimum number of stars")
    print("2. Maximum number of stars")
    print("3. City") 
    print("4. Name")   

def minStarsFilter():
    minStars = float(input("Enter the value of the minimal star rating [0,5]: "))
    if minStars <= 5 and minStars >= 0:
        anwser = " AND business.stars >= " + str(minStars)
        return anwser
    else:
        print("Incorrect input, please try again")
        minStarsFilter()

def maxStarsFilter():
    maxStars = float(input("Enter the value of the maximal star rating [0,5]: "))
    if maxStars <= 5 and maxStars >= 0:
        anwser = " AND business.stars <= " + str(maxStars)
        return anwser
    else:
        print("Incorrect input, please try again")
        maxStarsFilter()

def cityFilter():
    city = input("Enter the name of the city: ")
    anwser = " AND business.city like '%" + str(city) + "%'"
    return anwser

def nameFilter():
    name = input("Enter the name of the business: ")
    anwser = " AND business.name like '%" + str(name) + "%'"
    return anwser

def selectFilter():
    displayFilters()
    filterChoice = int(input("What filter would you like to apply: "))
    if(filterChoice == 1):
        print("You chose min number of stars filter")
        return minStarsFilter()
    elif(filterChoice == 2):
        print("You chose max number of stars filter")
        return maxStarsFilter()
    elif(filterChoice == 3):
        print("You chose city filter")
        return cityFilter()
    elif(filterChoice == 4):
        print("You chose name filter")
        return nameFilter()
    else:
        print("Invalid choice, please select again")
        selectFilter()
   
def searchBusiness():
    querry = "SELECT business.business_id, business.name, business.address, business.city, business.stars FROM business WHERE 1=1"
    print("============================================================")
    print("SEARCHING FOR BUSINESS")
    numFilters = int(input("How many filters would you like to apply? "))

    if(numFilters < 0 or numFilters > 4):
        print("Invalid value, enter a number in range [1,4] (1 try remaining)")
        numFilters = int(input("How many filters would you like to apply? "))
        if(numFilters < 0 or numFilters > 4):
            print("Process failed, invalid entry")
            menu()
            return
    
    for i in range(numFilters):
        querry += selectFilter()

    querryCursor = connection.cursor()
    querry += " ORDER BY business.name"
    querryCursor.execute(querry)
    businesses = querryCursor.fetchone()

    if(not businesses):
        print("No results matches this description, please try again")
        searchBusiness()
        
    while businesses:
        print("============================================================")
        print("Name: " + str(businesses[1]))
        print("Business ID: " + str(businesses[0]))
        print("Adress: " + str(businesses[2]))
        print("City: " + str(businesses[3]))
        print("Star rating: " + str(businesses[4]))
        businesses = querryCursor.fetchone()
    menu()

def searchUsers():
    querry = "SELECT user_yelp.user_id, user_yelp.name, user_yelp.useful, user_yelp.funny, user_yelp.cool, user_yelp.yelping_since FROM user_yelp WHERE 1 = 1"

    print("============================================================")
    print("SEARCHING FOR USERS")

    anwser1 = input("Would you like to search by the name of the user? (Yes/No): ").upper()
    if anwser1 == 'YES':
        name = input("Name of the user: ")
        querry += " AND user_yelp.name like '%" + str(name) + "%'"

    anwser2 = input("Would you like to search user with useful reviews? (Yes/No): ").upper()
    if anwser2 == 'YES':
        querry += " AND user_yelp.useful > 0"

    anwser3 = input("Would you like to search user with funny reviews? (Yes/No): ").upper()
    if anwser3 == 'YES':
        querry += " AND user_yelp.funny > 0"

    anwser4 = input("Would you like to search user with cool reviews? (Yes/No): ").upper()
    if anwser4 == 'YES':
        querry += " AND user_yelp.cool > 0"


    querry += " ORDER BY user_yelp.name"

    querryCursor = connection.cursor()
    querryCursor.execute(querry)
    users = querryCursor.fetchone()

    if(not users):
        print("No results matches this description, please try again")
        searchUsers()

    while users:
        print("============================================================")
        print("User_ID: " + str(users[0]))
        print("Name: " + str(users[1]))
        print("№ of useful reviews: " + str(users[2]))
        print("№ of funny reviews: " + str(users[3]))
        print("№ of cool reviews: " + str(users[4]))
        print("Date of registration: " + str(users[5]))
        users = querryCursor.fetchone()
    menu()

def validateUID(input):
    querry = "SELECT * FROM user_yelp WHERE user_yelp.user_id = '" + input + "'"
    querryCursor = connection.cursor()
    querryCursor.execute(querry)
    tester = querryCursor.fetchone()
    if(not tester or input == userID):
        return False
    else:
        return True


def makeFriend():
    friendUID = input("Enter a valid userID  that you would like to become freinds with: ")

    if (not validateUID(friendUID)):
        print("invalid business_id, please try again")
        makeFriend()
        return

    querry = "INSERT INTO friendship (user_id, friend) VALUES ('" + userID + "','" + friendUID + "')"

    querryCursor = connection.cursor()
    querryCursor.execute(querry)
    connection.commit()
    print("Succesfully added a friend")
    menu()

def generateReviewID(length=22):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    return random_string

def starInput():
    numStars = int(input("Enter a star rating [0,5]: "))
    if(numStars > 5 or numStars < 0):
        print("Invalid number, the input range is [0,5], you have 1 more try")
        numStars = int(input("Enter a star rating [0,5]: "))
        if(numStars > 5 or numStars < 0):
            print("Process failed, returning to main menu")
            menu()
            return 256
        else:
            return numStars
    else:
        return numStars

def checkBusExistance(business_id):
    querry = "SELECT * FROM business WHERE business.business_id = '" + business_id + "'"
    querryCursor = connection.cursor()
    querryCursor.execute(querry)
    tester = querryCursor.fetchone()
    if(not tester):
        return False
    else:
        return True

def writeReview():
    reviewID = generateReviewID(22)
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')[:-3]

    print("============================================================")
    print("WRITING A REVIEW")
    businessID = input("Enter a valid business_id that you would like to review: ")

    if (not checkBusExistance(businessID)):
        print("invalid business_id, please try again")
        writeReview()
        return
    
    numStars = starInput()
    if numStars == 256:
        return
    
    querry = f"INSERT INTO review (review_id, user_id, business_id, stars, useful, funny, cool, date) "
    querry += f"VALUES ('{reviewID}', '{userID}','{businessID}', {numStars}, 0, 0, 0, '{date}')"

    querryCursor = connection.cursor()
    querryCursor.execute(querry)
    connection.commit()
    print("Succesfully added a review")
    menu()

def menu():
    print("============================================================")
    print("Select one of the options by entering the number")
    print("0. Quit the application")
    print("1. Search Business")
    print("2. Search Users")
    print("3. Make Friend")
    print("4. Write Review")

    choice = input("Select function: ")
    choiceINT = int(choice)
    
    if(choiceINT == 0):
        print("Shutting down the application")
        return
    elif(choiceINT == 1):
        searchBusiness()
    elif(choiceINT == 2):
        searchUsers()
    elif(choiceINT == 3):
        makeFriend()
    elif(choiceINT == 4):
        writeReview()
    else:
        print("Invalid Input, please enter your input again! ")
        menu()


def main():
    if (not login()):
        print("Invalid UserID please try again (Tries left: 1)")
        login()
    else:
        print("User logged in")
        menu()

    connection.close()
    print("Connection succesfully closed")
    print("============================================================")

main()