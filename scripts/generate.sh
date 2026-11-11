#!/bin/zsh
# Monta a lib nfselib.giss a partir do pacote oficial de XSDs do GissOnline V2.
set -eu
LIB="$1"; SRC="$2"
mkdir -p "$LIB/schemas/giss/v2_04" "$LIB/tests/exemplos" "$LIB/scripts" "$LIB/nfselib/giss"
cp "$SRC/x/xsd_sp/Schemas_XSD-Servicos_Prestados/"*.xsd "$LIB/schemas/giss/v2_04/"
cp "$SRC/x/ex_sp/Exemplo XML - Serviços Prestados/"*.xml "$LIB/tests/exemplos/"
cd "$LIB"
rm -rf nfselib/giss/v2_04
uvx --from 'xsdata[cli]' xsdata generate schemas/giss/v2_04 --config scripts/.xsdata.xml 2>&1 | tail -2
find nfselib -name "*.py" | wc -l
shasum -a 256 schemas/giss/v2_04/tipos-v2_04.xsd | cut -c1-16
