#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float form(const float a, const float b, const float x, const float y)
{
  return ((a - x) * (b - y)) / ((5 * a - 150) * (5 * b - 150));
}

int main(const int ac, const char * const *av)
{
  if (ac != 3)
    {
      fprintf(stderr, "Usage: ./202invendus a b\n");
      return 1;
    }
  const int a = atoi(av[1]);
  const int b = atoi(av[2]);
  if (a < 51 || b < 51)
    {
      fprintf(stderr, "Error invalide number\n");
      return 1;
    }
  float **res;

  res = malloc(sizeof(float *)*6);
  for (register int i = 0;i<6;++i)
    res[i] = malloc(sizeof(float)*6);
  printf("\t\tX=10\tX=20\tX=30\tX=40\tX=50\tloi de Y\n");
  for (register char y = 10; y < 51; y+=10)
    {
      printf("Y=%d\t\t", (int)y);
      for (register char x = 10; x < 51; x+=10)
	{
	  res[y/10-1][x/10-1] = form((float)a, b, (float)x, (float)y);
	  printf("%.3f\t", res[y/10-1][x/10-1]);
	}
      res[y/10-1][5] = res[y/10-1][0] + res[y/10-1][1] + res[y/10-1][2] + res[y/10-1][3] + res[y/10-1][4];
      printf("%.3f\n", res[y/10-1][5]);
    }
  printf("loi de X\t");
  for (register int i = 0;i<5;++i)
    {
      res[5][i] = res[0][i] + res[1][i] + res[2][i] + res[3][i] + res[4][i];
      printf("%.3f\t", res[5][i]);
    }
  float *z = malloc(sizeof(float) * 9);
  z[0] = res[0][0];
  z[1] = res[0][1] + res[1][0];
  z[2] = res[0][2] + res[2][0] + res[1][1];
  z[3] = res[3][0] + res[0][3] + res[1][2] + res[2][1];
  z[4] = res[4][0] + res[0][4] + res[3][1] + res[1][3] + res[2][2];//HO la jolie pyramide :)
  z[5] = res[1][4] + res[4][1] + res[2][3] + res[3][2];
  z[6] = res[2][4] + res[4][2] + res[3][3];
  z[7] = res[3][4] + res[4][3];
  z[8] = res[4][4];
  printf("1\n\n");
  printf("z\t\t20\t30\t40\t50\t60\t70\t80\t90\t100\ttotal\n");
  printf("p(Z=z)\t\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\t1\n\n", z[0],z[1],z[2],z[3],z[4],z[5],z[6],z[7],z[8]);
  const float ex = 10*res[5][0] + 20*res[5][1] + 30*res[5][2] + 40*res[5][3] + 50*res[5][4];
  const float ey = 10*res[0][5] + 20*res[1][5] + 30*res[2][5] + 40*res[3][5] + 50*res[4][5];
  const float ez = 20*z[0] + 30*z[1] + 40*z[2] + 50*z[3] + 60*z[4] + 70*z[5] + 80*z[6] + 90*z[7] + 100*z[8];
  printf("espérance de X:\t\t%.3f\n", ex);
  const float vx = 100*res[5][0] + 400*res[5][1] + 900*res[5][2] + 1600*res[5][3] + 2500*res[5][4] - (ex*ex);
  printf("variance de X:\t\t%.3f\n", vx);
  printf("écart type de X:\t%.3f\n", sqrtf(vx));
  printf("espérance de Y:\t\t%.3f\n", ey);
  const float vy = 100*res[0][5] + 400*res[1][5] + 900*res[2][5] + 1600*res[3][5] + 2500*res[4][5] - (ey*ey);
  printf("variance de Y:\t\t%.3f\n", vy);
  printf("écart type de Y:\t%.3f\n", sqrtf(vy));
  printf("espérance de Z:\t\t%.3f\n", ez);
  const float vz = 400*z[0] + 900*z[1] + 1600*z[2] + 2500*z[3] + 3600*z[4] + 4900*z[5] + 6400*z[6] + 8100*z[7] + 10000*z[8] - (ez*ez);
  printf("variance de Z:\t\t%.3f\n", vz);
  printf("écart type de Z:\t%.3f\n", sqrtf(vz));
  return 0;
}
