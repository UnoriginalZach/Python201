import re 

def pig_latin(phrase):
    latin_phrase = ""
    words = phrase.split()
    for i in words:
        if re.search(r"[^aeiouAEIOU]", i[0]):
            if re.search(r"[aeiouAEIOU]", i[1]):
                x = i[0]
                i = i.lstrip(i[0])
                i += "-" + x + "ay"
            elif re.search(r"[^aeiouAEIOU]", i[1]):
                x = i[0] + i[1]
                i = i.lstrip(x)
                i += "-" + x + "ay"
        elif re.search(r"[aeiouAEIOU]", i[0]):
            i += "way"
        latin_phrase += " " + i
    print(latin_phrase.strip())
    

pig_latin(input("Phrase: "))