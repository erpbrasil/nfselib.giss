from __future__ import annotations

from dataclasses import dataclass, field

from nfselib.giss.v2_04.tipos_v2_04 import TcDeclaracaoPrestacaoServico

__NAMESPACE__ = "http://www.giss.com.br/gerar-nfse-envio-v2_04.xsd"


@dataclass(kw_only=True)
class GerarNfseEnvio:
    class Meta:
        namespace = "http://www.giss.com.br/gerar-nfse-envio-v2_04.xsd"

    rps: TcDeclaracaoPrestacaoServico = field(
        metadata={
            "name": "Rps",
            "type": "Element",
        }
    )
