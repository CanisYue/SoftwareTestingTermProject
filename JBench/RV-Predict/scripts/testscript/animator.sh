source $(cd `dirname $0`; pwd)/template.sh
test_name=animator
class_to_run=XtangoAnimation.XtangoAnimator
run $*
