#! /bin/sh

here=$(cd `dirname $0`; pwd)

if [ $# -lt 1 ]; then
	echo "param missing."
	echo "use like: sh agent.sh start|restart|stop|check"
	exit 0
fi

if [ "$1" = "-h" -o "$1" = "--help" ]; then
	echo "use like: sh agent.sh start|restart|stop|check"
	exit 0
fi

function start()
{
	python -m src.agent 8085 > console.log 2>&1 &
	echo "service start success."
}

function stop()
{
	ps -ef | grep src.agent | grep -v grep | awk '{print $2}' | xargs kill -9
	echo "service stop success."
}

function restart()
{
	stop
	start
	echo "service restart success"
}

function check()
{
	cnt=`ps -ef | grep "src.agent 8085" | grep -v grep | wc -l`
	if [ $cnt -eq 0 ]; then
		echo "service OFFLINE"
	else
		echo "service ONLINE"
	fi
}

cd $here
case $1 in
	"start")
	start
	;;
	"restart")
	restart
	;;
	"stop")
    stop
    ;;
    "check")
    check
    ;;
esac