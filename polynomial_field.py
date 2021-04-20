#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 18:09:58 2020

@author: matthias
"""


import numpy as np
import json
import scipy.io as sio
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

#Read file and load arrays
mat = sio.loadmat('eq_TCV.mat')

print( "Loading data ... ")
R= mat['eq']['R'][0][0][:,:]
print(np.shape(R))
miny=100
maxy=1300
minx=40
maxx=540
every=10
R= mat['eq']['R'][0][0][miny:maxy:every,minx:maxx:every]
Z= mat['eq']['Z'][0][0][miny:maxy:every,minx:maxx:every]
Psi = mat['eq']['psi'][0][0][miny:maxy:every,minx:maxx:every]/2/np.pi # normalized weirdly
BR = mat['eq']['BR'][0][0][miny:maxy:every,minx:maxx:every]
BZ = mat['eq']['BZ'][0][0][miny:maxy:every,minx:maxx:every]
Bpol = mat['eq']['Bpol'][0][0][miny:maxy:every,minx:maxx:every]
Bphi = mat['eq']['Bphi'][0][0][miny:maxy:every,minx:maxx:every]

print(np.shape(Psi)[0] )
dPsidz = np.diff( Psi, axis=0)/np.diff( Z, axis=0)

print(np.shape(dPsidz) )
dPsidz=np.append(np.zeros((1,(np.shape(Psi)[1]))),dPsidz, axis=0)
#print( np.shape(dPsidz))
BR_num = -1/R*dPsidz
#print( BR[1][0]/BR_num[1][0])
print ( np.shape(R))
print ( np.shape(Z))
print ( np.shape(Psi))
print ( np.shape(BR))
print ( np.shape(BZ))
print ( np.shape(Bpol))
print ( np.shape(Bphi))

# Normalization 
B0 = 0.929 # T
R0 =  0.906 # m
a = 0.25 # 
R = R/R0
Z = Z/R0
Psi = Psi/B0/R0/R0 # theoretically we could subtract an arbitrary constant
Bphi = Bphi / B0
BR = BR/B0
BR_num = BR_num/B0
BZ = BZ/B0
Bpol = Bpol/B0

def source_terms( R,Z, R0, Z0, a, b, c):
    if R > R0 :
        return np.exp( - (R-R0)*(R-R0)/a/a - (Z-Z0)*(Z-Z0)/b/b)
    return  0.5*np.exp(
            - (R-R0)*(R-R0)/a/a -2.*c*(R-R0)*(Z-Z0)- (Z-Z0)*(Z-Z0)/b/b )+0.5*np.exp(
            - (R-R0)*(R-R0)/a/a +2.*c*(R-R0)*(Z-Z0)- (Z-Z0)*(Z-Z0)/b/b )


                
# degR = 1
# degZ = 13
degR = 8
degZ = 8
def psi_ana( x, *c):
#    print(x)
    R , Z = x
    

    # psi = np.zeros([13,np.size(R)])
    # psi[0] = 1
    # psi[1] = R**2
    # psi[2] = Z**2 - R**2*np.log(R)
    # psi[3] = R**4 - 4*R**2*Z**2
    # psi[4] = 2*Z**4-9*R**2*Z**2 + 3*R**4*np.log(R) - 12*R**2*Z**2*np.log(R)
    # psi[5] = R**6-12*R**4*Z**2 + 8*R**2*Z**4
    # psi[6] = 8*Z**6-140*R**2*Z**4+75*R**4*Z**2-15*R**6*np.log(R)+180*R**4*Z**2*np.log(R)-120*R**2*Z**4*np.log(R)
    # psi[7] = Z
    # psi[8] = Z*R**2
    # psi[9] = Z**3-3*Z*R**2*np.log(R)
    # psi[10] = 3*Z*R**4 - 4*Z**3*R**2
    # psi[11] = 8*Z**5-45*Z*R**4 - 80*Z**3*R**2*np.log(R) + 60*Z*R**4*np.log(R)
    # psi[12] = R**4/8
    ##    psi[13] = R**2*np.log(R)/2 - R**4/8
    

    psi = np.zeros([degR*degZ,np.size(R)])
    for i in range( degR):
        for j in range (degZ):
            psi[i*degZ+j] = R**i*Z**j



    return np.dot(c,psi)

1
print( "Determine Fit Coefficients ")
c = np.array( np.zeros(degR*degZ))
#Test - coefficients from previous fit
# c =np.array([
#         1.19057914,  18.64900832, -17.98147622,  -8.38366912, 11.94641991,
#  -10.21508482, -0.41773262, -0.13350555, -4.26340698, 1.7611923,
#    0.55219432, -0.06051206, -5.08575381
#    , 0, 0
#    , 0, 0, 0, 0, 0, 0 # 21
#    , 0,0,0,0 # 25
#    ,0,0,0,0,0,0,0,0,0,0,0 # 36
#    ]
#     )

# We need to ravel the meshgrids of X1, Y points to a pair of 1-D arrays.
coords = np.vstack((R.ravel(),Z.ravel()))
#psip_ana = np.copy(coords[0])
psip_num = Psi.ravel()
psip_ana = psi_ana( coords, c)
#source = np.copy( coords[0])
#for i in range(len(coords[0])) :
#    source[i] = source_terms( coords[0][i], coords[1][i] , 0.98, -0.02, 0.0335,0.05, 565)

#print(c.shape)
def sigma ( x): 
    # if x < 0.07:
    #     return 10000 #basically removes these points from fit
    # if x > 0.56/2/np.pi:
    #     return 1
    # else:
        return 1

weights = np.array([sigma(psi) for psi in psip_num])

copt, pcov = curve_fit(psi_ana, coords, psip_num,c,weights)   
print( copt[0:len(copt)])
psip_ana = psi_ana( coords, copt)
difference = psip_ana-psip_num


def weightedL2(a,b,w):
    q = a-b
    return np.sqrt((q*q/w/w).sum())
norm = weightedL2(psip_ana, psip_num, weights)/np.linalg.norm( psip_num, ord=2)

psip_ana = psip_ana.reshape( R.shape)
psip_num = psip_num.reshape( R.shape)
#Bphi_ana = np.sqrt( 1-2*copt[13]/copt[12]**2 *psip_num)#/coords[0]
Bphi_ana = 1/coords[0]
difference = Bphi.ravel() - Bphi_ana
print("Relative Error in Bphi is      ", np.linalg.norm(difference, ord=2)/np.linalg.norm(Bphi.ravel(), ord=2))
Bphi_ana = Bphi_ana.reshape( R.shape)
#source = source.reshape( R.shape)

fig,ax=plt.subplots(3,3,figsize=(3*7.5,3*12),dpi= 80, facecolor='w', edgecolor='k')
levels = np.arange( 0.05,0.11,0.005)
im = ax[0][0].contourf(R*R0,Z*R0,psip_num, levels) 
fig.colorbar(im, ax=ax[0][0])
ax[0][0].set_title( "Psi")

#im = ax[0][1].pcolormesh(R,Z, source)
#ax[0][1].contour(R,Z,Psi,levels) 
#fig.colorbar(im, ax=ax[0][1])
#ax[0][1].set_title( "Source")
#im = ax[0][1].pcolormesh(R*R0,Z*R0,1 psip_num)

im = ax[0][1].contourf(R*R0,Z*R0,psip_ana, levels) 
fig.colorbar(im, ax=ax[0][1])
ax[0][1].set_title( "Psi fit")

im = ax[0][2].contourf(R*R0,Z*R0,psip_ana-psip_num) 
fig.colorbar(im, ax=ax[0][2])
ax[0][2].set_title( "Psi Diff")


levels = np.arange( 0.8,1.3,0.05)
im = ax[1][0].contourf(R*R0,Z*R0,Bphi,levels) 
fig.colorbar(im, ax=ax[1][0])
ax[1][0].set_title( "Bphi")

im = ax[2][0].contourf(R*R0,Z*R0,Bphi_ana,levels)
fig.colorbar(im, ax=ax[2][0])
ax[2][0].set_title( "Bphi fit")

#levels = np.arange( 0, 100,10)
#im = ax[1][1].contourf(R,Z,a*Bphi/R0/Bpol, levels)#(Bpol)/(a))
#fig.colorbar(im, ax=ax[1][1])
#ax[1][1].set_title( "q-factor")


levels = np.arange( -0.125,0.15,0.025)
im = ax[1][1].contourf(R*R0,Z*R0,BR,levels) 
fig.colorbar(im, ax=ax[1][1])
ax[1][1].set_title( "BR")

#im = ax[2][1].contourf(R*R0,Z*R0,BZ)
dPsidz = np.diff( psip_ana, axis=0)/np.diff( Z, axis=0)
dPsidz=np.append(np.zeros((1,(np.shape(dPsidz)[1]))),dPsidz, axis=0)
#print( np.shape(dPsidz))
BR_num = -1/R*dPsidz
im = ax[2][1].contourf(R*R0,Z*R0,BR_num,levels)
fig.colorbar(im, ax=ax[2][1])
ax[2][1].set_title( "BR fit")


levels = np.arange( -0.125,0.15,0.025)
im = ax[1][2].contourf(R*R0,Z*R0,BZ,levels) 
fig.colorbar(im, ax=ax[1][2])
ax[1][2].set_title( "BZ")

#im = ax[2][1].contourf(R*R0,Z*R0,BZ)
dPsidr = np.diff( psip_ana, axis=1)/np.diff( R, axis=1)
dPsidr=np.append(np.zeros(((np.shape(dPsidz)[0]),1)),dPsidr, axis=1)
#print( np.shape(dPsidz))
BZ_num = 1/R*dPsidr
im = ax[2][2].contourf(R*R0,Z*R0,BZ_num,levels)
fig.colorbar(im, ax=ax[2][2])
ax[2][2].set_title( "BZ fit")
#plt.savefig( "tcv")
plt.show()

print( "Relative Error norm in Psip is ", norm)

# The parameters are for Psi/R0 so that the FELTOR normalisation is automatically obtained
# Psi from EPFL is our -Psi_p (because how BR and BZ are defined )
# positive I from EPFL is negative in our coordinate system

# geom_file = { "A" : 0, "c": (copt[0:12]/copt[12]).tolist(), "PP": -copt[12], 
#              "PI": -1, "R_0": 906.38, "elongation": 1.5, "triangularity": 0.4,
#              "inverseaspectratio": a/R0
geom_file = { "M" : degR, "N": degZ,  "c": copt.tolist(), "PP": -1, 
              "PI": -1, "R_0": 906.38, "elongation": 1.5, "triangularity": 0.4,
              "inverseaspectratio": a/R0, "equilibrium" : "polynomial", 
              "description": "standardX"
        }
print( "Source psi", psi_ana( (1.075, -0.01), copt))
    
print(json.dumps(geom_file, indent=4))
with open('tcv.json', 'w') as f:
    print( json.dumps(geom_file, indent=4), file=f)
