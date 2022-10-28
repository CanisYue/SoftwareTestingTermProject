function check_env()
{
    if [ ! ${jacontebe} ]
    then
        echo "jacontebe is unset in the shell"
        echo "please set jacontebe to point to your experiment directory"
        echo "see README for more information:"
        exit 2
    fi
    experiment_dir=/home/ecelrc/students/ztang/22f/SoftwareTestingTermProject/JaConTeBe/jlint
}


function run()
{
    cd ${experiment_dir}/outputs/${test_name}
    cur_dir=${experiment_dir}/outputs/${test_name}
    if [ ! -d "${cur_dir}/classes" ]
    then
        mkdir classes
    else
        rm -rf classes
        mkdir classes
    fi
    class_dir=${experiment_dir}/outputs/${test_name}/classes
    

    for f in `find $PWD -name "*.class" | xargs ls -d`
    do
        cp ${f} ${class_dir}/
    done
    
    /home/ecelrc/students/ztang/jlint/jlint-3.1.2/bin/jlint -inheritance -data_flow ${class_dir}/*.class &> ${experiment_dir}/outputs/result/${test_name}.log
}

check_env