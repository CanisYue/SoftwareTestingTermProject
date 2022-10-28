source $(cd `dirname $0`; pwd)/template.sh
test_name=testRace10
class_to_run=testRace.TestRace10
run $*
