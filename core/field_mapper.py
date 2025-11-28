python
import geopandas as gpd
from shapely.geometry import Polygon

class FieldMapper:
    def create_field_map(self, coordinates):
        """Создаёт карту поля по координатам GPS"""
        polygon = Polygon(coordinates)
        gdf = gpd.GeoDataFrame(
            {'field_id': [1], 'geometry': [polygon]}
        )
        return gdf
    
    def save_map(self, gdf, filename):
        """Сохраняет карту в формате GeoJSON"""
        gdf.to_file(filename, driver='GeoJSON')
