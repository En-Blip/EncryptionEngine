import random

alphabet=' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR5STUVWXYZ1234567890'
keynums='123456789'
testNum=3

print("""

+------------------------------------------------------+
| Noah Vickerson's Encryption and Decryption Algorithm |
|                Created Dec 3, 2020                   |
|                                                      |
|    For Eny Questions Email: contact@communism.com    |
+------------------------------------------------------+



""")

def encryption(message, encryptionLevel):
    keySignature = "Key Signature: _"
    savedMessage=message

    for f in range (encryptionLevel):
        randomNum=random.randint(1,2)

        if randomNum == 1:
            
            newMessage = ''
            keySignature=keySignature.replace('_','_1')
            
            for i in message:
                position=alphabet.find(i)
            
                newposition=(position+5)%63
                newMessage+=alphabet[newposition]
                
            message=newMessage

        if randomNum == 2:

            newMessage = ''
            keySignature=keySignature.replace('_','_2')
            
            for i in message:
                position=alphabet.find(i)
            
                newposition=(position-9)
                if newposition < 0:
                    newposition +=63
                newMessage+=alphabet[newposition]
                
            message=newMessage
            
    outputMessage=message.replace(savedMessage,'')

    outputArray=['Output: '+outputMessage,keySignature.replace('_','')+':'+str(len(message))]

    
    return outputArray

def decryption(messageForDecryption, keyForDecryption):
    encrypt=''
    keyForDecryption=keyForDecryption.split(':')


    for number in keyForDecryption[0]:


        if number == '1':            
    
            for i in messageForDecryption:
                position=alphabet.find(i)
                
                newposition=position-5
                if newposition < 0:
                    newposition += 63
                encrypt+=alphabet[newposition]
            messageForDecryption = encrypt
            encrypt=''

        if number == '2':
            
            for i in messageForDecryption:
                position=alphabet.find(i)
            
                newposition=(position+9)%63
                if newposition < 0:
                    newposition += 63
                encrypt+=alphabet[newposition]
            messageForDecryption = encrypt
            encrypt=''

                
         
    return "Output: "+messageForDecryption

while 1 == 1:

    encryptOrDecrypt=input("Are you encrypting or decrypting? [e/d]")
    
    if encryptOrDecrypt == 'e':

        message=input("""Enter message to encrypt
>>""")
        howSafe=input("""
How safe do you want your encryption to be?

1: Not very safe
2: Mildly safe
3: Moderately safe
4: Super safe

>>""")
        trueOutput=encryption(message, int(howSafe))

        print(trueOutput[1])
        print(trueOutput[0])
        
    else:
        if encryptOrDecrypt == 'd':

            messageForDecryption=input("""Enter message to decrypt
>>""")
            keyForDecryption=input("""Enter decryption key
>>""")
            trueOutput=decryption(messageForDecryption, keyForDecryption)

            print(trueOutput)

        else:
            exit()
        

            

    


