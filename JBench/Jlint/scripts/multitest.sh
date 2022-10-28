#!/bin/bash
if [ ! ${jbench} ]
then
    echo "JBench is unset in the shell"
    echo "please set jbench to point to your experiment directory"
    echo "see README for more information:"
    exit 2
fi

output_dir=${jbench}/Jlint/outputs
src_dir=${jbench}/dataset/benchmark-suite
cd ${src_dir}

for f in `ls`
do
    if [ -d "${src_dir}/${f}" ]
    then
        cd ${src_dir}/${f}
        cur_dir=${src_dir}/${f}
        if [ ! -d "${cur_dir}/classes" ]
        then
            mkdir classes
        else
            rm -rf classes
            mkdir classes
        fi

        class_dir=${src_dir}/${f}/classes
        echo ${f}
        for cl in `find $PWD -name "*.class" | xargs ls -d`
        do
            cp ${cl} ${class_dir}/
        done

        jlint -inheritance -data_flow ${class_dir}/*.class &> ${output_dir}/${f}.log
    fi
      
done
