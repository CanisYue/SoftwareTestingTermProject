source $(cd `dirname $0`; pwd)/template.sh
test_name=real-world--tomcat8.0.26
class_to_run=
run $*
