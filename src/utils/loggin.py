import os
import logging
import json

def setup_logging():
    logging.basicConfig(
        filename='logs/app.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
    )

def load_config(config_file='config/config.json'):
    if not os.path.exists(config_file):
        logging.error(f"Config dosyası bulunamadı: {config_file}")
        raise FileNotFoundError(f"Config dosyası bulunamadı: {config_file}")

    with open(config_file, 'r') as file:
        config = json.load(file)
    
    return config
