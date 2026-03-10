"""
src/vrlc/vrlc.py

VRLC – VagalumeRaceLightCycle com núcleo SemVer
Módulo para manipulação de versões no formato VRLC, utilizando
a biblioteca 'semantic_version' para a parte SemVer.

Uso típico:
    from vrlc import VRLCVersion

    v = VRLCVersion("5.0.1.0.0_20260228")
    print(f"Caqui {v.estendida}")   # Caqui 5.0.1.0.0_20260228
    print(f"Caqui {v.resumida}")    # Caqui 1.0.0 (oficina)
    print(f"Caqui {v.compacta}")    # Caqui 1 (oficina)

    # Após o ciclo 1 (formato SemVer)
    v2 = VRLCVersion("1.17.0_0228")
    print(v2.estendida)   # 1.17.0_0228
    print(v2.resumida)    # 1.17.0
    print(v2.compacta)    # 1.17
"""

import re
import datetime
import warnings
from semantic_version import Version as SemVerVersion
from ._version import __version__  # Import relativo do gerado pelo scm

version = __version__  # Sem o ponto solto e aspa maluca

class VRLCVersion:
    """
    Representa uma versão VRLC ou SemVer, com suporte a parsing,
    comparação e incremento, aproveitando a biblioteca semantic_version.

    Atributos disponíveis:
        ciclo (int or None):    estágio de desenvolvimento (5 a 1) ou None se SemVer
        herdado (int or None):  último MAJOR do ciclo anterior ou None se SemVer
        major (int):            versão principal (>=1)
        minor (int):            versão com novas funcionalidades compatíveis (>=0)
        patch (int):            correções simples (>=0)
        data (str):             sufixo temporal (MMDD ou YYYYMMDD) ou vazio

        TODO: verificar se os testes de versão contemplam todas as situaçẽos possíveis imagináveis
    """

    # Mapeamento de ciclos para nomes (usado nas representações resumida/compacta)
    NOMES_CICLOS = {
        5: "oficina",
        4: "vermelho",
        3: "amarelo",
        2: "verde",
        1: "largada"
    }

    # Padrões regex para os dois formatos aceitos
    _REGEX_VRLC = re.compile(
        r"^(?P<ciclo>[1-5])\.(?P<herdado>\d+)\.(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)(?:_(?P<data>\d{4,8}))?$"
    )
    _REGEX_SEMVER = re.compile(
        r"^(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)(?:_(?P<data>\d{4,8}))?$"
    )

    def __init__(self, version_string):
        """
        Inicializa a versão a partir de uma string.
        Aceita os formatos:
          - VRLC:   ciclo.herdado.major.minor.patch[_data]
          - SemVer: major.minor.patch[_data]
        """
        # Tenta o formato VRLC primeiro
        match_vrlc = self._REGEX_VRLC.match(version_string)
        if match_vrlc:
            self.ciclo = int(match_vrlc.group("ciclo"))
            self.herdado = int(match_vrlc.group("herdado"))
            self.major = int(match_vrlc.group("major"))
            self.minor = int(match_vrlc.group("minor"))
            self.patch = int(match_vrlc.group("patch"))
            self.data = match_vrlc.group("data") or ""
            self._formato = "vrlc"
            # Guarda as strings originais para validação de data
            self._herdado_str = match_vrlc.group("herdado")
            self._major_str = match_vrlc.group("major")
            self._minor_str = match_vrlc.group("minor")
            self._patch_str = match_vrlc.group("patch")
            # Validações específicas VRLC
            self._validar_vrlc()
        else:
            # Tenta o formato SemVer
            match_semver = self._REGEX_SEMVER.match(version_string)
            if match_semver:
                self.ciclo = None
                self.herdado = None
                self.major = int(match_semver.group("major"))
                self.minor = int(match_semver.group("minor"))
                self.patch = int(match_semver.group("patch"))
                self.data = match_semver.group("data") or ""
                self._formato = "semver"
                # Guarda as strings originais
                self._major_str = match_semver.group("major")
                self._minor_str = match_semver.group("minor")
                self._patch_str = match_semver.group("patch")
                # Validações gerais (major, minor, patch)
                self._validar_componentes()
            else:
                raise ValueError(
                    f"Formato inválido: {version_string}. "
                    "Esperado: CICLO.HERDADO.MAJOR.MINOR.PATCH[_DATA] ou MAJOR.MINOR.PATCH[_DATA]"
                )

        # Validações comuns (data)
        self._validar_data()

        # Verifica se algum componente parece data (apenas se não houver data no sufixo ex: 0228, 20260228)
        self._verificar_componentes_data()

        # Cria a versão SemVer interna (para delegação)
        self._semver = SemVerVersion(
            major=self.major,
            minor=self.minor,
            patch=self.patch,
            prerelease=None,
            build=None
        )

    def _validar_componentes(self):
        """Validações básicas de major, minor, patch."""
        if self.major < 1:
            raise ValueError(f"MAJOR deve ser >= 1, obtido: {self.major}")
        if self.minor < 0:
            raise ValueError(f"MINOR deve ser >= 0, obtido: {self.minor}")
        if self.patch < 0:
            raise ValueError(f"PATCH deve ser >= 0, obtido: {self.patch}")

    def _validar_vrlc(self):
        """Validações específicas para formato VRLC."""
        if self.ciclo < 1 or self.ciclo > 5:
            raise ValueError(f"Ciclo deve ser entre 1 e 5, obtido: {self.ciclo}")
        # Regra do herdado:
        # - Ciclo 5: herdado pode ser 0 (significa "sem versão anterior")
        # - Ciclos 4,3,2,1: herdado deve ser >= 1
        if self.ciclo == 5:
            if self.herdado < 0:
                raise ValueError(f"Herdado no ciclo 5 deve ser >= 0, obtido: {self.herdado}")
        else:
            if self.herdado < 1:
                raise ValueError(f"Herdado no ciclo {self.ciclo} deve ser >= 1, obtido: {self.herdado}")
        # MAJOR, MINOR, PATCH
        self._validar_componentes()

        # Regra: primeira versão de um ciclo (major=1, minor=0, patch=0) deve ter data completa (8 dígitos)
        if self.major == 1 and self.minor == 0 and self.patch == 0:
            if not self.data or len(self.data) != 8:
                raise ValueError(
                    f"Primeira versão do ciclo {self.ciclo} deve ter data completa no formato _YYYYMMDD. "
                    f"Recebido: data={self.data!r}"
                )
        
        # TODO: Implementar RECALL de SemVer → VRLC
        #       Permitir bump com recall_ciclo=2..5 para reativar ciclo/herdado em casos graves
        #       Ex: "2.1.0" → bump_major(recall_ciclo=2, data="20270503") → "2.2.1.0.0_20270503" (ou herdado +1)
        # ---
        # Regra especial para ciclo 1: só a primeira versão é permitida no formato VRLC
        if self.ciclo == 1 and not (self.major == 1 and self.minor == 0 and self.patch == 0):
            raise ValueError(
                f"Ciclo 1 só permite a primeira versão (major=1, minor=0, patch=0). "
                f"Versões seguintes devem ser SemVer puras (sem ciclo/herdado)."
            )

    def _validar_data(self):
        """Valida o formato da data, se presente."""
        if not self.data:
            return
        if len(self.data) not in (4, 8):
            raise ValueError(f"DATA deve ter 4 (MMDD) ou 8 (YYYYMMDD) dígitos, obtido: {self.data}")
        if not self.data.isdigit():
            raise ValueError(f"DATA deve conter apenas dígitos, obtido: {self.data}")
        # Validação de data real e ano mínimo (>=1900) para 8 dígitos
        if len(self.data) == 8:
            try:
                ano = int(self.data[0:4])
                mes = int(self.data[4:6])
                dia = int(self.data[6:8])
                if ano < 1900:
                    raise ValueError(f"Ano {ano} muito antigo (deve ser >= 1900)")
                datetime.date(ano, mes, dia)
            except ValueError as e:
                raise ValueError(f"Data inválida: {self.data} ({e})")
        elif len(self.data) == 4:
            # Apenas valida mês e dia (ano implícito)
            mes = int(self.data[0:2])
            dia = int(self.data[2:4])
            try:
                # Usa um ano qualquer (ex: 2000) para validar a combinação mês/dia
                datetime.date(2000, mes, dia)
            except ValueError as e:
                raise ValueError(f"Data (MMDD) inválida: {self.data} ({e})")

    def _eh_data_valida(self, s):
        """Retorna True se a string s (4 ou 8 dígitos) for uma data válida (MMDD ou YYYYMMDD)."""
        if len(s) == 8:
            try:
                ano = int(s[0:4])
                mes = int(s[4:6])
                dia = int(s[6:8])
                datetime.date(ano, mes, dia)
                return True
            except ValueError:
                return False
        elif len(s) == 4:
            try:
                mes = int(s[0:2])
                dia = int(s[2:4])
                datetime.date(2000, mes, dia)
                return True
            except ValueError:
                return False
        return False

    def _verificar_componentes_data(self):
        """
        Emite um aviso se algum componente (exceto ciclo) tiver 4 ou 8 dígitos e for uma data válida,
        e não houver data no sufixo. A sugestão é adicionar um zero à esquerda para desabilitar o aviso.
        """
        if self.data:
            # Se já tem data no sufixo, não há ambiguidade
            return

        componentes = []
        if self._formato == "vrlc":
            componentes = [
                ("herdado", self._herdado_str),
                ("major", self._major_str),
                ("minor", self._minor_str),
                ("patch", self._patch_str)
            ]
        else:  # semver
            componentes = [
                ("major", self._major_str),
                ("minor", self._minor_str),
                ("patch", self._patch_str)
            ]

        for nome, valor_str in componentes:
            # Verifica se a string tem 4 ou 8 dígitos e é uma data válida
            if len(valor_str) in (4, 8) and self._eh_data_valida(valor_str): # Tenta interpretar como data
                warnings.warn(
                    f"Data no campo '{nome}' ({valor_str}). Isso foi intencional? "
                    f"Ponha um 0 à esquerda do campo '{nome}' para desligar o aviso.",
                    UserWarning,
                    stacklevel=3  # Para apontar para a linha do usuário, não para dentro da classe
                )

    @property
    def estendida(self):
        """Formato completo de armazenamento (igual à string de entrada)."""
        if self._formato == "vrlc":
            base = f"{self.ciclo}.{self.herdado}.{self.major}.{self.minor}.{self.patch}"
        else:  # semver
            base = f"{self.major}.{self.minor}.{self.patch}"
        return f"{base}_{self.data}" if self.data else base

    @property
    def resumida(self):
        """
        Formato resumido para exibição:
          - Se for VRLC e não for pós‑largada: "MAJOR.MINOR.PATCH (nome_do_ciclo)"
          - Caso contrário (SemVer ou pós‑largada): "MAJOR.MINOR.PATCH"
        """
        base = f"{self.major}.{self.minor}.{self.patch}"
        # Determina se deve mostrar o nome do ciclo
        if self._formato == "vrlc":
            # Ciclo 1 com major=1, minor=0, patch=0 é a largada (mostra nome)
            # Qualquer outra combinação no ciclo 1 não deveria existir, mas por segurança não mostra nome
            if self.ciclo == 1 and not (self.major == 1 and self.minor == 0 and self.patch == 0):
                return base
            nome = self.NOMES_CICLOS.get(self.ciclo, "desconhecido")
            return f"{base} ({nome})"
        return base

    @property
    def compacta(self):
        """
        Formato compacto para exibição:
          - "MAJOR" + (".MINOR" se MINOR != 0)
          - Se for VRLC e não for pós‑largada, acrescenta " (nome_do_ciclo)"
        O patch nunca é exibido.
        """
        if self.minor == 0:
            major_part = str(self.major)
        else:
            major_part = f"{self.major}.{self.minor}"

        if self._formato == "vrlc":
            # Mesma regra da resumida: pós‑largada não mostra ciclo
            if self.ciclo == 1 and not (self.major == 1 and self.minor == 0 and self.patch == 0):
                return major_part
            nome = self.NOMES_CICLOS.get(self.ciclo, "desconhecido")
            return f"{major_part} ({nome})"
        return major_part

    # --- Métodos SemVer úteis herdados da biblioteca ---
    def bump_major(self, novo_ciclo=None, novo_herdado=None, data=""):
        """
        Incrementa a versão MAJOR, reiniciando MINOR e PATCH.
        Se for VRLC, permite especificar novo ciclo e herdado.
        Se o ciclo atual for 1 (largada), a nova versão será SemVer (ciclo=None).
        """
        nova_semver = self._semver.next_major()
        if self._formato == "vrlc" and self.ciclo != 1:
            # Mantém VRLC, a menos que seja ciclo 1
            ciclo = novo_ciclo if novo_ciclo is not None else self.ciclo
            herdado = novo_herdado if novo_herdado is not None else self.herdado
            return VRLCVersion.from_parts(ciclo, herdado, nova_semver.major, 0, 0, data)
        else:
            # Se for ciclo 1 ou já SemVer, transiciona para SemVer
            return VRLCVersion.from_parts(None, None, nova_semver.major, 0, 0, data)

    def bump_minor(self, data=""):
        nova_semver = self._semver.next_minor()
        if self._formato == "vrlc" and self.ciclo != 1:
            return VRLCVersion.from_parts(self.ciclo, self.herdado, nova_semver.major, nova_semver.minor, 0, data)
        else:
            return VRLCVersion.from_parts(None, None, nova_semver.major, nova_semver.minor, 0, data)

    def bump_patch(self, data=""):
        nova_semver = self._semver.next_patch()
        if self._formato == "vrlc" and self.ciclo != 1:
            return VRLCVersion.from_parts(self.ciclo, self.herdado, nova_semver.major, nova_semver.minor, nova_semver.patch, data)
        else:
            return VRLCVersion.from_parts(None, None, nova_semver.major, nova_semver.minor, nova_semver.patch, data)

    @classmethod
    def from_parts(cls, ciclo, herdado, major, minor, patch, data=""):
        """Constrói uma versão a partir de componentes."""
        if ciclo is not None:
            s = f"{ciclo}.{herdado}.{major}.{minor}.{patch}"
        else:
            s = f"{major}.{minor}.{patch}"
        if data:
            s += f"_{data}"
        return cls(s)

    def __str__(self):
        return self.estendida

    def __repr__(self):
        return f"VRLCVersion('{self.estendida}')"

    # Delegação de comparações para a biblioteca subjacente
    def __eq__(self, other):
        if not isinstance(other, VRLCVersion):
            return NotImplemented
        return self._semver == other._semver and self.data == other.data

    def __lt__(self, other):
        if not isinstance(other, VRLCVersion):
            return NotImplemented
        if self._semver != other._semver:
            return self._semver < other._semver
        return self.data < other.data
# Outros métodos de comparação (__gt__, __le__, __ge__) podem ser implementados similarmente
# TODO: verificar se os testes de versão contemplam todas as situaçẽos possíveis imagináveis
# Exemplo de uso (executado apenas se o módulo for chamado diretamente)
if __name__ == "__main__":
    # Testes com os exemplos válidos
    exemplos_validos = [
        "5.0.1.0.0_20260228",          # oficina primeira versão
        "5.3.1.0.0_20260228",          # oficina com herdado 3 (projeto iniciou antes do VRLC)
        "5.0.1.0.1",                   # oficina patch 1
        "5.0.1.0.1_0228",              # oficina versão gêmea
        "5.0.20.3.5",                  # oficina final
        "4.20.1.0.0_20260228",         # vermelho primeira versão
        "4.20.1.0.1",                  # vermelho
        "4.20.2.0.0",                  # vermelho major 2
        "4.20.2.0.0_0228",             # vermelho versão gêmea
        "4.20.6.9.1",                  # vermelho final
        "3.6.1.0.0_20260228",          # amarelo primeira versão
        "3.6.5.0.0",                   # amarelo
        "3.6.5.0.0_0228",              # amarelo versão gêmea
        "3.6.7.17.10",                 # amarelo final
        "2.7.1.0.0_20260228",          # verde primeira versão
        "2.7.3.7.10",                  # verde
        "2.7.3.7.10_0228",             # verde versão gêmea
        "2.7.23.100.100",              # verde final
        "1.23.1.0.0_20260228",         # largada (única com ciclo 1)
        "1.17.50",                     # pós‑largada SemVer puro
        "1.17.50_0228",                # pós‑largada com data
        "5.4.1",                       # pós‑largada
        "1.0.1",                       # pós‑largada SemVer puro
        "1.0.1_0228",                  # SemVer com data (versão gêmea)
        "1.17.0",                      # SemVer puro
        "1.17.0_0228",                 # SemVer com data (versão gêmea)
        "1.1.0_20260228",              # SemVer com data completa (primeira do ano)
    ]

    print("Testando parsing e representações (com avisos de data):\n")
    for ex in exemplos_validos:
        v = VRLCVersion(ex)
        print(f"{v.estendida:30} -> {v.resumida:25} -> {v.compacta}")

    # Demonstração da transição de ciclo 1 para SemVer
    print("\n--- Transição a partir da largada ---")
    v_largada = VRLCVersion("1.23.1.0.0_20260228")
    print(f"Original: {v_largada.estendida} -> {v_largada.resumida} -> {v_largada.compacta}")
    v_proxima = v_largada.bump_minor()
    print(f"Após bump_minor: {v_proxima.estendida} -> {v_proxima.resumida} -> {v_proxima.compacta}")
    v_com_data = v_proxima.bump_patch(data="0301")
    print(f"Após bump_patch com data: {v_com_data.estendida} -> {v_com_data.resumida} -> {v_com_data.compacta}")

    # Testes de validação (alguns devem gerar avisos, outros erros)
    print("\n--- Testes de validação (avisos e erros esperados) ---")
    casos_teste = [
        "1.1020.1230",                  # Sem data, minor e patch parecem datas (deve gerar aviso)
        "1.1020.1230_20260228",          # Com data no sufixo, não deve gerar aviso
        "5.0.1.0.0228",                  # patch com data sem underscore (deve gerar aviso)
        "5.0.1.0.20260228",               # patch com data sem underscore (deve gerar aviso)
        "4.1.1.0.0",                      # primeira versão sem data (erro)
        "1.1.1.0.020260228",              # patch enorme (9 dígitos) – não se aplica, só 4/8 dígitos
        "5.0.1.0.0_20260240",             # data inválida (erro)
        "3.1.1.0.0_13500228",             # ano muito antigo (erro)
        "4.0.1.0.0_20260228",             # herdado=0 em ciclo 4 (erro)
        "1.1.1.1.0_20260228",             # ciclo 1 com versão que não é a primeira (erro)
    ]

    for ex in casos_teste:
        try:
            print(f"\n>>> Testando: {ex}")
            v = VRLCVersion(ex)
            print(f"  OK: {v.estendida} -> {v.resumida} -> {v.compacta}")
        except ValueError as e:
            print(f"  ERRO (esperado): {e}")
        # O aviso será impresso automaticamente pelo sistema de warnings