def word_sperator(word):
    new_word = ""
    for i in word:
        if i.isupper():
            new_word += " " + i
        else: 
            new_word += i
    print(new_word.strip())
    

word_sperator(input("Enter Word: "))
