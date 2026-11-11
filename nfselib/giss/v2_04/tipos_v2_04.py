from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

from xsdata.models.datatype import XmlDate, XmlDateTime

from nfselib.giss.v2_04.xmldsig_core_schema20020212 import Signature

__NAMESPACE__ = "http://www.giss.com.br/tipos-v2_04.xsd"


@dataclass(kw_only=True)
class TcrtcinfoTributosSitClas:
    """
    :ivar cst: Código de Situação Tributária do IBS e da CBS
    :ivar c_class_trib: Código de Classificação Tributária do IBS e da
        CBS
    """

    class Meta:
        name = "TCRTCInfoTributosSitClas"

    cst: str = field(
        metadata={
            "name": "CST",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    c_class_trib: str = field(
        metadata={
            "name": "cClassTrib",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "white_space": "preserve",
            "pattern": r"[0-9]{6}",
        }
    )


@dataclass(kw_only=True)
class TcrtclistaDocFiscalOutro:
    """
    :ivar c_mun_doc_fiscal: Código do município emissor do documento
        fiscal que não se encontra no repositório nacional
    :ivar n_doc_fiscal: Número do documento fiscal que não se encontra
        no repositório nacional
    :ivar x_doc_fiscal: Descrição do documento fiscal
    """

    class Meta:
        name = "TCRTCListaDocFiscalOutro"

    c_mun_doc_fiscal: str = field(
        metadata={
            "name": "cMunDocFiscal",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "max_length": 7,
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    n_doc_fiscal: str = field(
        metadata={
            "name": "nDocFiscal",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    x_doc_fiscal: str = field(
        metadata={
            "name": "xDocFiscal",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )


@dataclass(kw_only=True)
class TcrtclistaDocOutro:
    """
    :ivar n_doc: Número do documento não fiscal
    :ivar x_doc: Descrição do documento não fiscal
    """

    class Meta:
        name = "TCRTCListaDocOutro"

    n_doc: str = field(
        metadata={
            "name": "nDoc",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    x_doc: str = field(
        metadata={
            "name": "xDoc",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )


@dataclass(kw_only=True)
class TcrtctotalCbscredPres:
    """
    :ivar p_cred_pres_cbs: Alíquota do crédito presumido para a CBS
    :ivar v_cred_pres_cbs: Valor do Crédito Presumido da CBS
        vCredPresCBS = vBC x pCredPresCBS
    """

    class Meta:
        name = "TCRTCTotalCBSCredPres"

    p_cred_pres_cbs: Decimal = field(
        metadata={
            "name": "pCredPresCBS",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("99.99"),
            "total_digits": 4,
            "fraction_digits": 2,
        }
    )
    v_cred_pres_cbs: Decimal = field(
        metadata={
            "name": "vCredPresCBS",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        }
    )


@dataclass(kw_only=True)
class TcrtctotalIbscredPres:
    """
    :ivar p_cred_pres_ibs: Alíquota do crédito presumido para o IBS
    :ivar v_cred_pres_ibs: Valor do Crédito Presumido para o IBS
        vCredPresIBS = vBC x pCredPresIBS
    """

    class Meta:
        name = "TCRTCTotalIBSCredPres"

    p_cred_pres_ibs: Decimal = field(
        metadata={
            "name": "pCredPresIBS",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("99.99"),
            "total_digits": 4,
            "fraction_digits": 2,
        }
    )
    v_cred_pres_ibs: Decimal = field(
        metadata={
            "name": "vCredPresIBS",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        }
    )


@dataclass(kw_only=True)
class TcrtctotalIbsmun:
    """
    :ivar v_dif_mun: Total do Diferimento do IBS municipal vDifMun =
        vIBSMun x pDifMun
    :ivar v_ibsmun: Total valor do IBS municipal vIBSMun = vBC x
        (pIBSMun ou pAliqEfetMun)
    """

    class Meta:
        name = "TCRTCTotalIBSMun"

    v_dif_mun: Decimal = field(
        metadata={
            "name": "vDifMun",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        }
    )
    v_ibsmun: Decimal = field(
        metadata={
            "name": "vIBSMun",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        }
    )


@dataclass(kw_only=True)
class TcrtctotalIbsuf:
    """
    :ivar v_dif_uf: Total do Diferimento do IBS estadual vDifUF = vIBSUF
        x pDifUF
    :ivar v_ibsuf: Total valor do IBS estadual vIBSUF = vBC x (pIBSUF ou
        pAliqEfetUF)
    """

    class Meta:
        name = "TCRTCTotalIBSUF"

    v_dif_uf: Decimal = field(
        metadata={
            "name": "vDifUF",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        }
    )
    v_ibsuf: Decimal = field(
        metadata={
            "name": "vIBSUF",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        }
    )


@dataclass(kw_only=True)
class TcrtctotalTribCompraGov:
    """
    :ivar p_ibsuf: Alíquota do IBS de competência do Estado
    :ivar v_ibsuf: Valor do Tributo do IBS da UF calculado
    :ivar p_ibsmun: Alíquota do IBS de competência do Município
    :ivar v_ibsmun: Valor do Tributo do IBS do Município calculado
    :ivar p_cbs: Alíquota da CBS
    :ivar v_cbs: Valor do Tributo da CBS calculado
    """

    class Meta:
        name = "TCRTCTotalTribCompraGov"

    p_ibsuf: Decimal = field(
        metadata={
            "name": "pIBSUF",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("99.99"),
            "total_digits": 4,
            "fraction_digits": 2,
        }
    )
    v_ibsuf: Decimal = field(
        metadata={
            "name": "vIBSUF",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        }
    )
    p_ibsmun: Decimal = field(
        metadata={
            "name": "pIBSMun",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("99.99"),
            "total_digits": 4,
            "fraction_digits": 2,
        }
    )
    v_ibsmun: Decimal = field(
        metadata={
            "name": "vIBSMun",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        }
    )
    p_cbs: Decimal = field(
        metadata={
            "name": "pCBS",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("99.99"),
            "total_digits": 4,
            "fraction_digits": 2,
        }
    )
    v_cbs: Decimal = field(
        metadata={
            "name": "vCBS",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        }
    )


@dataclass(kw_only=True)
class TcrtctotalTribRegular:
    """
    :ivar p_aliq_efe_reg_ibsuf: Alíquota efetiva de tributação regular
        do IBS estadual
    :ivar v_trib_reg_ibsuf: Valor da tributação regular do IBS estadual
        vTribRegIBSUF = vBC x pAliqEfeRegIBSUF
    :ivar p_aliq_efe_reg_ibsmun: Alíquota efetiva de tributação regular
        do IBS municipal
    :ivar v_trib_reg_ibsmun: Valor da tributação regular do IBS
        municipal vTribRegIBSMun = vBC x pAliqEfeRegIBSMun
    :ivar p_aliq_efe_reg_cbs: Alíquota efetiva de tributação regular da
        CBS
    :ivar v_trib_reg_cbs: Valor da tributação regular da CBS vTribRegCBS
        = vBC x pAliqEfeRegCBS
    """

    class Meta:
        name = "TCRTCTotalTribRegular"

    p_aliq_efe_reg_ibsuf: Decimal = field(
        metadata={
            "name": "pAliqEfeRegIBSUF",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("99.99"),
            "total_digits": 4,
            "fraction_digits": 2,
        }
    )
    v_trib_reg_ibsuf: Decimal = field(
        metadata={
            "name": "vTribRegIBSUF",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        }
    )
    p_aliq_efe_reg_ibsmun: Decimal = field(
        metadata={
            "name": "pAliqEfeRegIBSMun",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("99.99"),
            "total_digits": 4,
            "fraction_digits": 2,
        }
    )
    v_trib_reg_ibsmun: Decimal = field(
        metadata={
            "name": "vTribRegIBSMun",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        }
    )
    p_aliq_efe_reg_cbs: Decimal = field(
        metadata={
            "name": "pAliqEfeRegCBS",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("99.99"),
            "total_digits": 4,
            "fraction_digits": 2,
        }
    )
    v_trib_reg_cbs: Decimal = field(
        metadata={
            "name": "vTribRegCBS",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        }
    )


@dataclass(kw_only=True)
class TcrtcvaloresIbscbsfed:
    """
    :ivar p_cbs: Alíquota da União para CBS parametrizada no sistema
    :ivar p_red_aliq_cbs: Percentual da redução de alíquota da CBS
    :ivar p_aliq_efet_cbs: pAliqEfetCBS = pCBS x (1 - pRedAliqCBS) x (1
        - pRedutor) Se pRedAliqCBS não for informado na DPS, então
        pAliqEfetCBS é a própria pCBS
    """

    class Meta:
        name = "TCRTCValoresIBSCBSFed"

    p_cbs: Decimal = field(
        metadata={
            "name": "pCBS",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("99.99"),
            "total_digits": 4,
            "fraction_digits": 2,
        }
    )
    p_red_aliq_cbs: None | Decimal = field(
        default=None,
        metadata={
            "name": "pRedAliqCBS",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999.99"),
            "total_digits": 5,
            "fraction_digits": 2,
        },
    )
    p_aliq_efet_cbs: Decimal = field(
        metadata={
            "name": "pAliqEfetCBS",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("99.99"),
            "total_digits": 4,
            "fraction_digits": 2,
        }
    )


@dataclass(kw_only=True)
class TcrtcvaloresIbscbsmun:
    """
    :ivar p_ibsmun: Alíquota do Município para IBS da localidade de
        incidência parametrizada no sistema
    :ivar p_red_aliq_mun: Percentual de redução de alíquota municipal
    :ivar p_aliq_efet_mun: pAliqEfetMun = pIBSMun x (1 - pRedAliqMun) x
        (1 - pRedutor) Se pRedAliqMun não for informado na DPS, então
        pAliqEfetMun é a própria pIBSMun
    """

    class Meta:
        name = "TCRTCValoresIBSCBSMun"

    p_ibsmun: Decimal = field(
        metadata={
            "name": "pIBSMun",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("99.99"),
            "total_digits": 4,
            "fraction_digits": 2,
        }
    )
    p_red_aliq_mun: None | Decimal = field(
        default=None,
        metadata={
            "name": "pRedAliqMun",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999.99"),
            "total_digits": 5,
            "fraction_digits": 2,
        },
    )
    p_aliq_efet_mun: Decimal = field(
        metadata={
            "name": "pAliqEfetMun",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("99.99"),
            "total_digits": 4,
            "fraction_digits": 2,
        }
    )


@dataclass(kw_only=True)
class TcrtcvaloresIbscbsuf:
    """
    :ivar p_ibsuf: Alíquota da UF para IBS da localidade de incidência
        parametrizada no sistema
    :ivar p_red_aliq_uf: Percentual de redução de alíquota estadual
    :ivar p_aliq_efet_uf: pAliqEfetUF = pIBSUF x (1 - pRedAliqUF) x (1 -
        pRedutor) Se pRedAliqUF não for informado na DPS, então
        pAliqEfetUF é a própria pIBSUF
    """

    class Meta:
        name = "TCRTCValoresIBSCBSUF"

    p_ibsuf: Decimal = field(
        metadata={
            "name": "pIBSUF",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("99.99"),
            "total_digits": 4,
            "fraction_digits": 2,
        }
    )
    p_red_aliq_uf: None | Decimal = field(
        default=None,
        metadata={
            "name": "pRedAliqUF",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999.99"),
            "total_digits": 5,
            "fraction_digits": 2,
        },
    )
    p_aliq_efet_uf: Decimal = field(
        metadata={
            "name": "pAliqEfetUF",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("99.99"),
            "total_digits": 4,
            "fraction_digits": 2,
        }
    )


@dataclass(kw_only=True)
class TctribTotalPercent:
    """
    :ivar p_tot_trib_fed: Valor percentual total aproximado dos tributos
        federais (%).
    :ivar p_tot_trib_est: Valor percentual total aproximado dos tributos
        estaduais (%).
    :ivar p_tot_trib_mun: Valor percentual total aproximado dos tributos
        municipais (%).
    """

    class Meta:
        name = "TCTribTotalPercent"

    p_tot_trib_fed: Decimal = field(
        metadata={
            "name": "pTotTribFed",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999.99"),
            "total_digits": 5,
            "fraction_digits": 2,
        }
    )
    p_tot_trib_est: Decimal = field(
        metadata={
            "name": "pTotTribEst",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999.99"),
            "total_digits": 5,
            "fraction_digits": 2,
        }
    )
    p_tot_trib_mun: Decimal = field(
        metadata={
            "name": "pTotTribMun",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999.99"),
            "total_digits": 5,
            "fraction_digits": 2,
        }
    )


class TscodNaoNif(Enum):
    """
    Motivo para não informação do NIF: 0 - Não informado na nota de origem;
    1 - Dispensado do NIF; 2 - Não exigência do NIF;.
    """

    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"


class TsenvMdic(Enum):
    """
    Compartilhar as informações da NFS-e gerada a partir desta DPS com a
    Secretaria de Comércio Exterior: 0 - Não enviar para o MDIC; 1 - Enviar
    para o MDIC;.
    """

    VALUE_0 = "0"
    VALUE_1 = "1"


class TsmecAfcomExPrest(Enum):
    """
    Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo
    prestador do serviço: 00 - Desconhecido (tipo não informado na nota de
    origem); 01 - Nenhum; 02 - ACC - Adiantamento sobre Contrato de Câmbio
    – Redução a Zero do IR e do IOF; 03 - ACE – Adiantamento sobre Cambiais
    Entregues - Redução a Zero do IR e do IOF; 04 - BNDES-Exim Pós-Embarque
    – Serviços; 05 - BNDES-Exim Pré-Embarque - Serviços; 06 - FGE - Fundo
    de Garantia à Exportação; 07 - PROEX - EQUALIZAÇÃO 08 - PROEX -
    Financiamento;.
    """

    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"


class TsmecAfcomExToma(Enum):
    """
    Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo tomador
    do serviço: 00 - Desconhecido (tipo não informado na nota de origem);
    01 - Nenhum; 02 - Adm.

    Pública e Repr. Internacional; 03 - Alugueis e Arrend. Mercantil de
    maquinas, equip., embarc. e aeronaves; 04 - Arrendamento Mercantil de
    aeronave para empresa de transporte aéreo público; 05 - Comissão a
    agentes externos na exportação; 06 - Despesas de armazenagem, mov. e
    transporte de carga no exterior; 07 - Eventos FIFA (subsidiária); 08 -
    Eventos FIFA; 09 - Fretes, arrendamentos de embarcações ou aeronaves e
    outros; 10 - Material Aeronáutico; 11 - Promoção de Bens no Exterior;
    12 - Promoção de Dest. Turísticos Brasileiros; 13 - Promoção do Brasil
    no Exterior; 14 - Promoção Serviços no Exterior; 15 - RECINE; 16 -
    RECOPA; 17 - Registro e Manutenção de marcas, patentes e cultivares; 18
    - REICOMP; 19 - REIDI; 20 - REPENEC; 21 - REPES; 22 - RETAERO; 23 -
    RETID; 24 - Royalties, Assistência Técnica, Científica e Assemelhados;
    25 - Serviços de avaliação da conformidade vinculados aos Acordos da
    OMC; 26 - ZPE;.
    """

    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"
    VALUE_13 = "13"
    VALUE_14 = "14"
    VALUE_15 = "15"
    VALUE_16 = "16"
    VALUE_17 = "17"
    VALUE_18 = "18"
    VALUE_19 = "19"
    VALUE_20 = "20"
    VALUE_21 = "21"
    VALUE_22 = "22"
    VALUE_23 = "23"
    VALUE_24 = "24"
    VALUE_25 = "25"
    VALUE_26 = "26"


class TsmodoPrestacao(Enum):
    """
    Modo de Prestação: 0 - Desconhecido (tipo não informado na nota de
    origem); 1 - Transfronteiriço; 2 - Consumo no Brasil; 3 - Presença
    Comercial no Exterior; 4 - Movimento Temporário de Pessoas Físicas;.
    """

    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"


class TsmovTempBens(Enum):
    """
    Vínculo da Operação à Movimentação Temporária de Bens: 0 - Desconhecido
    (tipo não informado na nota de origem); 1 - Não; 2 - Vinculada -
    Declaração de Importação; 3 - Vinculada - Declaração de Exportação;.
    """

    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"


class TsrtcfinNfse(Enum):
    """
    Indicador da finalidade da emissão de NFS-e: 0 - NFS-e regular;.
    """

    VALUE_0 = "0"


class TsrtcindDest(Enum):
    """
    A respeito do Destinatário dos serviços: 0 – O tomador identificado na
    NFS-e é o adquirente e o destinatário do fornecimento (tomador =
    adquirente = destinatário); 1 – O tomador e o adquirente são a mesma
    pessoa, mas o destinatário é uma pessoa física ou jurídica ou
    equiparada diversa do indicado como tomador/adquirente ou se trata de
    um estabelecimento do adquirente diferente do indicado no campo
    “tomador” (tomador = adquirente ≠ destinatário);.
    """

    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"


class TsrtcindFinal(Enum):
    """
    Indica operação de uso ou consumo pessoal (art. 57): 0 - Não; 1 - Sim;.
    """

    VALUE_0 = "0"
    VALUE_1 = "1"


class TsrtctipoChaveDfe(Enum):
    """
    Documento fiscal a que se refere a chaveDfe que seja um dos documentos
    do Repositório Nacional: 1 - NFS-e; 2 - NF-e; 3 - CT-e; 9 - Outro;.
    """

    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_9 = "9"


class TsrtctpEnteGov(Enum):
    """
    Tipo de ente governamental Para administração pública direta e suas
    autarquias e fundações: 1 - União; 2 - Estado; 3 - Distrito Federal; 4
    - Município; 9 - Outro;.
    """

    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_9 = "9"


class TsrtctpOper(Enum):
    """
    Tipo de Operação com Entes Governanementais ou outros serviços sobre
    bens imóveis: 1 – Fornecimento com pagamento posterior; 2 – Recebimento
    do pagamento com fornecimento já realizado; 3 – Fornecimento com
    pagamento já realizado; 4 – Recebimento do pagamento com fornecimento
    posterior; 5 – Fornecimento e recebimento do pagamento concomitantes.
    """

    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"


class TsrtctpReeRepRes(Enum):
    """
    Tipo de valor incluído neste documento, recebido por motivo de estarem
    relacionadas a operações de terceiros, objeto de reembolso, repasse ou
    ressarcimento pelo recebedor, já tributados e aqui referenciados 01 -
    Repasse de remuneração por intermediação de imóveis a demais corretores
    envolvidos na operação; 02 - Repasse de valores a fornecedor relativo a
    fornecimento intermediado por agência de turismo; 03 - Reembolso ou
    ressarcimento recebido por agência de propaganda e publicidade por
    valores pagos relativos a serviços de produção externa por conta e
    ordem de terceiro; 04 - Reembolso ou ressarcimento recebido por agência
    de propaganda e publicidade por valores pagos relativos a serviços de
    mídia por conta e ordem de terceiro; 99 - Outros reembolsos ou
    ressarcimentos recebidos por valores pagos relativos a operações por
    conta e ordem de terceiro;.
    """

    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_99 = "99"


class TstipoCst(Enum):
    """
    Código de Situação Tributária do PIS/COFINS (CST): 00 - Nenhum; 01 -
    Operação Tributável com Alíquota Básica; 02 - Operação Tributável com
    Alíquota Diferenciada; 03 - Operação Tributável com Alíquota por
    Unidade de Medida de Produto; 04 - Operação Tributável monofásica -
    Revenda a Alíquota Zero; 05 - Operação Tributável por Substituição
    Tributária; 06 - Operação Tributável a Alíquota Zero; 07 - Operação
    Isenta da Contribuição; 08 - Operação sem Incidência da Contribuição;
    09 - Operação com Suspensão da Contribuição; 49 - Outras Operações de
    Saída; 50 - Operação com Direito a Crédito – Vinculada Exclusivamente a
    Receita Tributada no Mercado Interno; 51 - Operação com Direito a
    Crédito – Vinculada Exclusivamente a Receita Não-Tributada no Mercado
    Interno; 52 - Operação com Direito a Crédito – Vinculada Exclusivamente
    a Receita de Exportação; 53 - Operação com Direito a Crédito –
    Vinculada a Receitas Tributadas e Não-Tributadas no Mercado Interno; 54
    - Operação com Direito a Crédito – Vinculada a Receitas Tributadas no
    Mercado Interno e de Exportação; 55 - Operação com Direito a Crédito –
    Vinculada a Receitas Não Tributadas no Mercado Interno e de Exportação;
    56 - Operação com Direito a Crédito – Vinculada a Receitas Tributadas e
    Não-Tributadas no Mercado Interno e de Exportação; 60 - Crédito
    Presumido – Operação de Aquisição Vinculada Exclusivamente a Receita
    Tributada no Mercado Interno; 61 - Crédito Presumido – Operação de
    Aquisição Vinculada Exclusivamente a Receita Não-Tributada no Mercado
    Interno; 62 - Crédito Presumido – Operação de Aquisição Vinculada
    Exclusivamente a Receita de Exportação; 63 - Crédito Presumido –
    Operação de Aquisição Vinculada a Receitas Tributadas e Não-Tributadas
    no Mercado Interno; 64 - Crédito Presumido – Operação de Aquisição
    Vinculada a Receitas Tributadas no Mercado Interno e de Exportação; 65
    - Crédito Presumido – Operação de Aquisição Vinculada a Receitas
    Não-Tributadas no Mercado Interno e de Exportação; 66 - Crédito
    Presumido – Operação de Aquisição Vinculada a Receitas Tributadas e
    Não-Tributadas no Mercado Interno e de Exportação; 67 - Crédito
    Presumido – Outras Operações; 70 - Operação de Aquisição sem Direito a
    Crédito; 71 - Operação de Aquisição com Isenção; 72 - Operação de
    Aquisição com Suspensão; 73 - Operação de Aquisição a Alíquota Zero; 74
    - Operação de Aquisição sem Incidência da Contribuição; 75 - Operação
    de Aquisição por Substituição Tributária; 98 - Outras Operações de
    Entrada; 99 - Outras Operações;.
    """

    VALUE_00 = "00"
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_49 = "49"
    VALUE_50 = "50"
    VALUE_51 = "51"
    VALUE_52 = "52"
    VALUE_53 = "53"
    VALUE_54 = "54"
    VALUE_55 = "55"
    VALUE_56 = "56"
    VALUE_60 = "60"
    VALUE_61 = "61"
    VALUE_62 = "62"
    VALUE_63 = "63"
    VALUE_64 = "64"
    VALUE_65 = "65"
    VALUE_66 = "66"
    VALUE_67 = "67"
    VALUE_70 = "70"
    VALUE_71 = "71"
    VALUE_72 = "72"
    VALUE_73 = "73"
    VALUE_74 = "74"
    VALUE_75 = "75"
    VALUE_98 = "98"
    VALUE_99 = "99"


class TstipoIndTotTrib(Enum):
    """
    Indicador de informação de valor total de tributos.

    Possui valor fixo igual a zero (indTotTrib=0). Não informar nenhum
    valor estimado para os Tributos (Decreto 8.264/2014). 0 - Não;.
    """

    VALUE_0 = "0"


class TstipoRetPiscofins(Enum):
    """
    Tipo de retencao do Pis/Cofins: 0 - PIS/COFINS/CSLL Não Retidos; 1 -
    PIS/COFINS Retidos; 2 - PIS/COFINS Não Retidos; 3 - PIS/COFINS/CSLL
    Retidos; 4 - PIS/COFINS Retidos, CSLL Não Retido; 5 - PIS Retido,
    COFINS/CSLL Não Retido; 6 - COFINS Retido, PIS/CSLL Não Retido; 7 - PIS
    Não Retido, COFINS/CSLL Retidos; 8 - PIS/COFINS Não Retidos, CSLL
    Retido; 9 - COFINS Não Retido, PIS/CSLL Retidos;.
    """

    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_7 = "7"
    VALUE_8 = "8"
    VALUE_9 = "9"


class TsvincPrest(Enum):
    """
    Vínculo entre as partes no negócio: 0 - Sem vínculo com o
    Tomador/Prestador 1 - Controlada; 2 - Controladora; 3 - Coligada; 4 -
    Matriz; 5 - Filial ou sucursal; 6 - Outro vínculo; 9 - Desconhecido
    (tipo não informado na nota de origem);.
    """

    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    VALUE_9 = "9"


@dataclass(kw_only=True)
class TcContato:
    class Meta:
        name = "tcContato"

    telefone: None | str = field(
        default=None,
        metadata={
            "name": "Telefone",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        },
    )
    email: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "max_occurs": 2,
            "min_length": 1,
            "max_length": 80,
            "white_space": "collapse",
            "sequence": 1,
        },
    )


@dataclass(kw_only=True)
class TcCpfCnpj:
    class Meta:
        name = "tcCpfCnpj"

    cpf: None | str = field(
        default=None,
        metadata={
            "name": "Cpf",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "length": 11,
        },
    )
    cnpj: None | str = field(
        default=None,
        metadata={
            "name": "Cnpj",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "length": 14,
            "white_space": "collapse",
        },
    )


@dataclass(kw_only=True)
class TcDadosConstrucaoCivil:
    class Meta:
        name = "tcDadosConstrucaoCivil"

    codigo_obra: None | str = field(
        default=None,
        metadata={
            "name": "CodigoObra",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 30,
            "white_space": "collapse",
        },
    )
    art: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Art",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "max_occurs": 2,
            "min_length": 1,
            "max_length": 30,
            "white_space": "collapse",
            "sequence": 1,
        },
    )


@dataclass(kw_only=True)
class TcEnderecoExterior:
    """
    :ivar codigo_pais:
    :ivar endereco_completo_exterior: Campo com descricoes adicionais
        sobre o endereço do exterior.
    :ivar c_end_post: Código alfanumérico do Endereçamento Postal no
        exterior do prestador do serviço.
    :ivar x_cidade: Nome da cidade no exterior do prestador do serviço.
    :ivar x_est_prov_reg: Estado, província ou região da cidade no
        exterior do prestador do serviço.
    """

    class Meta:
        name = "tcEnderecoExterior"

    codigo_pais: str = field(
        metadata={
            "name": "CodigoPais",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "length": 4,
            "white_space": "collapse",
        }
    )
    endereco_completo_exterior: str = field(
        metadata={
            "name": "EnderecoCompletoExterior",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        }
    )
    c_end_post: str = field(
        metadata={
            "name": "cEndPost",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 11,
            "white_space": "preserve",
        }
    )
    x_cidade: str = field(
        metadata={
            "name": "xCidade",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
        }
    )
    x_est_prov_reg: str = field(
        metadata={
            "name": "xEstProvReg",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
        }
    )


@dataclass(kw_only=True)
class TcEvento:
    class Meta:
        name = "tcEvento"

    identificacao_evento: None | str = field(
        default=None,
        metadata={
            "name": "IdentificacaoEvento",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 30,
            "white_space": "collapse",
        },
    )
    descricao_evento: list[str] = field(
        default_factory=list,
        metadata={
            "name": "DescricaoEvento",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "max_occurs": 2,
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
            "sequence": 1,
        },
    )


@dataclass(kw_only=True)
class TcFornecedorExterior:
    class Meta:
        name = "tcFornecedorExterior"

    nif_fornecedor: None | str = field(
        default=None,
        metadata={
            "name": "NifFornecedor",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 40,
            "white_space": "collapse",
        },
    )
    codigo_pais: str = field(
        metadata={
            "name": "CodigoPais",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "length": 4,
            "white_space": "collapse",
        }
    )


@dataclass(kw_only=True)
class TcIdentificacaoNfseDeducao:
    class Meta:
        name = "tcIdentificacaoNfseDeducao"

    codigo_municipio_gerador: int = field(
        metadata={
            "name": "CodigoMunicipioGerador",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "total_digits": 7,
        }
    )
    numero_nfse: int = field(
        metadata={
            "name": "NumeroNfse",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "total_digits": 15,
        }
    )
    codigo_verificacao: None | str = field(
        default=None,
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 9,
            "white_space": "collapse",
            "pattern": r"[a-zA-Z0-9]{1,9}",
        },
    )


@dataclass(kw_only=True)
class TcIdentificacaoRps:
    class Meta:
        name = "tcIdentificacaoRps"

    numero: int = field(
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "total_digits": 15,
        }
    )
    serie: str = field(
        metadata={
            "name": "Serie",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 5,
            "white_space": "collapse",
        }
    )
    tipo: str = field(
        metadata={
            "name": "Tipo",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "pattern": r"1|2|3",
        }
    )


@dataclass(kw_only=True)
class TcInfSubstituicaoNfse:
    class Meta:
        name = "tcInfSubstituicaoNfse"

    nfse_substituidora: int = field(
        metadata={
            "name": "NfseSubstituidora",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "total_digits": 15,
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )


@dataclass(kw_only=True)
class TcMensagemRetorno:
    class Meta:
        name = "tcMensagemRetorno"

    codigo: str = field(
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 4,
            "white_space": "collapse",
        }
    )
    mensagem: str = field(
        metadata={
            "name": "Mensagem",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        }
    )
    correcao: None | str = field(
        default=None,
        metadata={
            "name": "Correcao",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        },
    )
    contexto_tecnico: None | str = field(
        default=None,
        metadata={
            "name": "ContextoTecnico",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "max_length": 4000,
        },
    )


@dataclass(kw_only=True)
class TcOutroDocumentoDeducao:
    class Meta:
        name = "tcOutroDocumentoDeducao"

    identificacao_documento: str = field(
        metadata={
            "name": "IdentificacaoDocumento",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        }
    )


@dataclass(kw_only=True)
class TcValoresNfse:
    """
    :ivar base_calculo:
    :ivar aliquota:
    :ivar valor_iss:
    :ivar valor_liquido_nfse:
    :ivar valor_total_retencoes: Valor total das retencoes: PIS, COFINS,
        INSS, IR, CSLL, outras retencoes e ISSQN retidos
    """

    class Meta:
        name = "tcValoresNfse"

    base_calculo: Decimal = field(
        metadata={
            "name": "BaseCalculo",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    aliquota: None | Decimal = field(
        default=None,
        metadata={
            "name": "Aliquota",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 5,
            "fraction_digits": 4,
            "white_space": "collapse",
        },
    )
    valor_iss: None | Decimal = field(
        default=None,
        metadata={
            "name": "ValorIss",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    valor_liquido_nfse: Decimal = field(
        metadata={
            "name": "ValorLiquidoNfse",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_total_retencoes: None | Decimal = field(
        default=None,
        metadata={
            "name": "ValorTotalRetencoes",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        },
    )


class TsItemListaServico(Enum):
    """
    Subitem do serviço prestado conforme LC 116/2003.
    """

    VALUE_01_01 = "01.01"
    VALUE_01_02 = "01.02"
    VALUE_01_03 = "01.03"
    VALUE_01_04 = "01.04"
    VALUE_01_05 = "01.05"
    VALUE_01_06 = "01.06"
    VALUE_01_07 = "01.07"
    VALUE_01_08 = "01.08"
    VALUE_01_09 = "01.09"
    VALUE_02_01 = "02.01"
    VALUE_03_02 = "03.02"
    VALUE_03_03 = "03.03"
    VALUE_03_04 = "03.04"
    VALUE_03_05 = "03.05"
    VALUE_04_01 = "04.01"
    VALUE_04_02 = "04.02"
    VALUE_04_03 = "04.03"
    VALUE_04_04 = "04.04"
    VALUE_04_05 = "04.05"
    VALUE_04_06 = "04.06"
    VALUE_04_07 = "04.07"
    VALUE_04_08 = "04.08"
    VALUE_04_09 = "04.09"
    VALUE_04_10 = "04.10"
    VALUE_04_11 = "04.11"
    VALUE_04_12 = "04.12"
    VALUE_04_13 = "04.13"
    VALUE_04_14 = "04.14"
    VALUE_04_15 = "04.15"
    VALUE_04_16 = "04.16"
    VALUE_04_17 = "04.17"
    VALUE_04_18 = "04.18"
    VALUE_04_19 = "04.19"
    VALUE_04_20 = "04.20"
    VALUE_04_21 = "04.21"
    VALUE_04_22 = "04.22"
    VALUE_04_23 = "04.23"
    VALUE_05_01 = "05.01"
    VALUE_05_02 = "05.02"
    VALUE_05_03 = "05.03"
    VALUE_05_04 = "05.04"
    VALUE_05_05 = "05.05"
    VALUE_05_06 = "05.06"
    VALUE_05_07 = "05.07"
    VALUE_05_08 = "05.08"
    VALUE_05_09 = "05.09"
    VALUE_06_01 = "06.01"
    VALUE_06_02 = "06.02"
    VALUE_06_03 = "06.03"
    VALUE_06_04 = "06.04"
    VALUE_06_05 = "06.05"
    VALUE_06_06 = "06.06"
    VALUE_07_01 = "07.01"
    VALUE_07_02 = "07.02"
    VALUE_07_03 = "07.03"
    VALUE_07_04 = "07.04"
    VALUE_07_05 = "07.05"
    VALUE_07_06 = "07.06"
    VALUE_07_07 = "07.07"
    VALUE_07_08 = "07.08"
    VALUE_07_09 = "07.09"
    VALUE_07_10 = "07.10"
    VALUE_07_11 = "07.11"
    VALUE_07_12 = "07.12"
    VALUE_07_13 = "07.13"
    VALUE_07_16 = "07.16"
    VALUE_07_17 = "07.17"
    VALUE_07_18 = "07.18"
    VALUE_07_19 = "07.19"
    VALUE_07_20 = "07.20"
    VALUE_07_21 = "07.21"
    VALUE_07_22 = "07.22"
    VALUE_08_01 = "08.01"
    VALUE_08_02 = "08.02"
    VALUE_09_01 = "09.01"
    VALUE_09_02 = "09.02"
    VALUE_09_03 = "09.03"
    VALUE_10_01 = "10.01"
    VALUE_10_02 = "10.02"
    VALUE_10_03 = "10.03"
    VALUE_10_04 = "10.04"
    VALUE_10_05 = "10.05"
    VALUE_10_06 = "10.06"
    VALUE_10_07 = "10.07"
    VALUE_10_08 = "10.08"
    VALUE_10_09 = "10.09"
    VALUE_10_10 = "10.10"
    VALUE_11_01 = "11.01"
    VALUE_11_02 = "11.02"
    VALUE_11_03 = "11.03"
    VALUE_11_04 = "11.04"
    VALUE_11_05 = "11.05"
    VALUE_12_01 = "12.01"
    VALUE_12_02 = "12.02"
    VALUE_12_03 = "12.03"
    VALUE_12_04 = "12.04"
    VALUE_12_05 = "12.05"
    VALUE_12_06 = "12.06"
    VALUE_12_07 = "12.07"
    VALUE_12_08 = "12.08"
    VALUE_12_09 = "12.09"
    VALUE_12_10 = "12.10"
    VALUE_12_11 = "12.11"
    VALUE_12_12 = "12.12"
    VALUE_12_13 = "12.13"
    VALUE_12_14 = "12.14"
    VALUE_12_15 = "12.15"
    VALUE_12_16 = "12.16"
    VALUE_12_17 = "12.17"
    VALUE_13_02 = "13.02"
    VALUE_13_03 = "13.03"
    VALUE_13_04 = "13.04"
    VALUE_13_05 = "13.05"
    VALUE_14_01 = "14.01"
    VALUE_14_02 = "14.02"
    VALUE_14_03 = "14.03"
    VALUE_14_04 = "14.04"
    VALUE_14_05 = "14.05"
    VALUE_14_06 = "14.06"
    VALUE_14_07 = "14.07"
    VALUE_14_08 = "14.08"
    VALUE_14_09 = "14.09"
    VALUE_14_10 = "14.10"
    VALUE_14_11 = "14.11"
    VALUE_14_12 = "14.12"
    VALUE_14_13 = "14.13"
    VALUE_14_14 = "14.14"
    VALUE_15_01 = "15.01"
    VALUE_15_02 = "15.02"
    VALUE_15_03 = "15.03"
    VALUE_15_04 = "15.04"
    VALUE_15_05 = "15.05"
    VALUE_15_06 = "15.06"
    VALUE_15_07 = "15.07"
    VALUE_15_08 = "15.08"
    VALUE_15_09 = "15.09"
    VALUE_15_10 = "15.10"
    VALUE_15_11 = "15.11"
    VALUE_15_12 = "15.12"
    VALUE_15_13 = "15.13"
    VALUE_15_14 = "15.14"
    VALUE_15_15 = "15.15"
    VALUE_15_16 = "15.16"
    VALUE_15_17 = "15.17"
    VALUE_15_18 = "15.18"
    VALUE_16_01 = "16.01"
    VALUE_16_02 = "16.02"
    VALUE_17_01 = "17.01"
    VALUE_17_02 = "17.02"
    VALUE_17_03 = "17.03"
    VALUE_17_04 = "17.04"
    VALUE_17_05 = "17.05"
    VALUE_17_06 = "17.06"
    VALUE_17_08 = "17.08"
    VALUE_17_09 = "17.09"
    VALUE_17_10 = "17.10"
    VALUE_17_11 = "17.11"
    VALUE_17_12 = "17.12"
    VALUE_17_13 = "17.13"
    VALUE_17_14 = "17.14"
    VALUE_17_15 = "17.15"
    VALUE_17_16 = "17.16"
    VALUE_17_17 = "17.17"
    VALUE_17_18 = "17.18"
    VALUE_17_19 = "17.19"
    VALUE_17_20 = "17.20"
    VALUE_17_21 = "17.21"
    VALUE_17_22 = "17.22"
    VALUE_17_23 = "17.23"
    VALUE_17_24 = "17.24"
    VALUE_17_25 = "17.25"
    VALUE_18_01 = "18.01"
    VALUE_19_01 = "19.01"
    VALUE_20_01 = "20.01"
    VALUE_20_02 = "20.02"
    VALUE_20_03 = "20.03"
    VALUE_21_01 = "21.01"
    VALUE_22_01 = "22.01"
    VALUE_23_01 = "23.01"
    VALUE_24_01 = "24.01"
    VALUE_25_01 = "25.01"
    VALUE_25_02 = "25.02"
    VALUE_25_03 = "25.03"
    VALUE_25_04 = "25.04"
    VALUE_26_01 = "26.01"
    VALUE_27_01 = "27.01"
    VALUE_28_01 = "28.01"
    VALUE_29_01 = "29.01"
    VALUE_30_01 = "30.01"
    VALUE_31_01 = "31.01"
    VALUE_32_01 = "32.01"
    VALUE_33_01 = "33.01"
    VALUE_34_01 = "34.01"
    VALUE_35_01 = "35.01"
    VALUE_36_01 = "36.01"
    VALUE_37_01 = "37.01"
    VALUE_38_01 = "38.01"
    VALUE_39_01 = "39.01"
    VALUE_40_01 = "40.01"


class TsUf(Enum):
    """
    UF ( AC - Acre; AL - Alagoas; AM - Amazonas; AP - Amapa; BA - Bahia; CE
    - Ceara; DF - Distrito Federal; ES - Espirito Santo; GO - Goias; MA -
    Maranhao; MG - Minas Gerais; MS - Mato Grosso do Sul; MT - Mato Grosso;
    PA - Para; PB - Paraiba; PE - Pernambuco; PI - Piaui; PR - Parana; RJ -
    Rio de Janeiro; RN - Rio Grande do Norte; RO - Rondonia; RR - Roraima;
    RS - Rio Grande do Sul; SC - Santa Catarina; SE - Sergipe; SP - Sao
    Paulo; TO - Tocantins).
    """

    AC = "AC"
    AL = "AL"
    AM = "AM"
    AP = "AP"
    BA = "BA"
    CE = "CE"
    DF = "DF"
    ES = "ES"
    GO = "GO"
    MA = "MA"
    MG = "MG"
    MS = "MS"
    MT = "MT"
    PA = "PA"
    PB = "PB"
    PE = "PE"
    PI = "PI"
    PR = "PR"
    RJ = "RJ"
    RN = "RN"
    RO = "RO"
    RR = "RR"
    RS = "RS"
    SC = "SC"
    SE = "SE"
    SP = "SP"
    TO = "TO"


@dataclass(kw_only=True)
class ListaMensagemAlertaRetorno:
    class Meta:
        namespace = "http://www.giss.com.br/tipos-v2_04.xsd"

    mensagem_retorno: list[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ListaMensagemRetorno:
    class Meta:
        namespace = "http://www.giss.com.br/tipos-v2_04.xsd"

    mensagem_retorno: list[TcMensagemRetorno] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class TccomExterior:
    """
    :ivar md_prestacao: Modo de Prestação: 0 - Desconhecido (tipo não
        informado na nota de origem); 1 - Transfronteiriço; 2 - Consumo
        no Brasil; 3 - Movimento Temporário de Pessoas Físicas; 4 -
        Consumo no Exterior;
    :ivar vinc_prest: Vínculo entre as partes no negócio: 0 - Sem
        vínculo com o Tomador/Prestador 1 - Controlada; 2 -
        Controladora; 3 - Coligada; 4 - Matriz; 5 - Filial ou sucursal;
        6 - Outro vínculo;
    :ivar tp_moeda: Identifica a moeda da transação comercial
    :ivar v_serv_moeda: Valor do serviço prestado expresso em moeda
        estrangeira especificada em tpmoeda
    :ivar mec_afcomex_p: Mecanismo de apoio/fomento ao Comércio Exterior
        utilizado pelo prestador do serviço: 00 - Desconhecido (tipo não
        informado na nota de origem); 01 - Nenhum; 02 - ACC -
        Adiantamento sobre Contrato de Câmbio – Redução a Zero do IR e
        do IOF; 03 - ACE – Adiantamento sobre Cambiais Entregues -
        Redução a Zero do IR e do IOF; 04 - BNDES-Exim Pós-Embarque –
        Serviços; 05 - BNDES-Exim Pré-Embarque - Serviços; 06 - FGE -
        Fundo de Garantia à Exportação; 07 - PROEX - EQUALIZAÇÃO 08 -
        PROEX - Financiamento;
    :ivar mec_afcomex_t: Mecanismo de apoio/fomento ao Comércio Exterior
        utilizado pelo tomador do serviço: 00 - Desconhecido (tipo não
        informado na nota de origem); 01 - Nenhum; 02 - Adm. Pública e
        Repr. Internacional; 03 - Alugueis e Arrend. Mercantil de
        maquinas, equip., embarc. e aeronaves; 04 - Arrendamento
        Mercantil de aeronave para empresa de transporte aéreo público;
        05 - Comissão a agentes externos na exportação; 06 - Despesas de
        armazenagem, mov. e transporte de carga no exterior; 07 -
        Eventos FIFA (subsidiária); 08 - Eventos FIFA; 09 - Fretes,
        arrendamentos de embarcações ou aeronaves e outros; 10 -
        Material Aeronáutico; 11 - Promoção de Bens no Exterior; 12 -
        Promoção de Dest. Turísticos Brasileiros; 13 - Promoção do
        Brasil no Exterior; 14 - Promoção Serviços no Exterior; 15 -
        RECINE; 16 - RECOPA; 17 - Registro e Manutenção de marcas,
        patentes e cultivares; 18 - REICOMP; 19 - REIDI; 20 - REPENEC;
        21 - REPES; 22 - RETAERO; 23 - RETID; 24 - Royalties,
        Assistência Técnica, Científica e Assemelhados; 25 - Serviços de
        avaliação da conformidade vinculados aos Acordos da OMC; 26 -
        ZPE;
    :ivar mov_temp_bens: Vínculo da Operação à Movimentação Temporária
        de Bens: 0 - Desconhecido (tipo não informado na nota de
        origem); 1 - Não; 2 - Vinculada - Declaração de Importação; 3 -
        Vinculada - Declaração de Exportação;
    :ivar n_di: Número da Declaração de Importação (DI/DSI/DA/DRI-E)
        averbado
    :ivar n_re: Número do Registro de Exportação (RE) averbado
    :ivar mdic: Compartilhar as informações da NFS-e gerada a partir
        desta DPS com a Secretaria de Comércio Exterior: 0 - Não enviar
        para o MDIC; 1 - Enviar para o MDIC;
    """

    class Meta:
        name = "TCComExterior"

    md_prestacao: TsmodoPrestacao = field(
        metadata={
            "name": "mdPrestacao",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    vinc_prest: TsvincPrest = field(
        metadata={
            "name": "vincPrest",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    tp_moeda: str = field(
        metadata={
            "name": "tpMoeda",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "max_length": 3,
            "white_space": "preserve",
            "pattern": r"[0-9]{3}",
        }
    )
    v_serv_moeda: Decimal = field(
        metadata={
            "name": "vServMoeda",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        }
    )
    mec_afcomex_p: TsmecAfcomExPrest = field(
        metadata={
            "name": "mecAFComexP",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    mec_afcomex_t: TsmecAfcomExToma = field(
        metadata={
            "name": "mecAFComexT",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    mov_temp_bens: TsmovTempBens = field(
        metadata={
            "name": "movTempBens",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    n_di: None | str = field(
        default=None,
        metadata={
            "name": "nDI",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 12,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        },
    )
    n_re: None | str = field(
        default=None,
        metadata={
            "name": "nRE",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 12,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        },
    )
    mdic: TsenvMdic = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )


@dataclass(kw_only=True)
class TcrtcinfoTributosIbscbs:
    """
    :ivar g_ibscbs: Grupo de informações relacionadas ao IBS e à CBS
    """

    class Meta:
        name = "TCRTCInfoTributosIBSCBS"

    g_ibscbs: TcrtcinfoTributosSitClas = field(
        metadata={
            "name": "gIBSCBS",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )


@dataclass(kw_only=True)
class TcrtclistaDocDfe:
    """
    :ivar tipo_chave_dfe: Documento fiscal a que se refere a chaveDfe
        que seja um dos documentos do Repositório Nacional
    :ivar x_tipo_chave_dfe: Descrição da DF-e a que se refere a chaveDfe
        que seja um dos documentos do Repositório Nacional Deve ser
        preenchido apenas quando "tipoChaveDFe = 9 (Outro)"
    :ivar chave_dfe: Chave do Documento Fiscal eletrônico do repositório
        nacional referenciado para os casos de operações já tributadas
    """

    class Meta:
        name = "TCRTCListaDocDFe"

    tipo_chave_dfe: TsrtctipoChaveDfe = field(
        metadata={
            "name": "tipoChaveDFe",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    x_tipo_chave_dfe: None | str = field(
        default=None,
        metadata={
            "name": "xTipoChaveDFe",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        },
    )
    chave_dfe: str = field(
        metadata={
            "name": "chaveDFe",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 50,
            "white_space": "preserve",
        }
    )


@dataclass(kw_only=True)
class TcrtclistaDocFornec:
    """
    :ivar cnpj: Número da inscrição no Cadastro Nacional de Pessoa
        Jurídica (CNPJ) do Fornecedor do serviço
    :ivar cpf: Número da inscrição no Cadastro de Pessoa Física (CPF) do
        Fornecedor do serviço
    :ivar nif: Este elemento só deverá ser preenchido para fornecedores
        não residentes no Brasil
    :ivar c_nao_nif: Motivo para não informação do NIF: 0 - Não
        informado na nota de origem; 1 - Dispensado do NIF; 2 - Não
        exigência do NIF;
    :ivar x_nome: Nome / Razão Social do do Fornecedor do serviço
    """

    class Meta:
        name = "TCRTCListaDocFornec"

    cnpj: None | str = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r"[0-9A-Z]{14}",
        },
    )
    cpf: None | str = field(
        default=None,
        metadata={
            "name": "CPF",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "max_length": 11,
            "white_space": "preserve",
            "pattern": r"[0-9]{11}",
        },
    )
    nif: None | str = field(
        default=None,
        metadata={
            "name": "NIF",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 40,
            "white_space": "preserve",
        },
    )
    c_nao_nif: None | TscodNaoNif = field(
        default=None,
        metadata={
            "name": "cNaoNIF",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    x_nome: str = field(
        metadata={
            "name": "xNome",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 150,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )


@dataclass(kw_only=True)
class TcrtctotalCbs:
    """
    :ivar g_cbscred_pres: Grupo de valores referentes ao crédito
        presumido para CBS
    :ivar v_dif_cbs: Total do Diferimento CBS vDifCBS = vCBS x pDifCBS
    :ivar v_cbs: Total valor da CBS da União vCBS = vBC x (pCBS ou
        pAliqEfetCBS)
    """

    class Meta:
        name = "TCRTCTotalCBS"

    g_cbscred_pres: None | TcrtctotalCbscredPres = field(
        default=None,
        metadata={
            "name": "gCBSCredPres",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    v_dif_cbs: Decimal = field(
        metadata={
            "name": "vDifCBS",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        }
    )
    v_cbs: Decimal = field(
        metadata={
            "name": "vCBS",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        }
    )


@dataclass(kw_only=True)
class TcrtctotalIbs:
    """
    :ivar v_ibstot: Valor total do IBS. vIBSTot = vIBSUF + vIBSMun
    :ivar g_ibscred_pres: Grupo de valores referentes ao crédito
        presumido para IBS
    :ivar g_ibsuftot: Grupo de valores referentes ao IBS Estadual
    :ivar g_ibsmun_tot: Grupo de valores referentes ao IBS Municipal
    """

    class Meta:
        name = "TCRTCTotalIBS"

    v_ibstot: Decimal = field(
        metadata={
            "name": "vIBSTot",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        }
    )
    g_ibscred_pres: None | TcrtctotalIbscredPres = field(
        default=None,
        metadata={
            "name": "gIBSCredPres",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    g_ibsuftot: TcrtctotalIbsuf = field(
        metadata={
            "name": "gIBSUFTot",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    g_ibsmun_tot: TcrtctotalIbsmun = field(
        metadata={
            "name": "gIBSMunTot",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )


@dataclass(kw_only=True)
class TcrtcvaloresIbscbs:
    """
    :ivar v_calc_ree_rep_res: Valor monetário (R$) total relativo ao
        fornecimento próprio de bens materiais ou relacionados a
        operações de terceiros, objeto de reembolso, repasse ou
        ressarcimento pelo recebedor, já tributados e aqui referenciados
        e que não integram da base de cálculo (BC) do ISSQN, do IBS e da
        CBS.
    :ivar uf: Grupo de Informações relativas aos valores do IBS Estadual
    :ivar mun: Grupo de Informações relativas aos valores do IBS
        Municipal
    :ivar fed: Grupo de Informações relativas aos valores da CBS
    """

    class Meta:
        name = "TCRTCValoresIBSCBS"

    v_calc_ree_rep_res: None | Decimal = field(
        default=None,
        metadata={
            "name": "vCalcReeRepRes",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        },
    )
    uf: TcrtcvaloresIbscbsuf = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    mun: TcrtcvaloresIbscbsmun = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    fed: TcrtcvaloresIbscbsfed = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )


@dataclass(kw_only=True)
class TctribOutrosPisCofins:
    """
    :ivar cst: Código de Situação Tributária do PIS/COFINS (CST): 00 -
        Nenhum; 01 - Operação Tributável com Alíquota Básica; 02 -
        Operação Tributável com Alíquota Diferenciada; 03 - Operação
        Tributável com Alíquota por Unidade de Medida de Produto; 04 -
        Operação Tributável monofásica - Revenda a Alíquota Zero; 05 -
        Operação Tributável por Substituição Tributária; 06 - Operação
        Tributável a Alíquota Zero; 07 - Operação Tributável da
        Contribuição; 08 - Operação sem Incidência da Contribuição; 09 -
        Operação com Suspensão da Contribuição;
    :ivar v_bcpis_cofins: Valor da Base de Cálculo do PIS/COFINS (R$).
    :ivar p_aliq_pis: Valor da Alíquota do PIS (%).
    :ivar p_aliq_cofins: Valor da Alíquota da COFINS (%).
    :ivar v_pis: Valor monetário do PIS (R$).
    :ivar v_cofins: Valor monetário do COFINS (R$).
    :ivar tp_ret_pis_cofins: Tipo de retencao do Pis/Cofins: 1 - Retido;
        2 - Não Retido;
    """

    class Meta:
        name = "TCTribOutrosPisCofins"

    cst: TstipoCst = field(
        metadata={
            "name": "CST",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    v_bcpis_cofins: None | Decimal = field(
        default=None,
        metadata={
            "name": "vBCPisCofins",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        },
    )
    p_aliq_pis: None | Decimal = field(
        default=None,
        metadata={
            "name": "pAliqPis",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("99.99"),
            "total_digits": 4,
            "fraction_digits": 2,
        },
    )
    p_aliq_cofins: None | Decimal = field(
        default=None,
        metadata={
            "name": "pAliqCofins",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("99.99"),
            "total_digits": 4,
            "fraction_digits": 2,
        },
    )
    v_pis: None | Decimal = field(
        default=None,
        metadata={
            "name": "vPis",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        },
    )
    v_cofins: None | Decimal = field(
        default=None,
        metadata={
            "name": "vCofins",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        },
    )
    tp_ret_pis_cofins: None | TstipoRetPiscofins = field(
        default=None,
        metadata={
            "name": "tpRetPisCofins",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )


@dataclass(kw_only=True)
class TctribTotal:
    """
    :ivar p_tot_trib: Valor percentual total aproximado dos tributos, em
        conformidade com o artigo 1o da Lei no 12.741/2012
    :ivar ind_tot_trib: Indicador de informação de valor total de
        tributos. Possui valor fixo igual a zero (indTotTrib=0). Não
        informar nenhum valor estimado para os Tributos (Decreto
        8.264/2014). 0 - Não;
    :ivar p_tot_trib_sn: Valor percentual aproximado do total dos
        tributos da alíquota do Simples Nacional (%).
    """

    class Meta:
        name = "TCTribTotal"

    p_tot_trib: None | TctribTotalPercent = field(
        default=None,
        metadata={
            "name": "pTotTrib",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    ind_tot_trib: None | TstipoIndTotTrib = field(
        default=None,
        metadata={
            "name": "indTotTrib",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    p_tot_trib_sn: None | Decimal = field(
        default=None,
        metadata={
            "name": "pTotTribSN",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("99.99"),
            "total_digits": 4,
            "fraction_digits": 2,
        },
    )


@dataclass(kw_only=True)
class TcEndereco:
    class Meta:
        name = "tcEndereco"

    endereco: str = field(
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        }
    )
    numero: str = field(
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        }
    )
    complemento: None | str = field(
        default=None,
        metadata={
            "name": "Complemento",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    bairro: str = field(
        metadata={
            "name": "Bairro",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        }
    )
    codigo_municipio: int = field(
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "total_digits": 7,
        }
    )
    uf: TsUf = field(
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    cep: str = field(
        metadata={
            "name": "Cep",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "max_length": 8,
            "white_space": "preserve",
            "pattern": r"[0-9]{8}",
        }
    )


@dataclass(kw_only=True)
class TcIdentificacaoFornecedor:
    class Meta:
        name = "tcIdentificacaoFornecedor"

    cpf_cnpj: TcCpfCnpj = field(
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )


@dataclass(kw_only=True)
class TcIdentificacaoNfeDeducao:
    class Meta:
        name = "tcIdentificacaoNfeDeducao"

    numero_nfe: int = field(
        metadata={
            "name": "NumeroNfe",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "total_digits": 9,
        }
    )
    uf_nfe: TsUf = field(
        metadata={
            "name": "UfNfe",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    chave_acesso_nfe: None | int = field(
        default=None,
        metadata={
            "name": "ChaveAcessoNfe",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "total_digits": 44,
        },
    )


@dataclass(kw_only=True)
class TcIdentificacaoNfse:
    class Meta:
        name = "tcIdentificacaoNfse"

    numero: int = field(
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "total_digits": 15,
        }
    )
    cpf_cnpj: TcCpfCnpj = field(
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    inscricao_municipal: None | str = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )
    codigo_municipio: int = field(
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "total_digits": 7,
        }
    )


@dataclass(kw_only=True)
class TcIdentificacaoOrgaoGerador:
    class Meta:
        name = "tcIdentificacaoOrgaoGerador"

    codigo_municipio: int = field(
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "total_digits": 7,
        }
    )
    uf: TsUf = field(
        metadata={
            "name": "Uf",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )


@dataclass(kw_only=True)
class TcIdentificacaoPessoaEmpresa:
    class Meta:
        name = "tcIdentificacaoPessoaEmpresa"

    cpf_cnpj: TcCpfCnpj = field(
        metadata={
            "name": "CpfCnpj",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    inscricao_municipal: None | str = field(
        default=None,
        metadata={
            "name": "InscricaoMunicipal",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )


@dataclass(kw_only=True)
class TcInfRps:
    class Meta:
        name = "tcInfRps"

    identificacao_rps: None | TcIdentificacaoRps = field(
        default=None,
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    data_emissao: XmlDate = field(
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    status: str = field(
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "pattern": r"1|2",
        }
    )
    rps_substituido: None | TcIdentificacaoRps = field(
        default=None,
        metadata={
            "name": "RpsSubstituido",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )


@dataclass(kw_only=True)
class TcMensagemRetornoLote:
    class Meta:
        name = "tcMensagemRetornoLote"

    identificacao_rps: TcIdentificacaoRps = field(
        metadata={
            "name": "IdentificacaoRps",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    codigo: str = field(
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 4,
            "white_space": "collapse",
        }
    )
    mensagem: str = field(
        metadata={
            "name": "Mensagem",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 200,
            "white_space": "collapse",
        }
    )


@dataclass(kw_only=True)
class TcSubstituicaoNfse:
    class Meta:
        name = "tcSubstituicaoNfse"

    substituicao_nfse: TcInfSubstituicaoNfse = field(
        metadata={
            "name": "SubstituicaoNfse",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    signature: list[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "max_occurs": 2,
        },
    )
    versao: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        }
    )


@dataclass(kw_only=True)
class ListaMensagemRetornoLote:
    class Meta:
        namespace = "http://www.giss.com.br/tipos-v2_04.xsd"

    mensagem_retorno: list[TcMensagemRetornoLote] = field(
        default_factory=list,
        metadata={
            "name": "MensagemRetorno",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class TcrtclistaDoc:
    """
    :ivar d_fe_nacional: Grupo de informações de documentos fiscais
        eletrônicos que se encontram no repositório nacional
    :ivar doc_fiscal_outro: Grupo de informações de documento fiscais,
        eletrônicos ou não, que não se encontram no repositório nacional
    :ivar doc_outro: Grupo de informações de documento não fiscal.
    :ivar fornec: Grupo de informações do fornecedor do documento
        referenciado
    :ivar dt_emi_doc: Data da emissão do documento dedutível Ano, mês e
        dia (AAAA-MM-DD)
    :ivar dt_comp_doc: Data da competência do documento dedutível Ano,
        mês e dia (AAAA-MM-DD)
    :ivar tp_ree_rep_res: Tipo de valor incluído neste documento,
        recebido por motivo de estarem relacionadas a operações de
        terceiros, objeto de reembolso, repasse ou ressarcimento pelo
        recebedor, já tributados e aqui referenciados
    :ivar x_tp_ree_rep_res: Descrição do reembolso ou ressarcimento
        quando a opção é "99 – Outros reembolsos ou ressarcimentos
        recebidos por valores pagos relativos a operações por conta e
        ordem de terceiro"
    :ivar vlr_ree_rep_res: Valor monetário (total ou parcial, conforme
        documento informado) utilizado para não inclusão na base de
        cálculo do ISS e do IBS e da CBS da NFS-e que está sendo emitida
        (R$)
    """

    class Meta:
        name = "TCRTCListaDoc"

    d_fe_nacional: None | TcrtclistaDocDfe = field(
        default=None,
        metadata={
            "name": "dFeNacional",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    doc_fiscal_outro: None | TcrtclistaDocFiscalOutro = field(
        default=None,
        metadata={
            "name": "docFiscalOutro",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    doc_outro: None | TcrtclistaDocOutro = field(
        default=None,
        metadata={
            "name": "docOutro",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    fornec: None | TcrtclistaDocFornec = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    dt_emi_doc: str = field(
        metadata={
            "name": "dtEmiDoc",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
        }
    )
    dt_comp_doc: str = field(
        metadata={
            "name": "dtCompDoc",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "white_space": "preserve",
            "pattern": r"(((20(([02468][048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1\d)|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[1,3-9])|(1[0-2]))-(29|30)))))",
        }
    )
    tp_ree_rep_res: TsrtctpReeRepRes = field(
        metadata={
            "name": "tpReeRepRes",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    x_tp_ree_rep_res: None | str = field(
        default=None,
        metadata={
            "name": "xTpReeRepRes",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 150,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        },
    )
    vlr_ree_rep_res: Decimal = field(
        metadata={
            "name": "vlrReeRepRes",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        }
    )


@dataclass(kw_only=True)
class TcrtctotalCibs:
    """
    :ivar v_tot_nf: Valor Total da NF considerando os impostos por fora:
        IBS e CBS O IBS e a CBS são por fora, por isso seus valores
        devem ser adicionados ao valor total da NF vTotNF = vLiq (em
        2026) vTotNF = vLiq + vCBS + vIBSTot (a partir de 2027)
    :ivar g_ibs: Grupo de valores referentes ao IBS
    :ivar g_cbs: Grupo de valores referentes à CBS
    :ivar g_trib_regular: Grupo de informações de tributação regular
    :ivar g_trib_compra_gov: Grupo de informações da composição do valor
        do IBS e da CBS em compras governamentais
    """

    class Meta:
        name = "TCRTCTotalCIBS"

    v_tot_nf: Decimal = field(
        metadata={
            "name": "vTotNF",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        }
    )
    g_ibs: TcrtctotalIbs = field(
        metadata={
            "name": "gIBS",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    g_cbs: TcrtctotalCbs = field(
        metadata={
            "name": "gCBS",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    g_trib_regular: None | TcrtctotalTribRegular = field(
        default=None,
        metadata={
            "name": "gTribRegular",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    g_trib_compra_gov: None | TcrtctotalTribCompraGov = field(
        default=None,
        metadata={
            "name": "gTribCompraGov",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )


@dataclass(kw_only=True)
class TctribFederal:
    """
    :ivar piscofins: Grupo de informações dos tributos PIS/COFINS
    """

    class Meta:
        name = "TCTribFederal"

    piscofins: None | TctribOutrosPisCofins = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )


@dataclass(kw_only=True)
class TcDadosFornecedor:
    class Meta:
        name = "tcDadosFornecedor"

    identificacao_fornecedor: None | TcIdentificacaoFornecedor = field(
        default=None,
        metadata={
            "name": "IdentificacaoFornecedor",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    fornecedor_exterior: None | TcFornecedorExterior = field(
        default=None,
        metadata={
            "name": "FornecedorExterior",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )


@dataclass(kw_only=True)
class TcDadosIntermediario:
    class Meta:
        name = "tcDadosIntermediario"

    identificacao_intermediario: TcIdentificacaoPessoaEmpresa = field(
        metadata={
            "name": "IdentificacaoIntermediario",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    razao_social: str = field(
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        }
    )
    codigo_municipio: int = field(
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "total_digits": 7,
        }
    )


@dataclass(kw_only=True)
class TcDadosPrestador:
    class Meta:
        name = "tcDadosPrestador"

    razao_social: str = field(
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        }
    )
    nome_fantasia: None | str = field(
        default=None,
        metadata={
            "name": "NomeFantasia",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "collapse",
        },
    )
    endereco: TcEndereco = field(
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    contato: None | TcContato = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )


@dataclass(kw_only=True)
class TcDadosTomador:
    class Meta:
        name = "tcDadosTomador"

    identificacao_tomador: None | TcIdentificacaoPessoaEmpresa = field(
        default=None,
        metadata={
            "name": "IdentificacaoTomador",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    nif_tomador: None | str = field(
        default=None,
        metadata={
            "name": "NifTomador",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 40,
            "white_space": "collapse",
        },
    )
    razao_social: str = field(
        metadata={
            "name": "RazaoSocial",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        }
    )
    endereco: None | TcEndereco = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    endereco_exterior: None | TcEnderecoExterior = field(
        default=None,
        metadata={
            "name": "EnderecoExterior",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    contato: None | TcContato = field(
        default=None,
        metadata={
            "name": "Contato",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )


@dataclass(kw_only=True)
class TcIdentificacaoDocumentoDeducao:
    class Meta:
        name = "tcIdentificacaoDocumentoDeducao"

    identificacao_nfse: None | TcIdentificacaoNfseDeducao = field(
        default=None,
        metadata={
            "name": "IdentificacaoNfse",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    identificacao_nfe: None | TcIdentificacaoNfeDeducao = field(
        default=None,
        metadata={
            "name": "IdentificacaoNfe",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    outro_documento: None | TcOutroDocumentoDeducao = field(
        default=None,
        metadata={
            "name": "OutroDocumento",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )


@dataclass(kw_only=True)
class TcInfPedidoCancelamento:
    class Meta:
        name = "tcInfPedidoCancelamento"

    identificacao_nfse: TcIdentificacaoNfse = field(
        metadata={
            "name": "IdentificacaoNfse",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    codigo_cancelamento: str = field(
        metadata={
            "name": "CodigoCancelamento",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "pattern": r"1|2|3|4|5",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )


@dataclass(kw_only=True)
class TcinfoTributacao:
    """
    :ivar trib_fed: Grupo de informações de outros tributos relacionados
        ao serviço prestado
    :ivar tot_trib: Grupo de informações para totais aproximados dos
        tributos relacionados ao serviço prestado
    """

    class Meta:
        name = "TCInfoTributacao"

    trib_fed: None | TctribFederal = field(
        default=None,
        metadata={
            "name": "tribFed",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    tot_trib: TctribTotal = field(
        metadata={
            "name": "totTrib",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )


@dataclass(kw_only=True)
class Tcrtcibscbs:
    """
    :ivar x_localidade_incid: Nome da localidade de incidência do
        IBS/CBS
    :ivar x_cclass_trib: Descrição do Código de Classificação Tributária
        do IBS/CBS
    :ivar valores: Grupo de valores brutos referentes ao IBS/CBS
    :ivar tot_cibs: Grupo de Totalizadores
    """

    class Meta:
        name = "TCRTCIBSCBS"

    x_localidade_incid: str = field(
        metadata={
            "name": "xLocalidadeIncid",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 600,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    x_cclass_trib: str = field(
        metadata={
            "name": "xCClassTrib",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 600,
            "white_space": "preserve",
            "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
        }
    )
    valores: TcrtcvaloresIbscbs = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    tot_cibs: TcrtctotalCibs = field(
        metadata={
            "name": "totCIBS",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )


@dataclass(kw_only=True)
class TcrtcinfoReeRepRes:
    """
    :ivar documentos: Grupo relativo aos documentos referenciados nos
        casos de reembolso, repasse e ressarcimento que serão
        considerados na base de cálculo do ISSQN, do IBS e da CBS
    """

    class Meta:
        name = "TCRTCInfoReeRepRes"

    documentos: list[TcrtclistaDoc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_occurs": 1,
            "max_occurs": 1000,
        },
    )


@dataclass(kw_only=True)
class TcDadosDeducao:
    class Meta:
        name = "tcDadosDeducao"

    tipo_deducao: str = field(
        metadata={
            "name": "TipoDeducao",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "pattern": r"1|2|3|4|5|6|7|8|99",
        }
    )
    descricao_deducao: None | str = field(
        default=None,
        metadata={
            "name": "DescricaoDeducao",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 150,
            "white_space": "collapse",
        },
    )
    identificacao_documento_deducao: TcIdentificacaoDocumentoDeducao = field(
        metadata={
            "name": "IdentificacaoDocumentoDeducao",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    dados_fornecedor: TcDadosFornecedor = field(
        metadata={
            "name": "DadosFornecedor",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    data_emissao: XmlDate = field(
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    valor_dedutivel: Decimal = field(
        metadata={
            "name": "ValorDedutivel",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_utilizado_deducao: Decimal = field(
        metadata={
            "name": "ValorUtilizadoDeducao",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )


@dataclass(kw_only=True)
class TcPedidoCancelamento:
    class Meta:
        name = "tcPedidoCancelamento"

    inf_pedido_cancelamento: TcInfPedidoCancelamento = field(
        metadata={
            "name": "InfPedidoCancelamento",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
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
class TcrtcinfoValoresIbscbs:
    """
    :ivar g_ree_rep_res: Grupo de informações relativas a valores
        incluídos neste documento e recebidos por motivo de estarem
        relacionadas a operações de terceiros, objeto de reembolso,
        repasse ou ressarcimento pelo recebedor, já tributados e aqui
        referenciados
    :ivar trib: Grupo de informações relacionados aos tributos IBS e CBS
    :ivar c_localidade_incid: Código IBGE da localidade de incidência do
        IBS/CBS (local da operação)
    :ivar p_redutor: Percentual de redução de aliquota em compra
        governamental
    :ivar v_bc: Valor da Base de Cálculo do ISSQN (R$) = Valor do
        Serviço - Desconto Incondicionado - Deduções/Reduções -
        Benefício Municipal vBC = vServ - descIncond - (vDR ou vCalcDR +
        vCalcReeRepRes) - (vRedBCBM ou VCalcBM)
    """

    class Meta:
        name = "TCRTCInfoValoresIBSCBS"

    g_ree_rep_res: None | TcrtcinfoReeRepRes = field(
        default=None,
        metadata={
            "name": "gReeRepRes",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    trib: TcrtcinfoTributosIbscbs = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    c_localidade_incid: str = field(
        metadata={
            "name": "cLocalidadeIncid",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "white_space": "preserve",
            "pattern": r"[0-9]{7}",
        }
    )
    p_redutor: Decimal = field(
        metadata={
            "name": "pRedutor",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("99.99"),
            "total_digits": 4,
            "fraction_digits": 2,
        }
    )
    v_bc: None | Decimal = field(
        default=None,
        metadata={
            "name": "vBC",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0.00"),
            "max_inclusive": Decimal("999999999999999.99"),
            "total_digits": 17,
            "fraction_digits": 2,
        },
    )


@dataclass(kw_only=True)
class TcConfirmacaoCancelamento:
    class Meta:
        name = "tcConfirmacaoCancelamento"

    pedido: TcPedidoCancelamento = field(
        metadata={
            "name": "Pedido",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    data_hora: XmlDateTime = field(
        metadata={
            "name": "DataHora",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )


@dataclass(kw_only=True)
class TcrtcinfoIbscbs:
    """
    :ivar fin_nfse: Indicador da finalidade da emissão de NFS-e
    :ivar ind_final: Indica operação de uso ou consumo pessoal (art. 57)
    :ivar c_ind_op: Código indicador da operação de fornecimento,
        conforme tabela "código indicador de operação"
    :ivar tp_oper: Código indicador da operação com entes
        Governamentais, conforme situações previstas na LC 214/2025
    :ivar g_ref_nfse:
    :ivar tp_ente_gov: Tipo de ente governamental
    :ivar ind_dest: A respeito do Destinatário dos serviços
    :ivar valores: Grupo de informações relativas aos valores do serviço
        prestado para IBS e CBS
    """

    class Meta:
        name = "TCRTCInfoIBSCBS"

    fin_nfse: TsrtcfinNfse = field(
        metadata={
            "name": "finNFSe",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    ind_final: TsrtcindFinal = field(
        metadata={
            "name": "indFinal",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    c_ind_op: str = field(
        metadata={
            "name": "cIndOp",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "white_space": "preserve",
            "pattern": r"[0-9]{6}",
        }
    )
    tp_oper: None | TsrtctpOper = field(
        default=None,
        metadata={
            "name": "tpOper",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    g_ref_nfse: None | TcrtcinfoIbscbs.GRefNfse = field(
        default=None,
        metadata={
            "name": "gRefNFSe",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    tp_ente_gov: None | TsrtctpEnteGov = field(
        default=None,
        metadata={
            "name": "tpEnteGov",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    ind_dest: TsrtcindDest = field(
        metadata={
            "name": "indDest",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    valores: TcrtcinfoValoresIbscbs = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )

    @dataclass(kw_only=True)
    class GRefNfse:
        ref_nfse: list[str] = field(
            default_factory=list,
            metadata={
                "name": "refNFSe",
                "type": "Element",
                "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
                "max_occurs": 99,
                "min_length": 1,
                "max_length": 50,
                "white_space": "preserve",
                "pattern": r"[!-ÿ]{1}[ -ÿ]{0,}[!-ÿ]{1}|[!-ÿ]{1}",
            },
        )


@dataclass(kw_only=True)
class TcCancelamentoNfse:
    class Meta:
        name = "tcCancelamentoNfse"

    confirmacao: TcConfirmacaoCancelamento = field(
        metadata={
            "name": "Confirmacao",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
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
    versao: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        }
    )


@dataclass(kw_only=True)
class TcRetCancelamento:
    class Meta:
        name = "tcRetCancelamento"

    nfse_cancelamento: TcCancelamentoNfse = field(
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )


@dataclass(kw_only=True)
class TcValoresDeclaracaoServico:
    """
    :ivar valor_servicos:
    :ivar valor_deducoes:
    :ivar valor_pis:
    :ivar valor_cofins:
    :ivar valor_inss:
    :ivar valor_ir:
    :ivar valor_csll:
    :ivar outras_retencoes:
    :ivar val_tot_tributos:
    :ivar valor_iss:
    :ivar aliquota:
    :ivar desconto_incondicionado:
    :ivar desconto_condicionado:
    :ivar trib: Grupo de informações relacionados aos tributos federais
        e valor aproximado dos tributos referentes ao serviço prestado
    :ivar ibscbs: Grupo de informações declaradas pelo emitente
        referentes ao IBS e à CBS
    """

    class Meta:
        name = "tcValoresDeclaracaoServico"

    valor_servicos: Decimal = field(
        metadata={
            "name": "ValorServicos",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        }
    )
    valor_deducoes: None | Decimal = field(
        default=None,
        metadata={
            "name": "ValorDeducoes",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    valor_pis: None | Decimal = field(
        default=None,
        metadata={
            "name": "ValorPis",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    valor_cofins: None | Decimal = field(
        default=None,
        metadata={
            "name": "ValorCofins",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    valor_inss: None | Decimal = field(
        default=None,
        metadata={
            "name": "ValorInss",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    valor_ir: None | Decimal = field(
        default=None,
        metadata={
            "name": "ValorIr",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    valor_csll: None | Decimal = field(
        default=None,
        metadata={
            "name": "ValorCsll",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    outras_retencoes: None | Decimal = field(
        default=None,
        metadata={
            "name": "OutrasRetencoes",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    val_tot_tributos: None | Decimal = field(
        default=None,
        metadata={
            "name": "ValTotTributos",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    valor_iss: None | Decimal = field(
        default=None,
        metadata={
            "name": "ValorIss",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    aliquota: None | Decimal = field(
        default=None,
        metadata={
            "name": "Aliquota",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 5,
            "fraction_digits": 4,
            "white_space": "collapse",
        },
    )
    desconto_incondicionado: None | Decimal = field(
        default=None,
        metadata={
            "name": "DescontoIncondicionado",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    desconto_condicionado: None | Decimal = field(
        default=None,
        metadata={
            "name": "DescontoCondicionado",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    trib: None | TcinfoTributacao = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    ibscbs: None | TcrtcinfoIbscbs = field(
        default=None,
        metadata={
            "name": "IBSCBS",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )


@dataclass(kw_only=True)
class TcDadosServico:
    """
    :ivar valores:
    :ivar iss_retido:
    :ivar responsavel_retencao:
    :ivar item_lista_servico:
    :ivar codigo_cnae:
    :ivar codigo_tributacao_municipio:
    :ivar codigo_nbs:
    :ivar discriminacao:
    :ivar codigo_municipio:
    :ivar codigo_pais:
    :ivar exigibilidade_iss:
    :ivar identif_nao_exigibilidade:
    :ivar municipio_incidencia:
    :ivar numero_processo:
    :ivar com_ext: Grupo de informações relativas à
        exportação/importação de serviço prestado
    """

    class Meta:
        name = "tcDadosServico"

    valores: TcValoresDeclaracaoServico = field(
        metadata={
            "name": "Valores",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    iss_retido: str = field(
        metadata={
            "name": "IssRetido",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "pattern": r"1|2",
        }
    )
    responsavel_retencao: None | str = field(
        default=None,
        metadata={
            "name": "ResponsavelRetencao",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "pattern": r"1|2",
        },
    )
    item_lista_servico: TsItemListaServico = field(
        metadata={
            "name": "ItemListaServico",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    codigo_cnae: None | int = field(
        default=None,
        metadata={
            "name": "CodigoCnae",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "total_digits": 7,
        },
    )
    codigo_tributacao_municipio: None | str = field(
        default=None,
        metadata={
            "name": "CodigoTributacaoMunicipio",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        },
    )
    codigo_nbs: None | str = field(
        default=None,
        metadata={
            "name": "CodigoNbs",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 9,
            "white_space": "collapse",
        },
    )
    discriminacao: str = field(
        metadata={
            "name": "Discriminacao",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 2000,
            "white_space": "collapse",
        }
    )
    codigo_municipio: int = field(
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "total_digits": 7,
        }
    )
    codigo_pais: None | str = field(
        default=None,
        metadata={
            "name": "CodigoPais",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "length": 4,
            "white_space": "collapse",
        },
    )
    exigibilidade_iss: str = field(
        metadata={
            "name": "ExigibilidadeISS",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "pattern": r"1|2|3|4|5|6|7",
        }
    )
    identif_nao_exigibilidade: None | str = field(
        default=None,
        metadata={
            "name": "IdentifNaoExigibilidade",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 4,
            "white_space": "collapse",
        },
    )
    municipio_incidencia: None | int = field(
        default=None,
        metadata={
            "name": "MunicipioIncidencia",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "total_digits": 7,
        },
    )
    numero_processo: None | str = field(
        default=None,
        metadata={
            "name": "NumeroProcesso",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 30,
            "white_space": "collapse",
        },
    )
    com_ext: None | TccomExterior = field(
        default=None,
        metadata={
            "name": "comExt",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )


@dataclass(kw_only=True)
class TcInfDeclaracaoPrestacaoServico:
    class Meta:
        name = "tcInfDeclaracaoPrestacaoServico"

    rps: None | TcInfRps = field(
        default=None,
        metadata={
            "name": "Rps",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    competencia: XmlDate = field(
        metadata={
            "name": "Competencia",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    servico: TcDadosServico = field(
        metadata={
            "name": "Servico",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    prestador: TcIdentificacaoPessoaEmpresa = field(
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    tomador_servico: None | TcDadosTomador = field(
        default=None,
        metadata={
            "name": "TomadorServico",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    intermediario: None | TcDadosIntermediario = field(
        default=None,
        metadata={
            "name": "Intermediario",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    construcao_civil: None | TcDadosConstrucaoCivil = field(
        default=None,
        metadata={
            "name": "ConstrucaoCivil",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    regime_especial_tributacao: None | str = field(
        default=None,
        metadata={
            "name": "RegimeEspecialTributacao",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "pattern": r"1|2|3|4|5|6",
        },
    )
    optante_simples_nacional: str = field(
        metadata={
            "name": "OptanteSimplesNacional",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "pattern": r"1|2",
        }
    )
    incentivo_fiscal: str = field(
        metadata={
            "name": "IncentivoFiscal",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "pattern": r"1|2",
        }
    )
    evento: None | TcEvento = field(
        default=None,
        metadata={
            "name": "Evento",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    informacoes_complementares: None | str = field(
        default=None,
        metadata={
            "name": "InformacoesComplementares",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 2000,
            "white_space": "collapse",
        },
    )
    deducao: list[TcDadosDeducao] = field(
        default_factory=list,
        metadata={
            "name": "Deducao",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )


@dataclass(kw_only=True)
class TcDeclaracaoPrestacaoServico:
    class Meta:
        name = "tcDeclaracaoPrestacaoServico"

    inf_declaracao_prestacao_servico: TcInfDeclaracaoPrestacaoServico = field(
        metadata={
            "name": "InfDeclaracaoPrestacaoServico",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
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
class TcInfNfse:
    class Meta:
        name = "tcInfNfse"

    numero: int = field(
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "total_digits": 15,
        }
    )
    codigo_verificacao: str = field(
        metadata={
            "name": "CodigoVerificacao",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 9,
            "white_space": "collapse",
            "pattern": r"[a-zA-Z0-9]{1,9}",
        }
    )
    data_emissao: XmlDateTime = field(
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    nfse_substituida: None | int = field(
        default=None,
        metadata={
            "name": "NfseSubstituida",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "total_digits": 15,
        },
    )
    outras_informacoes: None | str = field(
        default=None,
        metadata={
            "name": "OutrasInformacoes",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 510,
            "white_space": "collapse",
        },
    )
    valores_nfse: TcValoresNfse = field(
        metadata={
            "name": "ValoresNfse",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    descricao_codigo_tributacao_municipio: None | str = field(
        default=None,
        metadata={
            "name": "DescricaoCodigoTributacaoMunicipio",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_length": 1,
            "max_length": 1000,
            "white_space": "collapse",
        },
    )
    valor_credito: None | Decimal = field(
        default=None,
        metadata={
            "name": "ValorCredito",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "min_inclusive": Decimal("0"),
            "total_digits": 15,
            "fraction_digits": 2,
        },
    )
    prestador_servico: TcDadosPrestador = field(
        metadata={
            "name": "PrestadorServico",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    orgao_gerador: TcIdentificacaoOrgaoGerador = field(
        metadata={
            "name": "OrgaoGerador",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    declaracao_prestacao_servico: TcDeclaracaoPrestacaoServico = field(
        metadata={
            "name": "DeclaracaoPrestacaoServico",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )


@dataclass(kw_only=True)
class TcLoteRps:
    class Meta:
        name = "tcLoteRps"

    numero_lote: int = field(
        metadata={
            "name": "NumeroLote",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "total_digits": 15,
        }
    )
    prestador: TcIdentificacaoPessoaEmpresa = field(
        metadata={
            "name": "Prestador",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    quantidade_rps: int = field(
        metadata={
            "name": "QuantidadeRps",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "total_digits": 4,
        }
    )
    lista_rps: TcLoteRps.ListaRps = field(
        metadata={
            "name": "ListaRps",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "name": "Id",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
        },
    )
    versao: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        }
    )

    @dataclass(kw_only=True)
    class ListaRps:
        rps: list[TcDeclaracaoPrestacaoServico] = field(
            default_factory=list,
            metadata={
                "name": "Rps",
                "type": "Element",
                "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
                "min_occurs": 1,
            },
        )


@dataclass(kw_only=True)
class TcNfse:
    class Meta:
        name = "tcNfse"

    inf_nfse: TcInfNfse = field(
        metadata={
            "name": "InfNfse",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
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
    versao: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r"[1-9]{1}[0-9]{0,1}\.[0-9]{2}",
        }
    )


@dataclass(kw_only=True)
class TcCompNfse:
    """
    :ivar nfse:
    :ivar nfse_cancelamento:
    :ivar nfse_substituicao:
    :ivar ibscbstotal: Grupo de informações geradas pelo sistema GISS
        referentes ao IBS e à CBS automaticamente na conversao em nfse
    :ivar chave_nota_nacional: chave de acesso da NFSE no ADN
    :ivar chave_dps: Identificador da DPS no padrao nacional, sem o
        literal DPS. Reservado: sera informado quando a chave passar a
        ser gerada na emissao da NFS-e
    :ivar serie_dps: Serie da DPS utilizada na transmissao da NFS-e ao
        Ambiente de Dados Nacional
    """

    class Meta:
        name = "tcCompNfse"

    nfse: TcNfse = field(
        metadata={
            "name": "Nfse",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        }
    )
    nfse_cancelamento: None | TcCancelamentoNfse = field(
        default=None,
        metadata={
            "name": "NfseCancelamento",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    nfse_substituicao: None | TcSubstituicaoNfse = field(
        default=None,
        metadata={
            "name": "NfseSubstituicao",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    ibscbstotal: None | Tcrtcibscbs = field(
        default=None,
        metadata={
            "name": "IBSCBSTotal",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
        },
    )
    chave_nota_nacional: None | str = field(
        default=None,
        metadata={
            "name": "ChaveNotaNacional",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "pattern": r"[0-9A-Z]{50}",
        },
    )
    chave_dps: None | str = field(
        default=None,
        metadata={
            "name": "ChaveDPS",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "pattern": r"[0-9]{42}",
        },
    )
    serie_dps: None | str = field(
        default=None,
        metadata={
            "name": "SerieDPS",
            "type": "Element",
            "namespace": "http://www.giss.com.br/tipos-v2_04.xsd",
            "pattern": r"[0-9]{1,5}",
        },
    )


@dataclass(kw_only=True)
class CompNfse(TcCompNfse):
    class Meta:
        namespace = "http://www.giss.com.br/tipos-v2_04.xsd"
