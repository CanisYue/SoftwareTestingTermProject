import os
import re
import json

def getFilePath():
    path = "../outputs"
    file_names = os.listdir(path)
    files_position = []
    for file_name in file_names:
        position = path + "/" + file_name
        files_position.append(position)
    return files_position

def handleSingleFile(path):
    f = open(path)
    lines = f.readlines()
    # print(path)
    total_error_num = 0
    # dic = {"deadlock":[], "race_condition":[], "wait_nosync":[]}
    dic = {"deadlock":[], "data race":[]}
    # record detail info
    try:
    # record total error number
        regNum = re.compile(r'\d+')
        total_error_num = re.findall(regNum, lines[-1])[0]
        if "Verification completed" not in lines[-1]:
            raise Exception("Fail to run the program")
        for i in range(0, len(lines) - 1):
            line = lines[i]
            # print(line)
            if "Failed to open file" in line:
                raise Exception("Fail to run the program")
            reg_bug_location = re.compile(r'/JBench/dataset/benchmark-suite/(.*?): ')
            bug_location = re.findall(reg_bug_location, line)
            if len(bug_location) == 0:
                continue
            bug_location = bug_location[0]
            reg_bug_log = re.compile(r': (.*)')
            bug_log = re.findall(reg_bug_log, line)[0]
            bug_type = ""
            reg_bug_log = re.compile(r': (.*)')
            bug_log = re.findall(reg_bug_log, line)[0]
            if "invocation of synchronized method" in line and "can cause deadlock" in line:
                dic["deadlock"].append({"location": bug_location, "code": "3.1.1-sync_loop"})
                bug_type = "deadlock"
            elif "invocation of method" in line and "forms the loop in class dependency graph" in line:
                dic["deadlock"].append({"location": bug_location, "code": "3.1.2-loop"})
                bug_type = "deadlock"
            elif "Lock" in line and "is requested while holding lock" in line and ", with other thread holding" in line:
                dic["deadlock"].append({"location": bug_location, "code": "3.1.3-lock"})
                bug_type = "deadlock"
            elif "Method wait() can be invoked with monitor of other object locked" in line:
                dic["deadlock"].append({"location": bug_location, "code": "3.1.4-wait"})
                bug_type = "deadlock"
            elif "Call sequence to method" in line and "can cause deadlock in wait()" in line:
                dic["deadlock"].append({"location": bug_location, "code": "3.1.5-wait_path"})
                bug_type = "deadlock"
            elif "Synchronized method" in line and "is overridden by non-synchronized method of derived class" in line:
                # dic["race_condition"].append({"location": bug_location, "code": "3.1.6-nosync"})
                # bug_type = "race_condition"
                dic["data race"].append({"location": bug_location, "code": "3.1.6-nosync"})
                bug_type = "data race"
            elif "can be called from different threads and is not synchronized" in line:
                # dic["race_condition"].append({"location": bug_location, "code": "3.1.7-concurrent_call"})
                # bug_type = "race_condition"
                dic["data race"].append({"location": bug_location, "code": "3.1.7-concurrent_call"})
                bug_type = "data race"
            elif "Field" in line and "of class" in line:
                # dic["race_condition"].append({"location": bug_location, "code": "3.1.8-concurrent_access"})
                # bug_type = "race_condition"
                dic["data race"].append({"location": bug_location, "code": "3.1.8-concurrent_access"})
                bug_type = "data race"
            elif "implementing 'Runnable' interface is not synchronized" in line:
                # dic["race_condition"].append({"location": bug_location, "code": "3.1.9-run_nosync"})
                # bug_type = "race_condition"
                dic["data race"].append({"location": bug_location, "code": "3.1.9-run_nosync"})
                bug_type = "data race"
            elif "Value of lock" in line and "is changed outside synchronization or constructor" in line:
                dic["deadlock"].append({"location": bug_location, "code": "3.1.10-loop_assign"})
                bug_type = "deadlock"
            elif "Value of lock" in line and "is changed while (potentially) owning it" in line:
                dic["deadlock"].append({"location": bug_location, "code": "3.1.11-loop_assign2"})
                bug_type = "deadlock"
            elif "lock(s):" in line:
                dic["deadlock"].append({"location": bug_location, "code": "Holding n lock(s)"})
                bug_type = "deadlock"
            elif "Method" in line and "is called without synchronizing on" in line:
                # dic["wait_nosync"].append({"location": bug_location, "code": "3.1.12-wait_nosync"})
                # bug_type = "wait_nosync"
                dic["data race"].append({"location": bug_location, "code": "3.1.12-wait_nosync"})
                bug_type = "data race"
            else:
                print(line)
            if bug_type not in all_res:
                all_res[bug_type] = 0
            all_res[bug_type] += 1
        with open(output_file, mode = 'a') as filename:
            reg_project_name = re.compile(r'outputs/(.*).log')
            project_name = re.findall(reg_project_name, path)[0]
            filename.write("Project name: " + project_name + ", #Bugs found: " + str(total_error_num) + '\n')
            for key in dic:
                filename.write("Bug Type: " + key + ", #Bugs found: " + str(len(dic[key])) + '\n')
                for li in dic[key]:
                    filename.write(json.dumps(li) + '\n')
            filename.write('\n')
    except :
        with open(output_file, mode = 'a') as filename:
            reg_project_name = re.compile(r'outputs/(.*).log')
            project_name = re.findall(reg_project_name, path)[0]
            filename.write("Project name: " + project_name + ", Fail to run the project" + '\n')
            filename.write('\n')
        
all_res = {}
all_bugs_num = 0


output_file = 'result.txt'
if os.path.exists(output_file):
    os.remove(output_file)
files_position = getFilePath()
for file_name in files_position:
    handleSingleFile(file_name)

for key in all_res:
    all_bugs_num += all_res[key]

with open(output_file, mode = 'a') as filename:
    filename.write("\n\n----------Overall Results for JBench----------\n")
    filename.write("Number of concurrency bugs found in JBench: " + str(all_bugs_num) + "\n")
    filename.write("Number of concurrency bug types found in JBench: " + str(len(all_res)) + "\n")
    filename.write("\n\n")
    for key in all_res:
        filename.write("Bug Type: " + key + "\n")
        # filename.write("Description: " + meanings[key] + "\n")
        filename.write("#Bugs found: " + str(all_res[key]) + "\n")
        filename.write("\n\n")
