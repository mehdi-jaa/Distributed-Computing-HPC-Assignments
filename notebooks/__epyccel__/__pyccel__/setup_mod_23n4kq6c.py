from setuptools import Extension, setup
import numpy

extension_mod = Extension("mod_23n4kq6c",
		[ r'mod_23n4kq6c_wrapper.c' ],
		extra_objects = [r'/home/mehdi_jaa/github/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__/bind_c_mod_23n4kq6c.o',
				r'/home/mehdi_jaa/github/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__/mod_23n4kq6c.o'],
		include_dirs = [r'/home/mehdi_jaa/github/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__', numpy.get_include()],
		libraries = [r'gfortran'],
		library_dirs = [r'/usr/lib/gcc/x86_64-linux-gnu/9'],
		extra_link_args = [r'-O3',
				r'-fPIC',
				r'-I"/home/mehdi_jaa/github/Distributed-Computing-HPC-Assignments/notebooks/__epyccel__/__pyccel__"'])

setup(name = "mod_23n4kq6c", ext_modules=[extension_mod])