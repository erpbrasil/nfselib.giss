from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from nfselib.giss.v2_04.tipos_v2_04 import TcIdentificacaoPessoaEmpresa

__NAMESPACE__ = (
    "http://www.giss.com.br/consultar-nfse-servico-tomado-envio-v2_04.xsd"
)


@dataclass(kw_only=True)
class ConsultarNfseServicoTomadoEnvio:
    class Meta:
        namespace = "http://www.giss.com.br/consultar-nfse-servico-tomado-envio-v2_04.xsd"

    consulente: TcIdentificacaoPessoaEmpresa = field(
        metadata={
            "name": "Consulente",
            "type": "Element",
        }
    )
    numero_nfse: None | int = field(
        default=None,
        metadata={
            "name": "NumeroNfse",
            "type": "Element",
            "total_digits": 15,
        },
    )
    periodo_emissao: None | ConsultarNfseServicoTomadoEnvio.PeriodoEmissao = (
        field(
            default=None,
            metadata={
                "name": "PeriodoEmissao",
                "type": "Element",
            },
        )
    )
    periodo_competencia: (
        None | ConsultarNfseServicoTomadoEnvio.PeriodoCompetencia
    ) = field(
        default=None,
        metadata={
            "name": "PeriodoCompetencia",
            "type": "Element",
        },
    )
    prestador: None | TcIdentificacaoPessoaEmpresa = field(
        default=None,
        metadata={
            "name": "Prestador",
            "type": "Element",
        },
    )
    tomador: None | TcIdentificacaoPessoaEmpresa = field(
        default=None,
        metadata={
            "name": "Tomador",
            "type": "Element",
        },
    )
    intermediario: None | TcIdentificacaoPessoaEmpresa = field(
        default=None,
        metadata={
            "name": "Intermediario",
            "type": "Element",
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

    @dataclass(kw_only=True)
    class PeriodoEmissao:
        data_inicial: XmlDate = field(
            metadata={
                "name": "DataInicial",
                "type": "Element",
            }
        )
        data_final: XmlDate = field(
            metadata={
                "name": "DataFinal",
                "type": "Element",
            }
        )

    @dataclass(kw_only=True)
    class PeriodoCompetencia:
        data_inicial: XmlDate = field(
            metadata={
                "name": "DataInicial",
                "type": "Element",
            }
        )
        data_final: XmlDate = field(
            metadata={
                "name": "DataFinal",
                "type": "Element",
            }
        )
