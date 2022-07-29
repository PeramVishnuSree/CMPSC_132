# LAB2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement

import random

class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    def __init__(self, cid, cname, credits):
        self.cid = cid
        self.cname = cname
        self.credits = credits


    def __str__(self):
        ans =  f'{self.cid}({self.credits}): {self.cname}'
        return ans

    __repr__ = __str__

    def __eq__(self, other):
        try:
            return self.cid is other.cid
        except:
            return False


class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> C.courseOfferings
        {'CMPSC132': (CMPSC132(3): Programming in Python II, 400), 'CMPSC360': (CMPSC360(3): Discrete Mathematics, 200)}
        >>> C.removeCourse('CMPSC360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC132': (CMPSC132(3): Programming in Python II, 400)}
        >>> isinstance(C.courseOfferings['CMPSC132'][0], Course)
        True
    '''

    def __init__(self):
        self.courseOfferings = {}

    def addCourse(self, cid, cname, credits, capacity):
        if cid in self.courseOfferings:
            return "Course already added"
        key = cid
        value = (Course(cid, cname, credits), capacity)
        self.courseOfferings[key] = value
        return "Course added successfully"


    def removeCourse(self, cid):
        if cid not in self.courseOfferings:
            return "Course not found"
        del self.courseOfferings[cid]
        return "Course removed successfully"
        pass


class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> semester = Semester(1)
        >>> semester
        No courses
        >>> semester.addCourse(cmpsc132)
        >>> isinstance(semester.courses['CMPSC132'], Course)
        True
        >>> semester.addCourse(math230)
        >>> semester
        CMPSC132, MATH 230
        >>> semester.isFullTime
        False
        >>> semester.totalCredits
        7
        >>> semester.addCourse(phys213)
        >>> semester.addCourse(econ102)
        >>> semester.addCourse(econ102)
        'Course already added'
        >>> semester.addCourse(phil119)
        >>> semester.isFullTime
        True
        >>> semester.dropCourse(phil119)
        >>> semester.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> semester.totalCredits
        16
        >>> semester.dropCourse(cmpsc131)
        'No such course'
        >>> semester.courses
        {'CMPSC132': CMPSC132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    '''

    def __init__(self, sem_num):
        self.sem_num = sem_num
        self.courses = {}
        self.totalcreds = 0

    def __str__(self):
        if len(self.courses) == 0:
            return 'No courses'
        ans = ''
        course_list = []
        for key in self.courses:
            course_list.append(key)

        for i in range(len(course_list)):
            if i == len(course_list)-1:
                ans += str(course_list[i])
            else:
                ans += f'{course_list[i]}, '
        return ans

    __repr__ = __str__

    def addCourse(self, course):
        if course.cid in self.courses:
            return 'Course already added'

        self.courses[course.cid] = course
        self.totalcreds += int(course.credits)

    def dropCourse(self, course):
        if course.cid not in self.courses:
            return "No such course"

        del self.courses[course.cid]
        self.totalcreds -= int(course.credits)

    @property
    def totalCredits(self):
        return self.totalcreds

    @property
    def isFullTime(self):
        if self.totalcreds >= 12:
            return True
        return False

    
class Loan:
    '''
        >>> import random
        >>> random.seed(2)  # Setting seed to a fixed value, so you can predict what numbers the random module will generate
        >>> first_loan = Loan(4000)
        >>> first_loan
        Balance: $4000
        >>> first_loan.loan_id
        17412
        >>> second_loan = Loan(6000)
        >>> second_loan.amount
        6000
        >>> second_loan.loan_id
        22004
        >>> third_loan = Loan(1000)
        >>> third_loan.loan_id
        21124
    '''
    

    def __init__(self, amount):
        self.loan_id = self.__getloanID
        self.amount = amount
        pass


    def __str__(self):
        return f'Balance: ${self.amount}'
        pass

    __repr__ = __str__


    @property
    def __getloanID(self):
        return random.randint(10000, 100000)


class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

    def __str__(self):
        last_four = self.ssn[len(self.ssn)-4:]
        return f'Person({self.name}, ***-**-{last_four})'

    __repr__ = __str__

    def get_ssn(self):
        return self.ssn
        pass

    def __eq__(self, other):
        try:
            if self.ssn == other.ssn:
                return True
            return False
        except:
            return False

class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> st1 = s1.createStudent(p)
        >>> isinstance(st1, Student)
        True
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC360', C, 1)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC132}
    '''

    def __init__(self, name, ssn, supervisor=None):
        self.name = name
        self.ssn = ssn
        self.supervisor = supervisor

    def __str__(self):
        return f'Staff({self.name}, {self.id})'

    __repr__ = __str__


    @property
    def id(self):
        name = self.name.split(' ')
        initials = ''
        for i in name:
            initials += i[0]
        initials = initials.lower()
        last_four = self.ssn[len(self.ssn) - 4:]
        return f'905{initials}{last_four}'

    @property   
    def getSupervisor(self):
        return self.supervisor
        pass

    def setSupervisor(self, new_supervisor):
        try:
            self.supervisor = new_supervisor.supervisor
            return "Completed!"
        except:
            return None

    def applyHold(self, student):
        try:
            student.hold = True
            return "Completed!"
        except:
            return None

    def removeHold(self, student):
        try:
            student.hold = False
            return "Completed!"
        except:
            return None

    def unenrollStudent(self, student):
        try:
            student.active = False
            return "Completed"
        except:
            return None

    def createStudent(self, person):
        student = Student(person.name, person.ssn, 'Freshman')
        return student
        pass




class Student(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC311', C, 1)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132, CMPSC360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC132', C, 1)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC360')
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC360')
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: No courses}
        >>> s1.enrollCourse('CMPSC360', C, 2)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
    '''
    def __init__(self, name, ssn, year):
        random.seed(1)
        self.year = year
        self.name = name
        self.ssn = ssn
        self.semesters = {}
        self.hold = False
        self.active = True
        self.account = StudentAccount(self)
        self.cur_sem = 0

    def __str__(self):
        return f'Student({self.name}, {self.id}, {self.year})'

    __repr__ = __str__

    def __createStudentAccount(self):
        if self.active is False:
            return None
        self.account = StudentAccount(self)
        return self.account


    @property
    def id(self):
        name = self.name.split(' ')
        initials = ''
        for i in name:
            initials += i[0].lower()
        last_four = self.ssn[len(self.ssn)-4:]
        return f'{initials}{last_four}'


    def registerSemester(self):

        if self.hold is True or self.active is False:
            return "Unsuccessful operation"

        for i in self.semesters:
            if i > self.cur_sem:
                self.cur_sem = i
        self.cur_sem += 1
        self.semesters[self.cur_sem] = Semester(self.cur_sem)
        if self.cur_sem == 1 or self.cur_sem == 2:
            self.year = 'Freshman'
        elif self.cur_sem == 3 or self.cur_sem == 4:
            self.year = 'Sophomore'
        elif self.cur_sem == 5 or self.cur_sem == 6:
            self.year = 'Junior'
        else:
            self.year = 'Senior'


    def enrollCourse(self, cid, catalog, semester):
        if self.hold is True or self.active is False:
            return "Unsuccessful operation"
        elif cid not in catalog.courseOfferings:
            return "Course not found"
        elif cid in self.semesters[semester].courses:
            return "Course already enrolled"
        else:
            c = catalog.courseOfferings[cid][0]
            self.semesters[semester].addCourse(c)
            self.account.balance += self.account.CREDIT_PRICE * c.credits
            return "Course added successfully"


    def dropCourse(self, cid):
        if self.active is False or self.hold is True:
            return "Unsuccessful operation"
        elif cid not in self.semesters[self.cur_sem].courses:
            return "Course not found"
        else:
            c = self.semesters[self.cur_sem].courses[cid]
            del self.semesters[self.cur_sem].courses[cid]
            self.account.balance -= (self.account.CREDIT_PRICE * c.credits)/2
            return "Course dropped successfully"

    def getLoan(self, amount):
        if self.hold is True or self.active is False:
            return "Unsuccessful Operation"
        elif self.semesters[self.cur_sem].isFullTime is False:
            return "Not full-time"
        else:
            obj = Loan(amount)
            self.account.loans[obj.loan_id] = obj
            self.account.balance -= amount
        pass




class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4, 600)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2, 500)
        'Course added successfully'
        >>> C.addCourse('CMPEN270', 'Digital Design', 4, 300)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN270', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.dropCourse('CMPEN270')
        'Course dropped successfully'
        >>> s1.account.balance
        1900.0
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
        >>> StudentAccount.CREDIT_PRICE = 1500
        >>> s2 = Student('Thomas Wang', '123-45-6789', 'Freshman')
        >>> s2.registerSemester()
        >>> s2.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s2.account.balance
        4500
        >>> s1.enrollCourse('CMPEN270', C,1)
        'Course added successfully'
        >>> s1.account.balance
        7900.0
    '''

    CREDIT_PRICE = 1000

    def __init__(self, student):
        self.student = student
        self.balance = 0
        self.loans = {}



    def __str__(self):
        return f'''Name: {self.student.name}
ID: {self.student.id}
Balance: ${self.balance}'''

    __repr__ = __str__


    def makePayment(self, amount):
        self.balance -= amount
        return self.balance


    def chargeAccount(self, amount):
        self.balance += amount
        return self.balance




if __name__=='__main__':
    import doctest
    # doctest.testmod()  # OR
    doctest.run_docstring_examples(Staff, globals(), name='HW22',verbose=True) # replace Course for the class name you want to test