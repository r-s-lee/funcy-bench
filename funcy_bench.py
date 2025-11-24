from utils.constants import *
from utils.data_util import *
from llm_code import llm_generated_code
from ref_code import reference_code
from utils.data_util import *
from utils.score_util import *


def funcy_bench(llms):
    for llm in llms:
        for i in range(3):        
            reference_write_path = f"{PYTHON_WRITE_PATH}/{model_name[llm]}"
            model_write_path = f"{RACKET_WRITE_PATH}/{model_name[llm]}/attempt_{i}"
            
            generate_test_files(reference_code[model_name[llm]], reference_write_path, ".py")
            generate_test_files(llm_generated_code[model_name[llm]][i], model_write_path, ".rkt")
            
            res_python = run_files(reference_write_path, "python")
            res_racket = run_files(model_write_path, "racket")
            
            get_score_report(llm, res_racket, res_python)
    
    
