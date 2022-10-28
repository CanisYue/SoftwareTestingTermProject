source $(cd `dirname $0`; pwd)/template.sh
test_name=testAtomicity14
class_to_run=benchmarks.testcases.TestAtomicity14
run $*
