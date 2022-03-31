import logging
import pathlib
import shutil

logger = logging.getLogger(__name__)
# logger.addHandler(logging.NullHandler())


def copy_mibs(miblist: list[pathlib.Path], dest_dir: pathlib.Path):
    if not dest_dir.exists():
        dest_dir.mkdir(parents=True)

    for mibfile in miblist:
        filename = mibfile.parts[-1]
        target = pathlib.Path.joinpath(dest_dir, filename)
        if target.exists():
            logger.error(f"Skipping %s: File Exists", str(target))
            continue
        shutil.copy2(mibfile, target)


from netdisc.snmp import asn1mibs, pymibs

ASN1MIBS = list(pathlib.Path(asn1mibs.__file__).parent.glob("[!_]*"))
ASN1TARGET = pathlib.Path.joinpath(pathlib.Path.home(), ".snmp", "mibs")

PYMIBS = list(pathlib.Path(pymibs.__file__).parent.glob("[!_]*"))
PYTARGET = pathlib.Path.joinpath(pathlib.Path.home(), ".pysnmp", "mibs")


if __name__ == "__main__":
    copy_mibs(ASN1MIBS, ASN1TARGET)
    copy_mibs(PYMIBS, PYTARGET)
