A Vector has both magnitude(how big it is) and direction(where it points).

If a vector has magnitude **M** and direction as **$\theta$** then, $x = M \space cos \space (\theta)$ and $y = M \space sin \space (\theta)$. Example: A vector **v** has a magnitude of 10 with direction $0\degree$. This means pointing direction along x-axis is: $$x = 10\space cos(0\degree) = 10$$
$$y = 10\space sin(0\degree) = 0 $$
Thus, 
$$\bold{v} = (10, 0)$$

In C programming, $sin()$ and $cons()$ only accepts radiance. Radiance has the following formula:
$$Radiance = degree \space \times \frac{\pi}{180}$$

Pseudo code to use:

START

INPUT magnitude1, direction1_in_degrees
INPUT magnitude2, direction2_in_degrees

CONVERT direction1 to radians
    direction1_rad = direction1_in_degrees × π / 180

CONVERT direction2 to radians
    direction2_rad = direction2_in_degrees × π / 180

COMPUTE components of vector 1
    x1 = magnitude1 × cos(direction1_rad)
    y1 = magnitude1 × sin(direction1_rad)

COMPUTE components of vector 2
    x2 = magnitude2 × cos(direction2_rad)
    y2 = magnitude2 × sin(direction2_rad)

ADD components to get resultant
    Rx = x1 + x2
    Ry = y1 + y2

COMPUTE magnitude of resultant
    R_magnitude = sqrt(Rx² + Ry²)

COMPUTE direction of resultant (in radians)
    R_direction_rad = atan2(Ry, Rx)

CONVERT resultant direction to degrees
    R_direction_deg = R_direction_rad × 180 / π

OUTPUT Rx, Ry
OUTPUT R_magnitude, R_direction_deg

END
