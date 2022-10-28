source $(cd `dirname $0`; pwd)/template.sh
test_name=testAtomicity1
class_to_run=benchmarks.testcases.TestAtomicity1
run $*
