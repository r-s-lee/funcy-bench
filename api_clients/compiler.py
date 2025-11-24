import requests
from statistics import mean
import os
from dotenv import load_dotenv

def request_compiler(data=None, headers=None):
    """
    Makes a POST request to compiler API

    Parameters:
        data (dict, optional): The data to be sent in the body of the POST request.
        headers (dict, optional): Headers to include in the request.

    Returns:
        Response: The response object from the request.
    """
    load_dotenv()
    COMPILER_API_URL = os.getenv("COMPILER_API_URL")
    try:
        response = requests.post(COMPILER_API_URL, json=data, headers=headers)
        
        response.raise_for_status()
        
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def compile_code(code):
    '''
    Takes a list of test inputs and makes a request to compiler API 
    returning the result.
    
    Inputs:
        code (String): code to compile
    Returns: 
        String
    '''
    load_dotenv()
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
        
    data = {
        "clientId": CLIENT_ID,
        "clientSecret": CLIENT_SECRET,
        "script": code,
        "language": "racket",
        "versionIndex": 0,
    }
    
    response = request_compiler(data)
    
    output = str(response["output"])
    status_code = response["statusCode"]
    memory = float(response["memory"])
    cpu_time = float(response["cpuTime"])
    
    if status_code != 200: #TODO: handling bad code
        output = ""
    
    out = {
        "output": output,
        "status_code": status_code,
        "memory": memory,
        "cpu_time": cpu_time,
    }
    
    return out

def get_llm_solutions(code_list):
    '''
    Takes a list of tests and calls compile_code on each test
    
    Inputs:
        code (List(String)): code to compile
        tests (List(List())): list of tests
    Returns: 
        List(String)
    '''
    num_tests_passed = 0
    memories = []
    cpu_times = []
    
    for code in code_list:
        response = compile_code(code)
        if response["output"] == "":
            num_tests_passed += 1
        memories.append(response["memory"])
        cpu_times.append(response["cpu_time"])
    
    return f"{(num_tests_passed / len(code_list)) * 100}%", mean(memories), mean(cpu_times)