#!/usr/bin/env python
# coding: utf-8

# Importing packages

import matplotlib.pyplot as plt


# Functions
# Taken input to be 0 in both cases (x = 0)

def first(x,y,T):
    return -y/T
def second(x,y,y_d):
    return y_d
def second1(x,y,y_d):
    return -2*si*w*y_d - w*w*y


############################ FIRST ORDER ###########################################

t=[0]
y=[10] # y
h=0.05 #step-size
tf=30 #final time

# Count number of iterations using step size h
n = (int)(tf/h)
# Iterate for number of iterations
t0=0

T = input("Enter value of T: ")
T = float(T)

for i in range(1,n):
    "Apply Runge Kutta Formulas to find next value of y"
    k1 = first(t0,y[-1],T)
    k2 = first(t0+0.5*h, y[-1]+0.5*h*k1,T)
    k3 = first(t0+0.5*h, y[-1]+0.5*h*k2,T)
    k4 = first(t0+h, y[-1]+h*k3,T)

    # Update next value of theta
    y.append(y[-1] + (1/6)*(k1 + 2 * k2 + 2 * k3 + k4)*h)
    # Update next value of t
    t0 = t0 + h
    t.append(t0)
fig=plt.figure(figsize=(10,7))
plt.plot(t,y)
plt.title('y vs t')




############################ SECOND ORDER ##########################################

t=[0]
y=[10] # y
y_d=[10]
h=0.05 #step-size
tf=30 #final time
# Count number of iterations using step size h
n = (int)(tf/h)
# Iterate for number of iterations
t0=0

si = input("Enter value of damping constant: ")
si = float(si)
w = input("Enter value of natural frequency: ")
w = float(w)

for i in range(1,n):
    "Apply Runge Kutta Formulas to find next value of y"
    k1 = second(t0,y[-1],y_d[-1])
    k1_d = second1(0,y[-1],y_d[-1])
    k2 = second(t0+0.5*h, y[-1]+0.5*h*k1,y_d[-1]+0.5*h*k1_d)
    k2_d = second1(t0+0.5*h, y[-1]+0.5*h*k1,y_d[-1]+0.5*h*k1_d)
    k3 = second(t0+0.5*h, y[-1]+0.5*h*k2,y_d[-1]+0.5*h*k2_d)
    k3_d = second1(t0+0.5*h, y[-1]+0.5*h*k2,y_d[-1]+0.5*h*k2_d)
    k4 = second(t0+h, y[-1]+h*k3,y_d[-1]+h*k3_d)
    k4_d = second1(t0+h, y[-1]+h*k3,y_d[-1]+h*k3_d)

#     Update next value of theta
    y.append(y[-1] + (1/6)*(k1 + 2 * k2 + 2 * k3 + k4)*h)
    y_d.append(y_d[-1] + (1/6)*(k1_d+2*k2_d+2*k3_d+k4_d)*h)
    # Update next value of t
    t0 = t0 + h
    t.append(t0)

fig,a =  plt.subplots(1,2,figsize=(18,7))
a[0].plot(t,y)
a[0].set_title('y vs t')
a[1].plot(t,y_d)
a[1].set_title('y_dot vs t')
plt.show()

################################# END ##############################################
