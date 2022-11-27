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
    "ESync",
    "MSF",
    "IS",
    "NN",
    "Ru",
    "SP",
    "TLW",
    "UW",
    "UG",
    "ML",
    "WS",
    "RS",
    "SC",
    "Wa",
    "No",
    "UL",
    "MWN",
    "LI",
    "JLM",
    "SWL",
    "RV",
    "SSD",
))

meanings = {
    "AT": "Sequence of calls to concurrent abstraction may not be atomic",
    "STCAL": "(1)Static Calendar field (2)Static DateFormat (3)Call to static Calendar (4)Call to static DateFormat",
    "NP": "Synchronize and null check on the same field",
    "VO": "(1)A volatile reference to an array doesn’t treat the array elements as volatile (2)An increment to a volatile field isn’t atomic",
    "Dm": "(1)Monitor wait() called on Condition (2)A thread was created using the default empty run method",
    "DC": "(1)Possible double-check of field (2)Possible exposure of partially initialized object",
    "DL": "(1)Synchronization on interned String (2)Synchronization on Boolean (3)Synchronization on boxed primitive (4)Synchronization on boxed primitive values",
    "WL": "Synchronization on getClass rather than class literal",
    "ESync": "Empty synchronized block",
    "MSF": "Mutable servlet field",
    "IS": "(1)Inconsistent synchronization (2)Field not guarded against concurrent access",
    "NN": "Naked notify",
    "Ru": "Invokes run on a thread (did you mean to start it instead?)",
    "SP": "Method spins on field",
    "TLW": "Wait with two locks held",
    "UW": "Unconditional wait",
    "UG": "Unsynchronized get method, synchronized set method",
    "ML": "(1)Synchronization on field in futile attempt to guard that field (2)Method synchronizes on an updated field",
    "WS": "Class’s writeObject() method is synchronized but nothing else is",
    "RS": "Class’s readObject() method is synchronized",
    "SC": "Constructor invokes Thread.start()",
    "Wa": "(1)Wait not in loop (2)Condition.await() not in loop",
    "No": "Using notify() rather than notifyAll()",
    "UL": "(1)Method does not release lock on all paths (2)Method does not release lock on all exception paths",
    "MWN": "(1)Mismatched wait() (2)Mismatched notify()",
    "LI": "(1)Incorrect lazy initialization of static field (2)Incorrect lazy initialization and update of static field",
    "JLM": "(1)Synchronization performed on util.concurrent instance (2)Using monitor style wait methods on util.concurrent abstraction (3)Synchronization performed on Lock",
    "SWL": "Method calls Thread.sleep() with a lock held",
    "RV": "Return value of putIfAbsent ignored, value passed to putIfAbsent reused",
    "SSD": "Instance level lock was used on a shared static data"
}

errcode = {
    0: "Data race",
    1: "Data race: Memory inconsistency",
    2: "Data race: Write-Write race",
    3: "Deadlock",
    4: "Livelock",
    5: "Starvation",
    6: "Suspension-based locking or Blocking suspension",
    7: "Order violation",
    8: "Atomicity violation",
    9: "Atomicity violation: Single variable atomicity violation",
    10: "Atomicity violation: Multi-variable atomicity violation",
    11: "Others"
}


categories = {
    "AT": 8, #"Sequence of calls to concurrent abstraction may not be atomic",
    "STCAL": 0,#"(1)Static Calendar field (2)Static DateFormat (3)Call to static Calendar (4)Call to static DateFormat",
    "NP": 0, #"Synchronize and null check on the same field",
    "VO": 8, #"(1)A volatile reference to an array doesn’t treat the array elements as volatile (2)An increment to a volatile field isn’t atomic",
    "Dm": 11, #"(1)Monitor wait() called on Condition (2)A thread was created using the default empty run method",
    "DC": 3, #"(1)Possible double-check of field (2)Possible exposure of partially initialized object",
    "DL": 0, #"(1)Synchronization on interned String (2)Synchronization on Boolean (3)Synchronization on boxed primitive (4)Synchronization on boxed primitive values",
    "WL": 0, #"Synchronization on getClass rather than class literal",
    "ESync": 6, #"Empty synchronized block",
    "MSF": 0, #"Mutable servlet field",
    "IS": 3, #"(1)Inconsistent synchronization (2)Field not guarded against concurrent access",
    "NN": 11, #"Naked notify",
    "Ru": 11, #"Invokes run on a thread (did you mean to start it instead?)",
    "SP": 3, #"Method spins on field",
    "TLW": 3,#"Wait with two locks held",
    "UW": 3, #"Unconditional wait",
    "UG": 3, #"Unsynchronized get method, synchronized set method",
    "ML": 3, #"(1)Synchronization on field in futile attempt to guard that field (2)Method synchronizes on an updated field",
    "WS": 0, #"Class’s writeObject() method is synchronized but nothing else is",
    "RS": 3, #"Class’s readObject() method is synchronized",
    "SC": 3, #"Constructor invokes Thread.start()",
    "Wa": 3, #"(1)Wait not in loop (2)Condition.await() not in loop",
    "No": 3, #"Using notify() rather than notifyAll()",
    "UL": 3, #"(1)Method does not release lock on all paths (2)Method does not release lock on all exception paths",
    "MWN": 3, #"(1)Mismatched wait() (2)Mismatched notify()",
    "LI": 0, #"(1)Incorrect lazy initialization of static field (2)Incorrect lazy initialization and update of static field",
    "JLM": 3, #"(1)Synchronization performed on util.concurrent instance (2)Using monitor style wait methods on util.concurrent abstraction (3)Synchronization performed on Lock",
    "SWL": 3, #"Method calls Thread.sleep() with a lock held",
    "RV": 0, #"Return value of putIfAbsent ignored, value passed to putIfAbsent reused",
    "SSD": 0, #"Instance level lock was used on a shared static data"
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
                    total_error_num += 1
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
                    #bug_code = meanings[bug_type]
                    
                    classified_bug_type = errcode[categories[bug_type]]

                    if classified_bug_type not in cur_dic:
                        cur_dic[classified_bug_type] = []
                    cur_dic[classified_bug_type].append({"location": bug_location})#, "code": bug_code})

                    if classified_bug_type not in all_res:
                        all_res[classified_bug_type] = 0
                    all_res[classified_bug_type] += 1

                        

        with open(output_file, mode = 'a') as filename:
            filename.write("Project name: " + project_name + ", #Bugs found: " + str(total_error_num) + '\n')
            for key in cur_dic:
                filename.write("Bug Type: " + key + ", #Bugs found: " + str(len(cur_dic[key])) + '\n')
                #filename.write("Description: " + meanings[key] + "\n")
                for li in cur_dic[key]:
                    filename.write(json.dumps(li) + "\n")
            filename.write("\n\n")

    except:
        print("!!!!!")
        with open(output_file, mode = 'a') as filename:
            filename.write("Project name: " + project_name + ", Fail to run the project" + '\n')
            filename.write("\n\n")
    

    
output_file = "result.txt"
log_path = "../outputs/result"


if os.path.exists(output_file):
    os.remove(output_file)

all_res = {}
all_bugs_num = 0

files_position = getFilePath(log_path)
for file_name in files_position:
    handleSingleFile(file_name, conc_set)

for key in all_res:
    all_bugs_num += all_res[key]

with open(output_file, mode = 'a') as filename:
    filename.write("\n\n----------Overall Results for JBench----------\n")
    filename.write("Number of concurrency bugs found in JBench: " + str(all_bugs_num) + "\n")
    filename.write("Number of concurrency bug types found in JBench: " + str(len(all_res)) + "\n")
    filename.write("\n\n")
    for key in all_res:
        filename.write("Bug Type: " + key + "\n")
        #filename.write("Description: " + meanings[key] + "\n")
        filename.write("#Bugs found: " + str(all_res[key]) + "\n")
        filename.write("\n\n")
