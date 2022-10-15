#!/bin/bash
source $(cd `dirname $0`; pwd)/jacontebe.sh

test_name=jdk6_3
#class_to_run=asm.LoggerModifier
run $*


