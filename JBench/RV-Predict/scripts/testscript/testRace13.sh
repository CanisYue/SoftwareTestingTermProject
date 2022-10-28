source $(cd `dirname $0`; pwd)/template.sh
test_name=testRace13
class_to_run="testRace.TestRace13"
run $*
