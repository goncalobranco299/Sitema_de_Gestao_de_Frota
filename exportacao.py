def exportar_inventario(frota, filename='inventario.txt'):
    with open(filename, 'w') as f:
        for veiculo in frota.vehicles:
            f.write(str(veiculo) + "\n")
