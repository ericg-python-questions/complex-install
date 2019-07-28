from cffi import FFI

ffibuilder = FFI()

ffibuilder.cdef( "int hello( void );" )
ffibuilder.set_source( "complex_install._hello",  # name of the output C extension
"""
    #include "hello.h"
""",
    include_dirs = [ 'hello_world' ],
    sources   = [ 'hello_world/hello.c' ],   # includes pi.c as additional sources
    libraries = [] )    # on Unix, link with the math library

if __name__ == "__main__":
    ffibuilder.compile( verbose = True )
