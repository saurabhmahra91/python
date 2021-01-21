"""
To customize this application according to 
your schedule, head over to bottom of this file 
and replace the courses with that of yours

"""




from datetime import datetime, time, date
from datetime import timedelta
import webbrowser

class Slot:
    def __init__(self, name, starting_time, length, day):
        self.weekday = day
        self.starting_time = starting_time
        self.ending_time = (datetime.combine(
            date.today(), starting_time) + length).time()
        self.name = name
        self.running_course = None

    def __repr__(self):
        return self.name

    def is_set(self):
        if self.running_course != None:
            print(f"course {self.running_course} is going on now")
            return True
        else:
            print(f"None of your classes run on the slot {self}")
            return False    

    def set_course(self, course):
        self.running_course = course

    def is_running(self):
        time = datetime.now()
        if time.weekday() == self.weekday and datetime.combine(date.today(), self.starting_time) - timedelta(minutes=10) <= time <= datetime.combine(date.today(), self.ending_time) + timedelta(minutes=15):
            print(f"Redirecting to slot {self}. Lemme check if there is a class going on now.")
            print(self)
            return True
        else:
            return False

    def get_course(self):
        return self.running_course


class Course:
    def __init__(self, name, links, slots):
        """
        first argument: Course Name  (string)
        Ex: "CS101"

        second argument: List of all links that should be opened during that course lecture (list) 
        Ex: ["https://google.com", "https://webmail.iitb.ac.in"]


        Third argument: List of slots in which the course runs, if you dont know 
        the slot pattern of iitb, head over to this image
        slots.png
        Ex: [A1, L3]
        """
        self.name = name
        self.links = links
        self.all_slots = slots
        for slot in self.all_slots:
            slot.set_course(self)

    def __repr__(self):
        return self.name




# all monday slots
A1 = Slot("A1", time(hour=8, minute=30), timedelta(minutes=55), 0)
A2 = Slot("A2", time(hour=9, minute=30), timedelta(minutes=55), 0)
A3 = Slot("A3", time(hour=10, minute=35), timedelta(minutes=55), 0)
A4 = Slot("A4", time(hour=11, minute=35), timedelta(minutes=55), 0)
A8 = Slot("A8", time(hour=14, minute=0), timedelta(hours=1, minutes=25), 0)
A9 = Slot("A9", time(hour=15, minute=30),
          timedelta(hours=1, minutes=25), 0)
A12 = Slot("A12", time(hour=14, minute=10), timedelta(minutes=55), 0)
A13 = Slot("A13", time(hour=14, minute=10), timedelta(minutes=55), 0)
L1 = Slot("L1", time(hour=2, minute=0), timedelta(hours=3), 0)

# all tuesday slots
B4 = Slot("B4", time(hour=8, minute=30), timedelta(minutes=55), 1)
B1 = Slot("B1", time(hour=9, minute=30), timedelta(minutes=55), 1)
B2 = Slot("B2", time(hour=10, minute=35), timedelta(minutes=55), 1)
B3 = Slot("B3", time(hour=11, minute=35), timedelta(minutes=55), 1)
A10 = Slot("A10", time(hour=14, minute=0),
           timedelta(hours=1, minutes=25), 1)
A11 = Slot("A11", time(hour=15, minute=30),
           timedelta(hours=1, minutes=25), 1)
A14 = Slot("A14", time(hour=17, minute=30),
           timedelta(hours=1, minutes=25), 1)
L2 = Slot("L2", time(hour=2, minute=0), timedelta(hours=3), 1)
A15 = Slot("A15", time(hour=19, minute=0),
           timedelta(hours=1, minutes=25), 1)

# all wednesday slots
A7 = Slot("A7", time(hour=8, minute=30), timedelta(hours=1, minutes=25), 2)
A5 = Slot("A5", time(hour=9, minute=30), timedelta(hours=1, minutes=25), 2)
A6 = Slot("A6", time(hour=11, minute=5), timedelta(hours=1, minutes=25), 2)
X1 = Slot("X1", time(hour=14, minute=0), timedelta(hours=1), 2)
X2 = Slot("X2", time(hour=15, minute=0), timedelta(hours=1), 2)
X3 = Slot("X3", time(hour=16, minute=0), timedelta(hours=1), 2)
LX = Slot("LX", time(hour=14, minute=0), timedelta(hours=3), 2)
XC = Slot("XC", time(hour=17, minute=30),
          timedelta(hours=1, minutes=25), 2)
XD = Slot("XC", time(hour=19, minute=0), timedelta(hours=1, minutes=25), 2)
L5 = Slot("L5", time(hour=9, minute=30), timedelta(hours=3), 2)


# all thursday slots
C3 = Slot("C3", time(hour=8, minute=30), timedelta(minutes=55), 3)
C4 = Slot("C4", time(hour=9, minute=30), timedelta(minutes=55), 3)
C1 = Slot("C1", time(hour=10, minute=35), timedelta(minutes=55), 3)
C2 = Slot("C2", time(hour=11, minute=35), timedelta(minutes=55), 3)
B8 = Slot("A8", time(hour=14, minute=0), timedelta(hours=1, minutes=25), 3)
L3 = Slot("L3", time(hour=2, minute=0), timedelta(hours=3), 3)
B9 = Slot("A9", time(hour=15, minute=30),
          timedelta(hours=1, minutes=25), 3)
B12 = Slot("A12", time(hour=17, minute=30),
           timedelta(hours=1, minutes=25), 3)
B13 = Slot("A13", time(hour=19, minute=0),
           timedelta(hours=1, minutes=25), 3)

# all friday slots
B7 = Slot("B7", time(hour=8, minute=30), timedelta(minutes=55), 4)
B5 = Slot("B5", time(hour=9, minute=30), timedelta(hours=1, minutes=25), 4)
B6 = Slot("A6", time(hour=11, minute=5), timedelta(hours=1, minutes=25), 4)
L4 = Slot("L4", time(hour=14, minute=0), timedelta(hours=3), 4)
B10 = Slot("B10", time(hour=14, minute=0),
           timedelta(hours=1, minutes=25), 4)
B11 = Slot("B11", time(hour=15, minute=30),
           timedelta(hours=1, minutes=25), 4)
B14 = Slot("B14", time(hour=17, minute=30),
           timedelta(hours=1, minutes=25), 4)
B15 = Slot("B15", time(hour=19, minute=0),
           timedelta(hours=1, minutes=25), 4)
L6 = Slot("L6", time(hour=9, minute=30), timedelta(hours=3), 4)


class Timetable:
    all_slots = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, B1, B2, B3, B4, B5, B6, B7,
                 B8, B9, B10, B11, B12, B13, B14, B15, C1, C2, C3, C4, X1, X2, X3, XC, XD, LX, L1, L2, L3, L4, L5, L6]

    def __init__(self, all_courses):
        self.all_courses = all_courses

    def which_class(self, slot):
        return slot.course

    def connect(self):
        for slot in self.all_slots:
            if slot.is_running() and slot.is_set():
                all_links = slot.get_course().links
                print(f"connecting to the course {slot.get_course()}")
                print("Attend it with full focus, best of luck!")
                for link in all_links:
                    webbrowser.open(link, new=0)
















####################To Be Edited By End User##########################################
"""


first argument: Course Name  (string)
Ex: "CS101"



second argument: List of all links that should be opened during that course lecture (list) 
Ex: ["https://google.com", "https://webmail.iitb.ac.in"]



Third argument: List of slots in which the course runs, if you dont know 
the slot pattern of iitb, head over to this image
slots.png
Ex: [A1, L3]


"""

CE228 = Course("CE228", [
               "https://kaksha.webex.com/webappng/sites/kaksha/meeting/info/c31f063dd5144d11a1baf701c14610a0?MTID=md9aa53f09ebc04d36a907886880d9cc9"], [A4, B4, C4])
CE232 = Course("CE232", [
               "https://teams.microsoft.com/_#/school/conversations/General?threadId=19:2bd7059932194bacbf9a188568178bbf@thread.tacv2&ctx=channel"], [A1, B1, C1])
ES200 = Course("ES200", [
               "https://teams.microsoft.com/_#/school/conversations/General?threadId=19:fdd9a344022f462286b045fda2e5c5b7@thread.tacv2&ctx=channel"], [A2, B2, C2])
CE204 = Course("CE204", [
               "https://teams.microsoft.com/_#/school/conversations/General?threadId=19:f9c30482a53543e8abc5d125a5085a70@thread.tacv2&ctx=channel"], [A3, B3, C3])
CE230 = Course("CE230", [
               "https://teams.microsoft.com/_#/school/conversations/General?threadId=19:3b3241f42cb0465caeff98f314f69936@thread.tacv2&ctx=channel"], [L2])
CE222 = Course("CE222", [
               "https://teams.microsoft.com/_#/school/conversations/General?threadId=19:63ffb46b34b84f76b58008defa6cf9bb@thread.tacv2&ctx=channel"], [A6, B6])

"""
after making all your course objects, create a timetable object
and put there all the courses that you just initialised

Thats all!.
run this file, if there is a class running at the moment it will redirect you the links related to the same class
"""

autumn2021 = Timetable([CE204, CE222, CE228, CE232, CE230, ES200])
autumn2021.connect()

####################################################################################################
