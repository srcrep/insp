import math
P=float(input("Inside pressure psig:"))
SE=float(input("Allowable limit psi:"))
D=float(input("Inside Diameter in:"))
Ca=float(input("Corrosion Allowance in:"))

#corrosion allowance
Di=D+2*Ca
R=Di/2

#per div1

#cir stress tmin
tc=(P*R)/(SE-0.6*P)

#long stress min
tt=(P*R)/(2*SE+0.4*P)

#greater of the two
t=max(tc,tt)
t1=t+Ca

#per div 2
t0=R*((math.exp(P/SE))-1)
t2=t0+Ca

#results

print("div1 tmin :", t, "in inches")
print("div1 tmin + Ca :", t1, "in inches")
print("div2 tmin :", t0, "in inches")
print("div2 tmin + Ca:", t2, "in inches")
print("tmin :", (min(t1,t2)), "in inches")
