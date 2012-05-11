#!/usr/bin/python
import tpypp.preprocessor as preprocessor
import sys

helpstring = \
'''usage: tpypp inputfile [outputfile]
tiny python preprocessor
(c) 2012 Isaac Evans

example macros:
#define TEMP r6
#define SWAP(A, B) mov TEMP, A\\n mov B, A\\n mov TEMP, B\\n
#include "../tests.asm"
#ifdef TEMP
SWAP(TEMP, r2)
#else
SWAP(r5, r2)
#endif'''

pass_verbose = False

if not 2 <= len(sys.argv) <= 4:
    print helpstring
    sys.exit(-1)
if len(sys.argv) == 3 and sys.argv[1] == sys.argv[2]:
    print 'input file cannot be same as output file'
    sys.exit(-1)
if (len(sys.argv) == 3 and sys.argv[2] == '--v') or (len(sys.argv) == 4 and sys.argv[3] == '--v'):
    pass_verbose = True

preprocessor.preprocessFile(sys.argv[1], None if len(sys.argv) != 3 else sys.argv[2], pass_verbose)
