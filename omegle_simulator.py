import random

def txt():

   while True:
    try:
        age = int(input("age?"))

        if age >= 18:
            print(age + 2)
            name1 = ["Jo", "Jam", "Will", "Dav", "Matt", "Rus"]
            name2 = ["chez", "phy", "ward"]
            answer2 = str(input("M or F?"))
            answer1 = str(input("pic?"))
            randname1 = random.choice(name1)
            randname2 = random.choice(name2)
            name = (randname1 + randname2)
        if answer2 in ["m", "M"]:
            break
        if answer2 in ["f", "F"]:

         if answer1 in ["n", "N", "no", "No", "NO"]:
                break
        elif answer1 in ["y", "Y", "Yes", "YES"]:
                print("snap = @" +name)
                break

        else:
            break
    finally:
        print("bye")


txt()
