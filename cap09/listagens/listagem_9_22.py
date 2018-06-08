"""Obtenção das horas em Python
"""

import time
agora = time.time()
agora
print(time.ctime(agora))
agora2 = time.localtime()
agora2
print(time.gmtime(agora))
