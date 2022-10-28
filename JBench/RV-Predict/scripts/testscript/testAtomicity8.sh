source $(cd `dirname $0`; pwd)/template.sh
test_name=testAtomicity8
class_to_run=benchmarks.testcases.TestAtomicity8
run $*
