#!/bin/bash
output_dir=/home/ecelrc/students/ztang/22f/SoftwareTestingTermProject/jbench_logs/SpotBugs/outputs
src_dir=/misc/scratch/zttest/ComRaDe-master/benchmark-suite
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

        for cl in `find $PWD -name "*.class" | xargs ls -d`
        do
            cp ${cl} ${class_dir}/
        done

        spotbugs -auxclasspath .:$jacontebe/versions.alt/lib/realLib ${class_dir}/*.class &> ${output_dir}/result/${f}.log
    fi
      
done
