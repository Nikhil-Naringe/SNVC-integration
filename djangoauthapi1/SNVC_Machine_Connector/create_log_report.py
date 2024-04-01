import os

def generate_log_report(output,suite_name):
    project_root = os.path.dirname(__file__)
    file_path=project_root+fr"\LogReport\{suite_name}.log"
    print(file_path)
    with open(file_path,'w+') as wp:
        wp.write(output)