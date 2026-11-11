from __future__ import annotations

from dataclasses import dataclass, field

from nfselib.giss.v2_04.tipos_v2_04 import (
    TcDeclaracaoPrestacaoServico,
    TcPedidoCancelamento,
)
from nfselib.giss.v2_04.xmldsig_core_schema20020212 import Signature

__NAMESPACE__ = "http://www.giss.com.br/gerar-nfse-resposta-v2_04.xsd"


@dataclass(kw_only=True)
class SubstituirNfseEnvio:
    class Meta:
        namespace = "http://www.giss.com.br/gerar-nfse-resposta-v2_04.xsd"

    substituicao_nfse: SubstituirNfseEnvio.SubstituicaoNfse = field(
        metadata={
            "name": "SubstituicaoNfse",
            "type": "Element",
        }
    )
    signature: None | Signature = field(
        default=None,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        },
    )

    @dataclass(kw_only=True)
    class SubstituicaoNfse:
        pedido: TcPedidoCancelamento = field(
            metadata={
                "name": "Pedido",
                "type": "Element",
            }
        )
        rps: TcDeclaracaoPrestacaoServico = field(
            metadata={
                "name": "Rps",
                "type": "Element",
            }
        )
        id: None | str = field(
            default=None,
            metadata={
                "name": "Id",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 255,
                "white_space": "collapse",
            },
        )
