import random
import time

print("Welcome to the Game of Thrones Life or Death simulator")

charcters = ["Eddard Ned Stark", "Robert Baratheon", "Jamie Lannister", "Catelyn Stark", "Cersie Lannister", "Daenerys Targaryen", "Jorah Mormont", "Petyr Littlefinger Baelish", "Viserys Targaryen", "Jon Snow", "Sansa Stark", "Arya Stark", "Robb Stark", "Theon Greyjoy", "Bran Stark", "Joffrey Baratheon", "Sandor The Hound Celgane", "Tyrion Lannister", "Davos Seaworth", "Samwell Tarly", "Margaery Tyrell", "Stannis Baratheon", "Melisandre", "Jeor Mormont", "Bronn", "Varys", "Shae", "Ygritte", "Talisa Maegyr", "Gendry", "Tormund Giantsbane", "Gilly", "Brienne of Tarth", "Ramsay Bolton", "Ellaria Sand", "Daario Naharis", "Missandei", "Jaqen Hghar", "Tommen Baratheon", "Roose Bolton", "The High Sparrow"]

print(" ")
print(" ")
time.sleep(1)
a1 = len(charcters)
results = []
outcome = []
def GOT():
    while True:
        print("There are", a1, "Charcters left.")
        global kill
        kill = int(input("How many Game of Thrones charcters would you like to kill off? "))
        if kill <= a1:
            for i in range(kill):
                global outcome


                outcome = random.choice(charcters)
                results.append(outcome)
                print(outcome)
        else:
            print("Pick a number between 0 and", a1, ".")
            continue
        return

GOT()
time.sleep(1)
print(" ")
print("Lets look at who lived and who died")
time.sleep(1)
a2 = len(outcome)
print("You killed this many charcters:", kill)
print("This many charcters are still alive:", a1 - kill)
print(" ")
if kill < 1:
    print("No one was killed!")
else:
    charcters.remove(outcome)


print(" ")
print("These charcters are still alive", charcters)
print(" ")
print("These charcters are dead", results)
