import os
from dotenv import load_dotenv
from openai import OpenAI
from utils.constants import *
from utils.data_util import *

def clean_responses(response):
    outputs = [(out if out != "None" else out) for out in response.split(",")]
    return outputs

def chat_with_gpt(prompt):
    load_dotenv()
    OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY", "")
    
    client = OpenAI(api_key = OPEN_AI_API_KEY)
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()

def chat_with_claude(prompt):
    return

def chat_with_gemini(prompt):
    return

def get_code(llm, problems):
    '''
    Takes a list of coding problems and feeds them to an LLM, returning 
    a list of the results
    
    Inputs: 
        llm (String): Name of LLM to call
        problems (List(String)): List of problems
    Returns:
        List(String)
    '''
    
    prompt = get_prompt(problems)
    
    if llm == CHAT_GPT:
        response = chat_with_gpt(prompt)
    # elif llm == CLAUDE:
    #     response = chat_with_claude(prompt)
    # elif llm == GEMINI:
    #     response = chat_with_gemini(prompt)
    else:
        return # TODO

    return clean_responses(response)