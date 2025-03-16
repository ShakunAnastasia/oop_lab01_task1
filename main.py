import math

class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        if not self._is_valid():
            return 0  # некоректний трикутник
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def _is_valid(self):
        return (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.a + self.c > self.b)

    def __str__(self):
        return f"Triangle({self.a}, {self.b}, {self.c})"

class Rectangle:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    def __str__(self):
        return f"Rectangle({self.a}, {self.b})"

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d
        self.h = self._calculate_height()

    def _calculate_height(self):
        try:
            s = (self.c + self.d - self.a + self.b) / 2
            height = 2 * math.sqrt(s * (s - self.c) * (s - self.d) * (s - (self.a - self.b))) / abs(self.a - self.b)
            return height if height > 0 else 0
        except (ValueError, ZeroDivisionError):
            return 0  # некоректна трапеція

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        return (self.a + self.b) * self.h / 2

    def __str__(self):
        return f"Trapeze({self.a}, {self.b}, {self.c}, {self.d})"

class Parallelogram:
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.h

    def __str__(self):
        return f"Parallelogram({self.a}, {self.b}, {self.h})"

class Circle:
    def __init__(self, r):
        self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * self.r ** 2

    def __str__(self):
        return f"Circle({self.r})"

def parse_shape(line):
    parts = line.strip().split()
    shape_type = parts[0]
    params = [float(x) for x in parts[1:]]
    
    if shape_type == "Triangle":
        return Triangle(*params)
    elif shape_type == "Rectangle":
        return Rectangle(*params)
    elif shape_type == "Trapeze":
        return Trapeze(*params)
    elif shape_type == "Parallelogram":
        return Parallelogram(*params)
    elif shape_type == "Circle":
        return Circle(*params)

def main():
    shapes = []
    for filename in ["input01.txt", "input02.txt", "input03.txt"]:
        try:
            with open(filename, "r") as f:
                for line in f:
                    shape = parse_shape(line)
                    shapes.append(shape)
        except FileNotFoundError:
            print(f"Файл {filename} не знайдено, пропускаємо.")

    if not shapes:
        print("Жодної фігури не знайдено.")
        return

    max_area_shape = max(shapes, key=lambda x: x.area())
    max_perimeter_shape = max(shapes, key=lambda x: x.perimeter())

    result = (
        f"Фігура з найбільшою площею: {max_area_shape}, Площа: {max_area_shape.area():.2f}\n"
        f"Фігура з найбільшим периметром: {max_perimeter_shape}, Периметр: {max_perimeter_shape.perimeter():.2f}"
    )

    print(result)
    with open("output.txt", "w") as f:
        f.write(result)

if __name__ == "__main__":
    main()