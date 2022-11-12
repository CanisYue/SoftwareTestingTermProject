#!/bin/bash
output_dir=/home/ecelrc/students/ztang/22f/SoftwareTestingTermProject/Real_World_Projects/SpotBugs/tomcat/outputs
src_dir=/misc/scratch/zttest/apache-tomcat-10.0.27


cd ${src_dir}
spotbugs -auxclasspath .:$jacontebe/versions.alt/lib/realLib ${src_dir}/res.jar &> ${output_dir}/result/tomcat.log
# for f in `ls`
# do
#     if [ -d "${src_dir}/${f}" ]
#     then
#         cd ${src_dir}/${f}
#         cur_dir=${src_dir}/${f}
#         if [ ! -d "${cur_dir}/classes" ]
#         then
#             mkdir classes
#         else
#             rm -rf classes
#             mkdir classes
#         fi

#         class_dir=${src_dir}/${f}/classes

#         for cl in `find $PWD -name "*.java" | xargs ls -d`
#         do
#             cp ${cl} ${class_dir}/
#         done

#         spotbugs -auxclasspath .:$jacontebe/versions.alt/lib/realLib ${class_dir}/*.java &> ${output_dir}/result/${f}.log
#     fi
      
# done
