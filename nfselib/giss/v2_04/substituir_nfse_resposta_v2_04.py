from __future__ import annotations

from dataclasses import dataclass, field

from nfselib.giss.v2_04.tipos_v2_04 import (
    CompNfse,
    ListaMensagemAlertaRetorno,
    ListaMensagemRetorno,
)

__NAMESPACE__ = "http://www.giss.com.br/gerar-nfse-resposta-v2_04.xsd"


@dataclass(kw_only=True)
class SubstituirNfseResposta:
    class Meta:
        namespace = "http://www.giss.com.br/gerar-nfse-resposta-v2_04.xsd"

    ret_substituicao: None | SubstituirNfseResposta.RetSubstituicao = field(
        default=None,
        metadata={
            "name": "RetSubstituicao",
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

    @dataclass(kw_only=True)
    class RetSubstituicao:
        nfse_substituida: SubstituirNfseResposta.RetSubstituicao.NfseSubstituida = field(
            metadata={
                "name": "NfseSubstituida",
                "type": "Element",
            }
        )
        nfse_substituidora: SubstituirNfseResposta.RetSubstituicao.NfseSubstituidora = field(
            metadata={
                "name": "NfseSubstituidora",
                "type": "Element",
            }
        )

        @dataclass(kw_only=True)
        class NfseSubstituida:
            comp_nfse: CompNfse = field(
                metadata={
                    "name": "CompNfse",
                    "type": "Element",
                    "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
                }
            )
            lista_mensagem_alerta_retorno: (
                None | ListaMensagemAlertaRetorno
            ) = field(
                default=None,
                metadata={
                    "name": "ListaMensagemAlertaRetorno",
                    "type": "Element",
                    "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
                },
            )

        @dataclass(kw_only=True)
        class NfseSubstituidora:
            comp_nfse: CompNfse = field(
                metadata={
                    "name": "CompNfse",
                    "type": "Element",
                    "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
                }
            )
