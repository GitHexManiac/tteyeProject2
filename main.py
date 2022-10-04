grades_file = open("Project2.txt", "r")
all_lines = grades_file.readlines()
for grade_line in all_lines:
    student_stuff = grade_line.split(":")
    ID = student_stuff[0]
    GPA = student_stuff[-1]
    print(ID, GPA)