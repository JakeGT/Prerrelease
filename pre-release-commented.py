# Skeleton Program for the AQA AS Summer 2018 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA AS Programmer Team
# developed in a Python 3 environment
# Version Number : 1.6

#Commented by Jake as if talking to a layman. All comments refer to the code relatively above.
#Any and all offense from reading these comments are unintentional... except this bit:
#I have seen hundreds of thousands of lines of code and never have I seen something this terrible... except Ryan's :P /sarcasm

SPACE = ' '
EOL = '#'
EMPTYSTRING = ''
#Assignment of constants

def ReportError(s):
  print('{0:<5}'.format('*'),s,'{0:>5}'.format('*')) 
  #Subroutine that is referred to when reporting an error to the user
  #'{0:<5}',format('*') outputs five spaces followed by an astrix
  #s is an argument passed to the subroutine

def StripLeadingSpaces(Transmission):
  #This subroutine is used to remove all spaces at the start of the program
  TransmissionLength = len(Transmission)
  #length of transmission
  if TransmissionLength > 0:
  #if length of transmission is more than 0
    FirstSignal = Transmission[0]
    #first signal is set to the first character of transmission
    while FirstSignal == SPACE and TransmissionLength > 0:
    #repeats while FirstSignal is a space and TransmissionLength is more than 0
      TransmissionLength -= 1
      #Reduces TransmissionLength by 1
      Transmission = Transmission[1:]
      #Transmission is set to transmission starting from the second character
      #[1:] means index 1 and onwards (2nd element and onwards)
      if TransmissionLength > 0:
        #If TransmissionLength is more than 0
        FirstSignal = Transmission[0]
        #FirstSignal is now set to the first character in Transmission
  if TransmissionLength == 0:
    #If TransmissionLength is zero, it means that the file is empty or only spaces
    ReportError("No signal received")
    #Reports this error to the user using subroutine (line 16)
  return Transmission
  #Returns Transmission to whatever called the subroutine

def StripTrailingSpaces(Transmission): 
  #This subroutine removes all spaces at the end of a string
  LastChar = len(Transmission) - 1
  #The last character will be the length of the string
  #Python indexing starts at 0
  #The last character - 1 is the index value.
  while Transmission[LastChar] == SPACE:
    #As long as the last character is a space
    LastChar -= 1
    #Reduce last character by 1
    Transmission = Transmission[:-1]
    #Transmission is now everything but the last character
  return Transmission
  #Return transmission to whatever called this subroutine

def GetTransmission():
  #This loads the file than contains the transmission
  FileName = input("Enter file name: ")
  #Takes user input for file name
  try:
  #Error handling. Try to run this stuff here
    FileHandle = open(FileName, 'r')
    #Opens the file with name provided by user
    Transmission = FileHandle.readline()
    #Reads one line from the file
    FileHandle.close()
    #Closes the file
    Transmission = StripLeadingSpaces(Transmission)\
    #Refer to subroutine in line 22
    if len(Transmission) > 0:
      #If the length of Transmission is more than 0
      Transmission = StripTrailingSpaces(Transmission)
      #Refer to subroutine in line 48
      Transmission = Transmission + EOL
      #Transmission is now transmission but with some extra jazz at the end
      # to indicate the end of the line
  except: #Error? Do This
  #Never do this; If you do this, you will be condemned
  #Specify your errors
    ReportError("No transmission found")
    #Reports error to user. Refer to line 16
    Transmission = EMPTYSTRING
    #Transmission is now an empty string
  return Transmission
  #Return transmission to whatever call this subroutine

def GetNextSymbol(i, Transmission):
  #Its in the name. Take a guess.
  if Transmission[i] == EOL:
  #If the current character in transmission is the end of line
    print()
    #Why? Just why?
    print("End of transmission")
    #Tells the user this stuff above
    Symbol = EMPTYSTRING
    #Symbol is now empty string
  else:
    #If anything else happens
    SymbolLength = 0
    #Symbol length is now 0
    Signal = Transmission[i]
    #Signal is whatever the current character is
    while Signal != SPACE and Signal != EOL:
    #While signal is not space and signal is not an EOL
    #Testing for EOL is redundant; of it is an EOL it would not get to this stage
    #This entire section just turns the = signs in the message to . and -
    #Three = is a -, one = is a .
    #Loops until space occurs which means next symbol
      i += 1
      #Increment i by 1 because variable names matter
      Signal = Transmission[i]
      #The signal is now the next character in transmission
      SymbolLength += 1
      #SymbolLength is now a bigger number
    if SymbolLength == 1:
      #If SymbolLength is one
      Symbol = '.'
      #We have found a .
    elif SymbolLength == 3:
      #If SymbolLength is three
      Symbol = '-'
      #We have found a -
    elif SymbolLength == 0: 
      #If symbol length is 0
      Symbol = SPACE
      #It is a space
    else:
      ReportError("Non-standard symbol received")
      #And if none of the above, something is wrong with the message
      Symbol = EMPTYSTRING
      #And therefore Symbol is empty string
  return i, Symbol 
  #Tell whatever called this subroutine the above.

def GetNextLetter(i, Transmission):
  #Returns the next letter in the transmission
  SymbolString = EMPTYSTRING
  #SymbolString has mastered the way of the buddha and is now empty of everything
  LetterEnd = False
  #The LetterEnd is in denial
  while not LetterEnd:
    #As long as the LetterEnd is in denial, keep going
    i, Symbol = GetNextSymbol(i, Transmission)
    #Gimme the next symbol
    if Symbol == SPACE:
      #If symbol is space
      LetterEnd = True
      #LetterEnd has accepted the true(th).
      i += 4
      #Increase i by 4
    elif Transmission[i] == EOL:
      #If ith character of Transmission is EOL
      LetterEnd = True
      #Then LetterEnd has accepted the true(th)
    elif Transmission[i + 1] == SPACE and Transmission[i + 2] == SPACE:
      #If next letter is a space and the following is also a space
      LetterEnd = True
      #Letter end has again accepted the true(th)
      i += 3
      #Increment i by 3
    else:
      i += 1
      #And if none of the above, increment i by 1
    SymbolString = SymbolString + Symbol
    #SymbolString is now SymbolString plus Symbol
  return i, SymbolString
  #Return the above to whatever called this subroutine

def Decode(CodedLetter, Dash, Letter, Dot):
  #This converts them dashes and dots into letters
  CodedLetterLength = len(CodedLetter)
  #Length of letter
  Pointer = 0
  #This is the first step of the mess that this program uses to convert
  for i in range(CodedLetterLength):
    #Loops for in the length of the coded letter
    Symbol = CodedLetter[i]
    #The symbol is now the next coded letter
    if Symbol == SPACE:
      return SPACE
      #If the symbol is a space, return space
    elif Symbol == '-':
      Pointer = Dash[Pointer]
      #If the symbol is a dash, set pointer to Dash with index of Pointer
    else:
      Pointer = Dot[Pointer]
      #Else set pointer to Dot with the index of pointer
  #This convoluted method of converting is explained in the document you were given
  #Don't ask me to explain this spaghetti
  return Letter[Pointer]
  #Once done, return letter with index pointer

def ReceiveMorseCode(Dash, Letter, Dot): 
  #Take the morse code and make it English
  PlainText = EMPTYSTRING
  MorseCodeString = EMPTYSTRING
  #Don't bother reading any further if you need me to explain this
  Transmission = GetTransmission() 
  #Refer to line 63
  LastChar = len(Transmission) - 1
  #The index of the last character is the length of the transmission - 1
  i = 0
  #set i to 0
  while i < LastChar:
    #While i is smaller than the last character
    i, CodedLetter = GetNextLetter(i, Transmission)
    #Refer to line 142
    MorseCodeString = MorseCodeString + SPACE + CodedLetter
    #Add EVERYTHING together
    PlainTextLetter = Decode(CodedLetter, Dash, Letter, Dot)
    #Refer to line 176
    PlainText = PlainText + PlainTextLetter
    #ADD
  print(MorseCodeString)
  print(PlainText)
  #Print that stuff

def SendMorseCode(MorseCode, Letter):
  #Converts entered string into morsecode
  PlainText = input("Enter your message (uppercase letters and spaces only): ")
  #Takes user input and stores as PlainText
  PlainTextLength = len(PlainText)
  #Stores the legnth of plain text
  MorseCodeString = EMPTYSTRING
  #Ze morse code string is now empty
  for i in range(PlainTextLength):
    #Loops i for all numbers in PlainTextLength
    PlainTextLetter = PlainText[i]
    #The plaintextletter is now the letter in the ith position
    if PlainTextLetter == SPACE:
      #If that letter is a space
      Index = 0
      #Index is now 0
    elif PlainTextLetter in Letter: 
      #If PlainTextLetter is an element of Letter
      Index = ord(PlainTextLetter) - ord('A') + 1
      #The index is now the charactercode of the plaintext letter minus 65 plus 1
      CodedLetter = MorseCode[Index]
      #The morsecode is indexed in the same order as the alphabet
      MorseCodeString = MorseCodeString + CodedLetter + SPACE
      #Just add all that together
    else:
      #If all else then an unsupported symbol was entered
      ReportError("Non-standard symbol entered")
      #Report that error to the user
      MorseCodeString = ""
      #MorseCodeString is now nothing
  if MorseCodeString != "":
    #If MorseCodeString is not nothing
    print(MorseCodeString)
    #Tell the user about it

def DisplayMenu():
  #Shows the user the menu
  print()
  print("Main Menu")
  print("=========")
  print("R - Receive Morse code")
  print("S - Send Morse code")
  print("X - Exit program")
  print()

def GetMenuOption():
  #Takes the user's input and that is now what the program is doing
  MenuOption = EMPTYSTRING
  while len(MenuOption) != 1:
    MenuOption = input("Enter your choice: ")
  return MenuOption
    
def SendReceiveMessages():
  Dash = [20,23,0,0,24,1,0,17,0,21,0,25,0,15,11,0,0,0,0,22,13,0,0,10,0,0,0]
  Dot = [5,18,0,0,2,9,0,26,0,19,0,3,0,7,4,0,0,0,12,8,14,6,0,16,0,0,0]
  Letter = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  MorseCode = [' ','.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..']
  #These should all really be global constants

  ProgramEnd = False
  #The program doesn't want to end yet
  while not ProgramEnd:
    DisplayMenu()
    #refer to line 252
    MenuOption = GetMenuOption()
    #Refer to line 262
    if MenuOption == 'R':
      #If the user wants R, they get R
      ReceiveMorseCode(Dash, Letter, Dot)
    elif MenuOption == 'S':
      #Same as above but S
      SendMorseCode(MorseCode, Letter) 
    elif MenuOption == 'X':
      #Goodbye
      ProgramEnd = True
      #The program wants to end now
    

if __name__ == "__main__":
  SendReceiveMessages()
  #This starts the program
