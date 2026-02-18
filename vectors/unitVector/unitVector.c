// Includes 
#include <stdio.h>
#include <math.h>

// Create unit datastructure
    typedef struct
    {
        double mag;
        double theta;
    }vector;
    typedef struct
    {
       double Ux;
       double Uy; 
    }vector2D;

 // Function Prototypes
double degree_to_radian(double theta);
vector2D convert_to_cartesian(double radiant);   

// Main function
int main(void)
{
    // Get user input
    vector vectors[2];
    for (int i = 0; i < 2; i++)
    {
        printf("Enter Magnitude %i: ", i + 1);
        scanf("%lf", &vectors[i].mag);
        printf("Enter theta %i: ", i + 1);
        scanf("%lf", &vectors[i].theta);
    }
    // Compute radiance
    double r1 = degree_to_radian(vectors[0].theta);
    double r2 = degree_to_radian(vectors[1].theta);

    // Convert polar to cartesian components
    vector2D U = convert_to_cartesian(r1);
    vector2D V = convert_to_cartesian(r2);

    // Normalizing and computing the sum
    double R1 = (vectors[0].mag * U.Ux) + (vectors[1].mag * V.Ux);
    double R2 = (vectors[0].mag * U.Uy) + (vectors[1].mag * V.Uy);

    // Print results
    printf("R1: %.4f and R2: %.4f\n", R1, R2);

    // Return 
    return 0;
}
// Conver theta to radiance
double degree_to_radian(double theta)
{
    return theta * (M_PI / 180);
}
// Convert polar to cartesian components
vector2D convert_to_cartesian(double radiant)
{
    vector2D v;
    v.Ux = cos(radiant);
    v.Uy = sin(radiant);
    return v;
}