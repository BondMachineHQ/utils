#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

#define N (3000)

double a[N][N]; 
double b[N][N];
double c[N][N];

int main()
{
  int k, i, j, ii, jj;
  double somma;
  float time1, time2, ttime1, ttime2, dub_time;

  ttime1 = clock();
  time1 = clock();
  for (j = 0; j < N; j++) {
    for (i = 0; i < N; i++) {
      a[j][i] = ((double)rand())/((double)RAND_MAX);
      b[j][i] = ((double)rand())/((double)RAND_MAX);
      c[j][i] = 0.0L;		
    }  
  }

  time2 = clock();
  dub_time = (time2 - time1)/(double) CLOCKS_PER_SEC;
  
  printf("Tempo impiegato per inizializzare %f s.\n", dub_time);

  time1 = clock();
  for (i=0; i<N; i++)
    for (j=0; j<N; j++)
      for (k=0; k<N; k++)
        c[i][j] = c[i][j] + a[i][k] * b[k][j];
  time2 = clock();
  dub_time = (time2 - time1)/(double) CLOCKS_PER_SEC;

  printf("Tempo per prodotto classico %f s.\n", dub_time);

  ttime2 = clock();
  dub_time = (ttime2 - ttime1)/(double) CLOCKS_PER_SEC;
  printf("Tempo totale %f s.\n\n", dub_time);
  printf("Mflops ----------------> %f \n", 
          2.0*N*N*N/(1000*1000*dub_time));

  /* semplice controllo */
  somma = 0.0L;
  for (i = 0; i < N; i++)
    for (j = 0; j < N; j++)
      somma = somma + c[i][j];
  printf("Controllo -------------> %f \n", somma);

  return EXIT_SUCCESS;  
}
