#!/usr/bin/env bash

#
#  This is used to load any mibs defined in netdisc/snmp/ and anything nested within
#  The mibs are specified by 'MIB = "SOMETHING-MIB"'
#
#  The mibs are passed to pysnmp's mibdump.py to load and to leave them in netdisc/snmp/pymibs
#
#  Then anything *.py that is in netdisc/snmp/pymibs, except for __init__.py, will be
#  copied to netdisc/snmp/asn1mibs
#
#  This is only necessary during development to make sure all necessary mibs are included
#  in the package
#
#
#  TODO:  Separate strategy for when easysnmp support is broken out of netdisc
#

#
debugging=1

pydest=$(find . -type d -path "*/netdisc/snmp/pymibs")
if [[ ! -d $pydest ]]; then
    echo "$pydest doesn't exist.  Exiting."
    exit 1
fi

asn1dest=$(find . -type d -path "*/netdisc/snmp/asn1mibs")
if [[ ! -d $asn1dest ]]; then
    echo "$asn1dest doesn't exist.  Exiting."
    exit 1
fi

source="/mibs.thola.io/"
if [[ ! -d $source ]]; then
    echo "$source doesn't exist.  Exiting."
    exit 1
fi

#Step 1.  Extract mib definitions that are needed
necessary_mibs=$(find . -name "*.py" -path "*netdisc/snmp*" ! -path "*mibs*" | xargs grep -Pho 'MIB\s*=\s*"\K.*(?=")' | sort | uniq)

for mib in $necessary_mibs; do
    existing=$(find $pydest -name "${mib}.py")
    if [[ -f $existing ]]; then
        [[ $debugging -ne 0 ]] && echo "$existing exists.  Skipping"
        continue
    fi
    [[ $debugging -ne 0 ]] && echo "Loading py mib version of $mib"
    cmd="mibdump.py --mib-source=$source --destination-directory=$pydest --rebuild $mib"
    eval $cmd &>/dev/null
    if [[ $? -ne 0 ]]; then
        echo "Problem with $mib"
        echo "recreate with: $cmd"
    fi
done

loaded_mibs=$(find $pydest -name "*.py" ! -name "__*" -printf "%f\n" | sed s/\.py//)

for pymib in $loaded_mibs; do
    asn1_mib=$(find $source -name $pymib)
    if [ -z $asn1_mib ]; then
        echo "Warning!  unable to find asn1: $pymib"
    else
        destfile=$(echo "${asn1dest}/${pymib}")
        [[ $debugging -ne 0 ]] && echo "Copying: $asn1_mib to $destfile"
        if [[ ! -f "$destfile" ]]; then
            cp $asn1_mib $asn1dest
        else
          [[ $debugging -ne 0 ]] && echo "ASN1 already exists: $pymib"
        fi
    fi
done
