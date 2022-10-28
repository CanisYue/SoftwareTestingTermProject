source $(cd `dirname $0`; pwd)/template.sh
test_name=testAtomicity6
class_to_run=benchmarks.testcases.TestAtomicity6
run $*
