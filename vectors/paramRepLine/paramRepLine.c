// Include
#include <stdio.h>
#include <string.h>

// Structure
typedef struct
{
    float px;
    float py;
}point2D;

typedef struct 
{
    float dx;
    float dy;
}direction2D;

// Prototype
void param(point2D p, direction2D d);

// Main function
int main(int argc, char argv[])
{
    // Validate user inputs
    if (argc != 2)
    {
        printf("Usage: ./paramRepLine [check]\n");
        return 1;
    }
    // Get user inputs
    // Cardinal point on a line
    point2D point;
    printf("Enter the point on a line (x, y): ");
    scanf("%f %f", &point.px, &point.py);

    // Directional vector
    direction2D direction;
    printf("Enter the directional vector (x, y): ");
    scanf("%f %f", &direction.dx, &direction.dy);

    // Print results
    param(point, direction);
}

// Function
void param(point2D p, direction2D d)
{
    char cx[50], cy[50];
    sprintf(cx, "L = %.2f + t(%.2f)", p.px, d.dx);
    sprintf(cy, "L = %.2f + t(%2f)", p.py, d.dy);

    printf("%s \n %s \n",cx, cy);
}
// Parallel function
bool isParallel(direction2D d1, direction2D d2)
{
    float proportion1 = (d1.dx / d2.dx);
    float proportion2 = (d1.dy / d2.dy);

    if (proportion1 == proportion2)
    {
        return true;
    }
    return false;
}