"""
Introduction
Given students' names along with the grade that they are in, create a roster for the school.

In the end, you should be able to:

Add a student's name to the roster for a grade
"Add Jim to grade 2."
"OK."
Get a list of all students enrolled in a grade
"Which students are in grade 2?"
"We've only got Jim just now."
Get a sorted list of all students in all grades. Grades should sort as 1, 2, 3, etc., and students within a grade should be sorted alphabetically by name.
"Who all is enrolled in school right now?"
"Grade 1: Anna, Barb, and Charlie. Grade 2: Alex, Peter, and Zoe. Grade 3…"
Note that all our students only have one name. (It's a small town, what do you want?)
"""

student1 = ("Alice", 1)
student2 = ("Bobby", 2)
student3 = ("Cathy", 1)
student4 = ("Dennis", 5)


class School:
    def __init__(self):
        self.roster = {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: []
        }

    def add_student(self, student):
