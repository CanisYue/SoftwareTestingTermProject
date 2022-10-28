source $(cd `dirname $0`; pwd)/template.sh
test_name=testAtomicity7
class_to_run=benchmarks.testcases.TestAtomicity7
run $*
