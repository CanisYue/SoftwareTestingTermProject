source $(cd `dirname $0`; pwd)/template.sh
test_name=testRace12
class_to_run=testRace.TestRace12
run $*
