from __future__ import annotations

from dataclasses import dataclass, field

from nfselib.giss.v2_04.tipos_v2_04 import (
    CompNfse,
    ListaMensagemAlertaRetorno,
    ListaMensagemRetorno,
    ListaMensagemRetornoLote,
)

__NAMESPACE__ = "http://www.giss.com.br/consultar-lote-rps-resposta-v2_04.xsd"


@dataclass(kw_only=True)
class ConsultarLoteRpsResposta:
    class Meta:
        namespace = (
            "http://www.giss.com.br/consultar-lote-rps-resposta-v2_04.xsd"
        )

    situacao: str = field(
        metadata={
            "name": "Situacao",
            "type": "Element",
            "pattern": r"1|2|3|4",
        }
    )
    lista_nfse: None | ConsultarLoteRpsResposta.ListaNfse = field(
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
    lista_mensagem_retorno_lote: None | ListaMensagemRetornoLote = field(
        default=None,
        metadata={
            "name": "ListaMensagemRetornoLote",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )

    @dataclass(kw_only=True)
    class ListaNfse:
        comp_nfse: list[CompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
                "min_occurs": 1,
            },
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
