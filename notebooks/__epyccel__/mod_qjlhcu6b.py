@types('float[:]','float[:]','int','int','float','float')
def solve_1d_nonlinearconv_pyccel(u, un, nt, nx, dt, dx):
    for t in range(nt):
        for k in range(nx): un[k]=u[k]
        for i in range(1,nx):
            u[i]=un[i]-un[i]*dt*(un[i]-un[i-1])/dx
    return 0
