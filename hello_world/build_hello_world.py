from cffi import FFI

try:

    ffibuilder = FFI()

    ffibuilder.cdef( "int hello( void );" )

    c_header_source = """
        #include "hello.h"
    """

    pkgconfig_libs = ['openssl']

    ffibuilder.set_source_pkgconfig("complex_install._hello",
                                    pkgconfig_libs,
                                    c_header_source,
                                    include_dirs=['hello_world'],
                                    sources=['hello_world/hello.c'],
                                    libraries=['crypto'])

except:

    ffibuilder.cdef( "" )
    ffibuilder.set_source( "complex_install._hello", "" )

    print( "I failed to build" )



if __name__ == "__main__":
        ffibuilder.compile( verbose = True )
