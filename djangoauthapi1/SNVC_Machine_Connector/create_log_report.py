def generate_log_report(output,suite_name):
    file_path=fr"./LogReport/{suite_name}.log"
    with open(file_path,'w+') as wp:
        wp.write(output)