# 🏎️ VRLC — VagalumeRaceLightCycle

## Estendida: VRLC 2.1.1.0.1  
**Resumida: VRLC 1.0.1-verde**  
**Compacta: VRLC 1-verde**

VagalumeRaceLightCycle é um modelo de versionamento semântico construído sobre o núcleo do SemVer, mas desenhado para clareza humana. Inspirado na grelha de partida da Fórmula 1, o VRLC substitui “Alpha”, “Beta” e “RC” por 5 ciclos visuais e obrigatórios (5 → 1).

## 🚀 Por que VRLC?

O SemVer deixa a transição entre pré-lançamentos subjetiva. O VRLC define exatamente onde o projeto está na pista:

| Ciclo | Cor   | Nome     | Descrição                                      |
|-------|-------|----------|------------------------------------------------|
| 5     | 🔧    | Oficina  | Fase experimental (pré-Alpha). Mudanças drásticas. |
| 4     | 🔴    | Vermelho | Motor ligado. Início de testes (Alpha).        |
| 3     | 🟡    | Amarelo  | Ajustes finos. Estabilização (Beta).           |
| 2     | 🟢    | Verde    | Pronto para testes de pista (Release Candidate). |
| 1     | 🏁    | Largada  | Versão estável e operacional (Final/GA).       |

## 📐 Anatomia da Versão VRLC

Formato completo (enquanto estiver nos ciclos 5–1):

**CICLO.HERDEIRO.MAJOR.MINOR.PATCH[_DATA]**

| Posição | Nome      | Obrigatório?                  | Valores típicos          | Regra importante |
|---------|-----------|-------------------------------|--------------------------|------------------|
| 1       | Ciclo     | Sempre (exceto pós-Largada)   | 1–5                      | Após o ciclo 1 vira SemVer puro |
| 2       | Herdeiro  | Sempre (exceto pós-Largada)   | 0–∞ (0 só em ciclo 5)    | Fixo durante todo o ciclo |
| 3       | MAJOR     | Sempre                        | 1–∞                      | Reinicia em 1 na transição de ciclo |
| 4       | MINOR     | Sempre                        | 0–∞                      | — |
| 5       | PATCH     | Sempre                        | 0–∞                      | — |
| _DATA   | Data      | Ver regras abaixo             | _YYYYMMDD ou _MMDD       | Ver seção _DATA |

## 🧬 O Diferencial: Campo Herdeiro

Mantém o histórico mesmo se você adotar o VRLC no meio do projeto.

### 🔄 Início em qualquer ciclo
```bash
5.12.1.0.0_20260304    # Oficina (herdeiro 12 = último MAJOR antigo)
4.12.1.0.0_20260304    # direto no Vermelho
3.12.1.0.0_20260304    # direto no Amarelo
2.12.1.0.0_20260304    # direto no Verde
1.12.1.0.0_20260304    # direto na Largada
```

### 🛠️ Retrocesso Seguro (Rollback)
Sempre lembra o progresso:
```bash
2.3.3.2.0                # estava no Verde
3.8.4.0.0_20270510       # volta pro Amarelo → MAJOR = 3+1, Herdeiro = último MAJOR do ciclo anterior (8)
4.115.9.0.0_20270630     # volta pro Vermelho → MAJOR = 8+1, Herdeiro = 115
5.0.116.0.0_20270811     # volta pra Oficina (projeto iniciado com VRLC)
```

## 👯 Versão Gêmea (_DATA)

Registra alterações mínimas que não mudam a lógica (comentários, formatação, doc, etc.).

**Regras de _DATA:**
- **Obrigatória (8 dígitos)**: toda transição de ciclo + primeira versão do projeto + primeira versão do ano
- **Opcional (4 dígitos)**: gêmeas dentro do ciclo (ajustes invisíveis)
- **Proibida**: em qualquer versão que mude MAJOR/MINOR/PATCH

Exemplo: `1.0.1_0305` = mesma lógica da `1.0.1`, só ajuste cosmético em 05/03.

## 🛠️ Instalação do validador

```bash
pip install git+https://github.com/w-marck/vrlc.git
```

```python
from vrlc import VRLCVersion

v = VRLCVersion("5.0.1.0.0_20260303")
print(v.status)      # oficina
print(v.is_stable)   # False

v_vermelho = v.bump_major()  # transição de ciclo = bump MAJOR
print(v_vermelho)    # 4.0.1.0.0_20260303
```
OBS: Instalação direta via PyPI: `pip install vrlc` em breve


## 📋 Exemplos Reais e Fluxos

### 1. Fluxo Normal Completo (5 → Pós-Largada)
```bash
# Ciclo 5 — Oficina
5.0.1.0.0_20260304      # primeira versão (obrigatório _8d)
5.0.1.0.1               # patch normal
5.0.1.0.1_0304          # gêmea
5.0.2.0.0               # novo MAJOR no ciclo 5
5.0.115.16.18_20270120  # primeira de 2027

# Transição → Ciclo 4 (sempre .1.0.0_8d)
4.115.1.0.0_20270125

# ... (evolução normal)

# Transição → Ciclo 1 — Largada (ÚNICA versão no ciclo 1)
1.2.1.0.0_20270412

# Pós-Largada → SemVer puro (ciclo e herdeiro desaparecem)
1.0.1                   # primeira versão estável
1.0.1_0305              # gêmea ainda permitida
2.0.0
2.15.20_20270105        # primeira versão do ano 2027 (resquício VRLC)
```

### 2. Retrocesso e Saltos
(ver exemplos na seção Herdeiro acima)

### 3. ❌ Versões que o validador REJEITA (atual)
- Herdeiro 0 em ciclo ≠ 5
- Ciclo 1 com MAJOR > 1 na transição ou MINOR/PATCH ≠ 0
- Transição sem _YYYYMMDD
- Data inválida (dia 40, mês 13, 6 dígitos)
- Ciclo 0 ou 6+

**Dica:** se um número parecer data sem underline, só avisa (não erro).

## 📖 Documentação Completa

Regras detalhadas de MAJOR/MINOR/PATCH, refatorações, mensagens ao usuário e toda a matemática do validador estão em:

👉 **[VRLC.md — Especificação Técnica](VRLC.md)**

---
Desenvolvido por Walter Marcondes.  
Licença: [Apache License 2.0](LICENSE)
