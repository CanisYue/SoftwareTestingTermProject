source $(cd `dirname $0`; pwd)/template.sh
test_name=sor
class_to_run="benchmarks.sor.Sor 10 10"
run $*
