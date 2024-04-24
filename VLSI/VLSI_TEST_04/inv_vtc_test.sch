v {xschem version=3.4.5 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
C {devices/vsource.sym} -240 50 0 0 {name=vdd value=1.8 savecurrent=false}
C {devices/vsource.sym} -180 50 0 0 {name=vin value=0 savecurrent=false}
C {devices/gnd.sym} -30 50 0 0 {name=l1 lab=GND}
C {devices/gnd.sym} -180 80 0 0 {name=l2 lab=GND}
C {devices/gnd.sym} -240 80 0 0 {name=l3 lab=GND}
C {devices/lab_pin.sym} -240 20 1 0 {name=p1 sig_type=std_logic lab=vdd}
C {devices/lab_pin.sym} -180 20 1 0 {name=p2 sig_type=std_logic lab=vin}
C {devices/lab_pin.sym} -60 0 0 0 {name=p3 sig_type=std_logic lab=vin}
C {devices/lab_pin.sym} 70 0 2 0 {name=p4 sig_type=std_logic lab=vout}
C {devices/lab_pin.sym} -30 -50 1 0 {name=p5 sig_type=std_logic lab=vdd}
C {devices/code_shown.sym} -370 -200 0 0 {name=VTC1 only_toplevel=false value=".lib /usr/local/share/pdk/sky130A/libs.tech/ngspice/sky130.lib.spice tt
.dc vin 0 2 1m   
.save all 
.end"}
C {inv_vtc.sym} 90 80 0 0 {name=x1}
