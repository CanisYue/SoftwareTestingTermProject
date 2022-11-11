import os
import re
import json

def getFilePath(path):
    file_names = os.listdir(path)
    files_position = []
    for file_name in file_names:
        position = path + "/" + file_name
        files_position.append(position)
    return files_position

def handleSingleFile(path):
    f = open(path)
    lines = f.readlines()
    print(path)
    total_error_num = 0
    dic = {"deadlock":[], "race_condition":[], "wait_nosync":[]}
    # record detail info
    try:
        # record total error number
        regNum = re.compile(r'\d+')
        total_error_num = re.findall(regNum, lines[-1])[0]
        if "Verification completed" not in lines[-1]:
            raise Exception("Fail to run the program")
        for i in range(0, len(lines) - 1):
            line = lines[i]
            reg_bug_location = re.compile(r'JaConTeBe/jlint/outputs/(.*?): ')
            bug_location = re.findall(reg_bug_location, line)[0]

            reg_bug_log = re.compile(r': (.*)')
            bug_log = re.findall(reg_bug_log, line)[0]
            if "invocation of synchronized method" in line and "can cause deadlock" in line:
                dic["deadlock"].append({"location": bug_location, "code": "3.1.1-sync_loop"})
            elif "invocation of method" in line and "forms the loop in class dependency graph" in line:
                dic["deadlock"].append({"location": bug_location, "code": "3.1.2-loop"})
            elif "Lock" in line and "is requested while holding lock" in line and ", with other thread holding" in line:
                dic["deadlock"].append({"location": bug_location, "code": "3.1.3-lock"})
            elif "Method wait() can be invoked with monitor of other object locked" in line:
                dic["deadlock"].append({"location": bug_location, "code": "3.1.4-wait"})
            elif "Call sequence to method" in line and "can cause deadlock in wait()" in line:
                dic["deadlock"].append({"location": bug_location, "code": "3.1.5-wait_path"})
            elif "Synchronized method" in line and "is overridden by non-synchronized method of derived class" in line:
                dic["race_condition"].append({"location": bug_location, "code": "3.1.6-nosync"})
            elif "can be called from different threads and is not synchronized" in line:
                dic["race_condition"].append({"location": bug_location, "code": "3.1.7-concurrent_call"})
            elif "Field" in line and "of class" in line:
                dic["race_condition"].append({"location": bug_location, "code": "3.1.8-concurrent_access"})
            elif "implementing 'Runnable' interface is not synchronized" in line:
                dic["race_condition"].append({"location": bug_location, "code": "3.1.9-run_nosync"})
            elif "Value of lock" in line and "is changed outside synchronization or constructor" in line:
                dic["deadlock"].append({"location": bug_location, "code": "3.1.10-loop_assign"})
            elif "Value of lock" in line and "is changed while (potentially) owning it" in line:
                dic["deadlock"].append({"location": bug_location, "code": "3.1.11-loop_assign2"})
            elif "Method" in line and "is called without synchronizing on name" in line:
                dic["wait_nosync"].append({"location": bug_location, "code": "3.1.12-wait_nosync"})
        with open(output_file, mode = 'a') as filename:
            reg_project_name = re.compile(r'outputs/result/(.*).log')
            project_name = re.findall(reg_project_name, path)[0]
            filename.write("Project name: " + project_name + ", #Bugs found: " + str(total_error_num) + '\n')
            for key in dic:
                filename.write("Bug Type: " + key + ", #Bugs found: " + str(len(dic[key])) + '\n')
                for li in dic[key]:
                    filename.write(json.dumps(li) + '\n')
            filename.write('\n')
    except :
        with open(output_file, mode = 'a') as filename:
            reg_project_name = re.compile(r'outputs/result/(.*).log')
            project_name = re.findall(reg_project_name, path)[0]
            filename.write("Project name: " + project_name + ", Fail to run the project" + '\n')
            filename.write('\n')

output_file = 'result.txt'
log_path = "../outputs/result"
if os.path.exists(output_file):
    os.remove(output_file)
files_position = getFilePath(log_path)
for file_name in files_position:
    handleSingleFile(file_name)
