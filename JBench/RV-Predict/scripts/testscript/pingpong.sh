source $(cd `dirname $0`; pwd)/template.sh
test_name=pingpong
class_to_run=pingpong.PingPong
run $*
