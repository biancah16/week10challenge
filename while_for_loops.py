#while loops-execute some code WHILE some condition remains true
#while loops and while loops are forms of iteratoin
#iteration is the process of repeating ir looping through a set of sets or intreuctions 
#to iterate is the verb
#form of iteratrion
#be careful of infinite loops
#they will crash your program
#and you will have to restart it
#infinite loops are loops that never end


# name = input ("enter ur name: ")
# while name== " ":
#     print("you didnt enter your name")#while loop
#     name= input ("enter your name: ")
# print(f"hello {name}")#getting out the loop


# age = int(input("enter your age: "))

# while age <0:
#     print("age cant be negative")
#     age= int(input("enter your age: "))

#  print(f"you are {age} years old")
# food = input("enter a good you like(q to quit): ")

# while not food == "q":
#     print(f"you like{food}")
#     food = input("enter another food you like(q to quit): ")

# print("bye")
# num=int(input("enter a number between 1 -10: "))

# while num < 1 or num > 10:
#    print(f"{num} is not valid")
#    num = int(input("enter a # between 1-10"))

# print(f"your number is {num}")

####################################################################
#for loops - execute a block of code a fixed number of times
             #you can iterate overa range, string, sequence, ect
#iterable has to b a list of things
#reversed reverses it

# for x in range(1, 11, 2 ):#, is exclusive
#    print(x)


# credit_card = "1234-5678-3456"

# for x in credit_card: #x becomes each number and prints thhem all
#     print(x)

# for x in range(1, 21):
#     if x == 13 or x==15:
#         continue#skip over
#     else:
#         print(x)

# for x in range(1, 21):
#     if x == 13:
#         break#stops there)
#     else:
#         print(x)

######################chalenge 1###########
horror_movies= ['the exorcist', 'the shinning' , 'the conjuring', 'the ring']
#loop through the lift of horro movies
#if the name is 'the shinning', print 'the shinninng
#otherwise, print 'the shinning was not found!' and 
#print out the other names using a loop\
for movie in horror_movies:
    if movie == 'the shinning':
        print('the shining is found')
        print(movie)
        break
    else:
        print("the shinning was not found")
        print(movie)

#########CHALLENGE 2#############
        
horror_characters= ['penywise' , 'ghostface' , 'freddy krueger' , 'chucky']
for character in horror_characters:
    if character == 'freddy krueger':
        continue
    else:
        print(character)

##########challenge 3##########
horror_monsters= ['babadook' , 'swampthing' , 'frankenstien' , 'beatlejuice']
for monster in horror_monsters:
    if monster == 'swampthing':
        print(monster.replace("godzilla"))
    else:
        print(monster)
