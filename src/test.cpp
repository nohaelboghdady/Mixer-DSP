#include<complex>
#include<iostream>
using namespace std;

extern "C"
{

void fft(std::complex<double> input_output_signal[] , int size)
{
	const size_t N = size;
	if (N <= 1){
		return;}
	int M = size/2;
	
	std::complex<double>* even = new std::complex<double>[M];
	std::complex<double>* odd = new std::complex<double>[M];

	for(int i = 0; i < M; i++)
	{
		even[i] = input_output_signal[2*i];
		odd [i] = input_output_signal[2*i + 1];
	}

	// conquer
	fft(even, M);
	fft(odd, M);

	// combine
	for (size_t k = 0; k < N/2; ++k)
	{
		std::complex<double> t = std::polar(1.0, -2 * M_PI * k / N) * odd[k];
		input_output_signal[k] = even[k] + t;
		input_output_signal[k+N/2] = even[k] - t;
	}
}

void dft ( complex<double>sig_data[],complex<double>output[], int N)
{
     complex<double> intSum;
   for ( int k=0; k<N; k++)
    {
        intSum=  complex<double>(0,0);
        for ( int n=0; n<N; n++)
        {
			double angle = 2 * M_PI * n * k / N;
            double real = cos (angle);
            double imaginary = sin (angle);
            complex<double> complex_fn  (real, -imaginary);
            intSum += sig_data[n] *complex_fn;
        }
        output[k]= intSum;
    }
    
}
}