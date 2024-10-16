m1 = 1382
m2 = 96.7
msol = 5
ri = 0.5727
ro = 0.891
d = 6.056
h = 1.5
a = 9.089
b = 1.4
boom = 10.5
mmag = 0.2

Ixx = (0.25*m1*ri**2 + (1/12)*m1*h**2)  # inner cylinder
print(Ixx)
Ixx += m2 * (0.25*(ro**4 - ri**4))/(ro**2 - ri**2) + (1/12)*m2*h**2  # outer hollow cylinder
print(Ixx)
Ixx += 2 * ((1/12)*msol*(a**2 + b**2) + msol*d**2)
print(Ixx)

Iyy = (0.25*m1*ri**2 + (1/12)*m1*h**2)  # inner cylinder
print(Iyy)
Iyy += m2 * (0.25*(ro**4 - ri**4))/(ro**2 - ri**2) + (1/12)*m2*h**2  # outer hollow cylinder
print(Iyy)
Iyy += 2 * mmag*boom**2  # magnetometer as point mass
print(Iyy)
Iyy += 2*((1/12)*msol*b**2 + msol*d**2)  # solar panels
print(Iyy)

Izz = 0.5*m1*ri**2  # inner cylinder
print(Izz)
Izz += 0.5*m2*(ro**2 + ri**2)  # outer hollow cylinder
print(Izz)
Izz+= 2 * ((1/12)*msol*a**2 + msol*d**2)  # solar panels
print(Izz)
