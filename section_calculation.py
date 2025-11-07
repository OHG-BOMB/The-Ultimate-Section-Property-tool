import math
import numpy as np
import matplotlib.pyplot as plt

# comment
class section:
        
    def __init__(self,n,X1,X2,Y1,Y2,t,nb,XB,YB,B):
      self.n = n 
      self.web = np.full((n,4),np.nan)
      self.X1points = X1
      self.X2points = X2
      self.Y1points = Y1
      self.Y2points = Y2
      self.nb = nb
      self.xboom = XB
      self.yboom = YB
      self.B = B
      self.b_area_total = np.sum(self.B)
      self.Xpoints = np.concatenate((self.X1points,self.X2points))
      self.Ypoints = np.concatenate((self.Y1points,self.Y2points))
      self.points = np.column_stack((self.Xpoints,self.Ypoints))
      self.get_CG()
      self.get_ik()
      self.get_end()
      self.get_principal_axes()
      
    def get_CG(self):
        
        self.length = np.full((self.n,1),np.nan)
        self.xcgw = 0
        self.ycgw = 0
        self.xcgb = 0
        self.ycgb = 0
        w_len_total = 0
        self.xcge = (self.X1points+self.X2points)/2
        self.ycge = (self.Y1points+self.Y2points)/2 

        
        for i in range(self.n):    
            self.length[i] = math.sqrt((self.X2points[i]-self.X1points[i])**2 + (self.Y2points[i]-self.Y1points[i])**2)
            w_len_total += self.length[i]

        
        for i in range(self.n):
            self.xcgw += (self.xcge[i]*self.length[i]/w_len_total).item()
            self.ycgw += (self.ycge[i]*self.length[i]/w_len_total).item()
            

        if self.b_area_total != 0:    
            for i in range(self.nb):
                self.xcgb += self.xboom[i] * self.B[i]/ self.b_area_total
                self.ycgb += self.yboom[i] * self.B[i]/ self.b_area_total
        
        self.xcg = self.xcgb + self.xcgw
        self.ycg = self.ycgb + self.ycgw
        
    def get_ik(self):
        
            iy_axis = self.length**3/12
            theta = np.zeros(self.n)
            
            self.ixw = 0
            self.iyw = 0
            self.ixyw = 0


            
            for i in range(self.n):
                theta[i] = math.atan2(self.Y2points[i]-self.Y1points[i],self.X2points[i]-self.X1points[i])
                ixe = iy_axis * math.sin(theta[i])**2
                iye = iy_axis * math.cos(theta[i])**2
                ixye = iy_axis/2 * math.sin(2*theta[i])
                
                self.ixw += (ixe[i] + self.length[i]*(self.ycge[i]-self.ycg)**2).item()
                self.iyw += (iye[i] + self.length[i]*(self.xcge[i]-self.xcg)**2).item()
                self.ixyw += (ixye[i] + self.length[i]*(self.ycge[i]-self.ycg)*(self.xcge[i]-self.xcg)).item()
                
            self.ixb = np.sum(self.B * (self.ycgb - self.ycg)**2)
            self.iyb = np.sum(self.B * (self.xcgb - self.xcg)**2)
            self.ixyb = np.sum(self.B * (self.ycgb - self.ycg)*(self.xcgb - self.xcg))
            
            self.ix = self.ixb+self.ixw
            self.iy = self.iyb+self.iyw
            self.ixy = self.ixyb+self.ixyw
            
            self.kb = self.ix * self.iy - self.ixy**2
            self.kx = self.ix/self.kb
            self.ky = self.iy/self.kb
            self.kxy = self.ixy/self.kb
            
            self.slope = -2*self.ixy/(self.ix-self.iy)
            self.beta = 0.5 * math.atan2(-2*self.ixy,self.ix-self.iy)
            
    def get_principal_axes(self):
        
            self.p_axes_scale = 0.1
            self.p_axes_minx = np.minimum(np.min(self.X1points),np.min(self.X2points))
            self.p_axes_maxx = np.maximum(np.max(self.X1points),np.max(self.X2points))
    
    def get_end(self):
        
        is_open_end = False
       
        self.open_end = self.points[0,0:2]
        while not is_open_end:
            for i in range(self.points.shape[0]):
                for j in range(self.points.shape[0]):
                    if np.array_equal(self.points[i,0:2], self.points[j,0:2]):
                        self.open_end = self.points[i,0:2]
                        is_open_end = True
                    else:
                        is_open_end = False
                        
                if is_open_end:
                    break

      

    # =============================================================================
    # 
    # def shear_center(self):
    #   TODO
    # =============================================================================

      

n_b = 0
n = 0
thickness = np.ones(n)

# ------------------------------------Uncomment if testing a section-----------------------------------------
# while(True):
#     is_boom  = input("Does the section contain booms? [Y], [N] ").lower()
    
#     if(is_boom == 'y'):
#         n_b = int(input("Enter Number of booms: "))
#         print()
#         boom = np.zeros((n_b,3))

#         for i in range(n_b):
#              print(f"################# Boom {i+1} #################")
#              print()
#              boom[i,0] = float(input("x: "))
#              boom[i,1] = float(input("y: "))
#              boom[i,2] = float(input("A: "))
#              print("------------------------------------------------------------")
#              print()
#         break
#     elif(is_boom == 'n'):
#         break
    
# while(True):
#     is_web  = input("Does the section contain webs? [Y], [N] ").lower()
#     if(is_web == 'y'):
#         while(True):
#             is_t_const = input("Does the section contain webs? [Y], [N] ").lower()
#             if(is_t_const == 'y'):
#                 t_const = True
#                 break
#             elif(is_t_const == 'n'):
#                 t_const = False
#                 break
        
#         n = int(input("Enter Number of webs: "))
#         print()
#         shape = np.zeros((n,4))
#         if(t_const):
#             thickness = np.ones(n)
#         else:
#             thickness = np.zeros(n)

#         for i in range(n):
#              print(f"################# Web {i+1} #################")
#              print()
#              shape[i,0] = float(input("x1: "))
#              shape[i,2] = float(input("y1: "))
#              print()
#              shape[i,1] = float(input("x2: "))
#              shape[i,3] = float(input("y2: "))
#              if (not t_const):
#                  thickness[i] = input("t: ")
#              print("------------------------------------------------------------")
#              print()
             
#         break
    
#     elif(is_web == 'n'):
#         break
    
# -----------------------------------------END Of CLI------------------------------------------------
       


  #                -----  Example (comment if testing a section) ----   
n = 4 
shape = np.array([[0,1,0,0],[0.5,0.5,0,1],[1,1,0,1],[0.5,1.5,1,1]])
boom = np.zeros((1,3))

length = np.zeros(n)
    
# ----------------------------------------------------------------------------- 




# Initializing
shape = section(n,shape[:,0],shape[:,1],shape[:,2],shape[:,3],thickness[:],n_b,boom[:,0],boom[:,1],boom[:,2])



################  Plotting

# Plotting lines

for i in range(n):
    
    plt.plot((shape.X1points,shape.X2points),(shape.Y1points,shape.Y2points))
    
    
    
# Plotting principal axes

xp = np.linspace(shape.p_axes_scale*shape.xcg - shape.p_axes_minx ,shape.p_axes_maxx-shape.p_axes_scale*shape.xcg,30)
yp1 = shape.slope* xp - shape.slope *shape.xcg + shape.ycg
yp2 =  -xp/shape.slope + 1/shape.slope *shape.xcg + shape.ycg
plt.plot(xp,yp1,'--')



if shape.slope == 0:
    plt.plot([shape.xcg, shape.xcg],
    np.linspace(1.2*np.minimum(np.min(shape.X1points), np.min(shape.X1points)),1.2*np.maximum(np.max(shape.X1points), np.max(shape.X1points)), 2), '--')

else:
    plt.plot(xp,yp2,'--')
    
for i in range(n_b):
    plt.plot(shape.xboom, shape.yboom )
    
    
    
plt.plot(shape.xcg,shape.ycg,'o')
plt.axis('equal')


plt.suptitle( f"Ix = {shape.ix:.4f} d³t | Iy = {shape.iy:.4f} d³t | Ixy = {shape.ixy:.4f} d³t\n" f"kx = {shape.kx:.4f}/(d³t) | ky = {shape.ky:.4f}/(d³t) | kxy = {shape.kxy:.4f}/(d³t)\n" f"β = {math.degrees(shape.beta):.2f}° \n Xg = {shape.xcg:.4f} | Yg = {shape.ycg:.4f}", y=0.98,fontsize=10)
print(f"Ix ={shape.ix:.4f} d^3t ")
print(f"Iy ={shape.iy:.4f} d^3t ")
print(f"Ixy ={shape.ixy:.4f} d^3t ")
print(f"kx = {shape.kx:.4f}/(d^3 t)")
print(f"ky = {shape.ky:.4f}/(d^3 t)")
print(f"kxy = {shape.kxy:.4f}/(d^3 t)")
print(f"beta = {math.degrees(shape.beta):.4f}°")
print()
plt.show()


# =============================================================================
# 
# def shear_center(shape,kx,ky,kxy):
#     is_open_end = False
#     points = np.column_stack((np.concatenate((shape[:,0],shape[:,1])),np.concatenate((shape[:,2],shape[:,3]))))
#     open_end = points[0,0:2]
#     while not is_open_end:
#         for i in range(points[0]):
#             for j in range(points[0]):
#                 if points[i,0:2] != points[j,0:2]:
#                     open_end = points[i,0:2]
#                     is_open_end = True
#                 else:
#                     is_open_end = False
#                     
#             if is_open_end:
#                 break
# =============================================================================

  
