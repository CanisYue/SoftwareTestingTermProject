source $(cd `dirname $0`; pwd)/template.sh
test_name=JGFMolDynBenchSizeA
class_to_run="benchmarks.JGFMolDynBenchSizeA 3"
run $*
