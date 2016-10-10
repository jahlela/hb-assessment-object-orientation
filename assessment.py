"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Object orientation gives us:
        1. Encapsulation: We can keep methods and the data that those methods 
            act upon in close, organized proximity.

        2. Abstraction: If one developer has designed a particularly complex 
            method, other developers or even users do not need to understand the 
            underlying mechanics in order to use that method.

        3. Polymorphism: 


2. What is a class?
    A: Classes are like more sophisticated dictionaries that can store data, 
    are structured -- helping control user error and organization -- and have 
    their own methods which are intrinsically linked to the types of data that
    they can store and act upon.


3. What is an instance attribute?
    A: An instance attribute is an attribute specific to the instance of a class.
    This attribute will not affect any other instance of the same class, nor 
    will it affect the class itself.


4. What is a method?
    A: A method is a function that can be called on an instance of the class 
    in which the method resides. 


5. What is an instance in object orientation?
    A: An instance is an object that is made in the image of its creator, the 
    Class. The instance will automatically have all of the attributes delineated
    by the class, as well as any others individually added as instance attributes.


6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A: A class attribute will apply to all instances of that attribute equally. 
   If we are creating classes of animals taxonomically, we know that all mammals
   are warm-blooded. Warm-bloodedness would be a good candidate for a class 
   attribute. 

   Instance attributes, on the other hand, are specific to each instance of 
   that class. For example, not all mammals give birth to live young. 
   The platypus lays eggs. It would be incorrect to set a class attribute for 
   all mammals to have live young. Instead, an instance attribute would be more 
   appropriate. In this example, a horse would have an instance attribute for 
   live young as True, and a platypus would be set to False.


"""


# Parts 2 through 5:
# Create your classes and class methods


class Student(object): 
    """
    Creates a student with instance attributes of first name, last name and address
    """

    def __init__(self, first_name, last_name, address):
        """ Initialize student attributes """

        self.first_name = first_name
        self.last_name = last_name 
        self.address = address



###############################

class Question(object): 

    def __init__(self, question, correct_answer):
        """ Initialize student attributes """

        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):

        student_answer = raw_input(self.question + " \n> ")

        return student_answer == self.correct_answer


###############################

class Exam(object): 

    def __init__(self, name, exam_questions = []):
        """ Initialize student attributes """

        self.name = name
        self.exam_questions = exam_questions

    def add_question(self, question, correct_answer):

        new_question = Question(question,correct_answer)
        self.exam_questions.append(new_question)


    def administer(self):
        score = 0

        for q in self.exam_questions:
            # Handily, 1 + True = 2, and 1 + False = 1
            score += q.ask_and_evaluate()

        return score


###############################


def take_test(exam, student):

    student.score = exam.administer()

###############################

def exam_example():

    # Instantiate student
    amir = Student('Amir', 'Fonso', '222 Renault St.')

    # Instantiate my_exam
    my_exam = Exam("My new exam")

    # Add questions
    my_exam.add_question("what's up", "not much")
    my_exam.add_question("Where do vanilla beans come from?", "orchids")

    # Administer test
    take_test(my_exam, amir)

    # Print results
    print amir.first_name, "scored ", amir.score


exam_example()

###############################


# # Ran out of time here, but I wanted to get the number of questions in the exam
# # and use that instead of feeding in possible score.


# class Quiz(Exam, possible_score):

#     def __init__(self):
#         self.possible_score = possible_score
#         raw_score = super(Exam, self).administer()

#     percent = raw_score/possible_score 

#     print percent > 0.5



