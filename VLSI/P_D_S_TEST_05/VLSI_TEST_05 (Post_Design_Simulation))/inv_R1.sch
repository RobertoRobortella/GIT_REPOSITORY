v {xschem version=3.4.5 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N 10 -80 10 -60 {
lab=A}
N 10 20 10 30 {
lab=A}
N 10 -60 10 20 {
lab=A}
N 50 -50 50 -0 {
lab=vout}
N 50 -160 50 -110 {
lab=VP}
N 50 60 50 110 {
lab=VN}
N 50 -20 130 -20 {
lab=vout}
N -60 -20 10 -20 {
lab=A}
N 50 -80 70 -80 {
lab=VP}
N 70 -130 70 -80 {
lab=VP}
N 50 -130 70 -130 {
lab=VP}
N 50 30 70 30 {
lab=VN}
N 70 30 70 80 {
lab=VN}
N 50 80 70 80 {
lab=VN}
C {sky130_fd_pr/pfet_01v8.sym} 30 -80 0 0 {name=M2
W=2
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
C {sky130_fd_pr/nfet_01v8.sym} 30 30 0 0 {name=M3
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
C {devices/ipin.sym} -60 -20 0 0 {name=p1 lab=A}
C {devices/opin.sym} 130 -20 0 0 {name=p2 lab=Y}
C {devices/ipin.sym} 50 -160 0 0 {name=p3 lab=VP
}
C {devices/ipin.sym} 50 110 0 0 {name=p4 lab=VN}
