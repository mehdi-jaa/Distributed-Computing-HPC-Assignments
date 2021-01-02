import random
import numpy as np
from mpi4py import MPI
import time
COMM=MPI.COMM_WORLD
rank=COMM.Get_rank()
size=COMM.Get_size()
t = time.time()
nb=1000000
xmin=0
xmax=3*np.pi/2
nbc=int(nb/size)+(size==(rank+1))*(nb%size)
k=0
#print("I ",rank," will generate ", nbc)
for i in range(nbc):
	x=random.uniform(xmin,xmax) 
	k=k+np.cos(x)
k=k/nbc
inner_point=COMM.reduce(k,op=MPI.SUM ,root=0)

if rank==0:
	time=time.time()-t
	I=inner_point/size
	print("I= ",I, 'in ',time,' s')
	
 	
