# include <stdio.h>
# include <math.h>
int main() {
	double N, J, H;
	int R = 1;
	scanf("%lf %lf %lf", &N, &J, &H);
	
	while (ceil(J/pow(2, R)) != ceil(H/pow(2, R))) {
		R++;
	}
	printf("%d", R);
	
}