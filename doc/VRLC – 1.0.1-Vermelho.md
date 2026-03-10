# VRLC – VagalumeRaceLightCycle 1.0.1-Vermelho

VRLC 4.1.1.0.1

OBS: A versão de oficina foi perdida.

🚀 Explicação Geral do VRLC e Por Que Existe

VRLC – VagalumeRaceLightCycle é um modelo de versionamento **baseado no SemVer (Semantic Versioning)**, criado para suprir algumas lacunas do modelo original e oferecer uma **cosmovisão mais detalhada** para o ciclo de vida do projeto. Em essência, **a cosmovisão é do VRLC, mas a base é do SemVer**.

O SemVer não define com clareza os significados das fases alpha e beta. O VRLC propõe uma abordagem mais específica, dividindo o ciclo de desenvolvimento em cinco fases, que indicam com precisão o estágio atual do projeto. Esses ciclos são inspirados nos momentos que antecedem a largada de uma corrida de Fórmula 1:

* **Ciclo 5** – fase experimental (pré-alpha), onde o projeto ainda está em construção e sujeito a grandes mudanças;
  
* **Ciclos 4, 3 e 2** – representam o acendimento progressivo das luzes de largada, indicando avanços no amadurecimento do projeto (fase alpha e beta com critérios definidos);
  
* **Ciclo 1** – o momento da "bandeirada de largada", em que o projeto atinge um estado estável e pronto para uso (release oficial).
  

Diferente do SemVer, o VRLC também permite manter o histórico de versões anteriores à adoção do modelo. Por meio de um campo chamado **valor herdeiro**, é **PODE** ser registrado o último número de versão MAJOR do ciclo anterior. Isso preserva a continuidade do histórico e evita o reinício artificial da contagem de versões quando o projeto muda de abordagem ou estrutura de versionamento.

Além disso, o VRLC introduz o conceito de **versão gêmea**: um mecanismo que registra alterações mínimas ou irrelevantes que não impactam a versão oficial, mas que indicam que o projeto foi modificado. Assim, mesmo mudanças sutis que normalmente não seriam registradas em sistemas convencionais são identificáveis.

💡 Visão Geral Simplificada do Modelo VRLC

O modelo de versionamento **VRLC (VagalumeRaceLightCycle)** **DEVE** seguir a estrutura: **`CICLO.HERDADO.MAJOR.MINOR.PATCH_DATA`**

Esta estrutura **DEVE** ser vista como a **cosmovisão do VRLC sobre o SemVer**, adicionando camadas de contexto e rastreabilidade:

* **`CICLO`**: Indica o estágio de maturidade do projeto (de 5 a 1).
  
* **`HERDADO`**: Reflete o último `MAJOR` do ciclo anterior ou a herança pré-VRLC.
  
* **`MAJOR`**: Grandes mudanças estruturais ou funcionais (conforme a interpretação do VRLC).
  
* **`MINOR`**: Novas funcionalidades ou melhorias compatíveis (conforme a interpretação do VRLC).
  
* **`PATCH`**: Correções de bugs ou ajustes pequenos (conforme a interpretação do VRLC).
  
* **`_DATA`**: Marca alterações mínimas que não justificam um `PATCH` (formato `_MMDD` ou `_YYYYMMDD`).
  

### Situações de Uso Comuns

* **Transição de Ciclo**: **DEVE** ser usada para indicar o início de um novo ciclo de desenvolvimento.
  
  * Exemplo: `4.10.1.0.0_0704` (Ciclo 4, herdando MAJOR 10 do ciclo anterior, iniciando novo MAJOR 1).
* **Versão Gêmea**: **DEVE** ser usada para indicar que houve uma pequena alteração no projeto, mas que não altera seu comportamento funcional.
  
  * Exemplo: `4.10.2.1.5_0710` (Mesmo número de versão, mas com `_DATA` para indicar modificação interna).

🏁 Ciclos de Desenvolvimento do Projeto

As palavras-chaves “DEVE”, “NÃO DEVE”, “OBRIGATÓRIO”, “DEVERÁ”, “NÃO DEVERÁ”, “PODEM”, “NÃO PODEM”, “RECOMENDADO”, “PODE” e “OPCIONAL” no presente documento **DEVEM** ser interpretados como descrito na RFC 2119.

http://tools.ietf.org/html/rfc2119

Cada ciclo **DEVE** representar um **estágio da maturidade** do projeto. Ele **DEVE** aparecer como **o primeiro dígito** da versão (`CICLO.HERDADO.MAJOR.MINOR.PATCH_DATA`) e **DEVE** determinar **o que esperar da estabilidade, da interface e da funcionalidade do software.**

### 🔧 `5 = oficina` (Fase Experimental / Pré-Alpha)

* **Fase experimental.**
  
* Código incompleto, funcionalidades básicas **PODEM** não existir.
  
* Interface **PODE** não estar presente ou ser mínima.
  
* Útil apenas para desenvolvedores e testes internos.
  
* **NÃO É RECOMENDADA** para uso externo.
  
* _Exemplo: testes de cálculo, esboço de estruturas, experimentos com algoritmos._
  

### 🔴 `4 = vermelho` (Primeira Versão Usável / Alpha)

* Primeira versão minimamente usável.
  
* A função principal **DEVE** começar a aparecer, mas ainda **PODE** estar **quebradiça**.
  
* A interface **DEVE** começar a tomar forma, mas **PODE** ser frágil.
  
* Bugs **PODEM** ser frequentes. Nada **ESTÁ GARANTIDO**.
  
* Já **PODE** dar para alguém usar, **com cuidado**.
  
* _Exemplo: ADEGPro consegue abrir e ler dados do GPro, mas não toma boas decisões._
  

### 🟡 `3 = amarelo` (Interface Estável / Beta)

* **Interface estável.**
  
* A funcionalidade principal já **DEVE** funcionar corretamente na maioria dos casos.
  
* Ainda **PODE** haver bugs, mas o software **É UTILIZÁVEL** por usuários comuns.
  
* Outras funções secundárias ainda **PODEM** estar em fase de testes.
  
* _Exemplo: o ADEGPro faz previsões válidas, mas ainda pode falhar em corridas específicas._
  

### 🟢 `2 = verde` (Estável e Confiável / Release Candidate)

* O programa **DEVE** ser **estável, funcional e confiável**.
  
* A interface **DEVE** estar polida e todas as partes visíveis **DEVEM** estar integradas.
  
* Apenas funções muito específicas **PODEM** ter erros.
  
* **DEVE** estar pronto para uso público com avisos mínimos.
  
* _Exemplo: ADEGPro funciona como planejado, erros são raros e pequenos._
  

### 🏁 `1 = largada` (Oficial e Robusta / Release)

* Versão **OFICIAL, MADURA e ROBUSTA**.
  
* **IDEAL** para uso contínuo.
  
* Bugs **DEVEM** ser raros e **NÃO DEVEM** ser críticos.
  
* O programa **PODE** crescer e evoluir, mas **o núcleo DEVE estar pronto.**
  
* Ao final do ciclo largada, o número **1 DEVE desaparecer**, e o versionamento **DEVE** seguir como `MAJOR.MINOR.PATCH` (SemVer puro).
  
* _Exemplo: ADEGPro está pronto para qualquer jogador usar sem medo._
  

📊 Componentes da Versão VRLC: Regras Detalhadas e Cosmovisão

Esta seção detalha cada componente da versão VRLC, integrando as regras de versionamento e a **cosmovisão do VRLC sobre o sistema SemVer**, incluindo os casos especiais.

### Herdado (`HERDADO`)

O campo **`HERDADO`** **DEVE** ser o **segundo número** da versão (`CICLO.HERDADO.MAJOR.MINOR.PATCH[_DATA]`) e **DEVE** carregar a **continuidade histórica do projeto** e o **progresso entre os ciclos VRLC**.

* **Contexto:** O `HERDADO` **DEVE** garantir a continuidade do histórico de versões, tanto para versões anteriores à adoção do VRLC quanto para a transição entre os próprios ciclos de desenvolvimento do VRLC. Ele **DEVE** impedir o reinício artificial da contagem de `MAJOR` e **DEVE** refletir o amadurecimento contínuo do projeto.
  
* **Regras:**
  
  1. **Início do VRLC (Herança Pré-VRLC):** Se o projeto **ESTÁ ADOTANDO** o VRLC e **NÃO POSSUI** um histórico de ciclos VRLC anteriores, o campo `HERDADO` **DEVE** assumir o último valor `MAJOR` da versão anterior ao VRLC. Essa herança **DEVE** ser conceitualmente tratada como pertencente ao **legado**, independentemente do ciclo VRLC em que o projeto inicie.
    
    * _Exemplo 1:_ Se o projeto estava na `v15` antes do VRLC, e inicia no Ciclo 5 (fase experimental), a primeira versão VRLC **DEVERÁ** ser `5.16.1.0.0_20250611`. O `16` **DEVE** ser o `MAJOR` herdado do **legado** (v15 + 1).
      
    * _Exemplo 2:_ Se o projeto estava na `v15` antes do VRLC, e inicia no Ciclo 3 (fase estável), a primeira versão VRLC **DEVERÁ** ser `3.16.1.0.0_20250722`. O `16` **DEVE** ser o `MAJOR` herdado do **legado** (v15 + 1).
      
  2. **Transição entre Ciclos VRLC:** Ao transitar de um ciclo para o próximo (ex: do Ciclo 5 para o Ciclo 4), o campo `HERDADO` **DEVE** assumir o **último valor `MAJOR` alcançado no ciclo de desenvolvimento** _**anterior**_.
    
    * _Exemplo:_ Se o Ciclo 5 terminou com a versão `5.16.2.0.0`, ao iniciar o Ciclo 4, a primeira versão **DEVERÁ** ser `4.2.1.0.0_0710`. O `2` **DEVE** ser o último `MAJOR` do Ciclo 5.
  3. **Flexibilidade de Início:** Esta dinâmica **PERMITE** que um projeto inicie o VRLC em qualquer ciclo (ex: Ciclo 3), herdando o `MAJOR` do ciclo conceitual anterior (seja o **legado** ou um ciclo VRLC anterior), **desde que esteja na sua fase de maturidade correspondente**.
    
  4. **Estabilidade do `HERDADO` dentro do ciclo:** Uma vez que o valor `HERDADO` **É DEFINIDO** na transição para um novo ciclo, ele **DEVE permanecer fixo** durante todo o desenvolvimento dentro daquele ciclo. Ele **SÓ DEVERÁ** ser atualizado na próxima transição de ciclo.
    
* **Futuro do Número Herdado:**
  
  * O número `HERDADO` **DEVERÁ** ser atualizado a cada transição de ciclo, refletindo o `MAJOR` final do ciclo anterior.
    
  * Ele **SÓ DEVE** deixar de ser usado quando o sistema amadurecer **após a “Largada” (Ciclo 1)** e adotar uma contagem natural de versões no formato `MAJOR.MINOR.PATCH` (SemVer puro), sem a necessidade de manter o contexto de ciclos.
    

### MAJOR (`MAJOR`)

O **`MAJOR`** **DEVE** ser o **terceiro número** da versão (`CICLO.HERDADO.MAJOR.MINOR.PATCH[_DATA]`) e **REPRESENTA** uma **grande atualização funcional ou conceitual** dentro do mesmo ciclo.

* **Significado:** O `MAJOR` **É RECOMENDADO** que seja alterado quando ocorre uma **mudança estrutural ou comportamental importante** no projeto, que **PODE** ou **NÃO PODE** quebrar a compatibilidade, mas **DEVE impactar significativamente** o software ou a experiência do usuário.
  
* **Quando Aumentar o MAJOR (Sugestões):**
  
  1. **Mudança de Funcionalidade Principal:** Uma nova mecânica principal **PODE** ser adicionada ao programa (ex: sistema de estratégia preditiva).
    
  2. **Alteração de Estrutura de Arquivos:** A estrutura dos arquivos gerados (como `.xlsx`, logs, etc.) **PODE** mudar, quebrando compatibilidade com versões anteriores.
    
  3. **Alteração/Remoção de Funções Públicas:** Uma função pública **PODE** ser alterada ou removida, exigindo adaptação de outros módulos ou usuários.
    
  4. **Substituição de Módulos:** Um módulo inteiro **PODE** ser substituído, reescrito ou realocado.
    
  5. **Novos Requisitos de Sistema:** **PODE** passar a exigir requisitos de sistema novos (ex: nova versão de Python, conexão obrigatória).
    
  6. **Integração/Mudança de API Externa:** Integração com API externa ou mudança de comunicação com sistemas como o GPro.
    
  7. **Exige Treinamento/Adaptação do Usuário:** Alterações que **EXIGEM** treinamento ou adaptação significativa do usuário.
    
  8. **Incompatibilidade de Dependências:** Incompatibilidade com versões antigas de dependências essenciais.
    
  9. **Mudança no Modo de Uso Principal:** Mudança significativa no modo de uso principal (ex: de terminal para GUI), alterando o fluxo mental do usuário.
    
  10. **Mudança de Filosofia/Identidade Funcional:** Mudança na filosofia ou identidade funcional do projeto (ex: de auxiliar para automatizador, ou alteração de narrativa que muda a interação).
    
  11. **Substituição de Bibliotecas Principais:** Substituição de bibliotecas principais por outras (ex: trocar `pandas` por `polars`) que **PODEM** quebrar a compatibilidade ou **PODEM** exigir modificações manuais no ambiente de execução.
    
  12. **Alterações em Leitura/Escrita de Arquivos (quebra de formato):** Alterações que **PODEM** mudar o formato ou estrutura dos arquivos gerados ou lidos pelo programa, quebrando compatibilidade com versões anteriores e **EXIGINDO** que usuários atualizem ou adaptem arquivos existentes.
    
* **Quando NÃO Aumentar o MAJOR (Sugestões de Classificação Alternativa):**
  
  * **Refatoração interna com mesmo comportamento externo:** **PODE** ser `MINOR`, `PATCH` ou `_DATA`, dependendo da sua abrangência interna.
    
  * **Correções de bugs ou ajustes de desempenho:** **PODE** ser `MINOR` (se melhoram estabilidade ou desempenho de forma notável) ou `PATCH` (se são correções pontuais ou ajustes sutis).
    
  * **Melhorias na interface sem quebra de funcionalidade:** **DEVE** ser `MINOR`.
    
  * **Traduções, renomeações pequenas, reorganizações visuais:** **PODE** ser `MINOR` (se houver nova funcionalidade, como suporte a um novo idioma), `PATCH` (se forem ajustes visíveis, mas sem impacto funcional), ou `_DATA` (se forem alterações mínimas e internas, como renomeação de variáveis locais).
    
  * **Melhorias incrementais nas funções existentes:** **PODE** ser `MINOR` (se adicionam novas capacidades) ou `PATCH` (se são variações ou atalhos de funcionalidades existentes).
    
  * **Mudanças em logs ou formatação de saída por si só:** **PODE** ser `MINOR` (se alteram significativamente a estrutura), `PATCH` (se são visíveis, mas não quebram estrutura), ou `_DATA` (se são mínimas e imperceptíveis).
    
  * **Ajustes em mensagens por clareza que NÃO ALTERAM o comportamento real do sistema:** **PODE** ser `_DATA` (se são mínimos e pontuais) ou `PATCH` (se melhoram a clareza ou evitam confusões).
    

### MINOR (`MINOR`)

O **`MINOR`** **DEVE** ser o **quarto número** da versão e **DEVE** ser usado para **adições, melhorias ou mudanças** que **SÃO** compatíveis com versões anteriores e **NÃO QUEBRAM** a funcionalidade principal.

* **Significado:** **INDICA** a adição de novas funcionalidades visíveis e estáveis, ou ajustes que aprimoram o software sem exigir grandes adaptações do usuário.
  
* **Quando Aumentar o MINOR (Sugestões):**
  
  1. **Novas Funcionalidades Pequenas:** Adição de funcionalidades novas, mesmo que pequenas, que **PODEM** ampliar as capacidades do programa (**PODEM** ser opcionais).
    
  2. **Correções de Bugs que Melhoram Estabilidade:** Correções de bugs ou falhas que **PODEM** melhorar a estabilidade sem alterar a interface do usuário.
    
  3. **Inclusão/Remoção de Dependências (sem quebra):** Inclusão ou remoção de dependências externas que **NÃO QUEBRAM** o uso do projeto, mas **EXIGEM** nova instalação.
    
  4. **Melhorias na Documentação:** Melhorias na documentação ou comentários que **PODEM** impactar a compreensão do projeto.
    
  5. **Mudanças em Configuração/Formatos (compatíveis):** Mudanças em configuração padrão ou suporte a novos formatos que **NÃO QUEBRAM** compatibilidade.
    
  6. **Remoção de Funcionalidades Depreciadas:** Remoção de funcionalidades depreciadas (com aviso prévio).
    
  7. **Testes Automatizados/Acessibilidade:** Inclusão de testes automatizados ou melhorias de acessibilidade.
    
  8. **Ajustes de Interface Gráfica/Layout:** Interface gráfica ou layout **PODE** ser ajustado sem impacto na lógica, mas **MELHORANDO** a usabilidade sem alterar o fluxo de uso.
    
  9. **Refatorações Estruturais Amplas:** Refatorações internas de grande impacto, que **REESTRUTURAM** o projeto em nível de arquitetura interna, múltiplos arquivos ou módulos (ex: divisão de arquivos grandes em módulos, conversão para orientação a objetos, padronização massiva de estilo).
    
  10. **Ajustes de Mensagens (alteram interpretação):** Alterações em mensagens que **PODEM** perder nuances importantes ou **PODEM** alterar levemente a interpretação, impactando o significado percebido.
    
  11. **Ajustes em Leitura/Escrita de Arquivos (interpretação):** Ajustes que **PODEM** modificar a forma como os arquivos são interpretados (sem mudar o formato básico), como suporte a variações ou formatos estendidos.
    
  12. **Alterações no Comportamento de Avisos:** Mudanças que **PODEM** alterar o comportamento dos avisos, impactando como o usuário reage ou o fluxo do programa (ex: transformar aviso em erro, remover mensagens que **PODEM** bloquear ações).
    
  13. **Mudanças Significativas no Log:** Mudanças significativas na estrutura ou padronização do log que **PODEM** impactar scripts ou automações.
    
  14. **Mudanças Significativas em Arquivos de Saída:** Mudanças significativas na estrutura de apresentação ou no formato do arquivo de saída (ex: `.xlsx` para `.csv`), que **PODEM** impactar ferramentas externas.
    
  15. **Mudança de Narrativa (puramente conceitual/estética):** Troca de nomes, temas ou personagens sem impacto na usabilidade ou lógica.
    
* **Quando NÃO Aumentar o MINOR (Sugestões de Classificação Alternativa):**
  
  * **Correções mínimas sem impacto funcional ou detalhes visuais/textuais:** **DEVE** ser `_DATA`.
    
  * **Refatorações internas invisíveis ou pequenas e localizadas:** **PODE** ser `_DATA` (se invisíveis e insignificantes) ou `PATCH` (se pequenas e localizadas).
    
  * **Ajustes estéticos ou corretivos em mensagens que NÃO ALTERAM o sentido:** **DEVE** ser `_DATA`.
    
  * **Reorganização de imports puramente estética:** **PODE** ser `_DATA` ou `PATCH`.
    
  * **Funcionalidades que SÃO apenas variações, atalhos ou extensões mínimas de algo que já existe (quase imperceptíveis):** **DEVE** ser `PATCH`.
    

### PATCH (`PATCH`)

O **`PATCH`** **DEVE** ser o **quinto número** da versão e **REFERE-SE** a **correções simples e localizadas**, sem impacto funcional significativo.

* **Significado:** **É RECOMENDADO** que seja usado para corrigir falhas, melhorar a estabilidade ou refinar aspectos técnicos sem introduzir novas funcionalidades ou quebrar a compatibilidade.
  
* **Quando Aumentar o PATCH (Sugestões):**
  
  1. **Correções de Falhas Específicas:** **PODE** corrigir falhas raras, bordas ou exceções específicas.
    
  2. **Melhorias de Estabilidade/Tratamento de Erro:** **PODE** melhorar a estabilidade, tratamento de erro ou compatibilidade.
    
  3. **Ajustes em Logs/Comentários Técnicos:** **PODE** ajustar logs ou comentários técnicos.
    
  4. **Refinamento de Permissões/Mensagens de Erro:** **PODE** refinar o sistema de permissões ou mensagens de erro.
    
  5. **Melhorias em Testes/Leitura de Arquivos:** **PODE** incluir melhorias em testes, ajustes de leitura de arquivos ou logs.
    
  6. **Mudança em Nomes de Variáveis/Funções Locais:** Mudança em nomes de variáveis **locais** ou funções auxiliares que **NÃO AFETAM** outras partes do código nem o usuário final.
    
  7. **Reorganização de Imports Estética:** Reorganização de imports puramente estética ou por organização interna.
    
  8. **Pequena Adição de Funcionalidade (Variação/Atalho):** A funcionalidade adicionada **NÃO É** nova de verdade, mas **SIM** uma **variação, atalho ou extensão mínima** de algo que já existe (quase imperceptível).
    
  9. **Correções Pontuais em Leitura/Escrita de Arquivos:** Correções pontuais e pequenas melhorias na leitura ou escrita de arquivos que **NÃO MUDAM** o formato nem a estrutura.
    
  10. **Atualizações de Mensagens (Suavização):** Ajustes que **SUAVIZAM** mensagens **SEM ALTERAR** seu significado ou impacto funcional, tornando-as menos intrusivas ou mais claras, mas mantendo o nível de severidade.
    
  11. **Atualizações no Formato de Log (Visíveis, sem quebra):** Mudanças **VISÍVEIS** no formato de log, mas que **NÃO QUEBRAM** estrutura e **NÃO AFETAM** ferramentas externas que analisam o log.
    
  12. **Alterações de Espaçamento/Formatação em Arquivos de Saída (Perceptíveis, compatíveis):** Mudança **PERCEPTÍVEL** na formatação de arquivos de saída (ex: marcadores, listas), mas que **AINDA SÃO** compatíveis com leituras anteriores.
    
  13. **Ajustes de Mensagens (Clareza/Evitar Confusão):** Ajustes em mensagens que **MELHORAM** a clareza ou **EVITAM** confusões, sem impacto semântico relevante.
    
* **Quando NÃO Aumentar o PATCH (Sugestões de Classificação Alternativa):**
  
  * **Correções puramente visuais/gramaticais ou reorganizações irrelevantes:** **DEVEM** se enquadrar em `_DATA`.
    
  * **Mudanças de performance mínimas:** **DEVE** ser `_DATA`.
    

### Data (`_DATA`)

O sufixo **`_DATA`** **DEVE** ser o **último componente** da versão e **DEVE** ser uma **marca temporal** usada para indicar que uma versão sofreu **alterações tão pequenas**, que o comportamento do código **DEVE** continuar **virtualmente idêntico**, embora tecnicamente ele **TENHA SIDO** alterado.

* **Formato:**
  
  * `_MMDD` = Dia/Mês (ex: `_0710`) para alterações rotineiras.
    
  * `_YYYYMMDD` = Ano/Mês/Dia (ex: `_20250704`) para:
    
    * **Início do projeto (primeira versão).**
      
    * **Primeira modificação do projeto em um novo ano.**
      
  * O valor `_DATA` **SÓ DEVE** ser usado quando **NECESSÁRIO** – **NÃO É OBRIGATÓRIO** em toda versão.
    
* **Função:**
  
  * **NÃO REPRESENTA** um novo recurso ou correção relevante.
    
  * **SERVE** como **rastro técnico**: houve alteração no código, mas **NÃO O SUFICIENTE** para justificar um novo `minor` ou `patch`.
    
  * **INDICA** que duas versões **DEVEM** funcionar **exatamente igual**, mas **NÃO SÃO** idênticas em seu conteúdo binário ou textual.
    
* **Quando Usar `_DATA`:**
  
  1. **Mudança de Ciclo (Transição de Estágio):** Quando uma versão **MUDA** de ciclo (ex: de **oficina** para **vermelho**), a versão **DEVERÁ** ser sempre `X.Y.1.0.0_DATA`. Isso **INDICA** a data oficial da mudança de ciclo (**PODE** ser `_YYYYMMDD` se for a primeira do ano/projeto).
    
  2. **Alterações Mínimas que Não Merecem Novo Patch:**
    
    * Correções em comentários, ortografia, formatação textual ou debug.
      
    * Alterações internas de nomes, organização ou legibilidade sem impacto real (ex: troca de nomes de variáveis locais, remoção de comentários).
      
    * Mudanças em espaços, pontuações, formatações ou defaults inócuos.
      
    * Ajustes no formato de hora/data, mensagens auxiliares ou texto interno.
      
    * Ajustes mínimos nos imports que **NÃO ALTERAM** nem a ordem lógica nem a funcionalidade (ex: unificar imports em uma linha, quebra de linha em blocos de importação).
      
    * Mudanças estéticas ou corretivas em mensagens exibidas ao usuário que **NÃO ALTERAM** o sentido ou impacto.
      
    * Mudanças mínimas e imperceptíveis em logs ou arquivos de saída que **NÃO AFETAM** leitura ou processamento automatizado.
      
    * Reformulação mínima ou clareza em mensagens **SEM RETIRAR** nenhuma informação funcional ou mudar o tom original.
      
* **Quando NÃO Usar `_DATA`:**
  
  * **NÃO DEVE** usar `_DATA` se a mudança **EXIGE** `patch`, `minor` ou `major` real.
    
  * **NÃO DEVE** usar para mudanças de comportamento, novos recursos, refatorações visíveis ou bugs resolvidos.
    
  * **NÃO DEVE** usar `_DATA` como substituto de controle de versão real.
    
* **Por que isso é útil?**
  
  * **PERMITE** que você **DOCUMENTA** pequenas mudanças sem poluir o histórico com versões falsas.
    
  * **AJUDA** a saber **EXATAMENTE** quando o código foi alterado, mesmo que seja "invisível".
    
  * **TORNA FÁCIL** rastrear quando você mexeu em algo que “**NÃO DEVERIA** ter feito diferença, mas fez”.
    

Exemplos Práticos de Versionamento VRLC

Esta seção apresenta exemplos práticos que ilustram o uso dos componentes do VRLC e as transições entre ciclos.

### Início do VRLC com Herança Pré-VRLC

* `5.16.1.0.0_20250611`
  
  > Início do ciclo 5 em 11/06/2025. O projeto estava na versão 15 antes do VRLC, que **É HERDADA** como `16` (considerado o último MAJOR do **legado**).
  
* `3.16.1.0.0_20250722`
  
  > Início do ciclo 3 em 22/07/2025. O projeto estava na versão 15 antes do VRLC, que **É HERDADA** como `16` (considerado o último MAJOR do **legado**). Este exemplo **DEMONSTRA** o início do VRLC em um ciclo avançado.
  

### Início do VRLC sem Herança (começando do zero)

* `5.0.1.0.0_20250704`
  
  > Início do ciclo 5 sem herança (começando do zero), fase de prototipagem.
  

### Transição entre Ciclos VRLC

* `4.2.1.0.0_0710`
  
  > O ciclo 4 começou em 10/07. O ciclo anterior (Ciclo 5) foi encerrado com MAJOR 2, que **É HERDADO**.
  

### Nova Funcionalidade Importante

* `5.16.2.0.0`
  
  > Nova funcionalidade importante no Ciclo 5.
  
* `4.2.2.0.0`
  
  > Outra funcionalidade importante no Ciclo 4.
  

### Primeira Modificação do Projeto no Ano

* `4.2.2.1.0_20260210`
  
  > Modificação menor feita pela primeira vez em 10/02/2026.
  

### Versão Gêmea (Modificações Mínimas)

* `5.16.2.0.0_0710`
  
  > Versão gêmea de `5.16.2.0.0` com ajustes mínimos feitos em 10/07.
  
* `2.0.0_0805`
  
  > Segue SemVer, gêmeo da versão `2.0.0` (após a fase de Largada).
  

### Tabela de Evolução com `HERDADO` Dinâmico

| Versão | Ciclo | Herdado | Major | Minor | Patch | Descrição |
| --- | --- | --- | --- | --- | --- | --- |
| `5.16.1.0.0_20250611` | Oficina | 16  | 1   | 0   | 0   | Protótipo interno (herda 16 do **legado** pré-VRLC) iniciado no dia 11/06/2025 |
| `5.16.2.0.0` | Oficina | 16  | 2   | 0   | 0   | Nova funcionalidade importante no Ciclo 5 |
| `5.16.2.0.0_0710` | Oficina | 16  | 2   | 0   | 0   | Versão gêmea de `5.16.2.0.0` (mudanças insignificantes) |
| `4.2.1.0.0_0710` | Vermelho | 2   | 1   | 0   | 0   | Ciclo vermelho iniciado dia 10/07 (herda o MAJOR 2 do Ciclo 5) |
| `4.2.2.0.0` | Vermelho | 2   | 2   | 0   | 0   | Outra funcionalidade importante no Ciclo 4 |
| `4.2.2.1.0_20260210` | Vermelho | 2   | 2   | 1   | 0   | Modificação menor feita pela primeira vez em 10/02/2026 |
| `3.2.1.0.0_0722` | Amarelo | 2   | 1   | 0   | 0   | UI e núcleo funcional, ciclo novo (herda o MAJOR 2 do Ciclo 4) iniciado no dia 22/07 |
| `2.1.1.0.0_0730` | Verde | 1   | 1   | 0   | 0   | Pronto para uso comum (herda o MAJOR 1 do Ciclo 3) iniciado no dia 30/07 |
| `1.1.1.0.0_0805` | Largada | 1   | 1   | 0   | 0   | Versão madura, para uso geral (herda o MAJOR 1 do Ciclo 2) iniciado no dia 05/08 |
| `2.0.0` | Largada+ | N/A | 2   | 0   | 0   | Depois da Largada, estágio e HERDADO somem, segue SemVer |
| `2.0.0_0805` | Largada+ | N/A | 2   | 0   | 0   | Segue SemVer, gêmeo do ciclo `2.0.0` |
| `3.16.1.0.0_20250722` | Amarelo | 16  | 1   | 0   | 0   | UI e núcleo funcional (herda 16 do **legado** pré-VRLC em fase avançada) iniciado no dia 22/07/2025 |