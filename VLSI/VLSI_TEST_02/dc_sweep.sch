v {xschem version=3.4.5 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N -40 -30 -40 10 {
lab=vds}
N -40 -30 100 -30 {
lab=vds}
N 100 -30 100 10 {
lab=vds}
N -170 40 -80 40 {
lab=vgs}
N -40 40 -20 40 {
lab=GND}
N -20 40 -20 70 {
lab=GND}
N -40 70 -40 100 {
lab=GND}
N -20 70 -20 90 {
lab=GND}
N -40 90 -20 90 {
lab=GND}
C {sky130_fd_pr/nfet_01v8.sym} -60 40 0 0 {name=M1
W=1
L=0.15
nf=1 
mult=1
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=nfet_01v8
spiceprefix=X
}
C {devices/vsource.sym} -170 70 0 0 {name=Vgs value=0 savecurrent=false}
C {devices/vsource.sym} 100 40 0 0 {name=Vds value=0 savecurrent=false}
C {devices/gnd.sym} -170 100 0 0 {name=l1 lab=GND}
C {devices/gnd.sym} -40 100 0 0 {name=l2 lab=GND}
C {devices/gnd.sym} 100 70 0 0 {name=l3 lab=GND}
C {devices/code_shown.sym} -180 -100 0 0 {name=s1 only_toplevel=false value=".lib /usr/local/share/pdk/sky130A/libs.tech/ngspice/sky130.lib.spice tt
.dc Vgs 0 1.8 1m Vds 0 2 .5   
.save all 
.end"}
C {devices/lab_pin.sym} -170 40 0 0 {name=p1 sig_type=std_logic lab=vgs}
C {devices/lab_pin.sym} 100 10 0 0 {name=p2 sig_type=std_logic lab=vds
}
