class Vector:
    """
    Clase que representa un vector n-dimensional con operaciones sobrecargadas.
    Implementado por: Steven Vizcaíno Cedeño
    """
    def __init__(self, elementos):
        """Inicializa el vector convirtiendo los elementos a float."""
        self.elementos = [float(x) for x in elementos]

    def __repr__(self):
        """Representación textual del vector."""
        return f"Vector({self.elementos})"

    def __mul__(self, other):
        """
        Sobrecarga del operador * (Producto de Hadamard o producto por escalar).
        """
        if isinstance(other, (int, float)):
            return Vector([a * other for a in self.elementos])
        return Vector([a * b for a, b in zip(self.elementos, other.elementos)])

    def __rmul__(self, other):
        """Permite la multiplicación por escalar por la izquierda (ej: 2 * v)."""
        return self.__mul__(other)

    def __matmul__(self, other):
        """
        Sobrecarga del operador @ (Producto escalar).
        """
        return sum(a * b for a, b in zip(self.elementos, other.elementos))

    def __floordiv__(self, other):
        """
        Sobrecarga del operador // (Componente paralela o tangencial).
        Calcula la proyección de 'self' sobre 'other'.
        """
        return other * ((self @ other) / (other @ other))

    def __mod__(self, other):
        """
        Sobrecarga del operador % (Componente normal o perpendicular).
        Calcula el resto de la proyección.
        """
        v_paralelo = self // other
        return Vector([a - b for a, b in zip(self.elementos, v_paralelo.elementos)])
