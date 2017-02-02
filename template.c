#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {

  int numElement = 0, searchElement = 0;
  int element[100];
  int i = 0;

  if(argc < 2) {
    printf("Usage <num of elements> <elements> <search element> \n");
    return -1;
  }

  numElement = argv[1];
  searchElement = argv[argc];

  for(i = 0; i < numElement; i++){
    element[i] = argv[i+1];
    printf("%d\t",element[i]);
  }

  return 0;
}
