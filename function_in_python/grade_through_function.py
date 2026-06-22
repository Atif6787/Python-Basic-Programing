while True:
    def get_grade(score):
        if score < 50:
            print(f"Your score is {score} and you got F grade")
        elif score >= 50 and score <= 60:
            print(f"Your score is {score} and you got E grade")
        elif score > 60 and score <= 70:
            print(f"Your score is {score} and you got D grade")
        elif score > 70 and score <= 80:
            print(f"Your score is {score} and you got C grade")
        elif score > 80 and score <= 90:
            print(f"Your score is {score} and you got B grade")
        else:
            print(f"Your score is {score} and you got A grade")

    score = int(input("Enter your score: "))
    if score == 0:
        print("The program execution is stop")
        break

    get_grade(score)