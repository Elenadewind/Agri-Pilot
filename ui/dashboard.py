python
from PyQt5.QtWidgets import QMainWindow, QGraphicsView, QLabel
from PyQt5.QtCore import Qt

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("АгроПилот — Панель управления")
        self.setGeometry(100, 100, 800, 600)
        
        # Область отображения карты
        self.map_view = QGraphicsView()
        self.setCentralWidget(self.map_view)
        
        # Статус-бар
        self.status_label = QLabel("Готов к работе")
        self.statusBar().addWidget(self.status_label)
