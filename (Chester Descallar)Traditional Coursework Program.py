 #importing files
import random,string,math,sys
def Menu():
        global line
        line = ('---------------------------------------------------------------------------------------')
        print ('******************************')
        print ('* Press 1 to Encrypt Message *')
        print ('*----------------------------*')
        print ('* Press 2 to Decrypt Message *')
        print ('*----------------------------*')
        print ('* Press 3 to Exit Program    *')
        print ('******************************')
        menuAnswer = input('Make your choice:')
        
        if menuAnswer == '1':
            answer = ansUser()
            print (answer)
            print (line)    
            if run == 1:
                genMe = genNumber()
                print (genMe)
                print (line)
                mesConvert = conASCII()
                print (mesConvert)
                Cipher = saveCipher()

                return Cipher
            else:
                return Menu()
        elif menuAnswer == '2':
                decrypt = decryptFile()
                print (decrypt)
                print (line)
                if run == 1:
                        eightKey = askEight()
                        print (eightKey)
                        conversion = conNewAscii()
                        return conversion
                else:
                        return Menu()
        elif menuAnswer == '3':
                exit()
        else:
                return Menu()

#loading the encrypted message
def ansUser ():
        global run
        global nstring
        run = 0
        #ask the user the name of the file
        uFile = input ('What is the name of the file? :') + '.txt'
        print(line)
        #loads the file mentioned by the user
        try:
                nstring = []
                openFile = open(uFile, 'r')
                string = openFile.read()
                nstring.append (string)
                openFile.close
                run = run + 1
                return nstring
                
        except:
                noFile = ('Error! File not found.')
                return noFile

#generate 8 character key
def genNumber():
        numbers = []
        converted = []
        global osFactor
        osFactor = 0
        for x in range(8):
            number = random.randint(33,126)
            char = chr(number)
            numbers.append (number)
            converted.append (char)
        #task 4 - Offset Factor
        osFactor = sum(numbers)
        osFactor = osFactor / 8
        osFactor = math.floor (osFactor)
        osFactor = osFactor - 32
        print ('Here is your Eight Character Key:')
        return converted
    
#converting the message into ASCII
def conASCII():
    global nstring
    global ciphertext
    myString = nstring
    myString = list(myString[0])
    tempString = []
    for x in range (len(myString)):
            if myString[x] == " ":
                    myString[x] == " "
                    tempString.append (myString[x])
            else:
                tempChar = ord(myString[x])
                tempChar = tempChar + osFactor
                if tempChar>126:
                    tempChar = tempChar-94
                else:
                        pass
                tempChar = chr(tempChar)
                tempString.append(tempChar)
    ciphertext = ''.join(tempString)
    return ciphertext


#saving the ciphertext into a new text file
def saveCipher():
        print (line)
        fileSaved = ('File Saved')
        namedFile = input ('What would be the name of this file? :') + '.txt'
        file = open(namedFile, "w")
        newFile = file.write(ciphertext)
        file.close()
        return fileSaved

def decryptFile():
        #ask the user the name of the file
        global decryptString
        global run
        run = 0
        cipherFile = input ('What is the name of the file needed to be decrypted? :') + '.txt'
        print(line)
        # tries to load the file mentioned by the user, it there isn't any -> ERROR!
        try:
                decryptString = []
                openCFile = open(cipherFile, 'r')
                decString = openCFile.read()
                decryptString.append (decString)
                openCFile.close
                run = run + 1
                return decryptString
                
        except:
                errorFile = ('Error! File not found.')
                return errorFile

#ask for the eight key character key
def askEight():
        global eightKey
        eightKey = []
        for x in range (8):
                askKey = input ('Give me one of the Eight Key Character you have recieved : ')
                eightKey.append (askKey)
        return eightKey

#calculating the offset factor from the eight character key entered previously^
def conNewAscii():
        print (line)
        decryptOSFactor = []
        for i in eightKey:
                newConverted = ord(i)
                decryptOSFactor.append (newConverted)

        newOSFactor = sum(decryptOSFactor)
        newOSFactor = newOSFactor / 8
        newOSFactor = math.floor (newOSFactor)
        newOSFactor = newOSFactor - 32
        #replacing the encrypted words or symbols with the correct words 
        decryptedString = decryptString
        decryptedString = list(decryptedString[0])
        newString = []
        for x in range (len(decryptedString)):
                if decryptedString[x] == " ":
                        decryptedString[x] == " "
                        newString.append (decryptedString[x])
                else:
                        myChar = ord(decryptedString[x])
                        myChar = myChar - newOSFactor
                        if myChar < 33:
                                myChar = myChar + 94
                        else:
                                pass
                        myChar = chr(myChar)
                        newString.append(myChar)
        message = ''.join(newString)
        return message

        
#main program
mainMenu = Menu()
print (mainMenu)
