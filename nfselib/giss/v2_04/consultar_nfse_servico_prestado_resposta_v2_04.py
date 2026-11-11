from __future__ import annotations

from dataclasses import dataclass, field

from nfselib.giss.v2_04.tipos_v2_04 import (
    CompNfse,
    ListaMensagemRetorno,
)

__NAMESPACE__ = (
    "http://www.giss.com.br/consultar-nfse-servico-prestado-resposta-v2_04.xsd"
)


@dataclass(kw_only=True)
class ConsultarNfseServicoPrestadoResposta:
    class Meta:
        namespace = "http://www.giss.com.br/consultar-nfse-servico-prestado-resposta-v2_04.xsd"

    lista_nfse: None | ConsultarNfseServicoPrestadoResposta.ListaNfse = field(
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
        comp_nfse: list[CompNfse] = field(
            default_factory=list,
            metadata={
                "name": "CompNfse",
                "type": "Element",
                "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
                "min_occurs": 1,
                "max_occurs": 50,
            },
        )
        pagina: int = field(
            metadata={
                "name": "Pagina",
                "type": "Element",
                "min_inclusive": 1,
                "max_inclusive": 999999,
            }
        )
