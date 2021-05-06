// demo15_cpp_extension.C A terrible implementation of an exponential function.
double ext_power(double x, unsigned int a)
{
    double result = 1;
    for(unsigned int i = 0; i < a; i++)
    {
        result *= x;
    }
    return result;
}