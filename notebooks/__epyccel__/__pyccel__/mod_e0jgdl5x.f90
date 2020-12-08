module mod_e0jgdl5x

use ISO_C_BINDING

implicit none

contains

!........................................
function solve_1d_linearconv_pyccel(u, un, nt, nx, dt, dx, c) result( &
      Out_0001)

  implicit none

  integer(C_LONG_LONG) :: Out_0001
  real(C_DOUBLE), intent(inout) :: u(0:)
  real(C_DOUBLE), intent(inout) :: un(0:)
  integer(C_LONG_LONG), value :: nt
  integer(C_LONG_LONG), value :: nx
  real(C_DOUBLE), value :: dt
  real(C_DOUBLE), value :: dx
  real(C_DOUBLE), value :: c
  integer(C_LONG_LONG) :: t
  integer(C_LONG_LONG) :: k
  integer(C_LONG_LONG) :: i

  do t = 0_C_LONG_LONG, nt-1_C_LONG_LONG, 1_C_LONG_LONG
    do k = 0_C_LONG_LONG, nx-1_C_LONG_LONG, 1_C_LONG_LONG
      un(k) = u(k)
    end do
    !un=u.copy()
    do i = 1_C_LONG_LONG, nx-1_C_LONG_LONG, 1_C_LONG_LONG
      u(i) = un(i) - c * dt * (un(i) - un(i - 1_C_LONG_LONG)) / dx
    end do
  end do
  Out_0001 = 0_C_LONG_LONG
  return

end function solve_1d_linearconv_pyccel
!........................................

end module mod_e0jgdl5x
