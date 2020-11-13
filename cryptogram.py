from random import shuffle

class Game:
  def __init__(self):
    self.letters = list("abcdefghijklmnopqrstuvwxyz")
    self.exclude = " .,'!()?"

  def Shuffle(self):
    shuffle(self.letters)
    player = input("What would you like in the Cryptogram?")
    #Opens both files
    files = open("Origanal.txt","w")
    files.write("you typed: ")
    files.write(player)
    files.close()
    fil = open("Original.txt","w")
    fil.write("the Crytogram is \n")
    #the for loop get's the letter placement and put's it opisit place
    for letter in player:
      for number in range(26):
        if letter == self.letters[number]:
          newLetter = number - 25          
          fil.write(self.letters[newLetter])
        elif letter in self.exclude:
          fil.write(letter)
          break
    fil.close()      
game = Game()
game.Shuffle()
