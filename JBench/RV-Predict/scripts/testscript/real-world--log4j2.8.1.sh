source $(cd `dirname $0`; pwd)/template.sh
test_name=real-world--log4j2.8.1
class_to_run=
run $*
