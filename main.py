from frota import Frota
from interface import Interface

if __name__ == "__main__":
    frota = Frota()
    interface = Interface(frota)
    interface.run()
