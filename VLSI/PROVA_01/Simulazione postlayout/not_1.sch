v {xschem version=3.4.5 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N 1810 -960 1840 -960 {
lab=A}
N 1810 -960 1810 -860 {
lab=A}
N 1810 -860 1840 -860 {
lab=A}
N 1760 -910 1810 -910 {
lab=A}
N 1880 -930 1880 -890 {
lab=xxx}
N 1880 -1050 1880 -990 {
lab=vp}
N 1880 -830 1880 -780 {
lab=vn}
N 1880 -960 1940 -960 {
lab=vp}
N 1940 -1010 1940 -960 {
lab=vp}
N 1880 -1010 1940 -1010 {
lab=vp}
N 1880 -860 1940 -860 {
lab=vn}
N 1940 -860 1940 -810 {
lab=vn}
N 1880 -810 1940 -810 {
lab=vn}
N 1880 -910 1980 -910 {
lab=xxx}
C {sky130_fd_pr/nfet_01v8.sym} 1860 -860 0 0 {name=M1
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
C {sky130_fd_pr/pfet_01v8.sym} 1860 -960 0 0 {name=M2
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
C {devices/ipin.sym} 1760 -910 0 0 {name=p1 lab=A}
C {devices/iopin.sym} 1880 -1050 2 1 {name=p2 lab=vp}
C {devices/iopin.sym} 1880 -780 0 0 {name=p3 lab=vn}
C {devices/opin.sym} 1980 -910 0 0 {name=p4 lab=Y}
