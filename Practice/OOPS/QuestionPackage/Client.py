from Question import Question

question = [
    ["What is the color of apple ? \n(a) Red \n(b) Green \n(c) Yellow \n(d) Blue\n", "a"],
    ["Whats the color of banana ? \n(a) Red \n(b) Green \n(c) Yellow \n(d) Blue\n", "c"],
    ["What is the color of grapes ? \n(a) Red \n(b) Green \n(c) Yellow \n(d) Blue\n", "b"],
    ["What is the color of mango ? \n(a) Red \n(b) Green \n(c) Yellow \n(d) Blue\n", "c"],
    ["What is the color of orange ? \n(a) Red \n(b) Green \n(c) Yellow \n(d) Blue\n", "d"]
]

questionList = []

for q in question:
    questionList.append(Question(q[0], q[1]))


def runQuiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if(answer.lower() == question.answer.lower()):
            print("Correct!")
            score += 1
    return score

print("Welcome to the Quiz!")
print("Please answer the following questions:")
print("Instructions: Type the letter corresponding to your answer and press Enter.")
result = runQuiz(questionList)
print("Quiz Completed!")
print("Thank you for participating!")
print("Your Score is " + str(result) + "/" + str(len(questionList)))


