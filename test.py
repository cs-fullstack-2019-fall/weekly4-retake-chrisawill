# 1. Ask a user for their first name and age. Print "[NAME] is [AGE] years old"

# user = input("What is your name")
# userA = input("What is your age")
# print(f"{user} is {userA} years old")







# 2. Ask the user to enter their age. Check if they entered a value between 0 and 125. If valid, print "REAL AGE". If invalid print “NOT A REAL AGE!!!”
#
# user = int(input("What is your age"))
# if user > 125:
#     print("Not a real age!")
# elif user < 0:
#     print("not a real age")
# else:
#     print("real age")






# 3. Use a for loop to print every 4 numbers from -50 to 50.
#
# for index in range(-50,51,+4):
#     print(index)







# 4. Ask the user to enter a number to add to a total. Keep asking the user to enter a number until they enter 0. Afterward, print the total of all numbers entered.

user = int(input("Enter a number. press q to quit"))
emptyarray = []


while user != "q":
   # user = input("Enter a number")
    for eachnum in emptyarray:
        emptyarray.append(user)
        print(emptyarray)




# 5. Create an array of 4 names. Print one string that has all of the arrays separated by commas.
#
# nameArray = ["kenn", "kevin", "bob", "greg"]
#
# print(f"{nameArray[0]}, {nameArray[1]}, {nameArray[2]}, {nameArray[3]}")


# 6. Create a function that’s passed three integer numbers. Print the sum of the first two numbers and return the product of the second two numbers.
#
# def main():
#     user = int(input("enter a number"))
#     user2 = int(input("enter another number"))
#     user3 = int(input("enter another number"))
#     print(f"The sum of {user} and {user2} is {user+user2}.")
#     print(f"The product of {user2} and {user3} is {user2*user3}.")
# main()












# 7. Create the class Boardgame with name, price, pieceCount, and publisher properties/attributes. Create a class method that will change the price of the book. Outside of the class, create three objects of the class Boardgame. Print the three boardgame objects using the newly created objects.
#
# class Boardgaame:
#     def __init__(self, name, price, peicecount, publisher):
#         self.name = name
#         self. price = price
#         self. peicecount = peicecount
#         self.publisher = publisher
#
#     def changeprice(self, newprice):
#         self.price = newprice
#
#
# game1 = Boardgaame("monopoly", "$10", "1000", "disney")
# game2 = Boardgaame("trouble", "$10", "6", "hasbro")
# game3 = Boardgaame("sorry", "15", "40", "hasbro")
#
# gamearray = [game1, game2, game3]
#
# for eachgame in gamearray:
#     print(eachgame)


# 8. Create a function that takes a string array and returns a string array with the letter 's' at the end of each element. Call the function.

# def main():
#     thegals = ["PinkyPie", "Rarity", "Applejack", "RainboDash"]
#
#     print(f"{thegals[0]}'s, {thegals[1]}s', {thegals[2]}'s, {thegals[3]}'s")
#
# main()




# # 9. Create a function that has a parameter of an integer array and returns only the positive numbers in the array. Call the function
# def main():
#     myarray = [-1, 2, -3, 4, 5]
#     for eachnum in myarray:
#         if eachnum > 0:
#             print(eachnum)
#
# main()






# 10. Create a Puppy class. It should have properties name and color. Create a program that will ask a user to enter the name, then the color of a puppy until they enter 'q' to quit. Put each entry in an array.
# class Puppy:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#
#     def userask(self):
#         self.name = userN
#         self.color = userC
#
#
# userN = input("what is the dog's name. press q to quit")
# userC = input("what color is the dog. press q to quit")
# while userN != "q":
#     userN = input("what is the dog's name.")
#     userC = input("what color is the dog.")
#     print(f"The dog, {userN} is the color {userC}")
#
