from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.giss.com.br/cabecalho-v2_04.xsd"


@dataclass(kw_only=True)
class Cabecalho:
    class Meta:
        name = "cabecalho"
        namespace = "http://www.giss.com.br/cabecalho-v2_04.xsd"

    versao_dados: str = field(
        metadata={
            "name": "versaoDados",
            "type": "Element",
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        }
    )
    versao: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        }
    )
