text = list(input(""))
output = []
vowels = list("aeiou")
closestvowels = list("aaaeeeeiiiiioooooouuuuuuuu")
consonants = list("bcdfghjklmnpqrstvwxyzz")
alphabet = list("abcdefghijklmnopqrstuvwxyz")

def find_vowel(character):
    return closestvowels[alphabet.index(character)]

for i in range(len(text)):
    try:
        if vowels.index(text[i]) != -1 :
            output.append(text[i])
    except ValueError:
        closestvowel = find_vowel(text[i])
        nextconsonant = consonants[consonants.index(text[i]) + 1]

        output.append(text[i])
        output.append(closestvowel)
        output.append(nextconsonant)

for j in range(len(output)):
    print(output[j], end='')