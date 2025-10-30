import math
import numpy as np
import matplotlib.pyplot as plt

class section:
        
    def __init__(self,n,X1,X2,Y1,Y2):
      self.n = n 
      self.section = np.full((n,4),np.nan)
      self.X1points = x1
      self.X2points = x2
      self.Y1points = y1
      self.Y2points = y2
      self.Xpoints = np.concatenate((self.X1points,self.X2points))
      self.Ypoints = np.concatenate((self.Y1points,self.Y2points))
      self.points = np.column_stack(self.Xpoints,self.Ypoints)

      
    def get_CG(self):
        
        self.length = np.full((n,1),np.nan)
        self.xcg = 0
        self.ycg = 0
        len_total = 0
        xcge = (self.X1points+self.X2points)/2
        ycge = (self.Y1points+self.Y2points)/2 

        
        for i in range(n):    
            self.length[i] = math.sqrt((self.X2points[i]-self.X1points[i])**2 + (self.Y2points[i]-self.Y1points[i])**2)
            len_total += self.length[i]

        
        for i in range(n):
            self.xcg += xcge[i]*length[i]/len_total
            self.ycg += ycge[i]*length[i]/len_total
            
    def get_ik(self):
        
            iy_axis = length**3/12
            theta = np.zeros(n)
            
            self.ix = 0
            self.ix = 0
            self.ixy = 0
            
            for i in range(n):
                theta[i] = math.atan2(y2[i]-y1[i],x2[i]-x1[i])
                ixe = iy_axis * math.sin(theta[i])**2
                iye = iy_axis * math.cos(theta[i])**2
                ixye = iy_axis/2 * math.sin(2*theta[i])
                
                self.ix += ixe[i] + length[i]*(ycge[i]-ycg)**2
                self.ix += iye[i] + length[i]*(xcge[i]-xcg)**2
                self.ixy += ixye[i] + length[i]*(ycge[i]-ycg)*(xcge[i]-xcg)
            
            self.kb = self.ix * self.ix - self.ixy**2
            self.kx = self.ix/self.kb
            self.ky = self.ix/self.kb
            self.kxy = self.ixy/self.kb
            
            shape_slope = -2*self.ixy/(self.ix-self.ix)
            self.beta = 0.5 * math.atan2(-2*self.ixy,self.ix-self.ix)
    
    def get_end(self):
        
        is_open_end = False
       
        self.open_end = points[0,0:2]
        while not is_open_end:
            for i in range(points.shape[0]):
                for j in range(points.shape[0]):
                    if np.array_equal(points[i,0:2], points[j,0:2]):
                        self.open_end = points[i,0:2]
                        is_open_end = True
                    else:
                        is_open_end = False
                        
                if is_open_end:
                    break

      
flag = True
while flag:

 
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

    #                               Example     
# =============================================================================
#     n = 4 
#     shape = np.array([[0,1,0,0],[0.5,0.5,0,1],[1,1,0,1],[0.5,1.5,1,1]])
#     length = np.zeros(n)
# =============================================================================
    #  End of Example
    
    len_sum = 0
    x1 = shape[0:n,0]
    x2 = shape[0:n,1]
    y1 = shape[0:n,2]
    y2 = shape[0:n,3]
    
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
    
    
    ###############  TEST ##################
    
    is_open_end = False
    points = np.column_stack((np.concatenate((shape[:,0],shape[:,1])),np.concatenate((shape[:,2],shape[:,3]))))
    open_end = points[0,0:2]
    while not is_open_end:
        for i in range(points.shape[0]):
            for j in range(points.shape[0]):
                if np.array_equal(points[i,0:2], points[j,0:2]):
                    open_end = points[i,0:2]
                    is_open_end = True
                else:
                    is_open_end = False
                    
            if is_open_end:
                break
            
    #############   END OF TEST  #################
    
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
    plt.suptitle( f"Ix = {ix:.4f} d³t | Iy = {iy:.4f} d³t | Ixy = {ixy:.4f} d³t\n" f"kx = {kx:.4f}/(d³t) | ky = {ky:.4f}/(d³t) | kxy = {kxy:.4f}/(d³t)\n" f"β = {math.degrees(beta):.2f}° \n Xg = {xcg:.4f} | Yg = {ycg:.4f}", y=0.98,fontsize=10)
    print(f"Ix ={ix:.4f} d^3t ")
    print(f"Iy ={iy:.4f} d^3t ")
    print(f"Ixy ={ixy:.4f} d^3t ")
    print(f"kx = {kx:.4f}/(d^3 t)")
    print(f"ky = {ky:.4f}/(d^3 t)")
    print(f"kxy = {kxy:.4f}/(d^3 t)")
    print(f"beta = {math.degrees(beta):.4f}°")
    print()
    plt.show()
    flag = False

def shear_center(shape,kx,ky,kxy):
    is_open_end = False
    points = np.column_stack((np.concatenate((shape[:,0],shape[:,1])),np.concatenate((shape[:,2],shape[:,3]))))
    open_end = points[0,0:2]
    while not is_open_end:
        for i in range(points[0]):
            for j in range(points[0]):
                if points[i,0:2] != points[j,0:2]:
                    open_end = points[i,0:2]
                    is_open_end = True
                else:
                    is_open_end = False
                    
            if is_open_end:
                break

  
