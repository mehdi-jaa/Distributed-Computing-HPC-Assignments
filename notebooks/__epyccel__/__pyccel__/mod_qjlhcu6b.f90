module mod_qjlhcu6b

use ISO_C_BINDING

implicit none

contains

!........................................
function solve_1d_nonlinearconv_pyccel(u, un, nt, nx, dt, dx) result( &
      Out_0001)

  implicit none

  integer(C_LONG_LONG) :: Out_0001
  real(C_DOUBLE), intent(inout) :: u(0:)
  real(C_DOUBLE), intent(inout) :: un(0:)
  integer(C_LONG_LONG), value :: nt
  integer(C_LONG_LONG), value :: nx
  real(C_DOUBLE), value :: dt
  real(C_DOUBLE), value :: dx
  integer(C_LONG_LONG) :: t
  integer(C_LONG_LONG) :: k
  integer(C_LONG_LONG) :: i

  do t = 0_C_LONG_LONG, nt-1_C_LONG_LONG, 1_C_LONG_LONG
    do k = 0_C_LONG_LONG, nx-1_C_LONG_LONG, 1_C_LONG_LONG
      un(k) = u(k)
    end do
    do i = 1_C_LONG_LONG, nx-1_C_LONG_LONG, 1_C_LONG_LONG
      u(i) = un(i) - un(i) * dt * (un(i) - un(i - 1_C_LONG_LONG)) / dx
    end do
  end do
  Out_0001 = 0_C_LONG_LONG
  return

end function solve_1d_nonlinearconv_pyccel
!........................................

end module mod_qjlhcu6b
