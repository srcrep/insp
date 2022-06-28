import math
P=float(input("Design Pressure:"))
SE=float(input("Allowable Stress:"))
D=float(input("Inside Diameter:"))
Ca=float(input("Corrosion Allowance:"))

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

print("tmin :", t, '"')
print("tMin + CA :", t1, '"')

print("By the way Ben, it's due to licensing costs.")

#print("div1 tmin :", t, '"')
#print("div1 tmin + Ca :", t1, '"')

#print("div2 tmin :", t0, '"')
#print("div2 tmin + Ca:", t2, '"')
