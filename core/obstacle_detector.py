python
import cv2

class ObstacleDetector:
    def detect(self, frame):
        """Обнаруживает препятствия на видеокадре"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 50, 150)
        
        # Поиск контуров
        contours, _ = cv2.findContours(
            edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        
        obstacles = []
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 100:  # Фильтр по размеру
                x, y, w, h = cv2.boundingRect(contour)
                obstacles.append((x, y, w, h))
        
        return obstacles
