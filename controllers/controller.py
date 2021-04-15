from flask import render_template, request
from app import app
from modules.events import events, add_event_to_events, remove_event_from_events
from modules.event import Event

@app.route("/")
def home():
    return render_template("index.html", title="title", events= events)

        # self.date = date
        # self.name_of_event = name_of_event
        # self.number_of_guests = number_of_guests
        # self.room_location = room_location
        # self.Description = Description

@app.route("/", methods=["POST"])
def add_event():
    print(request.form)
    date = request.form["name-of-event"]
    name = request.form["date"]
    number_of_guests = request.form["number-of-guests"]
    room_location = request.form["room-location"]
    description = request.form["description"]
    is_recurring = request.form.get("recurring")
    if is_recurring == None:
        is_recurring = False
    else:
        is_recurring = True
    
    new_event = Event(date, name, number_of_guests, room_location, description, is_recurring)
    add_event_to_events(new_event)
    return render_template("index.html", title="title", events= events)

