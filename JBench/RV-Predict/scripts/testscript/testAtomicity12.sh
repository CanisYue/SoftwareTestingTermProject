source $(cd `dirname $0`; pwd)/template.sh
test_name=testAtomicity12
class_to_run=benchmarks.testcases.TestAtomicity12
run $*
