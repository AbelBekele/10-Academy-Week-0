from datetime import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # where we initialzed our app
# by default the flask run in production
# python-dotenv allow to create a flask dotenv file to have default info
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1001@localhost/Week-0_Features'
db = SQLAlchemy(app)
CORS(app)

class Event(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    description=db.Column(db.String(100), nullable=False)
    created_at=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Event: {self.description}"
    
    def __init__(self, description):
        self.description = description

with app.app_context():
    db.create_all()

class channel_activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Message_count = db.Column(db.Integer, nullable=False)
    Reply_and_Reaction_count = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Channel_activity: id={self.id}, messages_count={self.Message_count}, reply_count={self.Reply_and_Reaction_count}"

@app.route('/channel_activity', methods=['GET'])
def get_channel_activity():
    channel_data = channel_activity.query.all()
    channel_list = []

    for channel in channel_data:
        channel_list.append({
            "name": f"Channel {channel.id}",
            "value": channel.Message_count,  # Correct column name
            "reply_count": channel.Reply_and_Reaction_count  # Correct column name
        })

    return jsonify({'channel_activity': channel_list})


@app.route('/')
def hello():
    return 'Hey'

@app.route('/event', methods = ['POST'])
def create_event():
    description = request.json['description']
    event = Event(description)
    db.session.add(event)
    db.session.commit()
    return format_event(event)

@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.order_by(Event.id.asc()).all()
    event_list = []
    for event in events:
        event_list.append(format_event(event))
    return {'events': event_list}

#get single event
@app.route('/events/<id>', methods=['GET'])
def get_event(id):
    event = Event.query.filter_by(id=id).one()
    formatted_event = format_event(event)
    return {'event': formatted_event}

#delete an event
@app.route('/events/<id>', methods=['DELETE'])
def delete_event(id):
    event = Event.query.filter_by(id=id).one()
    db.session.delete(event)
    db.session.commit()
    return f'Event(id: {id}) deleted!'

#update an event
@app.route('/events/<id>', methods=['PUT'])
def update_event(id):
    event = Event.query.filter_by(id=id)
    description = request.json['description']
    event.update(dict(description = description, created_at = datetime.utcnow()))
    db.session.commit()
    return {'event': format_event(event.one())}

if __name__ == '__main__':
    app.run()