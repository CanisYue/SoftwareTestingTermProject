source $(cd `dirname $0`; pwd)/template.sh
test_name=simpleExample
class_to_run=benchmarks.SimpleExample
run $*
