class Vector3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x},{self.y},{self.z})"

    def __add__(self,other):
        if isinstance(other,(int, float)):
            return Vector3D(self.x + other, self.y + other, self.z = other)
        elif isinstance(other, Vector3D):
            return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            #raise TypeError(f"Cannot add Vector 3D to ...")

    def __eq__(self,other):
        """Return True if self == other, otherwise return False"""
        return self.x == other.x and self.y == other.y and self.z == other.z

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

if __name__ == "__main__":
    v = Vector3D(1,4,2)
    u = Vector3D(1,1,1)
    w = u + v
    w == Vector3D(2,5,)
