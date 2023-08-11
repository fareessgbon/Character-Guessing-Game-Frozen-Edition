def character_descriptions():
  Elsa = "\033[1;37;40m\n\nElsa\nElsa is a blue-eyed, white-haired princess born with the power to create ice and snow, which she keeps under wraps from her kingdom. When she is crowned Queen, however, her secret is revealed. She runs away and hides in the mountains in fear. When her sister, Anna, finds her, she panics and accidentally curses her. She returns to Arendelle to help save her sister and, that accomplished, she returns to the throne."
  Anna = "\033[1;37;40m\n\nAnna\nAnna is green-eyed, red-haired younger princess of Arendelle. After her sister Elsa, the newly crowned Queen, disappears into the mountains Anna launches a quest to find her. Upon arriving at her new ice palace, she is cursed. She returns to Arendelle to search for a cure when her sister finds her and breaks the curse with true love."
  Kristoff = "\033[1;37;40m\n\nKristoff\nKristoff is a blonde, brown-eyed seasonal ice harvester. At a young age, he, and his reindeer companion named Sven, were adopted by trolls. He meets Princess Anna at a Trading Post and is coerced into helping her locate her sister. When Anna is cursed upon their arrival to her sister's palace, they part ways, with her going to Arendelle to find a cure. Later on, he returns to Arendelle to save Anna after realizing that his love for her may be the cure."
  Hans = "\033[1;37;40m\n\nHans\nHans is the Prince of the Southern Isles. He has red hair, sideburns, and green eyes. He rides a horse named Sitron. He seduces Anna, the princess of Arendelle, with the goal of killing her sister Elsa, the new Queen, to rise through to the throne. However, his plans are thwarted when Anna and Kristoff discover and halt them, leading to his imprisonment and Elsa\'s survival."
  Olaf = "\033[1;37;40m\n\nOlaf\nOlaf is a living snowman who loves the idea of summer. Originally created when Anna and Elsa were children, he was remade and given life shortly after Elsa, the new Queen\'s, coronation. He helps his companions Anna and Kristoff locate Elsa to end the Eternal Winter she cursed Arendelle with, and later on escape her bodyguard. He offers emotional support to Anna when she is cursed as well, before finally having his dream of experiencing summer come true when both Anna\'s and Arendelle\'s curse breaks."
  Sven = "\n\nSven\nSven is a reindeer who loves carrots, and is ridden by Kristoff, an ice harvester. He, along with Kristoff, originally lived with a group of ice harvesters before being adopted by trolls. Upon reaching adulthood, they begin their own ice business. They are coerced with supplies into helping Anna locate her sister Elsa. Once they reach her new ice palace, Anna is cursed, and they follow her to Arendelle to help her break it with true love."
  selectdescription = raw_input("\nThere are six characters you can choose from:\n  Elsa (Type E to see Elsa\'s character description) \n  Anna (Type A to see Anna\'s character description)\n  Kristoff (Type K to see Kristoff\'s character description)\n  Hans (Type H to see Hans\'s character description)\n  Olaf (Type O to see Olaf\'s character description)\n  Sven (Type S to see Sven\'s character description)\n\n")
  w = 0
  while w < 9:
    if selectdescription.upper() == "A":
      print Anna + "\n\n"
      selectdescription = raw_input("If you would like to view another character description, type the first letter of their name. If you would like to return to the homescreen to play the game instead, type \'1\'.\n\n")
      if selectdescription.upper() == "A" or selectdescription.upper() == "E" or selectdescription.upper() == "K" or selectdescription.upper() == "H" or selectdescription.upper() == "O" or selectdescription.upper() == "S":
        continue
      elif selectdescription == "1":
        break
      else:
        selectdescription = raw_input("\nI'm not sure if I understand. Please try again.\n\n")
        continue
    elif selectdescription.upper() == "E":
      print Elsa  + "\n\n"
      selectdescription = raw_input("\nIf you would like to view another character description, type the first letter of their name. If you would like to return to the homescreen to play the game instead, type \'1\'.\n\n")
      if selectdescription.upper() == "A" or selectdescription.upper() == "E" or selectdescription.upper() == "K" or selectdescription.upper() == "H" or selectdescription.upper() == "O" or selectdescription.upper() == "S":
        continue
      elif selectdescription == "1":
        break
      else:
        selectdescription = raw_input("\nI'm not sure if I understand. Please try again.\n\n")
        continue
    elif selectdescription.upper() == "K":
      print Kristoff + "\n\n"
      selectdescription = raw_input("If you would like to view another character description, type the first letter of their name. If you would like to return to the homescreen to play the game instead, type \'1\'.\n\n")
      if selectdescription.upper() == "A" or selectdescription.upper() == "E" or selectdescription.upper() == "K" or selectdescription.upper() == "H" or selectdescription.upper() == "O" or selectdescription.upper() == "S":
        continue
      elif selectdescription == "1":
        break
      else:
        selectdescription = raw_input("\nI'm not sure if I understand. Please try again.\n\n")
        continue
    elif selectdescription.upper() == "H":
      print Hans + "\n\n"
      selectdescription = raw_input("\nIf you would like to view another character description, type the first letter of their name. If you would like to return to the homescreen to play the game instead, type \'1\'.\n\n")
      if selectdescription.upper() == "A" or selectdescription.upper() == "E" or selectdescription.upper() == "K" or selectdescription.upper() == "H" or selectdescription.upper() == "O" or selectdescription.upper() == "S":
        continue
      elif selectdescription == "1":
        break
      else:
        selectdescription = raw_input("\nI'm not sure if I understand. Please try again.\n\n")
        continue
    elif selectdescription.upper() == "O":
      print Olaf + "\n\n"
      selectdescription = raw_input("If you would like to view another character description, type the first letter of their name. If you would like to return to the homescreen to play the game instead, type \'1\'.\n\n")
      if selectdescription.upper() == "A" or selectdescription.upper() == "E" or selectdescription.upper() == "K" or selectdescription.upper() == "H" or selectdescription.upper() == "O" or selectdescription.upper() == "S":
        continue
      elif selectdescription == "1":
        break
      else:
        selectdescription = raw_input("\nI'm not sure if I understand. Please try again.\n\n")
        continue
    elif selectdescription.upper() == "S":
      print Sven + "\n\n"
      selectdescription = raw_input("If you would like to view another character description, type the first letter of their name. If you would like to return to the homescreen to play the game instead, type \'1\'.\n\n")
      if selectdescription.upper() == "A" or selectdescription.upper() == "E" or selectdescription.upper() == "K" or selectdescription.upper() == "H" or selectdescription.upper() == "O" or selectdescription.upper() == "S":
        continue
      elif selectdescription == "1":
        break
      else:
        selectdescription = raw_input("\nI'm not sure if I understand. Please try again.\n\n")
        continue
    elif selectdescription == "1":
      break
    else:
      selectdescription = raw_input("\nI'm not sure I understand. Please try again, and remember to enter the first letter of your chosen character's name to view their description.\n\n")
      continue
def game():
  import os
  import time
  intro = raw_input("\033[1;37;46mHello! Welcome to \'Character Guessing Game: Frozen Edition\'!\nWould you like to:\nBegin the game (type 1)\nRead the character descriptions (type 2)\n\n")
  os.system('clear')
  while True == True:
    if intro == "1":
      while False == False:
        character = raw_input("\n Alright! Your character choices are:\nElsa\nAnna\nKristoff\nHans\nOlaf\nSven\n\nChoose one of these characters. During the game, you will be asked questions about your chosen character, so be prepared!\n\nWhen you are ready to begin, type 1. If you would like to view the character descriptions, type 2.\n\n\033[1;37;40m")
        os.system('clear')
        if character == "1":
          while 1 == 1:
            FirstQ = raw_input("\nIs your chosen character human?\n\nIf yes, type Y. If no, type N.\n\n")
            os.system('clear')
            if FirstQ.upper() == "Y":
              answer1 = 1
              while 2 == 2:
                SecondQ = raw_input("\nIs your chosen character male?\n\nIf yes, type Y. If no, type N.\n\n")
                os.system('clear')
                if SecondQ.upper() == "Y":
                  answer2 = 1
                  while 3 == 3:
                    ThirdQ = raw_input("\nIs your chosen character royalty?\n\nIf yes, type Y. If no, type N.\n\n")
                    os.system('clear')
                    if ThirdQ.upper() == "Y":
                      answer3 = 1
                      while 4 == 4:
                        answers(answer1, answer2, answerthree = answer3)
                    elif ThirdQ.upper() == "N":
                      answer3 = 0
                      while 4 == 4:
                        answers(answer1, answer2, answerthree = answer3)
                    else:
                      print "I'm not sure I understand. Please try again. Remember: type \'Y\' for yes and \'N\' for no."
                      time.sleep(1)
                      continue
                elif SecondQ.upper() == "N":
                  answer2 = 0
                  while 3 == 3:
                    ThirdQ = raw_input("\nDoes your chosen character have magical powers?\n\nIf yes, type Y. If no, type N.\n\n")
                    os.system('clear')
                    if ThirdQ.upper() == "Y":
                      answer3 = 4
                      answers(answer1, answer2, answerthree = answer3)
                    elif ThirdQ.upper() == "N":
                      answer3 = 3
                      answers(answer1, answer2, answerthree = answer3)
                    else:
                      print "I'm not sure I understand. Please try again. Remember: type \'Y\' for yes and \'N\' for no."
                      time.sleep(1)
                      continue
                else:
                  print "I'm not sure I understand. Please try again. Remember: type \'Y\' for yes and \'N\' for no."
                  time.sleep(1)
                  continue
            elif FirstQ.upper() == "N":
              answer1 = 0
              while 2 == 2:
                SecondQ = raw_input("\nWas your chosen character created?\n\nIf yes, type Y. If no, type N.\n\n")
                os.system('clear')
                if SecondQ.upper() == "Y":
                  answer2 = 4
                  answers(answer1, answer2)
                elif SecondQ.upper() == "N":
                  answer2 = 3
                  answers(answer1, answer2)
                else:
                  print "I'm not sure I understand. Please try again. Remember: type \'Y\' for yes and \'N\' for no."
                  time.sleep(1)
                  continue
            else:
                print "I'm not sure I understand. Please try again. Remember: type \'Y\' for yes and \'N\' for no."
                time.sleep(1)
                continue
        elif character == "2":
          character_descriptions()
          os.system('clear')
          intro = raw_input("Hello! Welcome to \'Character Guessing Game: Frozen Edition\'!\nWould you like to:\nBegin the game (type 1)\nRead the character descriptions (type 2)\n\n")
          continue
        else:
          print "\nI'm not sure if I understand. Please try again. Remember: to begin the game, type \'1\'. To view the character descriptions, type \'2\'.\n"
          time.sleep(1)
          print "You will now return to the mainscreen.\n"
          time.sleep(2.5)
          os.system('clear')
          continue
    elif intro == "2":
      character_descriptions()
      os.system('clear')
      intro = raw_input("Hello! Welcome to \'Character Guessing Game: Frozen Edition\'!\nWould you like to:\nBegin the game (type 1)\nRead the character descriptions (type 2)\n\n")
      continue
    else:
      intro = raw_input("I'm not sure if I understand. Please try again. Remember: to begin the game, type \'1\'. To view character descriptions, type \'2\'.\n\n")
      os.system('clear')
      continue
def end(LastQ):
  import os
  import sys
  import time
  if LastQ.upper() == "Y":
    while 5 == 5:
      redo = raw_input("\n\nAlright, then! If you would like to play again, type 1 to return to the homescreen. Otherwise, type 2 to end the game.\n\n")
      while 1 == 1:
        if redo == "1":
          os.system('clear')
          game()
        elif redo == "2":
          os.system('clear')
          print "Alright, thanks for playing!"
          time.sleep(1)
          sys.exit()
        else:
          redo = raw_input("\nI'm not sure if I understand. Please try again. Remember: type 1 to return to the homescreen. Otherwise, if you\'d rather end the game, type 2.\n\n")
          continue
  elif LastQ.upper() == "N":
    while 5 == 5:
      incorrect = raw_input("\nHmm. I don\'t think you've selected a character from the approved list. Or maybe you simply answered incorrectly. If you\'d like to try again, type 1 to return to the homescreen. Otherwise, if you\'d rather end the game, type 2.\n\n")
      while 1 == 1:
        if incorrect == "1":
          os.system('clear')
          game()
        elif incorrect == "2":
          os.system('clear')
          print "Alright, thanks for playing!"
          time.sleep(1)
          sys.exit()
        else:
          incorrect = raw_input("\nI'm not sure if I understand. Please try again. Remember: type 1 to return to the homescreen. Otherwise, if you\'d rather end the game, type 2.\n\n")
          continue
  else:
    retry = raw_input("\nI'm not sure I understand. Please try again. Remember: type \'Y\' for yes and \'N\' for no.\n\n")
    end(retry)
def answers(answerone, answertwo, answerthree = 0):
  if answerone == 1 and answertwo == 1 and answerthree == 1:
    while 4 == 4:
      FourthQ = raw_input("\nIs your chosen character Hans?\n\nIf yes, type Y. If no, type N.\n\n")
      end(FourthQ)
  elif answerone == 1 and answertwo == 1 and answerthree == 0:
    while 4 == 4:
      FourthQ = raw_input("\nIs your chosen character Kristoff?\n\nIf yes, type Y. If no, type N.\n\n")
      end(FourthQ)
  elif answerone == 1 and answertwo == 0 and answerthree == 4:
    while 4 == 4:
      FourthQ = raw_input("\nIs your chosen character Elsa?\n\nIf yes, type Y. If no, type N.\n\n")
      end(FourthQ)
  elif answerone == 1 and answertwo == 0 and answerthree == 3:
    while 4 == 4:
      FourthQ = raw_input("\nIs your chosen character Anna?\n\nIf yes, type Y. If no, type N.\n\n")
      end(FourthQ)
  elif answerone == 0 and answertwo == 4 and answerthree == 0:
    while 4 == 4:
      ThirdQ = raw_input("\nIs your chosen character Olaf?\n\nIf yes, type Y. If no, type N.\n\n")
      end(ThirdQ)
  elif answerone == 0 and answertwo == 3 and answerthree == 0:
    while 4 == 4:
      ThirdQ = raw_input("\nIs your chosen character Sven?\n\nIf yes, type Y. If no, type N.\n\n")
      end(ThirdQ)
game()