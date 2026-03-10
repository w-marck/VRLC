**VRLC – VagalumeRaceLightCycle 4.1.2.0.0**
================================================
**Descrição**
-------------

VRLC – VagalumeRaceLightCycle é um modelo de versionamento baseado no SemVer (Semantic Versioning), criado para suprir algumas lacunas do modelo original.

O SemVer não define com clareza os significados das fases alpha e beta. O VRLC propõe uma abordagem mais específica, dividindo o ciclo de desenvolvimento em cinco fases, que indicam com precisão o estágio atual do projeto. Esses ciclos são inspirados nos momentos que antecedem a largada de uma corrida de Fórmula 1:

● **Ciclo 5** – fase experimental (pré-alpha), onde o projeto ainda está em construção e sujeito a grandes mudanças;

● **Ciclos 4, 3 e 2** – representam o acendimento progressivo das luzes de largada, indicando avanços no amadurecimento do projeto (fase alpha e beta com critérios definidos);

● **Ciclo 1** – o momento da "bandeirada de largada", em que o projeto atinge um estado estável e pronto para lançamento oficial.

Diferente do SemVer, o VRLC também permite manter o histórico de versões anteriores à adoção do modelo. Por meio de um campo chamado **valor herdeiro**, é possível registrar o último número de versão MAJOR do ciclo anterior. Isso preserva a continuidade do histórico e evita o reinício artificial da contagem de versões quando o projeto muda de abordagem ou estrutura de versionamento.

Além disso, o VRLC introduz o conceito de **versão gêmea**: um mecanismo que registra alterações mínimas ou irrelevantes que não impactam a versão oficial, mas que indicam que o projeto foi modificado. Assim, mesmo mudanças sutis que normalmente não seriam registradas em sistemas convencionais são identificáveis.
**Explicação Curta sobre o Modelo VRLC**

----------------------------------------

O modelo de versionamento VRLC (VagalumeRaceLightCycle) segue a estrutura:

CICLO.HERDADO.MAJOR.MINOR.PATCH_DATA

### **Situações de Uso**

→ Primeira Situação (transição de ciclo)

Usada para indicar o início de um novo ciclo de desenvolvimento.

Exemplo: 4.10.1.0.0_0704

● **4** = ciclo atual (ciclo novo iniciando)

● **10** = versão herdada do ciclo anterior (último valor _MAJOR_ do ciclo anterior)

● **1** = nova fase principal do projeto

● **0** = nenhuma alteração menor feita ainda

● **0** = nenhuma correção feita ainda

● **_DATA** = data (mês/dia ou ano/mês/dia) da transição de ciclo

→ Segunda Situação (versão gêmea)

Usada para indicar que houve uma pequena alteração no projeto, mas que não altera seu comportamento.

Exemplo: 4.10.2.1.5_0710 (versão gêmea da 4.10.2.1.5)

● Mesmo número de versão, mas com _DATA adicionado

● Indica modificações quase invisíveis, como ajustes de formatação, comentários ou organização interna

### **Definições**

● **Ciclo atual:** valor de 5 a 1, representando o estágio do desenvolvimento. Inspirado na sequência de largada da Fórmula 1:

○ **5** = "oficina", fase experimental e livre

○ **4 a 2** = preparação, validação, estabilização

○ 1 = "largada", pronto para uso geral (operacional)  
Após o ciclo 1, o número do ciclo pode ser descartado da versão.

● **Herdado (herança):** representa o último valor _MAJOR_ do ciclo de desenvolvimento **anterior**. Se o projeto está iniciando o VRLC e não possui um ciclo anterior VRLC, ele herda o último valor _MAJOR_ da versão anterior ao VRLC, considerando essa versão como pertencente a um Ciclo "Legado" (pré-VRLC).

● **MAJOR:** mudanças estruturais ou incompatíveis com versões anteriores; altera funcionalidades fundamentais.

● **MINOR:** adições ou modificações compatíveis; novas funcionalidades ou ajustes visíveis e estáveis.

● **PATCH:** correções simples, localizadas, sem impacto funcional.

● **Transição de ciclo:** ocorre com uma versão X.Y.1.0.0_DATA, marcando o fim de um ciclo e o início de outro, preservando histórico.

● **Gêmeo:** qualquer versão com _DATA, mesmo que os números anteriores não mudem. Usado para indicar edições mínimas, como ajustes cosméticos ou internos irrelevantes à lógica do programa.

### **Exemplos Práticos**

→ Primeira versão com histórico herdado (início do VRLC com herança pré-VRLC)

5.16.1.0.0_20250704

Início do ciclo 5 em 04/07/2025. O projeto estava na versão 15 antes do VRLC, que é herdada como 16 (considerado o último MAJOR do "Ciclo 6").

5.0.1.0.0_20250704

Início do ciclo 5 sem herança (começando do zero), fase de prototipagem.

→ Fim e início de ciclo (transição entre ciclos VRLC)

4.10.1.0.0_0704

O ciclo 4 começou em 04/07. O ciclo anterior (ex: Ciclo 5) foi encerrado com MAJOR 10, que é herdado.

→ Novo ano, continuidade de projeto

4.10.3.2.7_20260103

Primeira versão do novo ano (03/01/2026). Terceira fase principal (MAJOR 3), segunda alteração menor (MINOR 2) e sétima correção (PATCH 7).

→ Versão gêmea (modificações mínimas)

4.10.3.3.1_0710

Quarta fase do projeto, com ajustes mínimos feitos em 10/07, quase idêntica à versão anterior 4.10.3.3.1.
**�� Ciclos de Desenvolvimento do Projeto**

-------------------------------------------

As palavras-chaves “DEVE”, “NÃO DEVE”, “OBRIGATÓRIO”, “DEVERÁ”, “NÃO DEVERÁ”, “PODEM”, “NÃO PODEM”, “RECOMENDADO”, “PODE” e “OPCIONAL” no presente documento devem ser interpretados como descrito na RFC 2119.

http://tools.ietf.org/html/rfc2119

Cada ciclo representa um **estágio da maturidade** do projeto. Ele aparece como **o primeiro dígito** da versão (CICLO.HERDADO.MAJOR.MINOR.PATCH_DATA) e determina **o que esperar da estabilidade, da interface e da funcionalidade do software.**

### **�� 5 = oficina**

● **Fase experimental.**

● Código incompleto, funcionalidades básicas podem não existir.

● Interface pode não estar presente ou ser mínima.

● Útil apenas para desenvolvedores e testes internos.

● **Não recomendada para uso externo.**

�� _Exemplo: testes de cálculo, esboço de estruturas, experimentos com algoritmos._

### **�� 4 = vermelho**

● Primeira versão minimamente usável.

● A função principal começa a aparecer, mas ainda está **quebradiça**.

● A interface começa a tomar forma, mas é frágil.

● Bugs frequentes. Nada está garantido.

● Já dá para alguém usar, **com cuidado**.

�� _Exemplo: ADEGPro consegue abrir e ler dados do GPro, mas não toma boas decisões._

### **�� 3 = amarelo**

● **Interface estável.**

● A funcionalidade principal já funciona corretamente na maioria dos casos.

● Ainda há bugs, mas o software é utilizável por usuários comuns.

● Outras funções secundárias ainda estão em fase de testes.

�� _Exemplo: o ADEGPro faz previsões válidas, mas ainda pode falhar em corridas específicas._

### **�� 2 = verde**

● O programa é **estável, funcional e confiável**.

● A interface está polida e todas as partes visíveis estão integradas.

● Apenas funções muito específicas podem ter erros.

● Pronto para uso público com avisos mínimos.

�� _Exemplo: ADEGPro funciona como planejado, erros são raros e pequenos._

### **�� 1 = largada**

● Versão **oficial, madura e robusta**.

● Ideal para uso contínuo.

● Bugs são raros e não críticos.

● O programa pode crescer e evoluir, mas **o núcleo está pronto.**

● Ao final do ciclo largada, o número **1 desaparece**, e o versionamento segue como MAJOR.MINOR.PATCH.

�� _Exemplo: ADEGPro está pronto para qualquer jogador usar sem medo._
**�� Transição entre Ciclos**

-----------------------------

A transição entre ciclos é **registrada com uma versão com data**, no formato:

X.Y.1.0.0_DATA  

● X = ciclo atual

● Y = último valor MAJOR do ciclo anterior (herdado)

● 1 = marcador fixo (indica o início de um novo MAJOR para o novo ciclo)

● 0.0 = Minor e Patch reiniciados

● _DATA = data da transição (pode ser _YYYYMMDD se for a primeira do ano/projeto)

### **Exemplo de Evolução com HERDADO Dinâmico**

| **Versão**     | **Ciclo** | **Herdado** | **Major** | **Minor** | **Patch** | **Data** | **Descrição**                                                  |
| -------------- | --------- | ----------- | --------- | --------- | --------- | -------- | -------------------------------------------------------------- |
| 5.16.1.0.0     | Oficina   | 16          | 1         | 0         | 0         |          | Protótipo interno (herda 16 do "Ciclo 6" pré-VRLC)             |
| 5.16.2.0.0     | Oficina   | 16          | 2         | 0         | 0         |          | Nova funcionalidade importante no Ciclo 5                      |
| 4.2.1.0.0_0710 | Vermelho  | 2           | 1         | 0         | 0         | 0710     | Ciclo vermelho iniciado dia 10/07 (herda o MAJOR 2 do Ciclo 5) |
| 4.2.2.0.0      | Vermelho  | 2           | 2         | 0         | 0         |          | Outra funcionalidade importante no Ciclo 4                     |
| 3.2.1.0.0_0722 | Amarelo   | 2           | 1         | 0         | 0         | 0722     | UI e núcleo funcional, ciclo novo (herda o MAJOR 2 do Ciclo 4) |
| 2.1.1.0.0_0730 | Verde     | 1           | 1         | 0         | 0         | 0730     | Pronto para uso comum (herda o MAJOR 1 do Ciclo 3)             |
| 1.1.1.0.0_0805 | Largada   | 1           | 1         | 0         | 0         | 0805     | Versão madura, para uso geral (herda o MAJOR 1 do Ciclo 2)     |
| 1.0.1          | Largada+  | N/A         | 2         | 0         | 0         |          | Depois da Largada, estágio e HERDADO somem, segue SemVer       |
| 2.0.0          | Largada+  | N/A         | 2         | 0         | 0         |          | Depois da Largada, estágio e HERDADO somem, segue SemVer       |



**�� MAJOR — Número Principal de Versão Dentro de um Ciclo**
------------------------------------------------------------

Representa uma **grande atualização funcional ou conceitual** dentro do mesmo ciclo (CICLO). É o segundo número da versão no formato:

CICLO.HERDADO.MAJOR.MINOR.PATCH[_DATA]  

### **�� Significado do MAJOR**

O **MAJOR** é alterado quando ocorre uma **mudança estrutural ou comportamental importante** no projeto, que **pode ou não quebrar a compatibilidade**, mas **impacta significativamente**:
**✅ Exemplos de Mudanças que Aumentam o MAJOR**

-----------------------------------------------

1. ✅ Uma nova **mecânica principal** é adicionada ao programa (ex: sistema de estratégia preditiva).

2. ✅ A estrutura dos **arquivos gerados** muda (ex: novo formato no geral.xlsx).

3. ✅ Uma **função pública** é alterada ou removida.

4. ✅ Um **módulo inteiro é substituído**, reescrito ou realocado.

5. ✅ Passa a exigir **requisitos de sistema novos** (ex: nova versão de Python, conexão obrigatória).

6. ✅ Integração com **API externa** ou mudança de comunicação com o GPro.

7. ✅ Alterações que exigem **treinamento ou adaptação do usuário**.

8. ✅ Incompatibilidade com versões antigas de dependências essenciais.

9. ✅ Mudança significativa no **modo de uso principal** (ex: de terminal para GUI).

10. ✅ Mudança na **filosofia ou identidade funcional** do projeto.

### **⚠️ Não Aumentam o MAJOR**

● ⚠️ Refatoração interna com mesmo comportamento externo.

● ⚠️ Correções de bugs ou ajustes de desempenho.

● ⚠️ Melhorias na interface sem quebra de funcionalidade.

● ⚠️ Traduções, renomeações pequenas, reorganizações visuais.

● ⚠️ Melhorias incrementais nas funções existentes.
**�� HERDADO – Continuidade Histórica e Transição de Ciclos**

-------------------------------------------------------------

O número **HERDADO** carrega a **herança histórica do projeto ADEGPro** e o **progresso entre os ciclos VRLC**.

### **�� Contexto**

O campo HERDADO foi concebido para garantir a **continuidade do histórico de versões** do projeto, tanto para versões anteriores à adoção do VRLC quanto para a transição entre os próprios ciclos de desenvolvimento do VRLC. Ele impede o reinício artificial da contagem de MAJOR e reflete o amadurecimento contínuo do projeto.

### **�� Regras do HERDADO**

1. �� **Início do VRLC (Herança Pré-VRLC):** Se o projeto está adotando o VRLC e não possui um histórico de ciclos VRLC anteriores, o campo HERDADO assume o último valor MAJOR da versão anterior ao VRLC. Essa versão pré-VRLC é conceitualmente tratada como pertencente a um **"Ciclo 6"**.

○ _Exemplo:_ Se o projeto estava na v15 antes do VRLC, e inicia no Ciclo 5, a primeira versão VRLC será 5.16.1.0.0_DATA. O 16 é o MAJOR herdado do "Ciclo 6" (v15 + 1).

2. �� **Transição entre Ciclos VRLC:** Ao transitar de um ciclo para o próximo (ex: do Ciclo 5 para o Ciclo 4), o campo HERDADO assume o **último valor MAJOR alcançado no ciclo de desenvolvimento** **_anterior_**.

○ _Exemplo:_ Se o Ciclo 5 terminou com a versão 5.16.3.0.0, ao iniciar o Ciclo 4, a primeira versão será 4.3.1.0.0_DATA. O 3 é o último MAJOR do Ciclo 5.

3. �� **Flexibilidade de Início:** Esta dinâmica permite que um projeto inicie o VRLC em qualquer ciclo (ex: Ciclo 3), herdando o MAJOR do ciclo conceitual anterior (seja o "Ciclo 6" ou um ciclo VRLC anterior).

4. �� **Estabilidade do HERDADO dentro do ciclo:** Uma vez que o valor HERDADO é definido na transição para um novo ciclo, ele **permanece fixo** durante todo o desenvolvimento dentro daquele ciclo. Ele só será atualizado na próxima transição de ciclo.

### **�� Exemplo Prático de Uso**

Versão antiga:          ADEGPro v15  
Nova versão herdada:    5.16.1.0.0_20250704 (equivalente funcional à antiga v15, iniciando VRLC)  

● 5: Ciclo atual ("Oficina")

● 16: Herdado do v15 anterior, convertido para 16 como marco de transição (campo HERDADO, do "Ciclo 6")

● 1: Novo MAJOR (primeira fase do novo modelo) (campo MAJOR)

● 0.0: Minor e Patch reiniciados

● 20250704: Data de início do projeto VRLC

### **�� Futuro do Número Herdado**

● O número HERDADO **será atualizado** a cada transição de ciclo, refletindo o MAJOR final do ciclo anterior.

● Ele só **deixa de ser usado** quando o sistema amadurecer **após a “Largada” (Ciclo 1)** e adotar uma contagem natural de versões no formato MAJOR.MINOR.PATCH (SemVer puro), sem a necessidade de manter o contexto de ciclos.
**��️ _DATA – Marcação de Variações Mínimas (Gêmeos de Código)**

----------------------------------------------------------------

O sufixo **_DATA** é uma **marca temporal** usada para indicar que uma versão sofreu **alterações tão pequenas**, que o comportamento do código continua **virtualmente idêntico**, embora tecnicamente ele **tenha sido alterado**.

### **�� Função do _DATA no Sistema de Versão**

● Não representa um novo recurso ou correção relevante.

● Serve como **rastro técnico**: houve alteração no código, mas não o suficiente para justificar um novo minor ou patch.

● Indica que duas versões são **gêmeas de código** – funcionam quase igual, mas **não são exatamente idênticas**.

### **�� Formato**

CICLO.HERDADO.MAJOR.MINOR.PATCH_DATA  

● _MMDD = Dia/Mês (ex: _0710) para alterações rotineiras.

● _YYYYMMDD = Ano/Mês/Dia (ex: _20250704) para:

○ Início do projeto (primeira versão).

○ Primeira modificação do projeto em um novo ano.

● O valor _DATA **só é usado quando necessário** – não é obrigatório em toda versão.

### **�� Quando Usar _DATA**

Use _DATA **exclusivamente** em duas situações:

#### **�� 1. Mudança de Ciclo (Transição de Estágio)**

● Quando uma versão muda de ciclo (ex: de **oficina** para **vermelho**), a versão será sempre:

X.Y.1.0.0_DATA  

● Isso indica:

○ X: Ciclo atual

○ Y: Valor herdado do ciclo anterior (campo HERDADO)

○ 1: Novo MAJOR para este ciclo (campo MAJOR)

○ 0.0: Minor e Patch reiniciados

○ _DATA: data oficial da mudança de ciclo (pode ser _YYYYMMDD se for a primeira do ano/projeto)

#### **�� 2. Alterações Mínimas que Não Merecem Novo Patch**

Exemplos:

● Correção ortográfica em um print()

● Mudança de None para 0 com efeito negligível

● Ajuste de indentação ou nome de variável interna

● Comentários alterados, docstrings reescritas, reorganização visual

● Alteração no nome de uma cor, emoji, estilo

### **�� Quando NÃO Usar _DATA**

● **Nunca** use _DATA se a mudança exige patch, minor ou major real.

● **Nunca** use para mudanças de comportamento, novos recursos, refatorações visíveis ou bugs resolvidos.

● **Nunca** use _DATA como substituto de controle de versão real.

### **�� Por que isso é útil?**

● Permite que você **documente pequenas mudanças** sem poluir o histórico com versões falsas.

● Ajuda a saber **exatamente quando** o código foi alterado, mesmo que seja "invisível".

● Torna fácil rastrear quando você mexeu em algo que “não deveria ter feito diferença, mas fez”.

### **�� Exemplo Prático:**

4.16.1.0.0          → versão sem mudanças  
4.16.1.0.0_0710     → exatamente igual, mas com ajuste mínimo (MMDD)  
5.0.1.0.0_20250101  → início do projeto (YYYYMMDD)  
5.0.10.3.5_20260105 → primeira modificação do projeto no ano (YYYYMMDD)  
**�� REGRAS DE VERSIONAMENTO DO ADEGPro**

-----------------------------------------

Baseado nas respostas fornecidas por Walter Augusto

### **�� MAJOR**

Representa mudanças que afetam **o comportamento, estrutura ou compatibilidade fundamental** do software. Deve ser incrementado quando:

● ✅ A estrutura dos arquivos gerados (como .xlsx, logs, etc) muda.

● ✅ Funções públicas são alteradas ou removidas.

● ✅ Um módulo importante é reescrito ou substituído (ex: previsão, combustível).

● ✅ Há quebra de compatibilidade com versões antigas do Excel ou do GPro.

● ✅ A linguagem de programação principal é alterada.

● ✅ A filosofia ou propósito principal do programa muda (ex: de auxiliar para automatizador).

● ✅ O programa passa a exigir conexão com a internet.

● ✅ Um sistema de plugins/extensões é adicionado.

● ✅ O projeto é reorganizado em pastas/estrutura nova.

● ✅ O suporte a versões antigas de Python é encerrado.

● ✅ A licença do projeto muda.

● ⚠️ Pode incluir mudanças drásticas de interface, dependências, nomes principais ou narrativa — avaliar o impacto.

● ❌ **Não** é major se só muda o processamento interno mantendo resultados, ou se apenas perde compatibilidade com arquivos .xlsx.

### **⚙️ MINOR**

Usado para **adições, melhorias ou mudanças** que não quebram compatibilidade. Deve ser incrementado quando:

● ✅ Correções de bugs ou falhas que melhoram estabilidade sem alterar interface.

● ✅ Novas funcionalidades pequenas são adicionadas.

● ✅ Há inclusão ou remoção de dependências externas.

● ✅ Melhorias na documentação ou comentários.

● ✅ Mudanças em configuração padrão ou suporte a novos formatos.

● ✅ Remoção de funcionalidades depreciadas.

● ✅ Inclusão de testes automatizados ou melhorias de acessibilidade.

● ✅ Interface gráfica ou layout é ajustado sem impacto na lógica.

● ⚠️ Pode incluir refatorações internas, ajustes de mensagens, melhorias de desempenho.

● ❌ **Não** é minor se for apenas uma correção mínima sem impacto ou um detalhe visual/textual.

### **�� PATCH**

Refere-se a **correções pequenas** que não alteram nenhuma funcionalidade significativa. Deve ser incrementado quando:

● ✅ Corrige falhas raras, bordas ou exceções específicas.

● ✅ Melhora a estabilidade, tratamento de erro ou compatibilidade.

● ✅ Ajusta logs ou comentários técnicos.

● ✅ Refina o sistema de permissões ou mensagens de erro.

● ⚠️ Pode incluir melhorias em testes, ajustes de leitura de arquivos ou logs.

● ❌ **Não** é patch se for uma correção visual/gramatical, performance mínima ou reorganização irrelevante.

### **�� _DATA**

Sufixo para marcar **gêmeos quase idênticos**: versões com mudanças tão pequenas que são funcionalmente iguais. Usado em:

● ✅ Correções em comentários, ortografia, formatação textual ou debug.

● ✅ Alterações internas de nomes, organização ou legibilidade sem impacto real.

● ✅ Mudanças em espaços, pontuações, formatações ou defaults inócuos.

● ✅ Ajustes no formato de hora/data, mensagens auxiliares ou texto interno.

● ⚠️ Pode incluir alterações na clareza das mensagens ou logs que não mudam significado.

● ❌ **Não** se aplica a mudanças de lógica, fluxo, estrutura ou qualquer impacto funcional.

ℹ️ O sufixo _DATA **só aparece**:

● ✅ Com versões onde o MAJOR é 1 e o MINOR e PATCH são 0, indicando o início de um novo MAJOR dentro de um ciclo, e o HERDADO reflete o último MAJOR do ciclo anterior (ex: 4.X.1.0.0_DATA onde X é o último MAJOR do ciclo anterior).

● ✅ Com qualquer outra versão se a alteração for puramente cosmética (ex: 4.16.1.0.1_0710)
**Casos Especiais**

-------------------

### **Regra: Mudança no Modo de Interação do Usuário**

#### **Minor**

● Mudanças visuais ou de posicionamento de elementos na interface que **não alteram o fluxo de uso** nem obrigam o usuário a reaprender etapas.

● Exemplos:

○ Reposicionar botões ou menus sem remover funcionalidades.

○ Alterar cores, tamanhos, ou layout, mantendo as mesmas funções acessíveis da mesma forma.

○ Pequenas melhorias na usabilidade que não impactam o modo como o usuário realiza as tarefas.

#### **Major**

● Mudanças que **alteram significativamente o fluxo mental do usuário ou a forma de usar o programa**, obrigando reaprendizado ou adaptação significativa.

● Exemplos:

○ Remover ou substituir funcionalidades essenciais de forma que o usuário precise procurar alternativas.

○ Trocar completamente o paradigma de interação (ex: sair do terminal para GUI) que muda o modo como o usuário realiza ações básicas.

○ Alterações que geram confusão, perda de produtividade ou dificuldade de adaptação sem aviso prévio.

### **Regra: Mudança nos Nomes de Comandos, Variáveis ou Funções Principais**

#### **Major**

● Mudança em nomes de comandos, funções ou APIs **públicas** que são acessadas ou chamadas diretamente pelo usuário ou por outros módulos externos.

● Impacto: Quebra a compatibilidade, exige adaptação do usuário ou código que usa essas funções.

● Exemplo:

○ Renomear um comando CLI que o usuário digita para executar uma ação.

○ Alterar nome de uma função pública utilizada por plugins ou scripts externos.

#### **Minor**

● Mudança em nomes de funções **internas** que, apesar de não serem diretamente usadas pelo usuário, podem impactar desenvolvedores que mexem no código (ex: módulos internos, helpers).

● Impacto: Pode exigir atualização em códigos internos, mas não afeta o uso final do programa diretamente.

● Exemplo:

○ Renomear uma função usada dentro do projeto que afeta outros módulos.

○ Alterar nomes de variáveis globais internas acessadas por partes do programa.

#### **Patch**

● Mudança em nomes de variáveis **locais** ou funções auxiliares que não afetam outras partes do código nem o usuário final.

● Impacto: Apenas melhora legibilidade ou organização interna, sem quebrar compatibilidade.

● Exemplo:

○ Renomear variáveis locais dentro de uma função.

○ Ajustes de nomes em pequenos trechos internos sem relação externa.

### **Regra: Alterar Significativamente a Organização das Dependências e Bibliotecas**

#### **✅ Major**

● Substituição de bibliotecas principais por outras (ex: trocar pandas por polars).

● Mudanças que **quebram a compatibilidade** com o ambiente atual (por exemplo, exige instalação de bibliotecas novas que não estavam documentadas).

● Alterações que exigem **modificações manuais no ambiente de execução** ou causam conflitos.

● Divisão do projeto em múltiplos pacotes ou mudanças estruturais profundas na forma como os módulos se comunicam.

#### **✅ Minor**

● Alterações nas dependências que **não quebram o uso do projeto**, mas exigem nova instalação (ex: adicionou uma nova lib útil).

● Mudança na forma como módulos são organizados ou importados (ex: mover funções para arquivos separados, refatorar pastas).

● Alterações nos requisitos (requirements.txt, pyproject.toml) sem afetar a execução atual.

#### **✅ Patch**

● Reorganização de imports puramente estética ou por organização interna:

○ Reordenar as importações por ordem alfabética ou por grupo (padrão, terceiros, internos).

○ Separar imports em linhas diferentes para legibilidade.

#### **✅ _DATA**

● Ajustes mínimos nos imports que **não alteram nem a ordem lógica nem a funcionalidade**, como:

○ Unificar vários imports em uma única linha (import os, time).

○ Quebra de linha ou mudança de espaçamento nos blocos de importação, **sem alterar a ordem ou os módulos**.

○ Mudanças de formatação visual sem impacto no carregamento ou funcionalidade.

### **Regra: Criar uma Nova Narrativa ou Identidade Conceitual para o Projeto**

_(ex: Gregório se aposenta e entra a Roberta dos Relatórios)_

#### **✅ MAJOR**

● A nova narrativa ou identidade **altera o modo de uso** do programa.

● Introduz **novas metáforas, personagens ou fluxos** que mudam **como o usuário interage ou entende o programa**.

● Obriga o usuário a **reaprender** partes da navegação, nomenclatura, menus ou funções.

● Exemplo: o personagem que era o centro do sistema é removido e sua substituição implica mudanças em comandos, fluxos ou lógicas principais.

#### **✅ MINOR**

● A mudança de narrativa é **puramente conceitual ou estética**, sem alterar o funcionamento prático.

● Troca de nomes, temas ou personagens **sem impacto na usabilidade** ou lógica.

● Exemplo: mudar o nome de “Relatórios Gregorianos” para “Arquivos de Roberta”, mas mantendo tudo igual no código e na interação.

### **Regra: Pequena Adição de Funcionalidade Nova, Sem Quebrar Compatibilidade**

#### **✅ MINOR**

● A funcionalidade adicionada **é nova**, mesmo que pequena, e **amplia** as capacidades do programa.

● Pode ser usada **opcionalmente** pelo usuário.

● Não interfere com fluxos antigos, mas **torna o programa mais poderoso ou versátil**.

● Exemplo: adicionar uma nova opção de exportação, uma nova aba, um novo argumento de linha de comando.

#### **✅ PATCH**

● A funcionalidade adicionada **não é nova de verdade**, mas sim uma **variação, atalho ou extensão mínima** de algo que já existe.

● Não adiciona complexidade, **não precisa ser explicada**, nem documentada separadamente.

● É algo **quase imperceptível**, um "a mais" que parece uma correção.

● Exemplo: permitir que uma função aceite um tipo extra de entrada que já era tecnicamente compatível.
**�� Escala Atualizada: Adição de Funcionalidade Nova (sem quebrar compatibilidade)**

-------------------------------------------------------------------------------------

| **Critério**                                           | **_DATA ✅**                                          | **PATCH ✅**                                   | **MINOR ✅**                                      |
| ------------------------------------------------------ | ---------------------------------------------------- | --------------------------------------------- | ------------------------------------------------ |
| **Visibilidade ao usuário (CLI, GUI, logs, arquivos)** | Nenhuma                                              | Baixa                                         | Média a alta                                     |
| **Complexidade da implementação**                      | 1-2 linhas                                           | 3-5 linhas                                    | 6+ linhas, novo bloco/função                     |
| **Impacto no comportamento do programa**               | Nenhum                                               | Marginal                                      | Funcionalidade nova ativável                     |
| **Mudança em mensagens, logs ou ajuda**                | Simples ou estética                                  | Corrige/informa                               | Introduz nova info/função                        |
| **Precisa de documentação no changelog**               | Não                                                  | Talvez                                        | Sim                                              |
| **Exige testes novos?**                                | Não                                                  | Raramente                                     | Sim                                              |
| **Afeta opções de configuração ou parâmetros?**        | Não                                                  | Não                                           | Sim                                              |
| **Exemplo típico**                                     | Corrige texto oculto, ajusta valor padrão silencioso | Permite novo valor interno, corrige edge case | Adiciona nova flag, novo modo, novo log ativável |

### **✔️ Regras Finais**

● **Se for uma adição invisível ao usuário**, mesmo que funcional, classifique como **_DATA**.

● **Se é visível mas não altera interface ou lógica principal, é PATCH**.

● **Se expande funcionalidade ou permite novos usos claros, é MINOR**.
**�� Refatoração Interna Sem Alterar o Comportamento**

------------------------------------------------------

Refatoração interna é toda mudança feita **dentro do código** com o objetivo de melhorar sua estrutura, legibilidade, organização ou manutenibilidade, **sem modificar o resultado final ou o comportamento externo do programa.**

### **�� _DATA — Refatorações Invisíveis e Insignificantes**

O código mudou, mas ninguém — nem mesmo o desenvolvedor comum — percebe a diferença funcional.

#### **Exemplos**

● Mudança na **ordem de funções** dentro do mesmo arquivo (sem impacto).

● Ajustes de **identação**, **espaços em branco**, **quebra de linha**, **linhas extras**.

● **Reorganização de imports** sem efeito real:  
import os  
import sys  
from datetime import datetime  

para:  
from datetime import datetime  
import os  
import sys  

● Troca de nomes de variáveis **locais ou internas** que não aparecem fora do escopo.

● Remoção de comentários redundantes ou correção de docstrings.

**Regra:**

_Mudanças internas 100% invisíveis para qualquer pessoa usando ou testando o programa._

### **�� PATCH — Refatorações Pequenas e Localizadas**

O código foi reestruturado pontualmente para ficar mais claro, reutilizável ou performático **sem mudar como funciona**.

#### **Exemplos**

● Separar um trecho repetido em uma **função auxiliar**.

● Simplificar estruturas (if aninhados, loops complexos).

● Tornar funções mais puras, organizadas ou diretas.

● Melhorar **tratamento de exceções** ou isolar responsabilidades.

● Refatorar uma função grande em várias menores.

● **Mover** funções entre arquivos, sem mudar o uso.

**Regra:**

_Melhorias úteis no código_ **_interno_**_, sem mudar a lógica, a estrutura de arquivos nem afetar o funcionamento do sistema para o usuário._

### **�� MINOR — Refatorações Amplas, Estruturais ou Profundas**

Mudanças que reestruturam o projeto em nível de arquitetura interna, múltiplos arquivos ou módulos.

#### **Exemplos**

● Divisão de um arquivo grande em **vários módulos**.

● Agrupamento de funções em **classes** ou pacotes novos.

● Conversão de código procedural para **orientado a objetos**.

● Alteração no esquema de **importação**, **organização de pacotes**.

● Padronização massiva de estilo ou convenção no projeto todo.

● Substituição de bibliotecas ou modelos de organização (ex: services, helpers, etc).

**Regra:**

_Reestruturação interna de_ **_grande impacto_**_, que exige manutenção ampla, testes em cadeia e atenção redobrada, mesmo sem alterar o funcionamento._
**�� Ajustes em Mensagens Exibidas ao Usuário (textos, avisos, alertas)**

-------------------------------------------------------------------------

### **�� _DATA — Ajustes Mínimos e Pontuais**

● Correções pequenas como:

○ Erros de digitação ou gramática.

○ Pequenas melhorias na clareza sem alterar o significado.

○ Ajustes de pontuação, espaçamento ou formatação do texto.

○ Reformulação leve que não altera o conteúdo ou fluxo de entendimento.

Exemplo:

"Por favor, aguarde..." → "Por favor aguarde..."

**Regra:**

Mudanças estéticas ou corretivas que não alteram o sentido ou o impacto da mensagem para o usuário.

### **�� PATCH — Ajustes que Melhoram a Clareza ou Evitam Confusões**

● Pequenas alterações que tornam a mensagem mais clara ou menos confusa.

● Ajustes para melhorar o tom da mensagem sem mudar seu propósito.

● Mudanças que evitam ambiguidade ou reduzem ruído (ex: mensagens repetitivas).

● Atualizações que não impactam a forma nem a lógica de interação.

Exemplo:

"Falha no carregamento do arquivo." → "Falha ao carregar o arquivo. Verifique se ele está acessível."

**Regra:**

Melhorias pontuais que tornam a experiência mais suave, sem alterar funcionalidades ou fluxo.
**�� Correções em Leitura e Escrita de Arquivos (sem modificar formatos)**

--------------------------------------------------------------------------

### **�� MAJOR**

● Alterações que **mudam o formato ou estrutura dos arquivos** gerados ou lidos pelo programa.

● Quebram compatibilidade com versões anteriores.

● Exigem que usuários atualizem ou adaptem arquivos existentes.

Exemplo:

Adicionar/remover colunas obrigatórias em arquivos .xlsx, mudar a estrutura do arquivo de log, alterar completamente o esquema dos dados.

### **�� MINOR**

● Ajustes que **modificam a forma como os arquivos são interpretados**, sem alterar o formato básico.

● Podem incluir suporte a variações ou formatos estendidos.

● Mantêm compatibilidade com arquivos antigos, mas introduzem funcionalidades novas ou melhorias importantes na leitura/escrita.

Exemplo:

Aceitar espaços extras, ignorar linhas comentadas, adicionar suporte para novas opções opcionais no arquivo sem quebrar arquivos antigos.

### **�� PATCH**

● Correções pontuais e pequenas melhorias na leitura ou escrita.

● Ajustam bugs raros ou bordas que não mudam o formato nem a estrutura.

● Melhoram robustez ou corrigem erros sem impacto na compatibilidade.

Exemplo:

Ignorar espaços extras na leitura, corrigir erros de encoding, tratar casos extremos de arquivos corrompidos, melhorar mensagens de erro ao ler arquivos.
**⚠️ Atualizações de Mensagens para Tornar Avisos Menos Invasivos**

-------------------------------------------------------------------

### **PATCH**

● Ajustes que suavizam mensagens **sem alterar seu significado ou impacto funcional**.

● Melhorias na forma de apresentar avisos, tornando-os menos intrusivos ou mais claros, mas mantendo o nível de severidade.

● Exemplo:

○ Tornar um aviso repetitivo menos frequente.

○ Ajustar o texto para ser mais amigável ou menos agressivo, sem mudar o comportamento.

### **MINOR**

● Mudanças que **alteram o comportamento dos avisos**, impactando como o usuário reage ou o fluxo do programa.

● Exemplos:

○ Transformar um aviso em erro (ou vice-versa).

○ Remover ou adicionar mensagens que podem bloquear ações do usuário.

○ Ajustes que mudam a lógica de exibição, como tornar obrigatório um aviso ou permitir ignorá-lo.
**�� Atualizações no Formato de Log (sem mudança de conteúdo)**

---------------------------------------------------------------

### **✅ _DATA**

● Mudanças **mínimas e imperceptíveis** ao ser humano.

● Alterações que não afetam nem a leitura humana nem o processamento automatizado.

● **Exemplos:**

○ Remoção ou adição de uma palavra redundante.

○ Pequenos ajustes de pontuação, espaços ou correção ortográfica discreta.

○ Ex:

■ Antes: gregório está acessando o circuito de interlagos

■ Depois: gregório está acessando interlagos

### **✅ PATCH**

● Mudanças **visíveis**, mas que **não quebram estrutura** e **não afetam ferramentas externas** que eventualmente analisam o log.

● Melhorias no texto, clareza ou padronização leve.

● **Exemplos:**

○ Remoção de colchetes, mudança na ordem de palavras, simplificação do texto.

○ Ex:

■ Antes: ddmm H:M [REGISTRO] gregório está acessando o circuito de interlagos

■ Depois: ddmm H:M gregório está acessando interlagos

### **✅ MINOR**

● Mudanças **significativas na estrutura ou padronização do log**.

● Possível impacto em scripts ou automações que leem os logs.

● **Exemplos:**

○ Alterar completamente o estilo da linha de log.

○ Mudar delimitadores, remover ou adicionar seções de forma perceptível.

○ Ex:

■ Antes: ddmm H:M [REGISTRO] gregório está acessando o circuito de interlagos

■ Depois: interlagos anotado

### **❌ MAJOR**

● Não aplicável: mudanças em logs, por si só, **nunca são Major**, pois não impactam diretamente a funcionalidade do programa para o usuário comum.
**�� Alterações de Espaçamento ou Formatação em Arquivos de Saída (sem mudança de dados)**

------------------------------------------------------------------------------------------

### **✅ _DATA**

● Mudança **visual mínima**: não interfere no entendimento nem na estrutura esperada.

● Apenas ajustes **de espaçamento, vírgulas, alinhamento** ou **organização leve do texto**.

● Não afeta ferramentas externas nem parsing.

● **Exemplo:**  

- Lorem ipsum dolor sit amet, consectetur adipiscing elit.  
+ Lorem ipsum dolor sit amet,  consectetur adipiscing elit.  

### **✅ PATCH**

● Mudança **perceptível**, mas **ainda compatível com leituras anteriores**.

● Pode alterar marcadores, listas, separação de seções — mas sem causar ambiguidade ou quebra no uso por humanos ou scripts.

● Reorganização visual moderada.

● **Exemplo:**  

- * Lorem ipsum  
- * Vestibulum non malesuada  
+ 1. Lorem ipsum  
+ 2. Vestibulum non malesuada  

### **✅ MINOR**

● Mudança **significativa** na estrutura de apresentação ou no **formato do arquivo** (ex: .xlsx para .csv, .txt, .json, etc.).

● Pode impactar ferramentas externas, scripts ou rotinas de importação/exportação.

● Também inclui reestruturações profundas de como a informação é exibida.

● **Exemplo:**  

- Arquivo original: Excel (.xlsx) com colunas  
+ Novo formato: Texto plano (.txt) com informações concatenadas em linha única  

### **❌ MAJOR**

● Não aplicável: mudanças de espaçamento ou formatação **nunca** escalam a um nível **MAJOR**, pois não quebram funcionalidades centrais.
**�� Ajustes em Mensagens (mesmo significado, mais clareza)**

-------------------------------------------------------------

### **✅ _DATA**

● Reformulação mínima ou clareza **sem retirar nenhuma informação funcional ou mudar o tom original**.

● Exemplo típico: pequenas reorganizações, trocas de palavras sinônimas, pontuação.

● **Exemplo:**  

- Gregório encontrou o arquivo geral.xlsx. Vai dar uma olhada nele.  
+ Gregório encontrou o arquivo geral.xlsx e vai dar uma olhada nele.  

### **✅ PATCH**

● Ajuste perceptível, mas ainda **sem impacto semântico** relevante.

● O tom ou o ritmo da mensagem muda, mas o conteúdo essencial continua.

● **Exemplo:**  

- Gregório encontrou o arquivo geral.xlsx. Vai dar uma olhada nele.  
+ Gregório encontrou o arquivo geral.xlsx.  

### **✅ MINOR**

● O texto muda de forma que **perde nuances importantes** ou **altera a interpretação possível** — mesmo que de leve.

● Pode parecer inofensivo, mas **impacta o significado percebido**, inclusive para o usuário interpretar o comportamento do sistema.

● **Exemplo:**  

- Gregório encontrou o arquivo geral.xlsx. Vai dar uma olhada nele.  
+ Arquivo geral acessado.  

### **❌ MAJOR**

● Não aplicável. Mudanças de mensagem por clareza, mesmo que profundas, **nunca** são Major sozinhas — só se acompanharem **mudança de comportamento real** do sistema.
