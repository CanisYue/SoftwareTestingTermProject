#!/bin/bash

target_dir=/misc/scratch/zttest/22f/projects/tomcat-8.5.84/modules/jdbc-pool/target/classes/org/apache/tomcat
cd ${target_dir}

root_dir=/misc/scratch/zttest/22f/projects/classes/

if [ ! -d "${root_dir}/tomcat" ]
then
    mkdir ${root_dir}/tomcat
else
    rm -rf ${root_dir}/tomcat
    mkdir ${root_dir}/tomcat
fi

class_dir=${root_dir}/tomcat

for f in `find $PWD -name "*.class" | xargs ls -d`
do
    cp ${f} ${class_dir}/
done


/home/ecelrc/students/ztang/jlint/jlint-3.1.2/bin/jlint -inheritance -data_flow ${class_dir}/*.class &> /misc/scratch/zttest/22f/SoftwareTestingTermProject/Real_World_Projects/Jlint/tomcat/outputs/tomcat.log