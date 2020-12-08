@types('float[:]','float[:]','int','int','float','float','float')
def solve_1d_diff_pyccel(u, un, nt, nx, dt, dx, nu):
    for n in range(nt):
        for k in range(nx-1): un[k]=u[k]
        for i in range(1,nx-1):
            u[i]=un[i]+nu*dt*(un[i-1]+un[i+1]-2*un[i])/(dx**2)
    
    return 0
