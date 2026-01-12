def exportar_inventario(frota, filename='inventario.txt'):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for veiculo in frota.vehicles:
                f.write(str(veiculo) + "\n")
        return True
    except Exception as e:
        print(f"Erro ao exportar: {e}")
        return False