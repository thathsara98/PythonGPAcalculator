subjects=int(input("How many subjects you have?: "))

gpaCount=0.000
gpaCount=float(gpaCount)
totalPointsEarned=0.0
totalHours=0.0

finalGpa=0.0


for  i in range(subjects):
    grade=input("Enter your Grades: ")
    hours=int(input("Enter Hours: "))
    #totalPointsEarned=gpaCount * hours
    totalHours+=hours

    if ((grade=="A+") or grade=="A") :
        gpaCount=+4.0

    elif grade=="A-":
        gpaCount=+3.7

    elif grade=="B+":
        gpaCount=+3.3
        

    elif grade=="B":
        gpaCount=+3.0
        

    elif grade=="B-":
        gpaCount=+2.7
        

    elif grade=="C+":
        gpaCount=+2.3
        

    elif grade=="C":
        gpaCount=+2.0


    elif grade=="C-":
        gpaCount=+1.7
        

    elif grade=="D+":
        gpaCount=+1.3
        

    elif grade=="D":
        gpaCount=+1.0
        

    else:
        break

    totalPoints=gpaCount * hours
    totalPointsEarned+=totalPoints

finalGpa=totalPointsEarned / totalHours
print("Your GPA is : ", finalGpa)