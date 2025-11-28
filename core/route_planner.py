python
import numpy as np

class RoutePlanner:
    def generate_parallel_paths(self, field_polygon, row_width):
        """Генерирует параллельные маршруты с заданным интервалом"""
        minx, miny, maxx, maxy = field_polygon.bounds
        rows = np.arange(miny, maxy, row_width)
        paths = []
        for y in rows:
            path = [(minx, y), (maxx, y)]
            paths.append(path)
        return paths
