source $(cd `dirname $0`; pwd)/template.sh
test_name=testAtomicity4
class_to_run=benchmarks.testcases.TestAtomicity4
run $*
