import random


class Game:
    def __init__(self, name="Unknow", game_card=[]):
        self.name: str = name
        self.point: int = 0
        self.card: dict = {}
        self.game_card: list = game_card


    def start(self):
        self.point = 0
        for i in range(2):
            a = random.choice(list(self.game_card[0].keys()))
            self.point += self.game_card[1][a]
            self.card[a] = self.game_card[0].pop(a)
            # del self.game_card[0][a]
        print(self.name)
        print("Yor's cards: ", self.card)
        print("You have at ", self.point, " point's")
        return self.card, self.point, self.game_card

    def step(self):
        print(self.name)
        answer = input("are you want to take more? y/n:")
        if answer == 'y':
            a = random.choice(list(self.game_card[0].keys()))
            self.card[a] = self.game_card[0][a]
            self.point += self.game_card[1][a]
            print("It's ", self.game_card[0][a])
            del self.game_card[0][a]
        print("Yor's cards: ", self.card)
        print("You have at ", self.point, " point's")
        if self.point > 21:
            print("Game Over")
            answer = "end"
        print("**************************************************************************")
        return self.card, self.point, self.game_card, answer



mast = ("cherv", "bub", "pik", "tref")
nominal = (2, 3, 4, 5, 6, 7, 8, 9, 10, "valet", "dama", "korol", "tuz")
koloda: list = [{}, {}]
id = 0
for i in nominal:
    for j in mast:
        koloda[0][id] = str(i)+"_"+j
        if type(i) == int:
            koloda[1][id] = i
        else:
            if i != "tuz":
                koloda[1][id] = 10
            else:
                koloda[1][id] = 11
        id += 1

gamer_one = Game("Evgeniy", koloda)
o4ko = gamer_one.start()

gamer_two = Game("Marina", o4ko[2])
o4ko_2 = gamer_two.start()

a_1, a_2 = 'y', 'y'
while True:
    if a_1 == 'y':
        o4ko = gamer_one.step()
        a_1 = o4ko[3]
        if a_1 == 'end':
            break
    if a_2 == 'y':
        o4ko_2 = gamer_two.step()
        a_2 = o4ko_2[3]
        if a_2 == 'end':
            break
    if a_1 and a_2 != 'y':
        if o4ko[1] > o4ko_2[1]:
            print("Win Evgeniy")
        elif o4ko[1] < o4ko_2[1]:
            print("Win Marina")
        else:
            print("Your's win TWO! ) Congratulate!")
        break
