Estrutura atual do diretório VRLC.

  VRLC/                    # Diretório raiz do repositório
│
├── doc/                          # Diretório de documentação
│   ├── CHANGELOG.md                 # Histórico de alterações
│   ├── estrutura_raiz.md         # Documentação desta estrutura
│   ├── TODO.md                   # Lista de tarefas
│   ├── VRLC – 1.0.1-Vermelho.md  # Documentação do VRLC 1-vm
│   ├── VRLC – 2.0.0-Vermelho.md  # Documentação do VRLC 2-vm
│   ├── VRLC.md                   # Documentação do VRLC
│   └── VRLCValidador.md          # Documentação do validador
└── src/                          # Pacote Python Estrutura src/ adotada pra isolamento e padrões modernos (evita imports acidentais da raiz).
│   ├── vrlc/                     # Pacote VRLC
│   │   ├── __init__.py               # Inicializador
│   │   ├── vrlc.py                   # Validador VRLC
│   └── vrlc.egg-info             # Metadados do repositório    
│
├── tests/                  # Diretório de testes
│   ├── test_validator.py   # Testes unitários
│   ├── test.md             # testes de markdown
│   ├── VRLCEdit.md         # Edição do Manual
│   └── VRLCTest.py         # Teste de modificação do validador VRLC
│
├── .gitignore             # ignorar arquivos e diretórios
├── LICENSE                # licença Apache-2.0
├── pyproject.toml         # configuração do projeto
└── README.md              # documentação do repositório


OBS: para editar alguma coisa do projeto, NÃO MEXA diretamente no arquivo, <u>mas no seu equivalente</u> em **tests** e depois substitua em **src**.