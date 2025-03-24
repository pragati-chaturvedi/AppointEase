import os
import openai
import json
from constants import APIKEY
from calendar_integration import schedule_appointment
from doc_integration import print_schedule
os.environ["OPENAI_API_KEY"] = APIKEY
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot(prompt):
    messages = [{ "role" : "user", "content": prompt },]
    functions = [
        {
            "name": "print_schedule",
            "description": "Get the schedule of the day from google docs and show availibility",
            "parameters":{
                "type" : "object",
                "properties" :{
                    "prompt" : {
                        "type" : "string",
                        "description" : "Prints the schedule for the date given in the prompt"
                    }
                },
                "required" : ["prompt"]
            },
        },
        {
            "name": "schedule_appointment",
            "description": "schedule an appointment and add to google calendar",
            "parameters": {
                        "type":"object",
                        "properties" : {
                            "summary" : {
                                "type" : "string",
                                "description" : "summary of event", 
                                },
                            "description" : {
                                "type" : "string",
                                "description":"Description of the event",
                                },
                            "start_time" : {
                                "type" : "string",
                                "description": "start time for the event in ISO format ",
                                }, 
                            "end_time" : {
                                "type" : "string",
                                "description": "end time for the event in ISO format",
                                },
                        },
                            "required" : ["prompt"]
            }
        }
    ]
        
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo-0613",
        messages = messages,
        functions = functions,
        function_call = "auto",
    )
    response_message = response.choices[0].message
    print(response_message.function_call)
    print(response_message)
    function_args = json.loads(response_message.function_call.arguments)
    print(function_args)
    available_functions = {
        "print_schedule" : print_schedule,
        "schedule_appointment" : schedule_appointment,
    }

    function_name = response_message.function_call.name
    print(function_name)
    function_to_call = available_functions[function_name]
    print(str(function_to_call))

    if "print_schedule" in str(function_to_call) :
        function_response =  function_to_call(
        prompt = function_args.get("prompt")
        )
        
    elif "schedule_appointment" in str(function_to_call):
        function_response =  function_to_call(
        summary  = function_args.get("summary"),
        description = function_args.get("description"),
        start_time = function_args.get("start_time"),
        end_time = function_args.get("end_time")
        )
    return function_response
    # print('ChatBot : %s' %(function_response))
