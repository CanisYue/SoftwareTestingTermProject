source $(cd `dirname $0`; pwd)/template.sh
test_name=testRace4
class_to_run=testRace.TestRace4
run $*
