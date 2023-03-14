def freq_letterfinder(phrase):
    phrase = phrase.lower()
    counter = 0
    freq_letter = ""
    for i in phrase:
        new_counter = 0
        for j in phrase:
            if i == j:
                new_counter+=1
        if new_counter > counter:
            counter = new_counter
            freq_letter = i;
    print(freq_letter)
    
    
freq_letterfinder(input("enter phrase: "))