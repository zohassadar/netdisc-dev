import argparse
import pathlib
import re
import shutil
import string
import subprocess

"""
find ~/netdisc/ndsnmp/ -name "*.py" \
 | xargs grep -hoP 'MIB = "\K[^"]*' \
 | uniq \
 | while read mib; \
 do python ~/netdisc/pymib.py -s ~/repos/netdisco-mibs/ -d ~/netdisc/netdisc/snmp/pymibs -r ~/netdisc/netdisc/snmp/asn1mibs $mib;
 done
"""

MIB_CONVERT = string.Template(
    r"""mibdump.py \
    --mib-source=/home/rwd/mibs.thola.io/ \
    --destination-directory=/home/rwd/.pysnmp/mibs/ \
    --rebuild  \
    LLDP-MIB"""
)


parser = argparse.ArgumentParser()

# parser.add_argument(
#     "-s",
#     "--source",
#     type=pathlib.Path,
#     required=True,
#     help="Source of ASN1 MIB Files",
# )

parser.add_argument(
    "-d",
    "--dest",
    type=pathlib.Path,
    required=True,
    help="Destination of Converted files",
)
parser.add_argument(
    "-r",
    "--raw",
    type=pathlib.Path,
    help="Destination of copied ASN1 files",
)
parser.add_argument(
    "mib",
    type=str,
    nargs=1,
    help="Name of MIB",
)


def main():
    import pprint

    args = parser.parse_args()
    mib = args.mib[0]
    # source: pathlib.Path = args.source
    dest: pathlib.Path = args.dest
    raw: pathlib.Path = args.raw
    pprint.pprint(vars(args))
    for path in (dest, raw):
        if path and not path.exists():
            path.mkdir(parents=True, exist_ok=True)

    subprocess.call(
        MIB_CONVERT.substitute(
            # source=str(source),
            dest=str(dest),
            mib=mib,
        ).split()
    )
    SOURCE_SEARCH = re.compile(
        r"^# ASN.1 source file://(?P<mib_source>.*)$", re.M
    ).search
    if args.raw:
        for converted_mib in dest.glob("*.py"):
            with open(converted_mib) as mib_file:
                contents = mib_file.read()
            if result := SOURCE_SEARCH(contents):
                mib_source = pathlib.Path(result.group("mib_source"))

                mib_destination = pathlib.Path.joinpath(raw, mib_source.parts[-1])
                print(mib_destination)
                if not mib_destination.exists():
                    print(f"Copying {mib_source}")
                    shutil.copy(mib_source, mib_destination)


if __name__ == "__main__":
    main()
