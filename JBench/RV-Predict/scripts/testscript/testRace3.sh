source $(cd `dirname $0`; pwd)/template.sh
test_name=testRace3
class_to_run=testRace.TestRace3
run $*
