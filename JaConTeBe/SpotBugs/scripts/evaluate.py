import os
import re
import json
conc_set = set((
    "AT",
    "STCAL",
    "NP",
    "VO",
    "Dm",
    "DC",
    "DL",
    "WL",

))
meanings = {
    "AT": "Sequence of calls to concurrent abstraction may not be atomic",
    "STCAL": "(1)Static Calendar field (2)Static DateFormat (3)Call to static Calendar (4)Call to static DateFormat",
    "NP": "Synchronize and null check on the same field",
    "VO": "(1)A volatile reference to an array doesn’t treat the array elements as volatile (2)An increment to a volatile field isn’t atomic",
    "Dm": "(1)Monitor wait() called on Condition (2)A thread was created using the default empty run method",
    "DC": "(1)Possible double-check of field (2)Possible exposure of partially initialized object",
    "DL": "(1)Synchronization on interned String (2)Synchronization on Boolean (3)Synchronization on boxed primitive (4)Synchronization on boxed primitive values",
    "WL": "",
    

}

def getFilePath(path):
    file_names = os.listdir(path)
    files_position = []
    for file_name in file_names:
        position = path + "/" + file_name
        files_position.append(position)
    return files_position

def handleSingleFile(path, conc_set):
    f = open(path)
    rows = f.readlines()
    
    reg_project_name = re.compile(r'outputs/result/(.*?).log')
    project_name = re.findall(reg_project_name, path)[0]
    print(project_name)
    total_error_num = 0

    #init
    cur_dic = {}

    try:
        for cur_row in rows:
            if ":[line" in cur_row:
                total_error_num += 1
                #print(cur_row)
                # get the type of bug
                bug_type = ""
                space_cnt = 0
                idx = 0
                while idx < len(cur_row) and space_cnt < 2:
                    if cur_row[idx] == ' ':
                        space_cnt += 1
                    idx += 1
                while cur_row[idx] != ':':
                    bug_type += cur_row[idx]
                    idx += 1
                
                if bug_type in conc_set:
                    # is a concurrency bug

                    mid_idx = cur_row.find(".java")
                    if mid_idx == -1:
                        continue
                    
                    left_idx = mid_idx
                    right_idx = mid_idx
                    while left_idx >= 0 and cur_row[left_idx] != ' ':
                        left_idx -= 1
                    while right_idx < len(cur_row) and cur_row[right_idx] != ']':
                        right_idx += 1
                    
                    #print(java_file_name)
                    bug_location = project_name + "/classes/" + cur_row[left_idx + 1 : right_idx + 1]
                    bug_code = meanings[bug_type]
                    
                    if bug_type not in cur_dic:
                        cur_dic[bug_type] = []
                    cur_dic[bug_type].append({"location": bug_location, "code": bug_code})

                        

        with open(output_file, mode = 'a') as filename:
            filename.write("Project name: " + project_name + ", #Bugs found: " + str(total_error_num) + '\n')
            for key in cur_dic:
                filename.write("Bug Type: " + key + ", #Bugs found: " + str(len(cur_dic[key])) + '\n')
                for li in cur_dic[key]:
                    filename.write(json.dumps(li) + "\n")
            filename.write("\n")

    except:
        print("!!!!!")
        with open(output_file, mode = 'a') as filename:
            filename.write("Project name: " + project_name + ", Fail to run the project" + '\n')
            filename.write('\n')
    

    


output_file = "result.txt"
log_path = "../outputs/result"

if os.path.exists(output_file):
    os.remove(output_file)

files_position = getFilePath(log_path)
for file_name in files_position:
    handleSingleFile(file_name, conc_set)