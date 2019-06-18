"""Fancy Title Skill.

This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.

"""

import boto3
import json



# ------- Skill specific business logic -------

SKILL_NAME = "Fancy Title"


# Make sure you use question marks or periods.

def lambda_handler(event, context):
    """
    Route the incoming request based on type (LaunchRequest, IntentRequest, etc).
    The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])
    print("event:" + json.dumps(event))

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
    """Called when the session starts."""
    print("on_session_started requestId=" +
          session_started_request['requestId'] + ", sessionId=" +
          session['sessionId'])


def on_launch(launch_request, session):
    """Called when the user launches the skill without specifying what they want."""
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """Called when the user specifies an intent for this skill."""
    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

   
    # Dispatch to your skill's intent handlers
    print("***********************intent section***************************")
    print(intent_name)
    if intent_name == "DadIntent":
        return handle_dadintent_request(intent, session)
    elif intent_name == "MomIntent":
        return handle_momintent_request(intent, session) 
    elif intent_name == "DodgerIntent":
        return handle_dodgerintent_request(intent, session)     
    elif intent_name == "AMAZON.HelpIntent":
        return handle_get_help_request(intent, session)
    elif intent_name == "AMAZON.StopIntent":
        return handle_finish_session_request(intent, session)
    elif intent_name == "AMAZON.CancelIntent":
        return handle_finish_session_request(intent, session)
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """
    Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here

# --------------- Functions that control the skill's behavior -------------


def get_welcome_response():
    """If we wanted to initialize the session to have some attributes we could add those here."""
    intro = ("Just ask {} to discover your true heritage. ".format(SKILL_NAME)) 
    should_end_session = False

    speech_output = intro 
    reprompt_text = intro
    attributes = {"speech_output": speech_output,
                  "reprompt_text": speech_output
                  }

    return build_response(attributes, build_speechlet_response(
        SKILL_NAME, speech_output, reprompt_text, should_end_session))



def handle_dadintent_request(intent, session):
    attributes = {}
    should_end_session = False
    user_gave_up = intent['name']
    speech_output = ("Sadly you don't have any fancy titles, quite unfortunate.")
    reprompt_text = "Don't you want to know who you really are, just ask {}".format(SKILL_NAME)
    
    speech_output=("All hail the grillmaster, mower of lawn and enemy of small talks, the dad")
    print(speech_output)
    
    return build_response(
            {},
            build_speechlet_response(
                SKILL_NAME, speech_output, reprompt_text, should_end_session
            ))
            
def handle_momintent_request(intent, session):
    attributes = {}
    should_end_session = False
    user_gave_up = intent['name']
    speech_output = ("Sadly you don't have any fancy titles, quite unfortunate.")
    reprompt_text = "Don't you want to know who you really are, just ask {}".format(SKILL_NAME)
    
    speech_output=("All bow to superwoman of the house, champion of chores, protector of sanity,the mom")
    print(speech_output)
    
    return build_response(
            {},
            build_speechlet_response(
                SKILL_NAME, speech_output, reprompt_text, should_end_session
            ))
            
def handle_dodgerintent_request(intent, session):
    attributes = {}
    should_end_session = False
    user_gave_up = intent['name']
    speech_output = ("Sadly you don't have any fancy titles, quite unfortunate.")
    reprompt_text = "Don't you want to know who you really are, just ask {}".format(SKILL_NAME)
    
    speech_output=("All beware of the fuzzy beast, lover of bones, king of the couch, dodger")
    print(speech_output)
    
    return build_response(
            {},
            build_speechlet_response(
                SKILL_NAME, speech_output, reprompt_text, should_end_session
            ))
            



def handle_get_help_request(intent, session):
    attributes = {}
    speech_output = "Just ask {} for your titles!".format(SKILL_NAME)
    reprompt_text = "what can I help you with?"
    should_end_session = False
    return build_response(
        attributes,
        build_speechlet_response(SKILL_NAME, speech_output, reprompt_text, should_end_session)
    )


def handle_finish_session_request(intent, session):
    """End the session with a message if the user wants to quit the app."""
    #attributes = session['attributes']
    attributes=""
    reprompt_text = None
    speech_output = "Thanks for using {}. Have a Great Day.".format(SKILL_NAME)
    should_end_session = True
    return build_response(
        attributes,
        build_speechlet_response_without_card(speech_output, reprompt_text, should_end_session)
    )



# --------------- Helpers that build all of the responses -----------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_speechlet_response_without_card(output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': attributes,
        'response': speechlet_response
    }


