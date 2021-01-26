from flask import Blueprint, render_template, request, jsonify

from app import db
from app.api import blueprint
from app.models import Events, People, Dates
from app.utils import validate_datetime, validate_duplicate


@blueprint.route('/list', methods=["GET"])
def get_all_events():
    """ List all events """

    events = Events.query.all()
    events_json = [
                    {
                        "id": event.id, 
                        "name": event.name
                    } 
                    for event in events]
    
    return jsonify({"events": events_json})



@blueprint.route('/', methods=["POST"])
def create_event():
    """ Create an event """

    # get request input
    name = request.json.get('name')
    dates = request.json.get('dates')

    # validate request input
    if not name:
        return jsonify({"error": "'name' missing"})
    
    if not dates:
        return jsonify({"error": "'dates' missing"})

    if not validate_duplicate(dates):
        return jsonify({"error": "find duplicate dates"})

    # interact with database
    event = Events(name=name)
    for date in dates:

        # validate the datetime format of input
        if not validate_datetime(date):
            return jsonify({"error": f"Invalid date '{date}'. Date format should be yyyy-mm-dd"})

        new_date = Dates(date_format=date)
        event.dates.append(new_date)

    db.session.add(event)
    db.session.commit()

    return jsonify({"id": event.id})
   
    

@blueprint.route('/<int:id>', methods=["GET"])
def show_event(id):
    """ Show an event """


    event = Events.query.get(id)

    # requested event not exist
    if not event:
        return jsonify({"error": f"Event {id} does not exist"})

    event_json = {
        "id": event.id,
        "name": event.name,
        "dates": [date.date_format for date in event.dates],
        "votes": [
                    {
                        "date": date.date_format,
                        "people": [p.name for p in date.people]
                    } 
                    for date in event.dates
                ]
    }

    return jsonify(event_json)


@blueprint.route('/<int:id>/vote', methods=["POST"])
def add_vote(id):
    """ Add votes to an event """

 
    event = Events.query.get(id)

    # requested event not exist
    if not event:
        return jsonify({"error": f"Event {id} does not exist"})

    # get request input
    name = request.json.get('name')
    votes = request.json.get('votes')

    # validate request input
    if not name:
        return jsonify({"error": "'name' missing"})
    
    if not votes:
        return jsonify({"error": "'votes' missing"})

    if not validate_duplicate(votes):
        return jsonify({"error": "find duplicate dates"})


    # interact with database
    person = People(name=name)

    # use hash map (key: date, value: index of date) to reduce time complexity
    date_index_map = {date.date_format: index for index, date in enumerate(event.dates)}
    for vote in votes:
        if not validate_datetime(vote):
            return jsonify({"error": f"Invalid date '{vote}'. Date format should be yyyy-mm-dd"})

        index = date_index_map.get(vote)
        if index is None:
            return jsonify({"error": f"date {vote} does not exist"})

        date = event.dates[index]       
        date.people.append(person)

    db.session.commit()


    event_json = {
        "id": event.id,
        "name": event.name,
        "dates": [date.date_format for date in event.dates],
        "votes": [
                    {
                        "date": date.date_format,
                        "people": [p.name for p in date.people]
                    } 
                    for date in event.dates
                ]
    }

    return jsonify(event_json)


@blueprint.route('/<int:id>/results', methods=["GET"])
def show_results(id):
    """ Show the results of an event """

    event = Events.query.get(id)
    if not event:
        return jsonify({"error": f"Event {id} does not exist"})
    
    maxNumPeople = max([len(date.people) for date in event.dates])
    suitableDates = [date for date in event.dates if len(date.people) == maxNumPeople]

    results_json = {
        "id": id,
        "name": event.name,
        "suitableDates": [
                            {
                                "date": suitableDate.date_format,
                                "people": [p.name for p in suitableDate.people]
                            }
                            for suitableDate in suitableDates
                        ]
    }

    return jsonify(results_json)