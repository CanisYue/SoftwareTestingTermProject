#!/bin/bash
start=`date +%s`

target_dir=/home/ecelrc/students/ztang/22f/projects/apache-log4j-2.19.0-src
cd ${target_dir}


root_dir=/home/ecelrc/students/ztang/22f/projects/classes/

# if [ ! -d "${root_dir}/log4j" ]
# then
#     mkdir ${root_dir}/log4j
# else
#     rm -rf ${root_dir}/log4j
#     mkdir ${root_dir}/log4j
# fi

class_dir=${root_dir}/log4j

# for f in `find $PWD -name "*.class" | xargs ls -d`
# do
#     cp ${f} ${class_dir}/
# done

for c in `ls ${class_dir}`
do
    echo ${c}
    /home/ecelrc/students/ztang/jlint/jlint-3.1.2/bin/jlint -inheritance -data_flow ${class_dir}/${c} >> /home/ecelrc/students/ztang/22f/SoftwareTestingTermProject/Real_World_Projects/Jlint/log4j/outputs/log4j.log
done

end=`date +%s`

time=`echo $start $end | awk '{print $2-$1}'`
echo $time >> /home/ecelrc/students/ztang/22f/SoftwareTestingTermProject/Real_World_Projects/Jlint/log4j/outputs/log4j.log