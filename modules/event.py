#event class goes here
## MVP

# Your application should have a single class - Event - and should contain the following properties:
# * Date
# * Name of Event
# * Number of guests
# * Room Location
# * Description

# Provide the following functionality:
# * List all events
# * Create an event in the event planner.
# from modules.events import events

class Event:
    def __init__(self, date, name_of_event, number_of_guests, room_location, description, recurring):
        self.date = date
        self.name = name_of_event
        self.num_guests = number_of_guests
        self.room_location = room_location
        self.desc = description
        self.recurring = recurring


