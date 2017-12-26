import os, random

class Tabellone(object):
    """Creazione del Tabellone."""
    matrice = []
    giocatori = []
    nome_giocarore = []
    num_cartelle = []
    cartelle = []
    vincita = 0
    def __init__(self):
        self.matrice = Tabellone.matrice
        for i in range(1, 91):
            self.matrice.append(i)

    def visualizza(self):
        os.system("clear")
        self.matrice = Tabellone.matrice
        print ("T O M B O L A by Claudio Francini")
        print(" __ __ __ __ __ __ __ __ __ __ ")
        for a in range(0, 9):
            for b in range (0, 10):
                c = (a * 10) + b
                print("|%02d" % (self.matrice[c]), end='')
            print("|")
        print("")
        for player in range(Tabellone.giocatori):
            for car_gio in range(Tabellone.num_cartelle):
                print("___________________________________________________________________")
                print("|\t\t  Giocatore %s - cartella %d  \t\t\t   |" % (Tabellone.nome_giocarore[player], car_gio))
                pos_fin = Cartelle.posizione(Tabellone.cartelle[player][car_gio])
                for p in range(3):
                    print("|", '\t'.join(repr(e) for e in pos_fin[p]), "|")
                print("-------------------------------------------------------------------")

class Regolamento(object):
    """Creazione giocatori e cartelle Regolamento."""

    def __init__(self):
        super(Regolamento, self).__init__()
        print("Benvenuti al gioco della tombola!!")
        print("")
        a = input("Quanti giocatori vuoi?: ")
        Tabellone.giocatori = int(a)
        b = input("Quante cartelle per giocatore?: ")
        Tabellone.num_cartelle = int(b)
        for c in range(int(a)):
            nome = input("Inserisci nome del giocatore %d: " % (c))
            print(nome)
            Tabellone.nome_giocarore.append(nome)
        for player in range(Tabellone.giocatori):
            gio_carte = []
            for car_gio in range(Tabellone.num_cartelle):
                carte = Cartelle
                gio_carte += carte.genera_cartella(Tabellone.nome_giocarore, 'ughi'),
            Tabellone.cartelle += gio_carte,

    def controlla(self, numeri):
        self.numeri = self
        numero = numeri
        pedina = numero.pesca_num()
        print("\nIl numero estratto è: ", pedina)
        Tabellone.matrice[pedina - 1] = 0
        check = pedina
        zero = 0
        for czero in Tabellone.cartelle:
            uno = 0
            for cuno in czero:
                due = 0
                for cdue in cuno:
                    tre = 0
                    for ctre in cdue:
                        if int(check) == int(ctre):
                            qui = Tabellone.cartelle[zero][uno][due][tre]
                            Tabellone.cartelle[zero][uno][due][tre] = 99
                        tre += 1
                    due += 1
                uno += 1
            zero += 1
        print("\nPremi il tasto INVIO")
        input()

    def vincita(self):
        """ Controlla se hai fatto Ambo, Terna, Quaterna, Cinquina o Tombola """
        self.numeri = self
        giocat = 0

        for i in Tabellone.cartelle:
            cartel = 0
            for k in i:
                tombola = 0
                for l in k:
                    n = l.count(99)
                    tombola += n
                    if Tabellone.vincita == 0:
                        if n == 2:
                            print("\nIL GIOCATORE %s CON LA CARTELLA %s HA FATTO AMBO!!!" % (Tabellone.nome_giocarore[giocat], cartel))
                            Tabellone.vincita  = 1
                    if Tabellone.vincita  == 1:
                        if n == 3:
                            print("\nIL GIOCATORE %s CON LA CARTELLA %s HA FATTO TERNA!!!" % (Tabellone.nome_giocarore[giocat], cartel))
                            Tabellone.vincita  = 2
                    if Tabellone.vincita  == 2:
                        if n == 4:
                            print("\nIL GIOCATORE %s CON LA CARTELLA %s HA FATTO QUATERNA!!!" % (Tabellone.nome_giocarore[giocat], cartel))
                            Tabellone.vincita  = 3
                    if Tabellone.vincita  == 3:
                        if n == 5:
                            print("\nIL GIOCATORE %s CON LA CARTELLA %s HA FATTO CINQUINA!!!" % (Tabellone.nome_giocarore[giocat], cartel))
                            Tabellone.vincita  = 4
                if tombola == 15:
                    print("\nIL GIOCATORE %s CON LA CARTELLA %s HA FATTO TOMBOLA!!!!!!" % (Tabellone.nome_giocarore[giocat], cartel))
                    exit()
                cartel +=1
            giocat +=1

class Cartelle(object):
    """Creazione Cartelle."""
    numeri_cart = []
    cmatrice = []
    def __init__(self, numero):
        self.numero = numero
        print("cartelle: ", self.numero)

    def genera_cartella(self, nome):
        num_cartella = self
        player = nome
        riga_cartella = []
        mnumeri = []
        cmatrice = []
        cmatrice += Tabellone.matrice
        for a in range(1,4):
            riga = []
            mnumeri = []
            mnumeri += cmatrice
            for b in range(1,6):
                pulito = []
                for h in range(0,90):
                    if mnumeri[h] != ' ':
                        puli = mnumeri[h]
                        pulito += puli,
                scelto = random.choice(pulito)
                riga += scelto,
                scelto = int(scelto)
                if scelto <= 10:
                    for g in range(0,10):
                        mnumeri[g] = ' '
                if scelto >= 11 and scelto <= 20:
                    for g in range(10,20):
                        mnumeri[g] = ' '
                if scelto >= 21 and scelto <= 30:
                    for g in range(20,30):
                        mnumeri[g] = ' '
                if scelto >= 31 and scelto <= 40:
                    for g in range(30,40):
                        mnumeri[g] = ' '
                if scelto >= 41 and scelto <= 50:
                    for g in range(40,50):
                        mnumeri[g] = ' '
                if scelto >= 51 and scelto <= 60:
                    for g in range(50,60):
                        mnumeri[g] = ' '
                if scelto >= 61 and scelto <= 70:
                    for g in range(60,70):
                        mnumeri[g] = ' '
                if scelto >= 71 and scelto <= 80:
                    for g in range(70,80):
                        mnumeri[g] = ' '
                if scelto >= 81 and scelto <= 90:
                    for g in range(80,90):
                        mnumeri[g] = ' '
                pippo = scelto -1
                cmatrice[pippo] = ' '
                riga.sort()
            riga_cartella += ((riga),)
        return riga_cartella

    def posizione(tupla):
        pos_final = []
        riga = tupla
        for el in range (3):
            linea = ['','','','','','','','','']
            for elem in range(5):
                if 0 < tupla[el][elem] < 11:
                    linea[0] = tupla[el][elem]
                    continue
                elif 10 < tupla[el][elem] < 21:
                    linea[1] = tupla[el][elem]
                    continue
                elif 20 < tupla[el][elem] < 31:
                    linea[2] = tupla[el][elem]
                    continue
                elif 30 < tupla[el][elem] < 41:
                    linea[3] = tupla[el][elem]
                    continue
                elif 40 < tupla[el][elem] < 51:
                    linea[4] = tupla[el][elem]
                    continue
                elif 50 < tupla[el][elem] < 61:
                    linea[5] = tupla[el][elem]
                    continue
                elif 60 < tupla[el][elem] < 71:
                    linea[6] = tupla[el][elem]
                    continue
                elif 70 < tupla[el][elem] < 81:
                    linea[7] = tupla[el][elem]
                    continue
                elif 80 < tupla[el][elem] <= 91:
                    linea[8] = tupla[el][elem]
                    continue
            pos_final += linea,
        return pos_final

class Numeri(object):
    numeri = []
    """Creazione sacchetto dei Numeri."""
    def __init__(self):
        self.pesca = Numeri.numeri
        for i in range(1, 91):
            self.pesca.append(i)
        Numeri.numeri = self.pesca


    def pesca_num(self):
        """Pesca un numero e lo elimina dalla lista"""
        self.numero = Numeri.numeri
        self.mischia = random.shuffle(self.numero)
        self.scelto = self.numero[0]
        self.numero.pop(0)
        return self.scelto

if __name__ == '__main__':
    gioco = Tabellone()
    rules = Regolamento()
    pesca = Numeri()
    rules
    while True:
        gioco.visualizza()
        rules.vincita()
        rules.controlla(pesca)
