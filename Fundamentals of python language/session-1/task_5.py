#task - 5: Python vs C vs Java Code Execution

# Script runs directly from top to bottom
a = 10
b = 20
print(a + b)

'''
C code is processed by a dedicated compiler (like GCC or Clang) that translates the entire source file directly into low-level binary machine instructions specific to the computer’s CPU and OS. There is no virtual machine layer at runtime, which makes execution significantly faster.

 Example:
 
#include <stdio.h>

int main() {
    int a = 10, b = 20;
    printf("%d\n", a + b);
    return 0;
}
    '''