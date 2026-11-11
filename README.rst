============
nfselib.giss
============

Bindings Python (xsdata) do webservice de NFS-e do GissOnline (Eicon), versao 2:
leiaute ABRASF 2.04 com os grupos da reforma tributaria (tributos federais,
comercio exterior, IBS/CBS, NBS).

Os bindings sao gerados do pacote oficial de XSDs publicado no portal de
desenvolvedores de cada municipio
(``https://<municipio>.giss.com.br/giss-ajuda/desenvolvedores.html``,
``Schemas_XSD-Servicos_Prestados.rar``). Os campos ficam em ``snake_case``
(``LoteRps`` vira ``lote_rps``): no ABRASF o nome do elemento e igual ao do tipo,
e manter o nome original faria o campo esconder a classe.

Uso
===

.. code-block:: python

    from xsdata.formats.dataclass.serializers import XmlSerializer

    from nfselib.giss.v2_04 import enviar_lote_rps_envio_v2_04 as envio
    from nfselib.giss.v2_04 import tipos_v2_04 as tipos

    lote = envio.EnviarLoteRpsEnvio(lote_rps=tipos.TcLoteRps(...))
    xml = XmlSerializer().render(lote)

A biblioteca so tem os tipos. Envelope SOAP, assinatura e transmissao ficam no
provedor ``Giss`` do ``erpbrasil.edoc``.

Regerar
=======

Nunca editar XSD nem binding a mao. Copiar os XSDs do pacote oficial para
``schemas/giss/v2_04`` e rodar ``scripts/generate.sh`` (xsdata com
``scripts/.xsdata.xml``). O XSD publicado ja ficou defasado em relacao a
producao: a validacao local por XSD nao deve bloquear o envio.

Schemas desta versao: ``tipos-v2_04.xsd`` com data interna de 01/10/2026
(sha256 ``09878c9257e24313...``).
