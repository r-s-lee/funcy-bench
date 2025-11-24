from utils.constants import *
from statistics import mean

def get_score_report(llm, res_racket, res_python):
    llm_scores = []
    reference_scores = []
    
    llm_cpu_times = []
    ref_cpu_times = []
    
    llm_mems = []
    ref_mems = []
    
    for i in range(NUM_PROBLEMS):
        llm_problem_score = res_racket[f"problem_{i}.rkt"].get("program_output", "").count("#t") / TEST_COUNT
        reference_problem_score = res_python[f"problem_{i}.py"].get("program_output", "").count("True") / TEST_COUNT
        
        llm_cpu_time = res_racket[f"problem_{i}.rkt"].get("elapsed_time_seconds", "")
        ref_cpu_time = res_python[f"problem_{i}.py"].get("elapsed_time_seconds", "")
        
        llm_mem = res_racket[f"problem_{i}.rkt"].get("max_resident_set_size_kb", "")
        ref_mem = res_python[f"problem_{i}.py"].get("max_resident_set_size_kb", "")
        
        print(f'''\t\tProblem #{i}: 
                    PASS RATE: {llm_problem_score*100}% | Ref: {reference_problem_score*100}%
                    CPU_TIME: {llm_cpu_time} s. | Ref: {ref_cpu_time} s.
                    MEMORY: {llm_mem} kb | Ref: {ref_mem}kb
                ''')
        
        llm_scores.append(llm_problem_score)
        reference_scores.append(reference_problem_score)
        
        if llm_problem_score > 0:
            llm_cpu_times.append(llm_cpu_time)
            ref_cpu_times.append(ref_cpu_time)
        
            llm_mems.append(llm_mem)
            ref_mems.append(ref_mem)
        
    print("----------")
    print(f"""{model_name[llm]}: 
          OVERALL PASS RATE: {mean(llm_scores)*100}% | Ref: {mean(reference_scores)*100}%
          AVG CPU TIME: {mean(llm_cpu_times)} s. | Ref: {mean(ref_cpu_times)} s. 
          AVG MEMORTY: {mean(llm_mems)} kb | Ref: {mean(ref_mems)} kb
          """)
        
        
    return 