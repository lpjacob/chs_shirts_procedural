import time

"""References - based on code at:
https://www.tutorialspoint.com/How-to-iterate-through-a-dictionary-in-Python
https://www.geeksforgeeks.org/python-check-if-a-variable-is-string/ 
https://towardsdatascience.com/sorting-a-dictionary-in-python-4280451e1637
"""
#setup global variables here:
shirtsQueue = [] # empty list to act as a queue for shirts 

def pushQueue(shirt):
    """add a shirt item to end of global queue"""
    global shirtsQueue
    shirtsQueue.append(shirt)
    print("Shirt added")
    return 

def popQueue():
    """remove and return a shirt from global queue"""
    global shirtsQueue
    if len(shirtsQueue) !=0:
        currentShirt = shirtsQueue.pop(0)
        return currentShirt
    else: 
        print("there are no shirts to remove")
        return None

def validateChoice():
    """validate menu choice is an int between 1 and 7, loops if not"""
    while True:
        choiceInput= input("enter a choice")
        if choiceInput.isnumeric():
            choiceInput = int(choiceInput)
            if choiceInput < 8 and choiceInput >0:
                return choiceInput
            else:
                print("Must enter a number between 1 and 72")
        else:
            print("must enter a valid number!")

def displayShirts():
    """Option 1 - print all items in global queue - to treat as queue, items must be popped off and pushed back in """
    global shirtsQueue
    numShirts = len(shirtsQueue)# get starting len of shirtQueue to avoid infinite loop
    counter = 0
    if numShirts == 0:
        print("Sorry no shirts to display")
        time.sleep(1)
    else:
        while counter < numShirts:
            currentShirt = popQueue()
            print("------------------------------")
            print("Shirt ", counter)
            print("------------------------------")
            for k in currentShirt.keys():
                print(k,": "," \t", currentShirt[k])
            time.sleep(1)
            pushQueue(currentShirt)
            counter+=1
    
def addShirts():
    """Option2 - add a new shirt to global queue"""
    global shirtsQueue
    shirtTemplate = {"colour":"colour","pattern":"pattern", "price":1.11, "style":"style"}#create a dictionary that will define the structure and data types
    print("------------------------------")
    print("Create a new shirt")
    print("------------------------------")
    for k in shirtTemplate.keys():
        print("Value for", k)
        if isinstance(shirtTemplate[k], str):
            shirtTemplate[k] = input("Enter text")
        elif isinstance(shirtTemplate[k],float):
            while True:
                try:
                    shirtTemplate[k] = float(input("Enter decimal number"))
                    break
                except:
                    print("Not a valid decmial number")
        else:
            print("something went wrong with the shirt")
            break
    pushQueue(shirtTemplate)

def validateRemove():
    global shirtsQueue
    """validate menu choice is an int in length of global queue, loops if not"""
    while True:
        choiceInput= input("enter a choice")
        if choiceInput.isnumeric():
            choiceInput = int(choiceInput)
            if choiceInput < len(shirtsQueue) and choiceInput >=0:
                return choiceInput
            else:
                print("Must enter a number between 0 and ", len(shirtsQueue)-1)
        else:
            print("must enter a valid number!")

def removeShirt():
    global shirtsQueue
    """Option 3 - remove a shirt from global queue based on an integer entered by user"""
    print("------------------------------")
    print("Delete a shirt")
    print("------------------------------")
    print("A list of shirts will be shown - pick its shirt number to delete")
    displayShirts()#print all shirts for user to choose from 
    choice = validateRemove()
    numShirts = len(shirtsQueue)
    counter = 0
    while counter < numShirts:
        currentShirt = popQueue()
        if choice != counter:
            pushQueue(currentShirt)#add shirt back to end of queue
        else:
            print("Shirt ", counter, "deleted")
        counter+=1

def priceUpdate():
    global shirtsQueue
    """Option 6 - remove a shirt from global queue based on an integer entered by user"""
    print("------------------------------")
    print("Update a shirt price")
    print("------------------------------")
    print("A list of shirts will be shown - pick its shirt number to update price")
    displayShirts()#print all shirts for user to choose from 
    choice = validateRemove()
    numShirts = len(shirtsQueue)
    counter = 0
    while counter < numShirts:
        currentShirt = popQueue()
        if choice == counter:
            while True:
                try:
                    newPrice = float(input("Enter new price as a decimal"))
                    currentShirt["price"]= newPrice
                    break
                except:
                    print("sorry, not a valid price")     
        pushQueue(currentShirt)#add shirt back to end of queue
        counter+=1


def searchStyle():
    """Option 4 - prints all shirts in global queue that have an exact syle match for the user's input"""
    global shirtsQueue
    print("------------------------------")
    print("Search for shirts by Style")
    print("------------------------------")
    styleChoice = input("Enter you choice of style") 
    if len(styleChoice) <2:
        print("Can't search for that")
    else:
           numShirts = len(shirtsQueue)
    counter = 0
    while counter < numShirts:
        currentShirt = popQueue()
        if currentShirt["style"] == styleChoice:
            for k in currentShirt.keys():
                print(k,": "," \t", currentShirt[k])
            time.sleep(1)
        pushQueue(currentShirt)#add shirt back to end of queue
        counter +=1

def displaySortedShirts(sortedShirts):
    """accepts a sorted list of dictionaries as a parameter.
    Iterate over list of sorted shirts and prints all keys """
    print("------------------------------")
    print("All shirts sorted by Price")
    print("------------------------------")
    for i in range(0, len(sortedShirts)):
        print("Shirt ", i, ":")
        currentShirt = sortedShirts[i]
        for k in currentShirt.keys():
            print(k,": "," \t", currentShirt[k])
        time.sleep(1)


def sortPrice():
    """Option 5 - uses a built in function to sort the queue in to a new list by price
    A lambda is used tell the sorted function what to sort by
    you don't need to know how these work 
    """
    global shirtsQueue
    numShirts = len(shirtsQueue)# get starting len of shirtQueue 
    if numShirts > 0:
        sortedPrice = sorted(shirtsQueue, key= lambda d:d["price"] )#makes a copy of the queue in to a sorted list structure
        displaySortedShirts(sortedPrice)
    else:
        print("No shirts to sort")

def searchCriteria():
    """Option 7 - search global queue by colour and pattern"""
    global shirtsQueue
    print("------------------------------")
    print("Search for shirts by Colour and Pattern")
    print("------------------------------")
    colourChoice = input("Enter you choice of Colour") 
    patternChoice = input("Enter you choice of Pattern")
    if len(patternChoice) <2 or len(colourChoice)<2:
        print("Can't search for that")
    else:
        numShirts = len(shirtsQueue)
        counter = 0
        while counter < numShirts:
            currentShirt = popQueue()
            if currentShirt["colour"] == colourChoice and currentShirt["pattern"] == patternChoice:
                print("GOOD MATCH")
                for k in currentShirt.keys():
                    print(k,": "," \t", currentShirt[k])
                time.sleep(1)
            elif currentShirt["colour"] == colourChoice or currentShirt["pattern"] == patternChoice:
                print("CLOSE MATCH")
                for k in currentShirt.keys():
                    print(k,": "," \t", currentShirt[k])
                time.sleep(1)
            pushQueue(currentShirt)#add shirt back to end of queue
            counter +=1
        
def menuActions(choice):
    """call function based on user's menu choice"""
    if choice == 1:
        displayShirts()
    elif choice == 2:
        addShirts()
    elif choice == 3:
        removeShirt()
    elif choice == 4:
        searchStyle()
    elif choice == 5:
        sortPrice()
    elif choice ==6:
        priceUpdate()
    elif choice == 7:
        searchCriteria()
    else:
        print("Sorry, can't do that yet")
        time.sleep(1)
    return

def main():
   choice = 0
   while True:
       print("-----------------------------------------")
       print("Welcome to the Shirt Selector Main Menu")
       print("-----------------------------------------")
       print("""
       Press 1 to display current shirts
       Press 2 to add a shirt
       Press 3 to remove a shirt
       Press 4 to search for a shirt by style name
       Press 5 to display shirts ordered by price
       Press 6 to update price of a shirt
       Press 7 to search for a shirt by 2 criteria
       """)
       choice = validateChoice()#get user input
       menuActions(choice)#decide what user input is 

if __name__ == '__main__':
    main() 