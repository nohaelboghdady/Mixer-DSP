#include<complex>
using namespace std;
#define DLLEXPORT extern "C" __declspec(dllexport)

extern "C"
{
 DLLEXPORT void fft(complex<double> *x, const int N) {
	if (N <= 1) {
		return;
	}

	    complex<double> odd[N/2];
	    complex<double> even[N/2];
	for (int i = 0; i < N / 2; i++) {
		even[i] = x[i*2];
		odd[i] = x[i*2+1];
	}

	fft(even, N/2);
	fft(odd, N/2);


	for (int k = 0; k < N / 2; k++) {
		complex<double> t = exp(complex<double>(0, -2 * M_PI * k / N)) *odd[k];
        x[k] = even[k] + t;
		x[N / 2 + k] = even[k] - t;
	}
}

DLLEXPORT void dft ( complex<double>sig_data[],complex<double>output[], int N)
{
     complex<double> intSum;

    for ( int k=0; k<N; k++)
    {
        intSum=  complex<double>(0,0);
        for ( int n=0; n<N; n++)
        {
            double real = cos (((2*M_PI)/N) *k * n);
            double imaginary = sin (((2*M_PI)/N) *k * n);
             complex<double> complex_fn  (real, -imaginary);
            intSum += sig_data[n] *complex_fn;
        }
        output[k]= intSum;
    }
    
}
}