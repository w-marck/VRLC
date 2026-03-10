from .vrlc import VRLCVersion  # Ajuste pro nome minúsculo
from ._version import __version__  # Do scm gerado

__all__ = ["VRLCVersion"]
__version__ = __version__  # Exposição simples, sem duplicata