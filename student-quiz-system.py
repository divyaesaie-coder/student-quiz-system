#Develop a Python quiz system that asks questions, checks answers, and calculates the final score.
correct_answers = ["b", "b"]
score = 0

name = input("Enter the name: ")

print("1) What comes after 4?")
print("a) 1  b) 5")
a1 = input("Answer (a/b): ")

print("2) What is the capital of India?")
print("a) India  b) New Delhi")
a2 = input("Answer (a/b): ")

student_answers = [a1, a2]

if student_answers[0] == correct_answers[0]:
    print("Question 1 correct")
    score += 10
else:
    print("Question 1 wrong")

if student_answers[1] == correct_answers[1]:
    print("Question 2 correct")
    score += 10
else:
    print("Question 2 wrong")

print("Score:", score)
