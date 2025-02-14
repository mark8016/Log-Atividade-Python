import logging
from datetime import datetime

# Configuração do logger
logging.basicConfig(filename="activity_log.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

def log_activity(message):
    """
    Função para registrar atividades no arquivo de log.
    :param message: Mensagem a ser registrada no log
    :return: None
    """
    logging.info(message)

# Exemplo de uso
log_activity("Início do processo de backup.")
log_activity("Serviço Apache reiniciado com sucesso.")
log_activity("Falha ao tentar reiniciar o MySQL.")
