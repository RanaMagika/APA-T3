"""
Tarea 3 de APA: Multiplicación de vectores y ortogonalidad
Alumno: Steven Daniel Vizcaino Cedeño

Este módulo implementa la clase Vector con operaciones de producto de Hadamard,
producto escalar y descomposición en componentes normal y paralela.
"""

class Vector:
    def __init__(self, elementos):
        """Inicializa el vector con una lista de elementos (convertidos a float)."""
        self.elementos = [float(x) for x in elementos]

    def __repr__(self):
        """Representación visual del vector."""
        return f"Vector({self.elementos})"

    def __mul__(self, other):
        """
        Sobrecarga de * (Hadamard o Escalar).
        >>> v1 = Vector([1, 2, 3])
        >>> v1 * 2
        Vector([2.0, 4.0, 6.0])
        >>> v2 = Vector([4, 5, 6])
        >>> v1 * v2
        Vector([4.0, 10.0, 18.0])
        """
        if isinstance(other, (int, float)):
            return Vector([a * other for a in self.elementos])
        return Vector([a * b for a, b in zip(self.elementos, other.elementos)])

    def __rmul__(self, other):
        """Multiplicación por escalar por la izquierda (n * v)."""
        return self.__mul__(other)

    def __matmul__(self, other):
        """
        Sobrecarga de @ (Producto escalar).
        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> v1 @ v2
        32.0
        """
        return sum(a * b for a, b in zip(self.elementos, other.elementos))

    def __floordiv__(self, other):
        """
        Sobrecarga de // (Componente paralela).
        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1, 0.5])
        >>> v1 // v2
        Vector([1.0, 2.0, 1.0])
        """
        factor = (self @ other) / (other @ other)
        return other * factor

    def __mod__(self, other):
        """
        Sobrecarga de % (Componente normal).
        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1, 0.5])
        >>> v1 % v2
        Vector([1.0, -1.0, 1.0])
        """
        v_paralelo = self // other
        return Vector([a - b for a, b in zip(self.elementos, v_paralelo.elementos)])

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)