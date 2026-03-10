# Manual de especificações do Validador do VRLC 1.0.0_20260310

Nome do Projeto: VRLC-v (VagalumeRaceLightCycle validador)
Versão: 5.0.1.0.0_DATA
Versionamento: VRLC 3.1.1.0.0_20260310

Especificações de desenvolvimento do validador: VRLC

## 1. Introdução

O validador do VRLC 3.1.1.0.0_20260310 consiste em um script Python que verifica se uma versão de software segue as regras do vrlc

## 2. Instalação

Instalação:

`pip install git+https://github.com/w-marck/vrlc.git`

Na importação do projeto, escreva:

`from vrlc import VRLCVersion`

Depois, escreva:

```python
v = VRLCVersion("5.0.1.0.1_YYYYMMDD")

version = v
```

