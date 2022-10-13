function check_env()
{
    if [ ! ${jacontebe} ]
    then
        echo "jacontebe is unset in the shell"
        echo "please set jacontebe to point to your experiment directory"
        echo "see README for more information:"
        exit 2
    fi
    data_dir=${jacontebe}/dataset/JaConTeBe
    subject_dir=${experiment_root}/JaConTeBe
    experiment_dir=${jacontebe}/RV-Predict
    cd ${subject_dir}
}

function run() 
{
    runtime_dependencies=${data_dir}/versions.alt/lib/${test_name}.jar:${experiment_dir}/outputs/${test_name}
    rv-predict ${Opt} -cp ${runtime_dependencies} ${class_to_run} &> ${experiment_dir}/outputs/result/${test_name}.log
}

check_env
