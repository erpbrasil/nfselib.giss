from __future__ import annotations

from dataclasses import dataclass, field

from nfselib.giss.v2_04.tipos_v2_04 import (
    CompNfse,
    ListaMensagemRetorno,
)

__NAMESPACE__ = "http://www.giss.com.br/consultar-nfse-rps-resposta-v2_04.xsd"


@dataclass(kw_only=True)
class ConsultarNfseRpsResposta:
    class Meta:
        namespace = (
            "http://www.giss.com.br/consultar-nfse-rps-resposta-v2_04.xsd"
        )

    comp_nfse: None | CompNfse = field(
        default=None,
        metadata={
            "name": "CompNfse",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    lista_mensagem_retorno: None | ListaMensagemRetorno = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetorno",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
