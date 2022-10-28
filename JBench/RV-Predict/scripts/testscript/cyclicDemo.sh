source $(cd `dirname $0`; pwd)/template.sh
test_name=cyclicDemo
class_to_run=benchmarks.testcases.CyclicDemo
run $*
