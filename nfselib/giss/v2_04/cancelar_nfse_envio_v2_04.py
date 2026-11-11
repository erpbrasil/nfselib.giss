from __future__ import annotations

from dataclasses import dataclass, field

from nfselib.giss.v2_04.tipos_v2_04 import TcPedidoCancelamento

__NAMESPACE__ = "http://www.giss.com.br/cancelar-nfse-envio-v2_04.xsd"


@dataclass(kw_only=True)
class CancelarNfseEnvio:
    class Meta:
        namespace = "http://www.giss.com.br/cancelar-nfse-envio-v2_04.xsd"

    pedido: TcPedidoCancelamento = field(
        metadata={
            "name": "Pedido",
            "type": "Element",
        }
    )
