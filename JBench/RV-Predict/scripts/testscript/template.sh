function check_env()
{
    if [ ! ${jbench} ]
    then
        echo "JBench is unset in the shell"
        echo "please set jbench to point to your experiment directory"
        echo "see README for more information:"
        exit 2
    fi
}

function run()
{
    echo ${test_name}
    jbench_dataset=${jbench}/dataset/benchmark-suite
    rv-predict --base-log-dir ${jbench}/RV-Predict/test --log-dirname ${test_name} -cp ${jbench_dataset}/${test_name}/bin ${class_to_run} &> ${jbench}/RV-Predict/outputs/${test_name}.log
}

check_env
