source $(cd `dirname $0`; pwd)/template.sh
test_name=tsp
class_to_run="benchmarks.tsp.Tsp ../src/tspfiles/map16c 5"
run $*
