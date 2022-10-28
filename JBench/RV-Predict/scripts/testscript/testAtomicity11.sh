source $(cd `dirname $0`; pwd)/template.sh
test_name=testAtomicity11
class_to_run=benchmarks.testcases.TestAtomicity11
run $*
