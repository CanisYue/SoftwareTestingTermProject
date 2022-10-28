source $(cd `dirname $0`; pwd)/template.sh
test_name=JGFRayTracerBenchSizeA
class_to_run="benchmarks.JGFRayTracerBenchSizeA 3"
run $*
