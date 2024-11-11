v {xschem version=3.4.5 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N -100 -140 -100 -110 {
lab=#net1}
N -100 -110 110 -110 {
lab=#net1}
N 110 -140 110 -110 {
lab=#net1}
N -100 -170 110 -170 {
lab=#net1}
N 0 -170 0 -110 {
lab=#net1}
N 110 -360 110 -200 {
lab=#net2}
N -100 -360 -100 -200 {
lab=#net3}
N -60 -390 70 -390 {
lab=#net3}
N -100 -340 -30 -340 {
lab=#net3}
N -30 -390 -30 -340 {
lab=#net3}
N 0 30 0 90 {
lab=GND}
N 0 -0 80 0 {
lab=GND}
N 80 0 80 50 {
lab=GND}
N 0 50 80 50 {
lab=GND}
N 240 0 320 0 {
lab=GND}
N 320 0 320 50 {
lab=GND}
N 240 50 320 50 {
lab=GND}
N 240 50 240 90 {
lab=GND}
N 240 30 240 50 {
lab=GND}
N -220 0 -40 0 {
lab=#net4}
N 0 -110 0 -30 {
lab=#net1}
N -260 -60 -260 -30 {
lab=#net4}
N -260 -60 -190 -60 {
lab=#net4}
N -190 -60 -190 -0 {
lab=#net4}
N 160 0 200 0 {
lab=#net4}
N 160 -60 160 0 {
lab=#net4}
N -190 -60 160 -60 {
lab=#net4}
N -330 0 -260 0 {
lab=GND}
N -330 0 -330 50 {
lab=GND}
N -330 50 -260 50 {
lab=GND}
N -260 50 -260 90 {
lab=GND}
N -260 30 -260 50 {
lab=GND}
N 240 -360 240 -30 {
lab=#net5}
N 190 -390 200 -390 {
lab=#net2}
N 190 -390 190 -330 {
lab=#net2}
N 110 -330 190 -330 {
lab=#net2}
N -100 -470 -100 -420 {
lab=VDD}
N 110 -470 110 -420 {
lab=VDD}
N 240 -470 240 -420 {
lab=VDD}
N -160 -390 -100 -390 {
lab=VDD}
N -160 -440 -160 -390 {
lab=VDD}
N -160 -440 -100 -440 {
lab=VDD}
N 110 -390 170 -390 {
lab=VDD}
N 170 -440 170 -390 {
lab=VDD}
N 110 -440 170 -440 {
lab=VDD}
N 240 -390 310 -390 {
lab=VDD}
N 310 -440 310 -390 {
lab=VDD}
N 240 -440 310 -440 {
lab=VDD}
N 110 -280 150 -280 {
lab=#net2}
N 210 -280 240 -280 {
lab=#net5}
N -500 -250 -500 -230 {
lab=VDD}
N -500 -170 -500 -140 {
lab=GND}
N 150 -170 170 -170 {
lab=V+}
N -260 -320 -260 -300 {
lab=VDD}
N -260 -240 -260 -60 {
lab=#net4}
N -170 -170 -140 -170 {
lab=V-}
C {sky130_fd_pr/nfet_01v8.sym} -20 0 0 0 {name=M1
W=1
L=1
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
C {sky130_fd_pr/nfet_01v8.sym} 220 0 0 0 {name=M2
W=1
L=1
nf=1 
mult=4
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=nfet_01v8
spiceprefix=X
}
C {sky130_fd_pr/nfet_01v8.sym} -240 0 0 1 {name=M3
W=1
L=1
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
C {sky130_fd_pr/nfet_01v8.sym} 130 -170 0 1 {name=M4
W=1
L=1
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
C {sky130_fd_pr/nfet_01v8.sym} -120 -170 0 0 {name=M5
W=1
L=1
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
C {sky130_fd_pr/pfet_01v8.sym} 220 -390 0 0 {name=M7
W=1
L=1
nf=1
mult=8
ad="'int((nf+1)/2) * W/nf * 0.29'" 
pd="'2*int((nf+1)/2) * (W/nf + 0.29)'"
as="'int((nf+2)/2) * W/nf * 0.29'" 
ps="'2*int((nf+2)/2) * (W/nf + 0.29)'"
nrd="'0.29 / W'" nrs="'0.29 / W'"
sa=0 sb=0 sd=0
model=pfet_01v8
spiceprefix=X
}
C {sky130_fd_pr/pfet_01v8.sym} 90 -390 0 0 {name=M6
W=1
L=1
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
C {sky130_fd_pr/pfet_01v8.sym} -80 -390 0 1 {name=M8
W=1
L=1
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
C {devices/capa.sym} 180 -280 1 0 {name=C1
m=1
value=1p
footprint=1206
device="ceramic capacitor"}
C {devices/gnd.sym} -260 90 0 0 {name=l1 lab=GND}
C {devices/gnd.sym} 0 90 0 0 {name=l2 lab=GND}
C {devices/gnd.sym} 240 90 0 0 {name=l3 lab=GND}
C {devices/vdd.sym} -100 -470 0 0 {name=l4 lab=VDD}
C {devices/vdd.sym} 110 -470 0 0 {name=l5 lab=VDD}
C {devices/vdd.sym} 240 -470 0 0 {name=l6 lab=VDD}
C {devices/vsource.sym} -500 -200 0 0 {name=V1 value=2.5 savecurrent=false}
C {devices/vdd.sym} -500 -250 0 0 {name=l7 lab=VDD}
C {devices/gnd.sym} -500 -140 0 0 {name=l8 lab=GND}
C {devices/lab_pin.sym} -170 -170 2 1 {name=p1 sig_type=std_logic lab=V-
}
C {devices/lab_pin.sym} 170 -170 2 0 {name=p2 sig_type=std_logic lab=V+
}
C {devices/lab_pin.sym} 260 -280 2 0 {name=p3 sig_type=std_logic lab=VOUT
}
C {devices/isource.sym} -260 -270 0 0 {name=I0 value=1u}
C {devices/vdd.sym} -260 -320 0 0 {name=l9 lab=VDD}
