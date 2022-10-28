source $(cd `dirname $0`; pwd)/template.sh
test_name=bufwriter
class_to_run=bufwriter.BufWriter
run $*
