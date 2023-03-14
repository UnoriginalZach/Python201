import re

f = open(r"c:\Users\zfredrin\Dev\Freddy\test.txt","r")
student_answers = f.readlines()

for x in student_answers:
    i = student_answers.index(x)
    x = x.strip()
    student_answers[i] = x
    f.close()
correct_answers = ["A", "C", "A", "A", "D"]
answers_correct = 0

for x in range(len(correct_answers)):
    if correct_answers[x] == student_answers[x]:
        answers_correct += 1

if answers_correct >= 3:
    print("pass")
else: print("fail")
print(student_answers)
print("questions correctly answered: ", answers_correct)
print("questions incorrectly answered:", (len(correct_answers) - answers_correct))

