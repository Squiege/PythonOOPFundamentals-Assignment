# Task 2
class Event:
    def __init__(self, name, date, participant_count):
        self.name = name
        self.date = date
        self.participant_count = participant_count
    
    def find_participant_count(self):
        print(f"Event Name: {self.name}, Number of Participants: {self.participant_count}")

    def add_participant(self):
        extra_participants = int(input("Please enter the number of extra participants that are coming to the event: "))
        self.participant_count += extra_participants

event1 = Event("Josie's Birthday Party", "09/07/24", 25)
event2 = Event("Gary's Auto Show", "10/09/24", 148)
event3 = Event("Tommy's Balloon Show", "12/02/24", 36)

event1.find_participant_count()
event2.find_participant_count()
event3.find_participant_count()

event1.add_participant()
event2.add_participant()
event3.add_participant()

event1.find_participant_count()
event2.find_participant_count()
event3.find_participant_count()