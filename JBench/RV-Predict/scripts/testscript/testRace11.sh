source $(cd `dirname $0`; pwd)/template.sh
test_name=testRace11
class_to_run=testRace.TestRace11
run $*
