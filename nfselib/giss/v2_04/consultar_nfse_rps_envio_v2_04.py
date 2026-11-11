from __future__ import annotations

from dataclasses import dataclass, field

from nfselib.giss.v2_04.tipos_v2_04 import (
    TcIdentificacaoPessoaEmpresa,
    TcIdentificacaoRps,
)
from nfselib.giss.v2_04.xmldsig_core_schema20020212 import Signature

__NAMESPACE__ = "http://www.giss.com.br/consultar-nfse-rps-envio-v2_04.xsd"


@dataclass(kw_only=True)
class ConsultarNfseRpsEnvio:
    class Meta:
        namespace = "http://www.giss.com.br/consultar-nfse-rps-envio-v2_04.xsd"

    identificacao_rps: TcIdentificacaoRps = field(
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
        }
    )
    prestador: TcIdentificacaoPessoaEmpresa = field(
        metadata={
            "name": "Prestador",
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
