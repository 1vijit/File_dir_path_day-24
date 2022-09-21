#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


file_2= open("./Input/Names/invited_names.txt", mode="r")
name = file_2.readlines()
print(name)

for count in range(0,len(name)):
    a=name[count].replace('\n', '')
    file_1 = open("./Input/Letters/starting_letter.txt", mode="r")
    body = file_1.read()
    body = body.replace('[name]',a)
    print(body)
    file_3 = open(f"./Output/ReadyToSend/Letter_for_{a}.txt", "w")
    file_3.write(body)
    file_3.close()
    file_1.close()




