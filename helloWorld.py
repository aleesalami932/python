class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def setAge(self):
        self.age = input("please enter age: ")

    def setFirstName(self):
        self.firstName = input("please enter first name: ")

    def setLastName(self):
        self.lastName = input("please enter last name: ")

    def getAge(self):
        return self.age

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName


def findOldestPerson(personList):
    if(len(personList) == 0):
        print("no data found")
        print("<--------------------------------------->")
        return

    oldest = personList[0]
    for person in personList:
        if(int(person.getAge()) > int(oldest.getAge())):
            oldest = person
    sent = "%s %s is the oldest of age:%s "
    print("<--------------------------------------->")
    print(sent % (oldest.getFirstName(), oldest.getLastName(), oldest.getAge()))


def listPersons(personList):
    sent = "%s %s, age: %s, index: %d"
    if(len(personList) == 0):
        print("no data found")
        print("<--------------------------------------->")
        return
    i = 0
    print("<--------------------------------------->")
    for person in personList:
        print(sent % (person.getFirstName(),
              person.getLastName(), person.getAge(), i+1))
        print("<--------------------------------------->")
        i = i + 1

    key = input("edit ? y/n: ")
    if(key == "y"):
        selectPersonToEdit(personList)
    else:
        return


def selectPersonToEdit(personList):
    print("<--------------------------------------->")
    key = int(input("please select index "))
    if(key <= len(personList)):
        personToEdit = personList[key-1]
        personToEdit.setFirstName()
        personToEdit.setLastName()
        personToEdit.setAge()
    else:
        print("please select a valid index")
        selectPersonToEdit(personList)


def createPerson(personList):
    p = Person("", "", "")
    print("<--------------------------------------->")
    p.setFirstName()
    p.setLastName()
    p.setAge()
    personList.append(p)
    print("<--------------------------------------->")
    key = input("one more ? y/n: ")
    if(key == "y"):
        createPerson(personList)
    elif(key == "n"):
        return
    else:
        print("fuck you wrong input")


personList = []
i = 0
while i >= 0:
    print("<--------------------------------------->")
    print("to create person press 1")
    print("to list person press 2")
    print("to find oldest person press 3")
    print("to exit press 0")
    print("<--------------------------------------->")

    key = input(" choose action: ")
    if(key == "0"):
        i = -1
    elif (key == "1"):
        createPerson(personList)
    elif (key == "2"):
        listPersons(personList)
    elif (key == "3"):
        findOldestPerson(personList)
    else:
        print("fuck you wrong input")
