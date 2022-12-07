#!/bin/bash
start=`date +%s`



target_dir=/misc/scratch/zttest/22f/projects/commons-dbcp2-2.9.0-src/target/classes/org
cd ${target_dir}

root_dir=/misc/scratch/zttest/22f/projects/classes/

# if [ ! -d "${root_dir}/tomcat" ]
# then
#     mkdir ${root_dir}/dbcp
# else
#     rm -rf ${root_dir}/dbcp
#     mkdir ${root_dir}/dbcp
# fi

class_dir=${root_dir}/dbcp

# for f in `find $PWD -name "*.class" | xargs ls -d`
# do
#     cp ${f} ${class_dir}/
# done


for c in `ls ${class_dir}`
do
    #echo ${c}
    /home/ecelrc/students/ztang/jlint/jlint-3.1.2/bin/jlint -inheritance -data_flow ${class_dir}/${c} >> /misc/scratch/zttest/22f/SoftwareTestingTermProject/Real_World_Projects/Jlint/dbcp/outputs/dbcp.log
done

end=`date +%s`

time=`echo $start $end | awk '{print $2-$1}'`
echo $time >> /misc/scratch/zttest/22f/SoftwareTestingTermProject/Real_World_Projects/Jlint/dbcp/outputs/dbcp.log