def file_parse_words(file1, file2):
    f1_set = set()
    f2_set = set()
    f1 = open(file1)
    f2 = open(file2)
    for word in f1:
        f1_set.add(word)
    for word in f2:
        f2_set.add(word)
    print(f1_set.difference(f2_set))
    print(f2_set.difference(f1_set))
    print(f1_set.intersection(f2_set))
    print(f1_set.symmetric_difference(f2_set))
    
    
file1 = input("please enter your first file location: ")
file2 = input("please enter your second file location: ")
file_parse_words(file1, file2)