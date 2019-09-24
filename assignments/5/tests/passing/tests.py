import pytest
import functions

def test_view_submission_not_null():

    submission = functions.viewSubmission("1234")

    print("\nTesting that view submission does not return null.")
    assert submission is not None

def test_student_fulltime():

    print("\nTesting that student has proper state.")

    student = functions.createStudent("0001", 15, ["testFile"])
    if (student["creditHours"] >= 12):
        assert student["isFullTime"] is True

    else:
        assert student["isFullTime"] is False

def test_verify_unique_filenames():

    print("\nTesting if duplicate file names are able to submit.")

    testFiles = ["1", "2", "3"]
    student = functions.createStudent("0001", 17, testFiles)
    functions.uploadStudentFile(student, "3")

    #Because sets get rid of duplicates, these should have the same length
    testSet = set(student["files"])
    assert len(student["files"]) == len(testSet)

def test_verify_unique_sections():

    course = {"name" : "testCourse", "sections" : []}

    print("\nTesting if sections of the same course can contain the same students.")
    section1 = functions.createSection(course, 0, ["student1", "student2", "student3"])
    section2 = functions.createSection(course, 1, ["student3", "student4", "student5"])
    intersect = set(section1["students"]) & set(section2["students"])

    assert len(intersect) == 0

def test_TA_download_submissions():
    testTA = {"name" : "Test Name", "role" : "TA", "id" : "20102", "courses" : ["testCourse1", "testCourse2", "testCourse3"]}

    print("\nTesting if TA's can get submissions from classes they're not in.")
    #this should return null, as this course does not exist in the user
    submissions = functions.downloadSubmissions("testCourse", testTA)
    assert submissions is None
