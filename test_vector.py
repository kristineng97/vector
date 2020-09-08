import pytest
from vector import Vector3D

def test_vector_str():
    v = Vector3D(1,2,3)
    assert str(v) == "(1,2,3)"

def test_vector_repr():
    v = Vector3D(1,2,3)
    assert repr(v) == "Vector3D(1,2,3)"

def test_vector_add():
    v = Vector3D(1,2,3)
    u = Vector3D(1,1,1)
    w = u + v
    assert w.x == 2
    assert w.y == 3
    assert w.z == 4

def test_vector_add_eq():
    u = Vector3D(1,2,3)
    v = Vector3D(1,1,1)
    w = u + v
    assert w == Vector3D(2,3,4)

def test_vector_add_integer():
    v = Vector3D(1,2,3)
    u = 1
    w = v + u
    assert w == Vector3D(2,3,4)

def test_vector_dot_product():
    u = Vector3D(1,2,3)
    v = Vector3D(1,1,1)
    w = u * v
    assert isinstance(w, (int, float))
    assert abs(w - 6) < 1e-12

def test_vector_dot_product_mul():
    u = Vector3D(1,2,3)
    v = Vector3D(1,1,1)
    w = u.dot(v)
    assert isinstance(w, (int, float))
    assert abs(w - 6) < 1e-12

def test_vector_cross_product():
    u = Vector3D(1,0,0)
    v = Vector3D(0,1,0)
    w = u.cross(v)
    assert w == Vector3D(0, 0, 1)
