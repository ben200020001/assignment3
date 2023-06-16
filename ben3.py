#char alphabets
#string sentence

sentence = input("Please enter a sentence: ")
modifiedsentence = ""

for char in sentence:
    if char in ["a","e","i","o","u"]:
        continue
    else:
        modifiedsentence += char

    print(modifiedsentence)