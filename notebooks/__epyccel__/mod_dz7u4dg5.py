@types('float[:,:]','float[:,:]','int','int','float','float','float')
def solve_1d_linearconv_pyccel(u, un, nt, nx, dt, dx, c):
    for i in range(nt):
        un=u.copy()
        for i in range(1,nx):
            u[i]=un[i]-c*dt*(un[i]-un[i-1])/dx
    return 0
