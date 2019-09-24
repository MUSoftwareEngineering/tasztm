def viewSubmission(submissionId):

    #In this version, the submissions are kept in a dictionary with
    #their Ids as their keys
    submissions = {"12345" : "Test Student Submission"}

    if submissionId in submissions.keys():
        return submissions[submissionId]

    else:
        return "No Submission Data!"

def createStudent(id, hours, files):

    student = {"id" : id, "creditHours" : hours, "isFullTime" : False, "files" : files}

    if(student["creditHours"] >= 12):
        student["isFullTime"] = True

    return student

def uploadStudentFile(student, file):
    if (file not in student["files"]):
        student["files"].append(file)

def createSection(course, num, sectionSet):
    newSection = {"courseName" : course["name"], "number" : num, "students" : sectionSet}
    allSections = []
    courseSections = course["sections"].copy()

    for sec in courseSections:
        allSections.extend(sec)

    allSections.extend(newSection)

    allSet = set(allSections)

    if (len(allSet) == len(allSections)):
        course["sections"].append(newSection)
        return newSection

    else:
        return {"courseName" : course, "number" : num, "students" : []}

def downloadSubmissions(course, user):
    #this should pull the course from somewhere by name and get the downloadSubmissions
    #for this to work, it would also need to make sure the TA is in the course
    if (user["role"] == "TA" and course in user["courses"]):
        return "Lots of submissions"

    else:
        return None
