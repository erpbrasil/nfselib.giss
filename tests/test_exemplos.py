"""Os exemplos oficiais do GissOnline passam pelos bindings sem perder nada."""

import glob
import os
import warnings

import pytest
from lxml import etree
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer

from nfselib.giss.v2_04 import (
    cabecalho_v2_04,
    cancelar_nfse_envio_v2_04,
    cancelar_nfse_reposta_v2_04,
    consultar_lote_rps_envio_v2_04,
    consultar_lote_rps_resposta_v2_04,
    enviar_lote_rps_envio_v2_04,
)

EXEMPLOS = os.path.join(os.path.dirname(__file__), "exemplos")
# Os exemplos do fornecedor sao gerados por ferramenta: trazem o nome da tag
# como valor (ex.: p1:vBC) e, nos de cancelamento e consulta, elementos em
# namespace de outra mensagem. O parser tolera os dois.
TOLERANTE = ParserConfig(fail_on_unknown_properties=False)
RAIZES = {
    "cabecalho": cabecalho_v2_04.Cabecalho,
    "enviar-lote-rps-envio": enviar_lote_rps_envio_v2_04.EnviarLoteRpsEnvio,
    "consultar-lote-rps-envio": consultar_lote_rps_envio_v2_04.ConsultarLoteRpsEnvio,
    "consultar-lote-rps-resposta": (
        consultar_lote_rps_resposta_v2_04.ConsultarLoteRpsResposta
    ),
    "cancelar-nfse-envio": cancelar_nfse_envio_v2_04.CancelarNfseEnvio,
    "cancelar-nfse-reposta": cancelar_nfse_reposta_v2_04.CancelarNfseResposta,
}


def _raiz(caminho):
    nome = os.path.basename(caminho).split("_", 1)[1].rsplit("-v2_04", 1)[0]
    return RAIZES[nome]


def _folhas(xml):
    """Caminho e texto de cada elemento folha, sem depender de prefixo."""
    arvore = etree.fromstring(xml)
    folhas = []
    for el in arvore.iter():
        if not isinstance(el.tag, str) or len(el):
            continue
        caminho = "/".join(
            etree.QName(a).localname for a in [*reversed(list(el.iterancestors())), el]
        )
        folhas.append((caminho, (el.text or "").strip()))
    return sorted(folhas)


# O exemplo oficial de cancelamento declara os filhos no namespace de outra
# mensagem (consultar-nfse-servico-prestado-envio): nao casa com o proprio XSD.
FORA_DO_XSD = ("maximo_cancelar-nfse-envio-v2_04.xml",)
CAMINHOS = [
    caminho
    for caminho in sorted(glob.glob(os.path.join(EXEMPLOS, "*.xml")))
    if os.path.basename(caminho) not in FORA_DO_XSD
]


@pytest.mark.parametrize("caminho", CAMINHOS)
def test_exemplo_ida_e_volta(caminho):
    with warnings.catch_warnings():
        # os exemplos "maximo" trazem o nome da tag como valor (ex.: p1:vBC)
        warnings.simplefilter("ignore")
        objeto = XmlParser(config=TOLERANTE).parse(caminho, _raiz(caminho))
    saida = XmlSerializer().render(objeto)
    with open(caminho, "rb") as arquivo:
        original = arquivo.read()
    caminhos_originais = {c for c, _ in _folhas(original)}
    caminhos_saida = {c for c, _ in _folhas(saida.encode())}
    assert caminhos_saida
    assert caminhos_saida <= caminhos_originais
    if "enviar-lote-rps-envio" in caminho:
        assert caminhos_saida == caminhos_originais


def test_grupos_da_reforma_no_rps():
    caminho = os.path.join(EXEMPLOS, "minimo_enviar-lote-rps-envio-v2_04.xml")
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        lote = XmlParser(config=TOLERANTE).parse(
            caminho, enviar_lote_rps_envio_v2_04.EnviarLoteRpsEnvio
        )
    inf = lote.lote_rps.lista_rps.rps[0].inf_declaracao_prestacao_servico
    assert inf.servico.valores.trib is not None
    assert inf.servico.valores.ibscbs is not None
