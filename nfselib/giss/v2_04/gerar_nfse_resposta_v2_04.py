from __future__ import annotations

from dataclasses import dataclass, field

from nfselib.giss.v2_04.tipos_v2_04 import (
    CompNfse,
    ListaMensagemAlertaRetorno,
    ListaMensagemRetorno,
)

__NAMESPACE__ = "http://www.giss.com.br/gerar-nfse-resposta-v2_04.xsd"


@dataclass(kw_only=True)
class GerarNfseResposta:
    class Meta:
        namespace = "http://www.giss.com.br/gerar-nfse-resposta-v2_04.xsd"

    lista_nfse: None | GerarNfseResposta.ListaNfse = field(
        default=None,
        metadata={
            "name": "ListaNfse",
            "type": "Element",
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

    @dataclass(kw_only=True)
    class ListaNfse:
        comp_nfse: CompNfse = field(
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            }
        )
        lista_mensagem_alerta_retorno: None | ListaMensagemAlertaRetorno = (
            field(
                default=None,
                metadata={
                    "name": "ListaMensagemAlertaRetorno",
                    "type": "Element",
                    "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
                },
            )
        )
