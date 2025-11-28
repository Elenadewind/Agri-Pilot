python
from core.field_mapper import FieldMapper
from core.route_planner import RoutePlanner
from core.obstacle_detector import ObstacleDetector
from ui.dashboard import Dashboard
import sys
from PyQt5.QtWidgets import QApplication

def main():
    # Инициализация компонентов
    mapper = FieldMapper()
    planner = RoutePlanner()
    detector = ObstacleDetector()
    
    # Запуск интерфейса
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
