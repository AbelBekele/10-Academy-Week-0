from collections import Counter, defaultdict
from datetime import datetime

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

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

class channel_messages_ts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    channel_name = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(255), nullable=False)
    timestamp_events = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Channel_messages_ts: id={self.id}, channel_name={self.channel_name}, text={self.text}, timestamp_events={self.timestamp_events}"

class channel_messages_sentiment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    channel = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(255), nullable=False)
    sentiment_score = db.Column(db.Float, nullable=False)
    sentiment = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Channel_messages_sentiment: id={self.id}, channel={self.channel}, text={self.text}, sentiment_score={self.sentiment_score}, sentiment={self.sentiment}"

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

@app.route('/channel_activity_ts', methods=['GET'])
def get_channel_activity_ts():
    channel_data = channel_messages_ts.query.filter(
        (channel_messages_ts.channel_name == 'all-community-building') |
        (channel_messages_ts.channel_name == 'all-resources')
    ).all()

    # Check if there's any data
    if not channel_data:
        return jsonify({'channel_activity_ts': []})

    # Extract the first and last timestamps
    min_timestamp = min(channel.timestamp_events for channel in channel_data)
    max_timestamp = max(channel.timestamp_events for channel in channel_data)

    # Convert string timestamps to datetime objects
    try:
        min_timestamp = datetime.strptime(min_timestamp, '%Y-%m-%d %H:%M:%S.%f')
        max_timestamp = datetime.strptime(max_timestamp, '%Y-%m-%d %H:%M:%S.%f')
    except ValueError:
        min_timestamp = datetime.strptime(min_timestamp, '%Y-%m-%d %H:%M:%S')
        max_timestamp = datetime.strptime(max_timestamp, '%Y-%m-%d %H:%M:%S')

    # Calculate date ranges
    date_ranges = [
        min_timestamp + i * ((max_timestamp - min_timestamp) / 5)
        for i in range(6)
    ]

    # Create a dictionary to store data grouped by date and channel
    data_dict = defaultdict(lambda: defaultdict(int))

    for channel in channel_data:
        # Convert string timestamp to datetime object
        channel_timestamp = datetime.strptime(channel.timestamp_events, '%Y-%m-%d %H:%M:%S')

        # Find the corresponding date range for the timestamp
        date_range = next(
            (date_ranges[i] for i in range(5) if date_ranges[i] <= channel_timestamp <= date_ranges[i + 1]),
            date_ranges[-1]
        )

        # Extract month and year from the date range
        month_year = date_range.strftime('%b %y')

        # Update the corresponding channel count based on the channel name
        data_dict[month_year][channel.channel_name] += 1  # Increment count by 1

    # Convert the dictionary to the required format
    chartdata = [
        {
            "date": date,
            "all-community-building": data_dict[date]["all-community-building"],
            "all-resources": data_dict[date]["all-resources"],
        }
        for date in data_dict
    ]

    return jsonify({'channel_activity_ts': chartdata})

@app.route('/top_channel_messages', methods=['GET'])
def get_top_channel_messages():
    # Retrieve the text column and channel_name from the database
    messages = channel_messages_ts.query.filter(channel_messages_ts.text.isnot(None)).all()

    # Extract text and channel_name from each message
    message_data = [(message.text.lower(), message.channel_name) for message in messages]

    # Calculate the frequency of each unique text and channel_name combination
    text_freq = Counter(message_data)

    # Display the top 10 most repeated full texts along with channel_name
    top_repeated_texts = text_freq.most_common(15)

    top_messages_list = []
    for (text, channel_name), count in top_repeated_texts:
        top_messages_list.append({
            "text": text,
            "channel_name": channel_name,
            "count": count
        })

    return jsonify({'top_channel_messages': top_messages_list})

@app.route('/channel_messages_sentiment', methods=['GET'])
def get_channel_messages_sentiment():
    # Use SQLAlchemy's func.avg to calculate average sentiment_score per channel
    avg_sentiment_data = db.session.query(
        channel_messages_sentiment.channel,
        func.avg(channel_messages_sentiment.sentiment_score).label('average_sentiment_score')
    ).group_by(channel_messages_sentiment.channel).all()
 
    avg_sentiment_list = []

    for avg_sentiment in avg_sentiment_data:
        avg_sentiment_list.append({
            "channel": avg_sentiment.channel,
            "average_sentiment_score": avg_sentiment.average_sentiment_score,
        })

    return jsonify({'average_sentiment_per_channel': avg_sentiment_list})


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