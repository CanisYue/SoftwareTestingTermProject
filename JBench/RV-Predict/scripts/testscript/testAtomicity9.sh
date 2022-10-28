source $(cd `dirname $0`; pwd)/template.sh
test_name=testAtomicity9
class_to_run=benchmarks.testcases.TestAtomicity9
run $*
