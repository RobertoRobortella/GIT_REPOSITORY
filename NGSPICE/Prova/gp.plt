set encoding utf8
set termoption noenhanced
set title "KiCad schematic CR Circuit"
set xlabel "Hz"
set grid
set logscale x
set xrange [1e+03:1e+08]
set mxtics 10
set grid mxtics
unset logscale y 
set yrange [-2.623840e+01:2.220182e+01]
#set xtics 1
#set x2tics 1
#set ytics 1
#set y2tics 1
set format y "%g"
set format x "%g"
plot 'gp.data' using 1:2 with lines lw 1 title "v(output)",\
'gp.data' using 3:4 with lines lw 1 title "vdb(output)",\
'gp.data' using 5:6 with lines lw 1 title "ph(output)"
