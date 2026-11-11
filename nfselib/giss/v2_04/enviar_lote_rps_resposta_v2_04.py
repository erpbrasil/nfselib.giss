from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from nfselib.giss.v2_04.tipos_v2_04 import ListaMensagemRetorno

__NAMESPACE__ = "http://www.giss.com.br/enviar-lote-rps-resposta-v2_04.xsd"


@dataclass(kw_only=True)
class EnviarLoteRpsResposta:
    class Meta:
        namespace = "http://www.giss.com.br/enviar-lote-rps-resposta-v2_04.xsd"

    numero_lote: None | int = field(
        default=None,
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "total_digits": 15,
        },
    )
    data_recebimento: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "DataRecebimento",
            "type": "Element",
        },
    )
    protocolo: None | str = field(
        default=None,
        metadata={
            "name": "Protocolo",
            "type": "Element",
            "max_length": 50,
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
