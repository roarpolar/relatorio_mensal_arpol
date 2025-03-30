import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

def setup_logger():
    """
    Configura o logger da aplicação
    """
    # Cria o diretório de logs se não existir
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Configura o logger
    logger = logging.getLogger('app_dash')
    logger.setLevel(logging.INFO)
    
    # Formato do log
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Handler para arquivo
    file_handler = RotatingFileHandler(
        f"{log_dir}/app_{datetime.now().strftime('%Y%m%d')}.log",
        maxBytes=10485760,  # 10MB
        backupCount=5
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # Handler para console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger

# Instância global do logger
logger = setup_logger() 