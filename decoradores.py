from datetime import datetime

def log_operacao(func):
    def wrapper(*args, **kwargs):
        agora = datetime.now()
        print(f"[{agora}] A executar: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
