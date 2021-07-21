from random import shuffle #the shuffle function allows us shuffle the deck

print("welcome")
def create_deck():
    #the first step is to create a card deck
    deck=[]

    facevalues=['A','K','Q','J']
    for i in range(4):#this creates the suits for the deck
        for card in range(2,11):#this ids for the regular cards
            deck.append(str(card))

        for card in facevalues:
            deck.append(card)

    shuffle(deck)

    return deck
 
class players:
    def __init__(self,cardds=[],money=100):
        self.hand=cardds
        self.score=self.setscore()
        self.cash=money
        self.bet=0


    def __str__(self): 
        currenthand=" "
        for card in self.hand:
            currenthand+=str(card)+" "

        finalstatus=currenthand + 'score: '+str(self.score)
        return finalstatus
    
    def setscore(self):
        self.score=0
        facevaluedict={"A":10,"J":10,"K":10,"Q":10,"2":2,"3":3,"4":4,"5":5,
        "6":6,"7":7,"8":8,"9":9,"10":10}
        for card in self.hand:
            self.score+=facevaluedict[card]
        
        return self.score

    def hit(self,card):
        self.hand.append(card)
        self.score=self.setscore()

    def play(self, newhand):
        self.hand=newhand
        self.score=self.setscore()

    def betmoney(self,betplaced):
        self.cash-=betplaced#this means we are deducting the bet placed from the amount of money a player already has
        self.bet+=betplaced#

    def win(self,success=False):
        if success==True:
            if self.score==21 and len(self.hand)==2:
                self.money+=2.5*self.bet
            else:
                self.cash+=2*self.bet

            self.bet=0
        else:
            self.bet=0

    def draw(self):
        self.cash+=self.bet
        self.bet=0

    def blackjack(self):
        if self.score==21 and (len(house.hand)):
            return True
        else:
            return False



def housecards(house):
    for card in range(len(house.hand)):
        if card==0:
            print("x", end=" ")
        if card==len(house.hand)-1:
            print(house.hand[card])


cardDeck=create_deck()
print(cardDeck)
firsthand=[cardDeck.pop(),cardDeck.pop()]#the pop method takes out the last item from a list
secondhand=[cardDeck.pop(),cardDeck.pop()]

player1=players(firsthand)
house=players(secondhand)

cardDeck=create_deck()
while(True):
    if len(cardDeck) <20:
        cardDeck=create_deck()

    firsthand=[cardDeck.pop(),cardDeck.pop()]
    secondhand=[cardDeck.pop(),cardDeck.pop()]

    player1=players(firsthand)
    house=players(secondhand)

    BET=int(input("please enter your bet: "))
    player1.betmoney(BET)
    print(player1)
    housecards(house)
    print(house)
    if player1.blackjack():#remember to use parentheses so you can call methods
        if house.blackjack():
            player1.draw()
        else:
            player1.win=True


    else:
        while (player1.score<21):
            action=input('do you want another card?(y/n)')
            if action =="y":
                player1.hit(cardDeck.pop())
                print(player1)
                print(house)
            else:
                break
                
        while (house.score<16):
            house.hit(cardDeck.pop())

        if player1.score>21:
            if house.score>21:
                player1.draw()
            else:
                player1.win(False)

        elif player1.score>house.score:
            player1.win(True)

        elif player1.score==house.score:
            player1.draw()

        else:
            if house.score>21:
                player1.win(True)
            else:
                player1.win(False)


    print(player1.cash)
    print(house)




#this portion of the code was used to check if the code was functional at various stages, this helps you spot errors early
"""player1=players(['4','7'])
print(player1)
player1.hit('A') 
print(player1)
player1.betmoney(30) 
print(player1.cash,player1.bet)  
player1.play(["A","K"])
print(player1)
player1.bet(40)
print(player1.cash)
player1.win(True)
print(player1.cash,player1.bet)"""