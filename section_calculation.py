import math
import numpy as np
import matplotlib.pyplot as plt


while True:

 
    n = int(input("Enter Number of elements: "))
    print()
    shape = np.zeros((n,4))
    length = np.zeros(n)
    
    for i in range(n):
         print(f"################# First coordinates of element {i+1} #################")
         print()
         shape[i,0] = float(input(f"Enter first x coordinates of element {i+1}: "))
         shape[i,2] = float(input(f"Enter first y coordinates of element {i+1}: "))
         print()
         print(f"################# Second coordinates of element {i+1} #################")
         print()
         shape[i,1] = float(input(f"Enter second x coordinates of element {i+1}: "))
         shape[i,3] = float(input(f"Enter second y coordinates of element {i+1}: "))
         print("------------------------------------------------------------")
         print()
    len_sum = 0
    x1 = shape[0:n,0]
    x2 = shape[0:n,1]
    y1 = shape[0:n,2]
    y2 = shape[0:n,3]
    #                               Example     
# =============================================================================
#     n = 4 
#     shape = np.array([[0,1,0,0],[0.5,0.5,0,1],[1,1,0,1],[0.5,1.5,1,1]])
#     length = np.zeros(n)
#     
# =============================================================================

    
    for i in range(n):
        length[i] = math.sqrt((x2[i]-x1[i])**2 + (y2[i]-y1[i])**2)
        len_sum += length[i]
        plt.plot((shape[i,0],shape[i,1]),(shape[i,2],shape[i,3]))
    
    xcge = (x1+x2)/2
    ycge = (y1+y2)/2
    
    xcg = 0
    ycg = 0
    
    
    for i in range(n):
    
        xcg += xcge[i]*length[i]/len_sum
        ycg += ycge[i]*length[i]/len_sum
    
    
    iy_axis = length**3/12
    theta = np.zeros(n)
    
    ix = 0
    iy = 0
    ixy = 0
    
    for i in range(n):
        theta[i] = math.atan2(y2[i]-y1[i],x2[i]-x1[i])
        ixe = iy_axis * math.sin(theta[i])**2
        iye = iy_axis * math.cos(theta[i])**2
        ixye = iy_axis/2 * math.sin(2*theta[i])
        
        ix += ixe[i] + length[i]*(ycge[i]-ycg)**2
        iy += iye[i] + length[i]*(xcge[i]-xcg)**2
        ixy += ixye[i] + length[i]*(ycge[i]-ycg)*(xcge[i]-xcg)
    
    kb = ix * iy - ixy**2
    kx = ix/kb
    ky = iy/kb
    kxy = ixy/kb
    
    shape_slope = -2*ixy/(ix-iy)
    beta = 0.5 * math.atan2(-2*ixy,ix-iy)
    
    
    
    p_axes_scale = 0.1
    p_axes_minx = np.minimum(np.min(x1),np.min(x2))
    p_axes_maxx = np.maximum(np.max(x1),np.max(x2))
    
    xp = np.linspace(p_axes_scale*xcg - p_axes_minx ,p_axes_maxx-p_axes_scale*xcg,30)
    yp1 = shape_slope* xp - shape_slope *xcg + ycg
    yp2 =  -xp/shape_slope + 1/shape_slope *xcg + ycg
    
    
    plt.plot(xp,yp1,'--')
    if shape_slope == 0:
        plt.plot([xcg, xcg],
        np.linspace(1.2*np.minimum(np.min(y1), np.min(y2)),1.2*np.maximum(np.max(y1), np.max(y2)), 2), '--')

    else:
        plt.plot(xp,yp2,'--')
    plt.plot(xcg,ycg,'o')
    plt.axis('equal')
    
    
    # plt.tight_layout(rect=[0, 0, 0.8, 1])
    # plt.figtext(0,1,f"Ix = {ix:.4f} d^3t")
    # plt.figtext(0,0.95,f"Iy = {iy:.4f} d^3t")
    # plt.figtext(0,0.9,f"Ixy = {ixy:.4f} d^3t")
    # plt.figtext(0.,0.8,f"kx = {kx:.4f}/(d^3 t)")
    # plt.figtext(0,0.75,f"ky = {ky:.4f}/(d^3 t)")
    # plt.figtext(0,0.7,f"kxy = {kxy:.4f}/(d^3 t)")
    # plt.figtext(0,0.6,f"beta = {math.degrees(beta):.4f}°")
    plt.suptitle( f"Ix = {ix:.4f} | d³t | Iy = {iy:.4f} d³t | Ixy = {ixy:.4f} d³t\n" f"kx = {kx:.4f}/(d³t) | ky = {ky:.4f}/(d³t) | kxy = {kxy:.4f}/(d³t)\n" f"β = {math.degrees(beta):.2f}° \n Xg = {xcg:.4f} | Yg = {ycg:.4f}", y=0.98,fontsize=10)
    print(f"Ix ={ix:.4f} d^3t ")
    print(f"Iy ={iy:.4f} d^3t ")
    print(f"Ixy ={ixy:.4f} d^3t ")
    print(f"kx = {kx:.4f}/(d^3 t)")
    print(f"ky = {ky:.4f}/(d^3 t)")
    print(f"kxy = {kxy:.4f}/(d^3 t)")
    print(f"beta = {math.degrees(beta):.4f}°")
    print()
    plt.show()

