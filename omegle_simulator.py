import random

class omegle():
    def idk(self):
        while True:
            try:
                age = int(input("age?"))
                if age >= 18:
                    print(age + 2)
                    question2 = str(input("M or F?"))
                    if question2 in ["m", "M", "male", "Male"]:
                        break
                    if question2 in ["f", "F", "female", "Female"]:
                        answer1 = str(input("pic?"))
                        if answer1 in ["n", "N", "no", "No", "NO"]:
                            break
                if answer1 in ["y", "Y", "Yes", "YES"]:
                    name1 = ["Jo", "Jam", "Will", "Dav", "Matt", "Rus"]
                    name2 = ["chez", "phy", "ward"]
                    randname1 = random.choice(name1)
                    randname2 = random.choice(name2)
                    name = (randname1 + randname2)
                    print("snap = @" +name)
                    break
                else:
                    break
            finally:
                print("bye")
bot = omegle
bot.idk(1)
