from __future__ import annotations

from dataclasses import dataclass, field

from nfselib.giss.v2_04.tipos_v2_04 import TcIdentificacaoPessoaEmpresa
from nfselib.giss.v2_04.xmldsig_core_schema20020212 import Signature

__NAMESPACE__ = "http://www.giss.com.br/consultar-lote-rps-envio-v2_04.xsd"


@dataclass(kw_only=True)
class ConsultarLoteRpsEnvio:
    class Meta:
        namespace = "http://www.giss.com.br/consultar-lote-rps-envio-v2_04.xsd"

    prestador: TcIdentificacaoPessoaEmpresa = field(
        metadata={
            "name": "Prestador",
            "type": "Element",
        }
    )
    protocolo: str = field(
        metadata={
            "name": "Protocolo",
            "type": "Element",
            "max_length": 50,
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
