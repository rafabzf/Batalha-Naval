import sys,os

sys.path.insert(0,os.path.abspath(os.curdir))

from controle.controlador_sistema import ControladorSistema
from controle.controlador_oceano import ControladorOceano

if __name__ == "__main__":
    ControladorOceano().abre_tela()
