from __future__ import annotations

from dataclasses import dataclass, field

from nfselib.giss.v2_04.tipos_v2_04 import TcIdentificacaoPessoaEmpresa
from nfselib.giss.v2_04.xmldsig_core_schema20020212 import Signature

__NAMESPACE__ = "http://www.giss.com.br/consultar-nfse-faixa-envio-v2_04.xsd"


@dataclass(kw_only=True)
class ConsultarNfseFaixaEnvio:
    class Meta:
        namespace = (
            "http://www.giss.com.br/consultar-nfse-faixa-envio-v2_04.xsd"
        )

    prestador: TcIdentificacaoPessoaEmpresa = field(
        metadata={
            "name": "Prestador",
            "type": "Element",
        }
    )
    faixa: ConsultarNfseFaixaEnvio.Faixa = field(
        metadata={
            "name": "Faixa",
            "type": "Element",
        }
    )
    pagina: int = field(
        metadata={
            "name": "Pagina",
            "type": "Element",
            "min_inclusive": 1,
            "max_inclusive": 999999,
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
    class Faixa:
        numero_nfse_inicial: int = field(
            metadata={
                "name": "NumeroNfseInicial",
                "type": "Element",
                "total_digits": 15,
            }
        )
        numero_nfse_final: int = field(
            metadata={
                "name": "NumeroNfseFinal",
                "type": "Element",
                "total_digits": 15,
            }
        )
