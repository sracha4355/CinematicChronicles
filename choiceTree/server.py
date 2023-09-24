from flask import Flask, session
from generator_satvik import runner, init_openai, query_openai
from query import QueryBuilder

app = Flask(__name__)
app.secret_key = 'key'
data_store = {}

@app.route('/setup/choices/<int:choices>/topic/<topic>/depth/<int:depth>')
def setup(choices, topic, depth):
    data_store['past_queries'] = QueryBuilder(choices)
    data_store['topic'] = topic
    data_store['ai'] = init_openai()
    data_store['depth'] = depth
    data_store['counter'] = 0 

    return "homepage"

@app.route('/storygen')
def story_gen():
    return "story generation started"

@app.route('/state')
def check_state():
    data_store['past_queries'].points.printPlotPoints()
    print(data_store['topic'])
    print(data_store['ai'].api_key)

    return "state"

@app.route('/generate')
def generate():
    _counter = data_store['counter']
    _choices = data_store['past_queries'].choices
    _topic = data_store['topic']
    _ai = data_store['ai']
    if _counter == 0:
        init_msg = f"This is the topic of the story: {_topic}. Generate {_choices} choices for what happens next in a numbered list format, and make it so the choices generate do not have an empty line in between them"
        msg = query_openai(_ai, init_msg)
        newChoices = data_store['past_queries'].extractChoices(msg)
        data_store['counter'] += 1
        
        return newChoices 

    else:
        msg = ["Here is what happened in the past in the story"]
        for query in data_store['past_queries'].points.plotPoints:
            msg.append(query)
        msg.append(f"Generate {_choices} choices for what happens next in the story in a numbered list format")
        msg = '\n'.join(msg)

        msg = query_openai(_ai, msg)
        newChoices = data_store['past_queries'].extractChoices(msg)
        data_store['counter'] += 1
        return newChoices



@app.route('/selected/choice/<choice>')
def chose_choice(choice):
    data_store['past_queries'].points.addPlotPoint(choice)
    

        


if __name__ == '__main__':
    app.run(debug=True)

