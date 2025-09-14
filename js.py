import json # Importando erramientas 
import os
from typing import Dict, List, Optional, Any, Union, Callable

JSON_CUENTAS = "data/JsonCuentas.json"

# Creacion de archivo json
def write_json(file_path: str, data: Dict) -> None:
    with open(file_path, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4)
        