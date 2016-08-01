"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

       encapsulation: keeps related things together 

       abstraction: you dont need to know the information a method uses. 

       polymorphism: interchange the compoents  

2. What is a class?
    class is a type. it holds shared attributes which are applicable to all members of that class

3. What is an instance attribute?
    is given when that instance is intiated 

    def __init__(self, name):
        self.name = name 

4. What is a method?
    a function defined on a class 
        def name(self):
            return "Krisha"

5. What is an instance in object orientation?
    is an indivdual instance of that class, 

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   a class attribute is an attribute that all instances of that class
    (and decendents of that class) will have.  SO if you want all decendents 
    of that class to hav that attribute 

        eg. 
        def __init__(self, name, color, moves, num_wheels):
        self.moves = True
   
   an instance attribute is an attribute that only affects that instance of the class. this will override 
   
   eg. in the example below - if you had a yellow bike (not all bikes are yellow)


"""


# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """Student information"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address




class Question(object):
    """Questions and correct answers"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_question(self):
        print self.question 
        user_answer = raw_input("> ")
        return self.correct_answer == user_answer




class Exam(object):
    """student name and question"""
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions


    def add_question(self, question, correct_answer):
        """Add question to exam."""

        question_object = Question(question, correct_answer)
        self.questions.append(question_object)

    def administer(self):
        """Administer a test, returning the score."""

        score = 0

        for question in self.questions:
            if question.ask_question():
                score += 1

        return float(score) / len(self.questions)


def take_test(student, exam):
    """Administer exam to student and record score on student."""

    score = exam.administer()
    student.score = score

    print "Your score is %2f percent." % (student.score * 100)


def example():
    """Show usage of exam, questions, and student."""

    exam = Exam('midterm', [])

    exam.add_question(
        'What is the third planet from the sun?',
        'earth')

    exam.add_question(
        'which data structure has keys and values?',
        'dictionaries')

    exam.add_question(
        'true or false, tuples are mutable'
        'false')

    student = Student(
        'krisha',
        'nalavadi',
        'california')

    take_test(student, exam)
















