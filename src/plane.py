class Plane:
    # Build the constructor
    def __init__(self, a, b, c, d):
        """
        Represent a plane in 3-dimension space:

        ax + by + cz + d = 0
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def evaluate(self, point):
        """
        Evaluate: f(x, y, z) = ax + by + cz + b
        """
        x, y, z = point
        return self.a*x + self.b*y + self.c*z + self.d
    def classify(self, point):
        """
        Determine which side of the plane the point lies to 
        """
        value = self.evaluate(point)
        if value > 0:
            return "Normal"
        elif value < 0:
            return "Suspicious"
        else:
            return "On the plane"
