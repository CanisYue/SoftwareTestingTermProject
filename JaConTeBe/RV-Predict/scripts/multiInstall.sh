#!/bin/bash
# set path variable and clean up
# jacontebe=/home/ecelrc/students/yxiong/softwaretesting/JaConTeBe
data_dir=${jacontebe}/dataset/JaConTeBe
experiment_dir=${jacontebe}/RV-Predict
echo removing old files
rm -f -r ${jacontebe}/RV-Predict/outputs/*

# creating directory
# echo copying files for orig version
# touch ${experiment_dir}/outputs/dir_name.txt
# ls ${data_dir}/versions.alt | xargs > ${experiment_dir}/outputs/dir_name.txt
# cd ${jacontebe}/RV-Predict/outputs/
# xargs -r mkdir < ${experiment_dir}/outputs/dir_name.txt
# rmdir lib

# copy files and compile
cd ${data_dir}/versions.alt
for i in `ls`;
do  
    if [ $i != "lib" ]; then
        mkdir ${experiment_dir}/outputs/$i
        cp -a ${data_dir}/versions.alt/$i/orig/* ${experiment_dir}/outputs/$i
        cd ${experiment_dir}/outputs/$i
        find . -name "*.java" | xargs javac -cp ${data_dir}/versions.alt/lib/$i.jar
        cd ..
    fi
done
