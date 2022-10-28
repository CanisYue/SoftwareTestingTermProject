source $(cd `dirname $0`; pwd)/template.sh
test_name=account
class_to_run=account.Account
run $*
