"""usando getcwd - para ver onde estamos
          chdir - para alterar diretorio de trabalho
"""

import os
print(f'Diretorio atual: {os.getcwd()}')

os.chdir('subextra')
print(f'Diretorio atual: {os.getcwd()}')
