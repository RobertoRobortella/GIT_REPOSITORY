v {xschem version=3.4.5 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N -220 -310 -220 -270 {
lab=vout}
N -220 -340 -200 -340 {
lab=vcc}
N -220 -410 -220 -370 {
lab=vcc}
N -200 -390 -200 -340 {
lab=vcc}
N -220 -390 -200 -390 {
lab=vcc}
N -220 -240 -200 -240 {
lab=GND}
N -200 -240 -200 -190 {
lab=GND}
N -220 -210 -220 -190 {
lab=GND}
N -220 -190 -200 -190 {
lab=GND}
N -220 -190 -220 -170 {
lab=GND}
N -280 -340 -260 -340 {
lab=vin}
N -280 -340 -280 -240 {
lab=vin}
N -280 -240 -260 -240 {
lab=vin}
N -350 -290 -280 -290 {
lab=vin}
N -230 -290 -220 -290 {
lab=vout}
C {devices/vsource.sym} -100 -40 0 0 {name=vcc1 value=1.8 savecurrent=false}
C {devices/vsource.sym} -40 -40 0 0 {name=vcc value="pulse(0 1.8 1ns 1ns 1ns 5ns 10ns)"  savecurrent=false}
C {sky130_fd_pr/nfet_01v8.sym} -240 -240 0 0 {name=M1
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
C {sky130_fd_pr/pfet_01v8.sym} -240 -340 0 0 {name=M2
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
model=pfet_01v8
spiceprefix=X
}
C {devices/lab_pin.sym} -100 -70 0 0 {name=p1 sig_type=std_logic lab=vcc
}
C {devices/lab_pin.sym} -40 -70 0 0 {name=p2 sig_type=std_logic lab=vin}
C {devices/lab_pin.sym} -230 -290 0 0 {name=p3 sig_type=std_logic lab=vout
}
C {devices/lab_pin.sym} -340 -290 0 0 {name=p4 sig_type=std_logic lab=vin}
C {devices/lab_pin.sym} -220 -410 0 0 {name=p5 sig_type=std_logic lab=vcc
}
C {devices/gnd.sym} -220 -170 0 0 {name=l1 lab=GND}
C {devices/gnd.sym} -100 -10 0 0 {name=l2 lab=GND}
C {devices/gnd.sym} -40 -10 0 0 {name=l3 lab=GND}
C {devices/code_shown.sym} 20 -160 0 0 {name=s1 only_toplevel=false value=".lib /usr/local/share/pdk/sky130A/libs.tech/ngspice/sky130.lib.spice tt
.tran 0.1n 100n
.save all"
}
