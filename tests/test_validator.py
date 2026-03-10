# tests/test_validator.py
# from VRLCTest import VRLCVersion
from vrlc import VRLCVersion

v = VRLCVersion("4.1.1.10.123") # Vamos chamar de 'v' pra ficar curto
print(f"Estendida: {v.estendida}")
print(f"Resumida:  {v.resumida}")
print(f"Compacta:  {v.compacta}")

# Para dar o bump_major no VRLC, você precisa passar a DATA 
# porque toda transição de ciclo EXIGE data, lembra?
v_proxima = v.bump_major(data="20260304") 
print(f"Nova:      {v_proxima.estendida}")