Agri‑Pilot
A prototype system for parallel driving of agricultural machinery.

Description
The system provides:

field mapping (GeoJSON format);
parallel route planning;
obstacle detection using video analytics;
a graphical user interface for the operator.

Installation
1. Requirements
Python 3.10+;
pip package manager.

2. Installing dependencies
Run the following command:
bash
pip install opencv-python geopandas s

# Agri‑Pilot
Прототип системы параллельного вождения для сельскохозяйственной техники.

## Описание
Система обеспечивает:
- построение карт полей (формат GeoJSON);
- планирование параллельных маршрутов;
- обнаружение препятствий с помощью видеоаналитики;
- графический интерфейс оператора.

## Установка
### 1. Требования
- Python 3.10+
- Менеджер пакетов `pip`

### 2. Установка зависимостей
Выполните команду:
```bash
pip install opencv-python geopandas shapely pyqt5 numpy scipy

## 3. Running the application

Execute the following command:

```bash
python main.py
Project structure
agri-pilot/
├── main.py                  # Entry point
├── core/
│   ├── field_mapper.py     # Field mapping (creates field maps)
│   ├── route_planner.py   # Route planning (generates movement paths)
│   ├── obstacle_detector.py # Obstacle detection (analyzes video feed)
│   └── controller.py       # Motion control
├── ui/
│   └── dashboard.py         # Operator interface (GUI)
├── data/
│   └── maps/              # Map storage (GeoJSON/Shapefile formats)
├── config/
│   └── settings.json        # System configuration
├── tests/                 # Test scripts
└── README.md              # Documentation
Core modules
Field mapping (core/field_mapper.py)
Creates a field map from GPS coordinates and saves it in GeoJSON format.

Route planning(core/route_planner.py)
Generates parallel routes with a specified interval within the field.

Obstacle detection(core/obstacle_detector.py)
Analyzes video frames, extracts contours, and identifies obstacles based on area.

Operator interface (ui/dashboard.py)
PyQt5‑based GUI with a map display area and status bar.

Entry point (main.py)
Initializes all components and launches the graphical interface.

Usage
Launch the application: python main.py

Load or create a field map.

Set route parameters (e.g., row spacing).

Enable the video stream for obstacle detection.

Control movement via the interface.

Future development
Planned features:

Integration with GPS receivers (via pyserial)

Autopilot algorithms (PID controllers)

RTK correction support

Report export to PDF/Excel

Modular testing (pytest)

Recommendations
Use a virtual environment: python -m venv venv

Add comments to your code

Maintain a CHANGELOG.md file

Set up CI/CD via GitHub Actions



markdown
## 3. Запуск приложения

Выполните команду:

```bash
python main.py
Структура проекта
agri-pilot/
├── main.py                  # Точка входа
├── core/
│   ├── field_mapper.py     # Построение карт полей
│   ├── route_planner.py   # Планирование маршрутов
│   ├── obstacle_detector.py # Обнаружение препятствий
│   └── controller.py       # Управление движением
├── ui/
│   └── dashboard.py         # Интерфейс оператора
├── data/
│   └── maps/              # Хранилище карт (GeoJSON/Shapefile)
├── config/
│   └── settings.json        # Настройки системы
├── tests/                 # Тестовые сценарии
└── README.md              # Документация
Основные модули
Построение карт полей(core/field_mapper.py)
Создаёт карту поля по координатам GPS и сохраняет в формате GeoJSON.

Планирование маршрутов(core/route_planner.py)
Генерирует параллельные маршруты с заданным интервалом внутри поля.

Обнаружение препятствий(core/obstacle_detector.py)
Анализирует видеокадры, выделяет контуры и определяет препятствия по площади.

Интерфейс оператора(ui/dashboard.py)
Графический интерфейс на базе PyQt5 с областью отображения карты и статус‑баром.

Точка входа (main.py)
Инициализирует все компоненты и запускает графический интерфейс.

Использование
Запустите приложение: python main.py

Загрузите или создайте карту поля.

Задайте параметры маршрута (ширина междурядий и т. п.).

Включите видеопоток для обнаружения препятствий.

Управляйте движением через интерфейс.

Дальнейшее развитие
Планируемые функции:

интеграция с GPS‑приёмниками (через pyserial);

алгоритмы автопилотирования (PID‑регуляторы);

поддержка RTK‑коррекции;

экспорт отчётов в PDF/Excel;

модульное тестирование (pytest).

Рекомендации
Используйте виртуальное окружение: python -m venv venv

Добавляйте комментарии к коду.

Ведите CHANGELOG.md.

Настройте CI/CD через GitHub Actions.
