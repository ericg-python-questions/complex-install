import sys

from complex_install._hello import ffi, lib

def main():

    print( "Main" )
    print( f"Returned: { lib.hello() }" )

    return 0

if __name__ == "__main__":
    sys.exit( main() )  # pragma: no cover
