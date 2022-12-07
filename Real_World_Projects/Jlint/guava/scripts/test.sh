#!/bin/bash
start=`date +%s`


target_dir=/misc/scratch/zttest/22f/projects/guava-31.1/guava/target/classes
cd ${target_dir}

root_dir=/misc/scratch/zttest/22f/projects/classes/

# if [ ! -d "${root_dir}/guava" ]
# then
#     mkdir ${root_dir}/guava
# else
#     rm -rf ${root_dir}/guava
#     mkdir ${root_dir}/guava
# fi

class_dir=${root_dir}/guava

# for f in `find $PWD -name "*.class" | xargs ls -d`
# do
#     cp ${f} ${class_dir}/
# done


for c in `ls ${class_dir}`
do
    echo ${c}
    /home/ecelrc/students/ztang/jlint/jlint-3.1.2/bin/jlint -inheritance -data_flow ${class_dir}/${c} >> /misc/scratch/zttest/22f/SoftwareTestingTermProject/Real_World_Projects/Jlint/guava/outputs/guava.log
done

end=`date +%s`

time=`echo $start $end | awk '{print $2-$1}'`
echo $time >> /misc/scratch/zttest/22f/SoftwareTestingTermProject/Real_World_Projects/Jlint/guava/outputs/guava.log