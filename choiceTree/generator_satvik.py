from dotenv import load_dotenv
import os
import openai
from query import *

'''
give the AI an inital prompt
generate choices
store the choice chosen in an array

query format:
"what happened in the past"
"the things" -> up to x number of things
"generate 3 choices to decide what happens next"
"choose choice"

repeat
'''

path = '../.env'
load_dotenv(path)
API_KEY= os.getenv('API_KEY')

def extract_msg(response):
    return response['choices'][0]['message']['content']

def runner(choices, depth, topic):
    openai.api_key = API_KEY
    queryBuilder = QueryBuilder(choices)
    init_msg = f"This is the topic of the story: {topic}. Generate {choices} choices for what happens next in a numbered list format, and make it so the choices generate do not have an empty line in between them"
    print(init_msg)
    chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": init_msg}]
    )
    
    returnedMsg = extract_msg(chat_completion)
    print(returnedMsg)
 
    extractedChoices = queryBuilder.extractChoices(returnedMsg)

    while True:
        choiceNumber = int(input("choose a choice number "))
        if 0 <= choiceNumber - 1 <= len(extractedChoices) - 1:
            break
        print('choose a valid choice ')
   
    choiceNumber -= 1
    choiceToAdd = extractedChoices[choiceNumber]
    queryBuilder.points.addPlotPoint(choiceToAdd)
        
    depth -= 1    
    while depth != -1:
        
        msg = ["Here is what happened in the past in the story"]
        for query in queryBuilder.points.plotPoints:
            msg.append(query)
        msg.append(f"Generate {choices} choices for what happens next in the story in a numbered list format")
        msg = '\n'.join(msg)
        
        print(msg, '\n')

        chat_completion = openai.ChatCompletion.create(
             model="gpt-3.5-turbo", messages=[{"role": "user", "content": msg}]
        )
         
        returnedMsg = extract_msg(chat_completion)
        print('the choices: \n', returnedMsg)
        extractedChoices = queryBuilder.extractChoices(returnedMsg)
        
        while True:
            choiceNumber = int(input("choose a choice number "))
            if 0 <= choiceNumber - 1 <= len(extractedChoices) - 1:
                break
            print('choose a valid choice ')
   
        choiceNumber -= 1
        choiceToAdd = extractedChoices[choiceNumber]
        queryBuilder.points.addPlotPoint(choiceToAdd)
        
        if depth == 0:
            print('this is how the story ends')
            print(choiceToAdd)
            break
        depth -= 1



topic = input('Enter a topic ')
runner(3, 3, topic)



def setup():
    openai.api_key = API_KEY

    chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": "batman is eating a banana. Generate six choices for what batman should do next in a numbered list format"}]
    )   
    msg = chat_completion['choices'][0]['message']['content']
    print(extract_msg(chat_completion))


def generate_img(_prompt):
    response = openai.Image.create(
        prompt=_prompt,
        n=1,
        size="1024x1024"
    )
    return response['data'][0]['url']

