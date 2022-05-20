import sys
import random

N = 8
M = 1000000
uint = True

if len(sys.argv) != 3:
    print("Usage: ", sys.argv[0], " matrixdim outerloopdim")
    exit(1)
else:
    N = int(sys.argv[1])
    M = int(sys.argv[2])

if uint:
    print("#include <stdint.h>")

print("#define N ", N)
print("")
print("int main ()")
print("{")
print("  int k, i, j;")
print("")
if uint:
    print("  uint8_t a[",N,"][",N,"] = {")
    for i in range(N*N):
        print("                         %d,"%(
            random.randint(1,11)))
else:
    print("  int a[",N,"][",N,"] = {") 
    for i in range(N*N):
        print("                         %d,"%(
            random.randint(1,N+1)))

print("                         };")
print("")
if uint:
    print("  uint8_t b[",N,"] = {")
    for i in range(N):
        print("                 %d,"%(
            random.randint(1,11)))
else:
    print("  int b[",N,"] = {")
    for i in range(N):
        print("                 %d,"%(
            random.randint(1,N+1)))

print("                  };")
print("  int c[",N,"];")
print("")
print("  for(k=0; k<",M,"; ++k)")
print("  {")
print("    for(i=0; i<",N,"; ++i)")
print("    {")
print("      c[i] = 0;")
print("      for(j=0; j<",N,"; ++j)")
print("        c[i] += b[j] * a[j][i];")
print("    }")
print("  }")
print("  return 0;")
print("}")


if uint:
    print("#include <stdint.h>", file=sys.stderr)

print("#define N ", N, file=sys.stderr)
print("", file=sys.stderr)
print("int main ()", file=sys.stderr)
print("{", file=sys.stderr)
print("  int k, i, j;", file=sys.stderr)
print("", file=sys.stderr)
if uint:
    print("  uint8_t a[",N,"][",N,"] = {", file=sys.stderr)
    for i in range(N*N):
        print("                         %d,"%(
            random.randint(1,11)), file=sys.stderr)
else:
    print("  int a[",N,"][",N,"] = {", file=sys.stderr) 
    for i in range(N*N):
        print("                         %d,"%(
            random.randint(1,N+1)), file=sys.stderr)

print("                         };", file=sys.stderr)
print("", file=sys.stderr)
if uint:
    print("  uint8_t b[",N,"] = {", file=sys.stderr)
    for i in range(N):
        print("                 %d,"%(
            random.randint(1,11)), file=sys.stderr)
else:
    print("  int b[",N,"] = {", file=sys.stderr)
    for i in range(N):
        print("                 %d,"%(
            random.randint(1,N+1)), file=sys.stderr)

print("                  };", file=sys.stderr)
print("  int c[",N,"];", file=sys.stderr)
print("", file=sys.stderr)
print("  for(k=0; k<",M,"; ++k)", file=sys.stderr)
print("  {", file=sys.stderr)
print("    for(i=0; i<",N,"; ++i)", file=sys.stderr)
print("    {", file=sys.stderr)
print("      c[i] = 0;", file=sys.stderr)
print("    }", file=sys.stderr)
print("  }", file=sys.stderr)
print("  return 0;", file=sys.stderr)
print("}", file=sys.stderr)
