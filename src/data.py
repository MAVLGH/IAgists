import os
import json
import datetime
from glob import glob
from typing import Optional

class JSONDataManager:
    def __init__(self, base_path='data'):
        self.base_path = base_path

    def save_info(self, dict_info, now=None):
        now = now or datetime.datetime.utcnow()
        date_path = now.strftime('%Y-%m')
        time_filename = now.strftime('%Y-%m-%dT%H:%M:%S') + '.json'
        folder_path = os.path.join(self.base_path, date_path)
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, time_filename)
        with open(file_path, 'w') as json_file:
            json.dump(dict_info, json_file, indent=4)
        return file_path

    def read_info(self, file_path: str) -> Optional[dict]:
        try:
            with open(file_path, 'r') as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            print(f"El archivo {file_path} no fue encontrado.")
            return None

    def update_info(self, file_path: str, updates: dict):
        try:
            with open(file_path, 'r+') as json_file:
                data = json.load(json_file)
                data.update(updates)
                json_file.seek(0)
                json.dump(data, json_file, indent=4)
                json_file.truncate()
        except FileNotFoundError:
            print(f"El archivo {file_path} no fue encontrado.")

    def delete_info(self, file_path: str):
        try:
            os.remove(file_path)
            print(f"Archivo {file_path} eliminado con éxito.")
        except FileNotFoundError:
            print(f"El archivo {file_path} no fue encontrado.")

    def list_json_files(self):
        return glob(os.path.join(self.base_path, '**/*.json'), recursive=True)

# Ejemplo de cómo usar la clase
if __name__ == "__main__":
    manager = JSONDataManager()
    
    # Crear información
    info = {'mensaje': 'Este es un ejemplo de CRUD en JSON'}
    file_path = manager.save_info(info)
    
    # Leer información
    read_data = manager.read_info(file_path)
    print(read_data)
    
    # Actualizar información
    manager.update_info(file_path, {'actualización': 'Aquí va la nueva información'})
    
    # Eliminar información
    manager.delete_info(file_path)
    
    # Listar archivos JSON
    for f in manager.list_json_files():
        print(f)
