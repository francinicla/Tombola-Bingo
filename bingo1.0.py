import os, random

class Board(object):
    """Board creation"""
    matrix = []
    players = []
    player_name = []
    num_cards = []
    cards = []
    win = 0
    def __init__(self):
        self.matrix = Board.matrix
        for i in range(1, 91):
            self.matrix.append(i)

    def show(self):
        os.system("clear")
        self.matrix = Board.matrix
        print ("B I N G O by Claudio Francini")
        print(" __ __ __ __ __ __ __ __ __ __ ")
        for a in range(0, 9):
            for b in range (0, 10):
                c = (a * 10) + b
                print("|%02d" % (self.matrix[c]), end='')
            print("|")
        print("")
        for player in range(Board.players):
            for car_gio in range(Board.num_cards):
                print("___________________________________________________________________")
                print("|\t\t  Player %s - card %d  \t\t\t   |" % (Board.player_name[player], car_gio))
                pos_fin = Cards.position(Board.cards[player][car_gio])
                for p in range(3):
                    print("|", '\t'.join(repr(e) for e in pos_fin[p]), "|")
                print("-------------------------------------------------------------------")

class Rules(object):
    """Players e cards Rules creation."""

    def __init__(self):
        super(Rules, self).__init__()
        print("Welcome in the BINGO game!!")
        print("")
        a = input("How many players?: ")
        Board.players = int(a)
        b = input("How many cards for player?: ")
        Board.num_cards = int(b)
        for c in range(int(a)):
            name = input("Insert player name %d: " % (c))
            #print(name)
            Board.player_name.append(name)
        for player in range(Board.players):
            gio_cards = []
            for car_gio in range(Board.num_cards):
                cards = Cards
                gio_cards += cards.generate_card(Board.player_name, 'ughi'),
            Board.cards += gio_cards,

    def check_card(self, num_chosen):
        self.num_chosen = self
        number = num_chosen
        num_piece = number.draw_num()
        print("\nThe number extracted is: ", num_piece)
        Board.matrix[num_piece - 1] = 0
        check = num_piece
        zero = 0
        for czero in Board.cards:
            uno = 0
            for cuno in czero:
                due = 0
                for cdue in cuno:
                    tre = 0
                    for ctre in cdue:
                        if int(check) == int(ctre):
                            qui = Board.cards[zero][uno][due][tre]
                            Board.cards[zero][uno][due][tre] = 99
                        tre += 1
                    due += 1
                uno += 1
            zero += 1
        print("\nPress RETURN key to continue")
        input()

    def win(self):
        """ Check if you have done Lines or Bingo """
        self.num_chosen = self
        pla = 0

        for i in Board.cards:
            cardsl = 0
            for k in i:
                bingo = 0
                for l in k:
                    n = l.count(99)
                    bingo += n
                    if Board.win  == 0:
                        if n == 5:
                            print("\nTHE PLAYER %s WITH CARD NUMBER %s HAVE DONE CINQUINA!!!" % (Board.player_name[pla], cardsl))
                            Board.win  = 4
                if bingo == 15:
                    print("\nTHE PLAYER %s WITH CARD NUMBER %s HAVE DONE BINGO!!!!!!" % (Board.player_name[pla], cardsl))
                    exit()
                cardsl +=1
            pla +=1

class Cards(object):
    """Card creation"""
    num_chosen_cart = []
    cmatrix = []
    def __init__(self, number):
        self.number = number
        print("cards: ", self.number)

    def generate_card(self, name):
        num_cardslla = self
        player = name
        line_card = []
        mnum_chosen = []
        cmatrix = []
        cmatrix += Board.matrix
        for a in range(1,4):
            line_tupl = []
            mnum_chosen = []
            mnum_chosen += cmatrix
            for b in range(1,6):
                pulito = []
                for h in range(0,90):
                    if mnum_chosen[h] != ' ':
                        puli = mnum_chosen[h]
                        pulito += puli,
                chosen = random.choice(pulito)
                line_tupl += chosen,
                chosen = int(chosen)
                if chosen <= 10:
                    for g in range(0,10):
                        mnum_chosen[g] = ' '
                if chosen >= 11 and chosen <= 20:
                    for g in range(10,20):
                        mnum_chosen[g] = ' '
                if chosen >= 21 and chosen <= 30:
                    for g in range(20,30):
                        mnum_chosen[g] = ' '
                if chosen >= 31 and chosen <= 40:
                    for g in range(30,40):
                        mnum_chosen[g] = ' '
                if chosen >= 41 and chosen <= 50:
                    for g in range(40,50):
                        mnum_chosen[g] = ' '
                if chosen >= 51 and chosen <= 60:
                    for g in range(50,60):
                        mnum_chosen[g] = ' '
                if chosen >= 61 and chosen <= 70:
                    for g in range(60,70):
                        mnum_chosen[g] = ' '
                if chosen >= 71 and chosen <= 80:
                    for g in range(70,80):
                        mnum_chosen[g] = ' '
                if chosen >= 81 and chosen <= 90:
                    for g in range(80,90):
                        mnum_chosen[g] = ' '
                pippo = chosen -1
                cmatrix[pippo] = ' '
                line_tupl.sort()
            line_card += ((line_tupl),)
        return line_card

    def position(tupla):
        pos_final = []
        line_tupl = tupla
        for el in range (3):
            line_tupla = ['','','','','','','','','']
            for elem in range(5):
                if 0 < tupla[el][elem] < 11:
                    line_tupla[0] = tupla[el][elem]
                    continue
                elif 10 < tupla[el][elem] < 21:
                    line_tupla[1] = tupla[el][elem]
                    continue
                elif 20 < tupla[el][elem] < 31:
                    line_tupla[2] = tupla[el][elem]
                    continue
                elif 30 < tupla[el][elem] < 41:
                    line_tupla[3] = tupla[el][elem]
                    continue
                elif 40 < tupla[el][elem] < 51:
                    line_tupla[4] = tupla[el][elem]
                    continue
                elif 50 < tupla[el][elem] < 61:
                    line_tupla[5] = tupla[el][elem]
                    continue
                elif 60 < tupla[el][elem] < 71:
                    line_tupla[6] = tupla[el][elem]
                    continue
                elif 70 < tupla[el][elem] < 81:
                    line_tupla[7] = tupla[el][elem]
                    continue
                elif 80 < tupla[el][elem] <= 91:
                    line_tupla[8] = tupla[el][elem]
                    continue
            pos_final += line_tupla,
        return pos_final

class Numbers(object):
    num_chosen = []
    """Creazione sacchetto dei Numbers."""
    def __init__(self):
        self.draw = Numbers.num_chosen
        for i in range(1, 91):
            self.draw.append(i)
        Numbers.num_chosen = self.draw


    def draw_num(self):
        """Pesca un number e lo elimina dalla lista bingo"""
        self.number = Numbers.num_chosen
        self.mischia = random.shuffle(self.number)
        self.chosen = self.number[0]
        self.number.pop(0)
        return self.chosen

if __name__ == '__main__':
    gioco = Board()
    rules = Rules()
    draw = Numbers()
    rules
    while True:
        gioco.show()
        rules.win()
        rules.check_card(draw)
