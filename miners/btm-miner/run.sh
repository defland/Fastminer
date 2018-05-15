#!/bin/bash

cd $(dirname $0)


SMI=nvidia-smi


DRV=$( $SMI -h |grep Interface | awk -Fv '{print $2}' | cut -d. -f1 )


if [ $DRV -lt 387 ];then
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:cuda8
else
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:cuda9
fi


PID=$( pidof miner )
if  [ "$PID" != "" ];then
kill -9 $PID
sleep 1
fi

python btm.py  $@
