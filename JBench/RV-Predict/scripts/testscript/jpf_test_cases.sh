source $(cd `dirname $0`; pwd)/template.sh
test_name=jpf_test_cases
class_to_run=benchmarks.jpf_test_cases.rax.START
run $*
