import sys
import random

N = 8
M = 1000000

if len(sys.argv) != 3:
    print("Usage: ", sys.argv[0], " matrixdim outerloopdim")
    exit(1)
else:
    N = int(sys.argv[1])
    M = int(sys.argv[2])


print("#define N ", N)
print("")
print("int main ()")
print("{")
print("  int k, i, j;")
print("")
print("  int a[",N,"][",N,"] = {") 
for i in range(N*N):
    print("                         %d,"%(
        random.randint(1,N+1)))
print("                         };")
print("")
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
