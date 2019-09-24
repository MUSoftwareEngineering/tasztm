def viewSubmission(submissionId):

    #In this version, the submissions are kept in a dictionary with
    #their Ids as their keys
    submissions= {"12345" : "Test Student Submission"}

    if submissionId in submissions.keys():
        return submissions[submissionId]

    else:
        return None

def createStudent(id, hours, files):

    student = {"id" : id, "creditHours" : hours, "isFullTime" : False, "files" : files}

    if(student["creditHours"] >= 12):
        #student["isFullTime"] = True
        student["isFullTime"] = False

    return student

def uploadStudentFile(student, file):
    student["files"].append(file)

def createSection(course, num, sectionSet):
    #in the real system we would get the course and add the set
    newSection = {"courseName" : course, "number" : num, "students" : sectionSet}
    return newSection

def downloadSubmissions(course, user):
    #this should pull the course from somewhere by name and get the downloadSubmissions
    #for this to work, it would also need to make sure the TA is in the course
    if (user["role"] == "TA" and course in user["courses"]):
        return "Lots of submissions"

    else:
        return None
