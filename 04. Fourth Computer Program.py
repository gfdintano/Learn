def main():
    print("This program computes for your final grade.")
    print("By: German Francis Intano\n") #Program author hard encoded for transparency

    #Get user-input
    exam_scores = []
    for i in range (1,4):
        score = float(input("Enter your score in Exam {}: ".format(i)))
        exam_scores.append(score)
    print("")
    quiz_scores = []
    for i in range (1,5):
        score = float(input("Enter your score in Quiz {}: ".format(i)))
        quiz_scores.append(score)
    print("")
    final_exam_score = float(input("Enter your score in Final Exam: "))

    import math

    #Calculate grades
    avg_exam_score = sum(exam_scores)/len(exam_scores)
    avg_quiz_score = sum(quiz_scores)/len(quiz_scores)
    class_standing = 0.6*avg_exam_score+0.4*avg_quiz_score
    final_score = math.floor(0.7*class_standing+0.3*final_exam_score)

    #Determine equivalent grade
    if final_score >= 95:
        equivalent_grade = 1.00
    elif final_score >= 90:
        equivalent_grade = 1.25
    elif final_score >= 85:
        equivalent_grade = 1.50
    elif final_score >= 80:
        equivalent_grade = 1.75
    elif final_score >= 75:
        equivalent_grade = 2.00
    elif final_score >= 70:
        equivalent_grade = 2.25
    elif final_score >= 65:
        equivalent_grade = 2.50
    elif final_score >= 60:
        equivalent_grade = 2.75
    elif final_score >= 55:
        equivalent_grade = 3.00
    else:
        equivalent_grade = 5.00

    #Output
    print("\nYour average in the Exams = {:.2f}".format(avg_exam_score))
    print("Your average in the Quizzes = {:.2f}".format(avg_quiz_score))
    print("Your Class Standing prior to the Final Exam = {:.1f}".format(class_standing))
    print("Your Final Grade is: {} = {}".format(final_score,equivalent_grade))   
if __name__ == "__main__":
    main()
