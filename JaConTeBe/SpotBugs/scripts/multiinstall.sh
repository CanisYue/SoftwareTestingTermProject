#!/bin/bash

# jacontebe = /home/ecelrc/students/ztang/myja/JaConTeBe
src_data_dir=${jacontebe}
experiment_dir=/home/ecelrc/students/ztang/22f/SoftwareTestingTermProject/JaConTeBe/SpotBugs
echo "removing old files in SpotBugs"
rm -rf ${experiment_dir}/outputs/*


cd ${src_data_dir}/versions.alt
for i in `ls`;
do
    if [ $i != "lib" ]; then
        mkdir ${experiment_dir}/outputs/$i
        cp -a ${src_data_dir}/versions.alt/$i/orig/* ${experiment_dir}/outputs/$i
        cd ${experiment_dir}/outputs/$i
        find . -name "*.java" | xargs javac -cp ${src_data_dir}/versions.alt/lib/$i.jar
        cd ..
    fi
done

mkdir ${experiment_dir}/outputs/result