# function check_env()
# {
#     if [ ! ${jacontebe} ]
#     then
#         echo "jacontebe is unset in the shell"
#         echo "please set jacontebe to point to your experiment directory"
#         echo "see README for more information:"
#         exit 2
#     fi
#     experiment_dir=/home/ecelrc/students/ztang/22f/SoftwareTestingTermProject/JaConTeBe/SpotBugs
# }

# function run()
# {
#     cd ${experiment_dir}/outputs/${test_name}
#     spotbugs -auxclasspath .:$jacontebe/versions.alt/lib/realLib ./*.class & > ${experiment_dir}/outputs/result/${test_name}.log
# }

# check_env