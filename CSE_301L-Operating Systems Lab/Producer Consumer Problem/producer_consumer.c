#include<stdio.h>
#include<stdlib.h>

int mutex = 1, full = 0, empty = 10, x = 0;

void producer() {
  --mutex;
  ++full;
  --empty;
  x++;
  printf("Producer produces item: %d\n", x);
}

void consumer() {
  --mutex;
  --full;
  ++empty;
  printf("Consumer consumes item: %d\n", x);
  x--;
}

int main() {
  int n, i;
  printf("1. Consumer\n"
         "2. Producer\n"
         "3. Exit\n"
      );

  for (i=0;i>=0;i++){
    printf("\nEnter your choice: ");
    scanf("%d", &n);

    switch(n) {
      case 1:
        if((mutex == 1) && (empty!=0)) {
          producer();
        }
        else {
          printf("Buffer is full!\n");
        }
      case 2:
        if((mutex == 1) && (full != 0)) {
          consumer();
        }
        else {
          printf("Buffer is empty\n");
        }
      case 3: 
        exit(0);
        break;
    }
  }
}
