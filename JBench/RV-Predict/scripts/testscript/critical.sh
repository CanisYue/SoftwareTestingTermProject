source $(cd `dirname $0`; pwd)/template.sh
test_name=critical
class_to_run=critical.Critical
run $*
