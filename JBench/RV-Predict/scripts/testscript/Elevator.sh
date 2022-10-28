source $(cd `dirname $0`; pwd)/template.sh
test_name=Elevator
class_to_run="elevator.Simulator 10"
run $*
