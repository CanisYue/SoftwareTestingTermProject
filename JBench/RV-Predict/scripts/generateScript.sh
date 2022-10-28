files=$(ls ${jbench}/dataset/benchmark-suite)
for filename in $files
do
    cd ${jbench}/RV-Predict/scripts/testscript
    touch $filename.sh
    echo "source \$(cd \`dirname \$0\`; pwd)/template.sh" > $filename.sh
    echo "test_name=${filename}" >> $filename.sh
    echo "class_to_run=" >> $filename.sh
    echo "run \$*" >> $filename.sh
    chmod 777 $filename.sh
done