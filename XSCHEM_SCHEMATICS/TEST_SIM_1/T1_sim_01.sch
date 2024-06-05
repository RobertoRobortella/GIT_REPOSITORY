v {xschem version=3.4.5 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N 0 130 0 140 {
lab=GND}
N 160 100 160 130 {
lab=GND}
N 160 10 160 40 {
lab=vsin}
N 160 -80 160 -50 {
lab=#net1}
N 0 -80 160 -80 {
lab=#net1}
N 0 -80 0 -0 {
lab=#net1}
N 0 60 0 130 {
lab=GND}
N 60 60 60 100 {
lab=GND}
N 0 100 60 100 {
lab=GND}
N 60 -30 60 0 {
lab=vsin}
N 60 -10 110 -10 {
lab=vsin}
N 110 -10 110 30 {
lab=vsin}
N 110 30 160 30 {
lab=vsin}
N 60 100 60 120 {
lab=GND}
C {vsource.sym} 0 30 0 0 {name=V1 value=3 savecurrent=false}
C {res.sym} 160 -20 0 0 {name=R1
value=1k
footprint=1206
device=resistor
m=1}
C {res.sym} 160 70 0 0 {name=R2
value=10k
footprint=1206
device=resistor
m=1}
C {gnd.sym} 0 130 0 0 {name=l1 lab=GND}
C {gnd.sym} 160 130 0 0 {name=l2 lab=GND}
C {code_shown.sym} 270 -70 0 0 {name=s1 only_toplevel=false value=".tran 0.1m 0.1"}
C {lab_pin.sym} 60 -30 1 0 {name=p1 sig_type=std_logic lab=vsin}
C {vsource.sym} 60 30 0 0 {name=V2 value="SIN(0 1 100)" savecurrent=false}
