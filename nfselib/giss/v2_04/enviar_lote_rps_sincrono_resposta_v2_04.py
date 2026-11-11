from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from nfselib.giss.v2_04.tipos_v2_04 import (
    CompNfse,
    ListaMensagemAlertaRetorno,
    ListaMensagemRetorno,
    ListaMensagemRetornoLote,
)

__NAMESPACE__ = (
    "http://www.giss.com.br/enviar-lote-rps-sincrono-resposta-v2_04.xsd"
)


@dataclass(kw_only=True)
class EnviarLoteRpsSincronoResposta:
    class Meta:
        namespace = "http://www.giss.com.br/enviar-lote-rps-sincrono-resposta-v2_04.xsd"

    numero_lote: None | int = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "total_digits": 15,
        },
    )
    data_recebimento: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "DataRecebimento",
            "type": "Element",
        },
    )
    protocolo: None | str = field(
        default=None,
        metadata={
            "name": "Protocolo",
            "type": "Element",
            "max_length": 50,
        },
    )
    lista_nfse: None | EnviarLoteRpsSincronoResposta.ListaNfse = field(
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
