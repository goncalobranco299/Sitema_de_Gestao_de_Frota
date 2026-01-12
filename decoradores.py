from datetime import datetime

def log_operacao(func):
    def wrapper(*args, **kwargs):
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{agora}] Ação: {func.__name__} executada com sucesso.")
        return func(*args, **kwargs)
    return wrapper