source $(cd `dirname $0`; pwd)/template.sh
test_name=boundedbuffer
class_to_run=boundedbuffer.BoundedBuffer
run $*
