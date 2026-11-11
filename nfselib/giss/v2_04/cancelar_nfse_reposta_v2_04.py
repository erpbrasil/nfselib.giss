from __future__ import annotations

from dataclasses import dataclass, field

from nfselib.giss.v2_04.tipos_v2_04 import (
    ListaMensagemRetorno,
    TcRetCancelamento,
)

__NAMESPACE__ = "http://www.giss.com.br/cancelar-nfse-resposta-v2_04.xsd"


@dataclass(kw_only=True)
class CancelarNfseResposta:
    class Meta:
        namespace = "http://www.giss.com.br/cancelar-nfse-resposta-v2_04.xsd"

    ret_cancelamento: None | TcRetCancelamento = field(
        default=None,
        metadata={
            "name": "RetCancelamento",
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
