
import cyrtranslit

# all words are in the Nominitive(Dictionary) case

adjectives = ("маленький", "большой", "высокий", "низкий", "новый", "старый", "сильный", "красивый", "богатый", "здоровый")

noun = ("мужчина", "женщина", "кот", "собака", "город", "дерево", "машина", "сестра", "брат", "стол")

verb = ("знать", "любить", "работать", "говорить", "думать", "гулять", "хотеть", "сделать", "давать", "идти")

prepositions = ("в", "на", "между", "из", "с", "от")

conjunctions = ("и")

la = ()
ln = ()
lv = ()
lp = ()
lc = ()

for a in adjectives:
    la += (cyrtranslit.to_latin(a, "ru"),)

for n in noun:
    ln += (cyrtranslit.to_latin(n, "ru"),)

for v in verb:
    lv += (cyrtranslit.to_latin(v, "ru"),)

for p in prepositions:
    lp += (cyrtranslit.to_latin(p, "ru"),)

for c in conjunctions:
    lc += (cyrtranslit.to_latin(c, "ru"),)

print(la)
print(ln)
print(lv)
print(lp)
print(lc)

run = True

def is_valid_sentence(phrase):
    phrase = phrase.split()
    # if a phrase has a preposition check if the prepositions comes before a noun or verb
    adj = 0
    noun = 0
    verb = 0
    preposition = 0
    conjunction = 0

    step = 0

    valid = False

    if phrase == []:
        valid = False

    print(phrase)
    # check if the phrase has at least a noun and verb, noun and adjective, or verb and adjective
    for word in phrase:
        # loop through the whole phrase and check if the phrase has at least 1 noun and 1 verb or 1 noun and 1 adjective or 1 verb and 1 adjective and update the counters

        while step < len(phrase): 
            if phrase[step] in ln:
                noun += 1
            elif phrase[step] in lv:
                verb += 1
            elif phrase[step] in la:
                adj += 1
            elif phrase[step] in lp:
                preposition += 1
            elif phrase[step] in lc:
                conjunction += 1
            step += 1
        
        if noun >= 1 and verb >= 1:
            valid = True
        elif noun >= 1 and adj >= 1:
            valid = True
        elif verb >= 1 and adj >= 1:
            valid = True
        elif noun >= 1 and adj >= 1 and verb >= 1:
            valid = True
        else:
            valid = False
            break

        # check if the phrase has a conjunction 
        if word in lc:
            try:
                #check to see if the following amd previous words are of the same type ex: noun conjunction noun or verb conjunction verb
                if phrase[phrase.index(word) + 1] in ln or phrase[phrase.index(word) + 1] in lv or phrase[phrase.index(word) + 1] in la:
                    if phrase[phrase.index(word) - 1] in ln or phrase[phrase.index(word) - 1] in lv or phrase[phrase.index(word) - 1] in la:
                        valid = True
                        break
                    else:
                        valid = False
                        break               
            except Exception:
                print("A conjunction must be follwed be either a noun, verb, or adjective. You can't string conjunctions")
                valid = False
                break

        print(word)

        # check if the phrase has a preposition and if it does check if the preposition comes before a noun or verb
        if word in lp:
            #check to see if the following word is a noun, or verb
            try:
                if phrase[phrase.index(word) + 1] in ln or phrase[phrase.index(word) + 1] in lv or phrase[phrase.index(word) + 1] in la:
                    valid = True
                    break
                # if index is out of range set valid to False
                else:
                    valid = False
                    break
            except Exception:
                print("A preposition must be follwed be either a noun, verb, or adjective.")
                valid = False
                break

    print("noun: " + str(noun))
    print("verb: " + str(verb))
    print("adj: " + str(adj))
    print("preposition: " + str(preposition))
    print("conjunction: " + str(conjunction))

    return valid

"""
while run:                                                            
    again = input("Do you want to continue? (y/n): ")
    if again.lower() == "y":           
        phrase = input("Enter a Russian phrase and I'll tell you if it's a valid sentence: ")
        if is_valid_sentence(phrase) == True:
            print("This is a valid sentence.")
        else:
            print("This is not a valid sentence.")
    elif again.lower() == "n":
        print("Goodbye!")
        break
"""

def main():
    phrase = str(input("Enter a Russian phrase and I'll tell you if it's a valid sentence: "))
    if is_valid_sentence(phrase) == True:
        print("This is a valid sentence.")
    elif is_valid_sentence(phrase) == False:
        print("This is not a valid sentence.")

if __name__ == "__main__":
    main()
    