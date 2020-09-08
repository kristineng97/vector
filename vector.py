class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x},{self.y},{self.z})"

    # def __radd__():
    """
    method for adding number with string (?)
    """

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Vector3D(self.x + other, self.y + other, self.z + other)
        elif isinstance(other, Vector3D):
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError(f"Cannot add Vector 3D to object of {type(other)}")

    def __eq__(self, other):
        """Return True if self == other, otherwise return False"""
        return self.x == other.x and self.y == other.y and self.z == other.z

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __mul__(self, other):
        """ The det dot product between this vector
        an another vector

        .. math:

            \cdot v = u_1 v_1 + u_2 v_2 + u_3 v_3

        Parameters
        __________
        other: Vector3D
            The vector to be dotted with

        Returns
        _______
        float
            The dot product
        """
        return self.dot(other)

    def cross(self, other):
        """Take the cross product between this vector
        and the other vector

        Parameters
        __________
        other: Vector3D
            The ector to be crossed with

        Returns
        _______
        Vector3D
            The cross product
        """
        return Vector3D(self.y * other.z - self.z * other.y,
        self.z *other.x - self.x * other.z,
        self.x * other.y - self.y * other.x)



if __name__ == "__main__":
    v = Vector3D(1, 4, 2)
    u = Vector3D(1, 1, 1)
    w = u + v
    w == Vector3D(2, 5, 3)
