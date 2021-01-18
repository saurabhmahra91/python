from datetime import datetime
from datetime import timedelta
import webbrowser


class WeekSlot:
    def __init__(self, starting_times):
        self.all_slots = []
        for starting_time in starting_times:
            for i in range(Course.TOTAL_WEEKS):
                self.all_slots.append(starting_time + i*timedelta(days=7))


class Course:
    # assuming n_of_weeks in 4months to be = 120 days / 7days in a week
    TOTAL_WEEKS = 120//7

    def __init__(self, link, first_week_slots):
        self.link = link
        self.first_week_slots = first_week_slots
        self.slots = WeekSlot(first_week_slots).all_slots


class Timetable:
    def __init__(self, all_courses):
        self.all_courses = all_courses


CE228 = Course("https://kaksha.webex.com/webappng/sites/kaksha/meeting/info/c31f063dd5144d11a1baf701c14610a0?MTID=md9aa53f09ebc04d36a907886880d9cc9", [datetime(day=4, month=1, year=2021, hour=11, minute=35), datetime(
    day=5, month=1, year=2021, hour=8, minute=30), datetime(day=7, month=1, year=2021, hour=9, minute=30)])
CE232 = Course("https://teams.microsoft.com/_#/school/conversations/General?threadId=19:2bd7059932194bacbf9a188568178bbf@thread.tacv2&ctx=channel", [datetime(day=4, month=1, year=2021, hour=8, minute=30), datetime(
    day=5, month=1, year=2021, hour=9, minute=30), datetime(day=7, month=1, year=2021, hour=10, minute=35)])
ES200 = Course("https://teams.microsoft.com/_#/school/conversations/General?threadId=19:fdd9a344022f462286b045fda2e5c5b7@thread.tacv2&ctx=channel", [datetime(day=4, month=1, year=2021, hour=9, minute=30), datetime(
    day=5, month=1, year=2021, hour=10, minute=35), datetime(day=7, month=1, year=2021, hour=11, minute=35)])
CE204 = Course("https://teams.microsoft.com/_#/school/conversations/General?threadId=19:f9c30482a53543e8abc5d125a5085a70@thread.tacv2&ctx=channel", [datetime(day=4, month=1, year=2021, hour=10, minute=35), datetime(
    day=5, month=1, year=2021, hour=11, minute=35), datetime(day=7, month=1, year=2021, hour=8, minute=30)])
CE222 = Course("https://teams.microsoft.com/_#/school/conversations/General?threadId=19:1fa1bc8d2956472da13e2f686d2d1855@thread.tacv2&ctx=channel", [datetime(day=6, month=1, year=2021, hour=11, minute=5), datetime(
    day=6, month=1, year=2021, hour=3, minute=0), datetime(day=8, month=1, year=2021, hour=11, minute=5)])
CE230 = Course("https://google.com/",
               [datetime(day=5, month=1, year=2021, hour=14, minute=35)])

all_courses = [CE228, CE232, ES200, CE204, CE222, CE230, ]
spring2021 = Timetable(all_courses)




for course in spring2021.all_courses:
    for slot in course.slots:
        if slot.weekday() == datetime.now().weekday() and (slot - timedelta(minutes=10) <= datetime.now() <= slot + timedelta(minutes=40)):
            print("success")
            webbrowser.open(course.link, new=0)
