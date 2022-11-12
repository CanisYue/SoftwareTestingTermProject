#!/bin/bash
output_dir=/home/ecelrc/students/ztang/22f/SoftwareTestingTermProject/Real_World_Projects/Jlint/tomcat/outputs
src_dir=/misc/scratch/zttest/apache-tomcat-10.0.27

cd ${src_dir}
if [ ! -d "${cur_dir}/class_dir" ]
then
    mkdir class_dir
else
    rm -rf class_dir
    mkdir class_dir
fi

cp ${src_dir}/bin/*.jar ./class_dir/
cp ${src_dir}/libs/*.jar ./class_dir/