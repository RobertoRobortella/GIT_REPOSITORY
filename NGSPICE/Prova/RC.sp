.title KiCad schematic CR Circuit
.param res=1000
C1 output NC_01 1n
R1 output gnd res
**VDD gnd NC_01 20
VDD gnd NC_01 5 AC=10
.AC DEC 10 1K 100MEG

.control
op
run
gnuplot gp v(output) vdb(output) ph(output)
write RC_F_SweepR1K.raw
alterparam res=10000
run
gnuplot gp v(output) vdb(output) ph(output)
write RC_F_Sweep_R10K.raw
alterparam res=100000
write RC_F_Sweep_R100K.raw
run
gnuplot gp v(output) vdb(output) ph(output)
**write RC_F_Sweep.raw
**write RC_R_Sweep.raw
**print all
.endc

.end