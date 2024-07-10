import random

suites = ('S','H','D','C')
cards = ('A','K','Q','J','9','8','7','6','5','4','3','2','1')
ls = [s+""+c for s in suites for c in cards]
random.shuffle(ls)

class Player:

    def __init__(self, name,plist):
        self.name = name
        self.plist = plist

    def __str__(self):
        return f"{self.name} {self.plist}"

    def get_list(self):
        return self.plist
    def play_round(self,iswar):
        if iswar:
            # Return the 4 items on the list
            if len(self.plist) < 4:
                retls = self.plist[:-1]
                self.plist = self.plist[-1]
                ##print("self.plist for less than 4 len : " , self.plist , "returned ls = " , retls)
                return retls
            else:
                retls = self.plist[:3]
                self.plist = self.plist[3:]
                return retls
        else:
            # Return only the 1st item on the list
            return self.plist.pop(0)

    def add_cards(self,card1,card2):
        self.plist.append(card1)
        self.plist.append(card2)

    def extend_cards(self,cardstoextend):
        self.plist.extend(cardstoextend)

def __main__():
    """
    War game with 2 players
    Deck of 52 cards - shuffled
    Deck divided equally between 2 players
    Player 1 and Player 2 maintain 2 lists

    Each round is played
    If war next 4 items are collected and played again


    :param args:
    :return:
    """
    print("Welcome to War Game")
    player1 = Player("Player 1",ls[0:26])
    #print("Player 1 will start playing")
    #print(player1)
    player2 = Player("Player 2", ls[26:])
    #print("Player 2 will start playing")
    #print(player2)

    iswar = False
    i=True
    counter = 1
    tmpls_war = []
    while i:
        #print("XXXX Playing Round: " , counter)
        counter = counter + 1
        p1card = player1.play_round(iswar)
        p2card = player2.play_round(iswar)
        #print("p1card" , p1card[1] , " XX p2card" , p2card[1])
        if cards.index(p1card[1]) == cards.index(p2card[1]):
            iswar = True
            #print("-> Player 1 and Player 2 at War now! <-")
            pls1 = player1.play_round(iswar)
            pls2 = player2.play_round(iswar)
            if len(pls1) < 3:
                print("PLAYER 2 WINS THE GAME")
                break
            elif len(pls2)<3:
                print("PLAYER 1 WINS THE GAME")
                break
            tmpls_war.extend(pls2)
            tmpls_war.extend(pls1)
            tmpls_war.append(p1card)
            tmpls_war.append(p2card)
            #print("tmpls_war" , tmpls_war)
            iswar = False
            continue
        elif cards.index(p2card[1]) > cards.index(p1card[1]):
            iswar = False
            player1.add_cards(p1card,p2card)
            if(len(tmpls_war) > 0):
                random.shuffle(tmpls_war)
                player1.extend_cards(tmpls_war)
                tmpls_war = []

        elif cards.index(p2card[1]) < cards.index(p1card[1]):
            iswar = False
            player2.add_cards(p2card, p1card)
            if (len(tmpls_war) > 0):
                random.shuffle(tmpls_war)
                player2.extend_cards(tmpls_war)
                tmpls_war = []
        #print("END OF ROUND")
        #print("Player 1 : ", "len: p1", len(player1.get_list()), "\n -> ls: ", player1.get_list())
        #print("Player 2 : ", "len: p2", len(player2.get_list()), "\n -> ls: ", player2.get_list())

        if counter >= 1000 or len(player1.get_list())==0 or len(player2.get_list()) == 0:
            if len(player1.get_list()) == 0 :
                print("PLAYER 2 WINS THE GAME")
            elif len(player2.get_list()) == 0:
                print("PLAYER 1 WINS THE GAME")
            break

__main__()
