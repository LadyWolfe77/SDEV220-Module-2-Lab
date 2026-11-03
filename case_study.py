#get last name as input and test whether it's 'ZZZ'
while True:
    last_name = input("Enter student's last name or ZZZ to quit: ")

    if last_name == 'ZZZ':
        break

    first_name = input("Enter student's first name: ")
    gpa = input("Enter student's G.P.A.: ")
#convert string input into float
    gpa = float(gpa)
#test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
    if gpa >= 3.5:
        print(f"{first_name} {last_name} made the Dean's List.")
#test if the student's GPA is 3.25 or greater and, if so, print a message saying that the studnet has made the Honor Roll.
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} made the Honor Roll.")
    
print("Goodbye")