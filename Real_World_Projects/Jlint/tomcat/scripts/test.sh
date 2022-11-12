#!/bin/bash
output_dir=/home/ecelrc/students/ztang/22f/SoftwareTestingTermProject/Real_World_Projects/Jlint/tomcat/outputs
src_dir=/misc/scratch/zttest/apache-tomcat-10.0.27

cd ${src_dir}
if [ ! -d "${cur_dir}/jar_dir" ]
then
    mkdir jar_dir
else
    rm -rf jar_dir
    mkdir jar_dir
fi

cp ${src_dir}/bin/*.jar ./jar_dir/
cp ${src_dir}/lib/*.jar ./jar_dir/

cd jar_dir

if [ ! -d "${cur_dir}/class_dir" ]
then
    mkdir class_dir
else
    rm -rf class_dir
    mkdir class_dir
fi

for j in `ls`
do
    jar xvf ${j}
done


for cl in `find $PWD -name "*.class" | xargs ls -d`
do
    cp ${cl} class_dir/
done
ls class_dir/*.class
cd class_dir

/home/ecelrc/students/ztang/jlint/jlint-3.1.2/bin/jlint -inheritance -data_flow ./*.class &> ${output_dir}/result/tomcat.log
