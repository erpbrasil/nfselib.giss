from __future__ import annotations

from dataclasses import dataclass, field

from nfselib.giss.v2_04.tipos_v2_04 import TcLoteRps
from nfselib.giss.v2_04.xmldsig_core_schema20020212 import Signature

__NAMESPACE__ = (
    "http://www.giss.com.br/enviar-lote-rps-sincrono-envio-v2_04.xsd"
)


@dataclass(kw_only=True)
class EnviarLoteRpsSincronoEnvio:
    class Meta:
        namespace = (
            "http://www.giss.com.br/enviar-lote-rps-sincrono-envio-v2_04.xsd"
        )

    lote_rps: TcLoteRps = field(
        metadata={
            "name": "LoteRps",
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
