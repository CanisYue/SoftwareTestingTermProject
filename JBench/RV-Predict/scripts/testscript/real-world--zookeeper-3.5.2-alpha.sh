source $(cd `dirname $0`; pwd)/template.sh
test_name=real-world--zookeeper-3.5.2-alpha
class_to_run=
run $*
