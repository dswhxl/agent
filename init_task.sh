#! /bin/sh

if [ $# -lt 1 ]; then
    echo "task_id missing"
    exit 1
fi

task_id=$1

mkdir -p ../workspace/$task_id/jtls ../workspace/$task_id/reports ../workspace/$task_id/words
mkdir -p ../workspace/$task_id/jmxs
