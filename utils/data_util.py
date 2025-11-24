import subprocess
import os
import re
from data.solutions import solutions
from data.test_inputs import test_inputs

def get_prompt(problems):
    prompt = f'''
    You are an expert Racket developer tasked with solving a series of problems in Racket.
    You will be given a list of problem statements. Analyze each problem thoroughly and
    consider the examples and constraints given. For each problem, you must write a function 
    called solve in the latest version of Racket that solves the corresponding problem. Do 
    not include any code other than your function. Return each solution as a markdown string 
    delimited by a comma.
    
    problems: {problems}
    
    Your output:
    '''
    return prompt


def write_code_to_file(code, directory, file_name):
    """
    Writes code to a new file in the specified directory.

    :param code: str, the code to be written to the file.
    :param directory: str, the directory where the file will be created.
    :param file_name: str, the name of the file to create.
    """
    os.makedirs(directory, exist_ok=True)
    
    file_path = os.path.join(directory, file_name)

    with open(file_path, 'w') as file:
        file.write(code)


def run_one_file(file_path, language):
    try:
        result = subprocess.run(
            ["time", "-l", language, file_path],
            text=True,
            capture_output=True,
            shell=False
        )
        
        metrics = {}
        stderr_lines = result.stderr.splitlines()
        for line in stderr_lines:
            if "real" in line:
                time_match = re.search(r"(\d+\.\d+)", line)
                if time_match:
                    metrics["elapsed_time_seconds"] = float(time_match.group(1))
            elif "maximum resident set size" in line.lower():
                rss_match = re.search(r"(\d+)", line)
                if rss_match:
                    metrics["max_resident_set_size_kb"] = int(rss_match.group(1))
        
        metrics["program_output"] = result.stdout.strip()
        
        return metrics
    
    except subprocess.CalledProcessError as e:
        print("Error running Racket file:")
        print(e.stderr)


def run_files(directory_path, language):
    tot_res = {}
    
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            res = run_one_file(file_path, language)
            tot_res[file_name] = res
    return tot_res

    
def get_racket_string(input_data):
    if isinstance(input_data, list):
        converted_elements = map(get_racket_string, input_data)
        return f"`({' '.join(converted_elements)})"
    elif isinstance(input_data, bool):
        return '#t' if input_data else '#f'
    elif isinstance(input_data, str):
        return f"\"{input_data}\""
    else:
        return str(input_data)


def clean_inputs(test):
    out = ""
    
    for input in test:
        out += get_racket_string(input)
        out += " "
        
    return out.strip()


def get_code_with_tests(solution, test_suite, answers_list):
    tests = ""
    for test, answer in zip(test_suite, answers_list):
        tests += f"(print (equal? (solve {clean_inputs(test)}) {clean_inputs([answer])}))\n"
                        
    code = f'''{solution}\n{tests}'''
    return code


def get_python_string(input_data):
    if isinstance(input_data, list):
        converted_elements = map(get_python_string, input_data)
        return f"[{','.join(converted_elements)}]"
    elif isinstance(input_data, bool):
        return 'True' if input_data else 'False'
    elif isinstance(input_data, str):
        return f"\"{input_data}\""
    else:
        return str(input_data)
    
def get_code_with_tests_python(solution, test_suite, answers_list):
    tests = ""
    
    for test, answer in zip(test_suite, answers_list):
        converted_elements = map(get_python_string, test)
        tests += f"print(solve({','.join(converted_elements)}) == {answer})\n"
        
    code = f'''{solution}\n{tests}'''
    return code

def write_test_files(code_list, path, file_ending):
    for i, code in enumerate(code_list):
        write_code_to_file(code, path, f"problem_{i}{file_ending}")
        
def generate_test_files(code_list, path, file_ending):
    out = []
    for code, test_suite, ans_list in zip(code_list, test_inputs, solutions):
        if file_ending == ".py":
            out.append(get_code_with_tests_python(code, test_suite, ans_list))
        else:
            out.append(get_code_with_tests(code, test_suite, ans_list))
    
    write_test_files(out, path, file_ending)