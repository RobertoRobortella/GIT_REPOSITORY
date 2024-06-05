v {xschem version=3.4.5 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N 170 20 190 20 {
lab=GND}
N 190 20 190 40 {
lab=GND}
N -460 100 -460 130 {
lab=GND}
N -530 100 -530 130 {
lab=GND}
C {not_1.sym} 20 0 0 0 {name=x1}
C {devices/vsource.sym} -530 70 0 0 {name=V1 value=0 savecurrent=false}
C {devices/vsource.sym} -460 70 0 0 {name=V2 value=0 savecurrent=false}
C {devices/gnd.sym} -530 130 0 0 {name=l1 lab=GND}
C {devices/gnd.sym} -460 130 0 0 {name=l2 lab=GND}
C {devices/gnd.sym} 190 40 0 0 {name=l3 lab=GND}
C {devices/lab_pin.sym} -130 -20 0 0 {name=p1 sig_type=std_logic lab=vin}
C {devices/lab_pin.sym} 170 -20 2 0 {name=p2 sig_type=std_logic lab=vdd}
C {devices/lab_pin.sym} 170 0 2 0 {name=p3 sig_type=std_logic lab=vout}
C {devices/lab_pin.sym} -530 40 1 0 {name=p4 sig_type=std_logic lab=vdd}
C {devices/lab_pin.sym} -460 40 1 0 {name=p6 sig_type=std_logic lab=vin}
C {devices/res.sym} 290 60 0 0 {name=R1
value=100k
footprint=1206
device=resistor
m=1}
C {devices/lab_pin.sym} 290 30 1 0 {name=p8 sig_type=std_logic lab=vout}
C {devices/gnd.sym} 290 90 0 0 {name=l4 lab=GND}
