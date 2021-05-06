#!/bin/bash

dia=$(date '+%Y-%m-%d %H:%M:%S')

echo $dia

mes="${dia:5:2}"
dd="${dia:8:2}"
aa="${dia:2:2}"
hh="${dia:11:2}"
mm="${dia:14:2}"

echo ${mes}
echo ${dd}
echo ${aa}
echo ${hh}
echo ${mm}

fecha="M"${mes}"D"${dd}"A"${aa}"h"${hh}"m"${mm}

echo $fecha

mkdir Res_Fotos_$fecha

mv *.jpg ./Res_Fotos_$fecha/.

tar -zcvf Res_Fotos_$fecha.tar ./Res_Fotos_$fecha/

rm -rf Res_Fotos_$fecha



