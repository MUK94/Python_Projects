Data_Obj = {
    "1": {
            "question": "When was Python created ?",
            "answer": "1991",
        },
    "2": {
            "question": "Who created Python ?",
            "answer": "Guido Rossum"
        },
    "3": {
            "question": "What is the most popular full-stack python web framework ?",
            "answer": "django"
        },
    "4": {
            "question": "Which technique of OOP does Python use to implement Abstraction ?",
            "answer": "Inheritance"
        },
    "5": {
            "question": "Which architecture does Django use ?",
            "answer": "MVT"
        },
}


def main():
    score = 0
    print("================ //////// ================")
    print("Ready to take the Quizz? let's start :)")

    for k, v in Data_Obj.items():
        print(v["question"])
        answer = input("Type your answer: ")
        
        if answer.lower() == v["answer"].lower():
            score = score + 1
            print("[** Correct **] 👍")
            print("Your score is: " + str(score))
            print("")

        else:
            print("[^^ Wrong Answer ^^] 👎")
            print("The answer is: " + str(v["answer"]))
            print("your score is: " + str(score))
            print("")

    if score == 2:
        print("🎉Congratulations🎉")
        print("Your scored " + str(score) + " out of 5 Questions")
    else:
        print("Keep trying!")
        print("Your scored " + str(score) + " out of 5 Questions")

main()