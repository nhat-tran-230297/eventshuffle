import json

from flask import render_template, url_for, request, redirect, jsonify

from app import db
from app.base import blueprint
from app.models import Events, Dates, People
from app.utils import validate_datetime, validate_duplicate


# default page
@blueprint.route('/')
def default_page():
    """
    Displays UI for all requests
    """

    # used for easily rendering index.html
    requests = [
        # List all events 
        {
            "title": "List all events",
            "name": "list-all-events",
            "endpoints": "/api/v1/event/list",
            "method": "get",
            "button-type": "btn-primary",
            "parameters": False
        }, 

        # Create an event
        {
            "title": "Create an event",
            "name": "create-an-event",
            "endpoints": "/api/v1/event",
            "method": "post",
            "button-type": "btn-success",
            "parameters": ["Body"]
        },

        # Show an event
        {
            "title": "Show an event",
            "name": "show-an-event",
            "endpoints": "/api/v1/event/{id}",
            "method": "get",
            "button-type": "btn-primary",
            "parameters": ["id"]
        },
        
        # Add votes to an event
        {
            "title": "Add votes to an event",
            "name": "add-votes-to-event",
            "endpoints": "/api/v1/event/{id}/vote",
            "method": "post",
            "button-type": "btn-success",
            "parameters": ["id", "Body"]
        },

        # Show the results of an event
        {
            "title": "Show the results of an event",
            "name": "show-results-of-event",
            "endpoints": "/api/v1/event/{id}/results",
            "method": "get",
            "button-type": "btn-primary",
            "parameters": ["id"]
        }   
    ]

    return render_template('index.html', requests=requests)



@blueprint.route('/event/list', methods=["GET"])
def get_all_events():
    """ List all events """


    events = Events.query.all()
    num_events = len(events)

    # when query length exceeds 100, return part of the query to prevent long loading 
    if num_events > 100:
        events_json = []
        for i in range(5):           
            events_json.append({"id": events[i].id, "name": events[i].name})
        
        events_json.append({"...": "..."})

        for i in range(num_events-20, num_events):
            events_json.append({"id": events[i].id, "name": events[i].name})                           

        return jsonify({"events": events_json}), 200


    # otherwise, display all events
    events_json = [
                    {
                        "id": event.id, 
                        "name": event.name
                    } 
                    for event in events]
    
    return jsonify({"events": events_json}), 200



@blueprint.route('/event', methods=["POST"])
def create_event():
    """ 
    Create an event 
    """

    # retrieves request input via AJAX call
    responseBody = request.form.get('responseBody')

    # handle error when user enters invalid JSON format
    try:
        responseBodyJSON = json.loads(responseBody)
    except json.decoder.JSONDecodeError:
        return jsonify({"error": "invalid input"}), 404

    # get valid request input 
    name = responseBodyJSON.get('name')
    dates = responseBodyJSON.get('dates')

    # validate request input
    if not name:
        return jsonify({"error": "'name' missing"}), 404
    
    if not dates:
        return jsonify({"error": "'dates' missing"}), 404

    if not validate_duplicate(dates):
        return jsonify({"error": "find duplicate dates"}), 404


    # interact with database
    event = Events(name=name)
    for date in dates:

        # validate the datetime format of input
        if not validate_datetime(date):
            return jsonify({"error": f"Invalid date '{date}'. Date format should be yyyy-mm-dd"}), 404

        new_date = Dates(date_format=date)
        event.dates.append(new_date)

    db.session.add(event)
    db.session.commit()

    return jsonify({"id": event.id}), 200



@blueprint.route('/event/<int:id>', methods=["GET"])
def show_event(id):
    """ 
    Show an event 
    """

    event = Events.query.get(id)

    # request event not exist
    if not event:
        return jsonify({"error": f"Event {id} does not exist"}), 404

    # response body
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

    return jsonify(event_json), 200



@blueprint.route('/event/<int:id>/vote', methods=["POST"])
def add_vote(id):
    """ 
    Add votes to an event 
    """
 
    event = Events.query.get(id)

    # requested event not exist
    if not event:
        return jsonify({"error": f"Event {id} does not exist"}), 404

    # retrieves request input via AJAX call
    responseBody = request.form.get('responseBody')

    # handle error when user enters invalid JSON format
    try:
        responseBodyJSON = json.loads(responseBody)
    except json.decoder.JSONDecodeError:
        return jsonify({"error": "invalid input"}), 404

    # get valid request input
    name = responseBodyJSON.get('name')
    votes = responseBodyJSON.get('votes')

    # validate request input
    if not name:
        return jsonify({"error": "'name' missing"}), 404
    
    if not votes:
        return jsonify({"error": "'votes' missing"}), 404

    if not validate_duplicate(votes):
        return jsonify({"error": "find duplicate dates"}), 404


    # interact with database
    person = People(name=name)

    # use hash map (key: date, value: index of date) to reduce time complexity
    date_index_map = {date.date_format: index for index, date in enumerate(event.dates)}
    for vote in votes:

        # validate the datetime format of input
        if not validate_datetime(vote):
            return jsonify({"error": f"Invalid date '{vote}'. Date format should be yyyy-mm-dd"}), 404

        # validate whether user votes for date that exists in the event
        index = date_index_map.get(vote)
        if index is None:
            return jsonify({"error": f"date {vote} does not exist"}), 404

        date = event.dates[index]       
        date.people.append(person)

    db.session.commit()

    # response body
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

    return jsonify(event_json), 200



@blueprint.route('/event/<int:id>/results', methods=["GET"])
def show_results(id):
    """ 
    Show the results of an event 
    """

    event = Events.query.get(id)

    # requested event not exist
    if not event:
        return jsonify({"error": f"Event {id} does not exist"})
    
    # get the most suitable date
    # if there are more than 1 suitable dates, display them all
    maxNumPeople = max([len(date.people) for date in event.dates])
    suitableDates = [date for date in event.dates if len(date.people) == maxNumPeople]

    # response body
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