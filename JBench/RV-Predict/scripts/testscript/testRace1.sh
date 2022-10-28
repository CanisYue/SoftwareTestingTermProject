source $(cd `dirname $0`; pwd)/template.sh
test_name=testRace1
class_to_run=testRace.TestRace1
run $*
