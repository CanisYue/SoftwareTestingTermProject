#!/bin/bash
start=`date +%s`

target_dir=/misc/scratch/zttest/22f/projects/apache-zookeeper-3.7.1
cd ${target_dir}


root_dir=/home/ecelrc/students/ztang/22f/projects/classes/

# if [ ! -d "${root_dir}/zookeeper" ]
# then
#     mkdir ${root_dir}/zookeeper
# else
#     rm -rf ${root_dir}/zookeeper
#     mkdir ${root_dir}/zookeeper
# fi

class_dir=${root_dir}/zookeeper

# for f in `find $PWD -name "*.class" | xargs ls -d`
# do
#     cp ${f} ${class_dir}/
# done

for c in `ls ${class_dir}`
do
    echo ${c}
    /home/ecelrc/students/ztang/jlint/jlint-3.1.2/bin/jlint -inheritance -data_flow ${class_dir}/${c} >> /home/ecelrc/students/ztang/22f/SoftwareTestingTermProject/Real_World_Projects/Jlint/zookeeper/outputs/zookeeper.log
done

end=`date +%s`

time=`echo $start $end | awk '{print $2-$1}'`
echo $time >> /home/ecelrc/students/ztang/22f/SoftwareTestingTermProject/Real_World_Projects/Jlint/zookeeper/outputs/zookeeper.log