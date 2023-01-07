student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass



data=pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict={row.letter:row.code for (index,row) in data.iterrows()}



def alphabet():
    user_input=input("Enter your word: ").upper()
    try:
        output=[alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        alphabet()
    else:
        print(output)

alphabet()

