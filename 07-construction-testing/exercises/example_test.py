import pytest
import System
import Staff
import Professor
import Student
import User
import RestoreData
# Tests if the program can handle a wrong username
def test_login(grading_system):
    # This one can not handle bad input
    with pytest.raises(KeyError) as excinfo:
        username = 'thtrhg'
        password =  'fhjhjdhjdfh'
        # username = 'goggins'
        # password = 'augurrox'
        grading_system.login(username,password)
    assert "key error is created so the function can not handle a wrong password" in str(excinfo.value)
def test_password(grading_system):
    # First I test if it can handle an incorrect password
    username = 'goggins'
    password = 'aug sadjf23423'
    grading_system.check_password(username, password)
    # Now I check if it can handle all the correct the users in the system and log them all in
    for user in grading_system.users:
        if grading_system.check_password(user, grading_system.users[user]['password']) != True:
            assert False
    assert True

def test_grade(staff_system, grading_system):
    # This is one is false because it doesn't change the correct grade it tries to change every grade to 0 
    name = 'yted91'
    course = 'cloud_computing'
    assignment = 'assignment1'
    grade = 10
    staff_system.change_grade(name,course, assignment, grade)
    assert grading_system.users[name]['courses'][course][assignment]['grade'] == grade

def test_create_assignment(staff_system, grading_system):
    ## this fails since the staff does not have an attribute all courses
    assignment_name = 'assignment20'
    due_date = "2/2/25"
    course = "comp_sci"
    staff_system.create_assignment(assignment_name, due_date, course)
    grading_system.load_data()
    assert grading_system.courses[course][assignment_name] != None

def test_add_student(grading_system, staff_system):
    # This one doesn't work because of a bug in Professor class
    name = 'Nick Wylie'
    course = 'software_engineering'
    
    prof = Professor.Professor("goggins", grading_system.users, grading_system.courses)
    prof.add_student(name, course)
    grading_system.load_data()
    assert grading_system.users[name][course]  != None

def test_drop_student(grading_system):
    # This one works
    # user = User.User()
    temp_class = grading_system.users["yted91"]["courses"]["software_engineering"]
    print(temp_class)
    prof = Professor.Professor("goggins", grading_system.users, grading_system.courses)
    prof.drop_student("yted91", "software_engineering")
    grading_system.load_data()
    if "software_engineering" not in grading_system.users["yted91"]["courses"]:
        grading_system.users["yted91"]["courses"]["software_engineering"] = temp_class
        prof_2 = Professor.Professor("goggins", grading_system.users, grading_system.courses)
        prof_2.update_user_db()
        assert True
    else:
        grading_system.users["yted91"]["courses"]["software_engineering"] = temp_class
        prof_3 = Professor.Professor("goggins", grading_system.users, grading_system.courses)
        prof_3.update_user_db()
        assert False

def test_submit_assignment( grading_system):
    # I cant get the function to initialize
    # (self,course,assignment_name,submission,submission_date)
    studentSystem = Student.Student("yted91",grading_system.users,grading_system.courses)
    submission = "This is a test submission"
    assignment_name = "assignment2"
    course = "cloud_computing"
    studentSystem.submit_assignment(course,assignment_name,submission, "1/3/25")
    grading_system.load_data()
    if grading_system.users["yted91"]["courses"][course][assignment_name]['submission'] == submission:
        assert True
    else:
        assert False
def test_check_ontime(grading_system):
    # This function is wrong because the check on time will always return true
    studentSystem = Student.Student("yted91",grading_system.users,grading_system.courses)
    student_name = "yted91"
    course = "cloud_computing"
    assignment_name = "assignment1"
    if grading_system.users["yted91"]["courses"][course][assignment_name]['ontime'] == True:
        if studentSystem.check_ontime("07/11/20","08/11/21") == True:
            assert True
        else:
            assert False
    else:
        if studentSystem.check_ontime("07/11/24","08/11/25") == True:
            assert False
        else:
            assert True

def test_check_grades(grading_system):
    # This was works
    studentSystem = Student.Student("yted91",grading_system.users,grading_system.courses)
    the_grades = studentSystem.check_grades("cloud_computing")
    ## checks to see if all the assignments have the same grades 
    if len(the_grades) != len(grading_system.users["yted91"]["courses"]["cloud_computing"]):
        assert False
    for i in range(0, len(the_grades)):
        # print(grading_system.users["yted91"]["courses"]["cloud_computing"][assignment]['grade'])
        if grading_system.users["yted91"]["courses"]["cloud_computing"][the_grades[i][0]]['grade'] != the_grades[i][1]:
            assert False
    assert True

def test_view_assignments(grading_system):
    # This one passes
    studentSystem = Student.Student("yted91",grading_system.users,grading_system.courses)
    the_assignments = studentSystem.view_assignments("cloud_computing")
    print(the_assignments)
    print(grading_system.users["yted91"]["courses"]["cloud_computing"])
    if len(the_assignments) != len(grading_system.users["yted91"]["courses"]["cloud_computing"]):
        assert False
    for i in range(0, len(the_assignments)):
        print(the_assignments[i])
        print(grading_system.users["yted91"]["courses"]["cloud_computing"])
        if grading_system.users["yted91"]["courses"]["cloud_computing"][the_assignments[i][0]] == None:
            assert False
    assert True




@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

@pytest.fixture
def staff_system():
    staffSystem = Staff.Staff()
    return staffSystem

# @pytest.fixture
# def student_system():
#     studentSystem = Student.Student("yted91",grading_system.users,grading_system.courses)
#     return studentSystem
