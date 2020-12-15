#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]" 
with open('./Input/Names/invited_names.txt') as names_file:
  names = names_file.readlines()
  name_list = []
  for i in names:
    for j in range(0, 8):
      name_list.append(names[j][:-1])
with open('./Input/Letters/starting_letter.docx') as letter_file:
  letter_contents = letter_file.read()
  for name in name_list:
    new_letter = letter_contents.replace(PLACEHOLDER, name)
    file1 = open(f'./Output/ReadyToSend/letter_for_{name}.docx', 'w')
    file1.write(new_letter)