#Written by TheSpaceCowboy
#Date 12/08/17
#Coding challange from: http://usingpython.com/python-programming-challenges/

def star(length):#Finds the amount fo stars i need to print
    
    stars = []#Array to store the amount of stars
    
    for x in range(0,length):#For each char in the name add a star
        
        stars.append("*")
        
    stars = "".join(stars)#Turns the array into a string
    
    return stars#Returns the ammount of stars required for the banner

def bannerMaker(name):#Makes the name
    
    length = len(name)+2#Gets the length of the name
    s = star(length)#Gets the ammount of stars needed for the banner
    
    print(s)#Prints stars
    print("*"+name+"*")#Prints name
    print(s)#Prints stars
    




bannerMaker(input("Input your name please: "))#Gets input
