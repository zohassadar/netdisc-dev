import logging
import os
import re
import functools
from netdisc.tools import helpers, pandor

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
# from netdisc.tools import pandor
INDEX = "index"
PROMPT = "Enter something> "
SHORTEN = 60


def print_device_info(device):
    print(f"These neighbors came from: {device.hostname}")
    print("")


def print_short_help():

    cmds = [
        "f <filter> [!]",
        "i <range> [!]",
        "e <range> [!]",
        "s <key>",
        "rs <key>",
        "a",
        "A",
        "n",
        "N",
        "r",
        "h for help",
        "! to commit",
    ]
    print(f'Usage: {", ".join(cmds)}')


def print_long_help():
    print(
        """
    The list displayed is a list of neighbors that have been discovered.
    Use the following commands to narrow down the list either by index
    or by filtering the field.

    Filter Syntax:
    <cmd> [args] [!]

    Use "!" at end of the command to immediately commit after applying filter, otherwise
    the filtered neighbors will display with the chance to review the results. Using "!"
    by itself can be used to commit what is displayed after filtering.

    Simple filters:
    a - all neighbors
    A - all neighbors for remainder of session

    n - no neighbors
    N - no neighbors for remainder of session

    i <range> [!] - include neighbors by index.
        i 1,3,5-10
        i 1-100 !

    e <range> [!] - exclude neighbors by index
        i 7-9,14-7
        i 5,7 !

    f <filter> [!] - filter by arbitrary expression
        f ip in 192.168.42.0/24
        f hostname ~ '(?i)-gw[12]?'
        f ip in 192.168.42.0/24 and hostname ~ '(?i)-gw[12]?'
        f ip in 192.168.42.0/24 and (hostname ~ '(?i)-gw[12]? or hostname ~ '(?i)core')
        f sysinfo !: 'Phone' !


    Other commands:

    ! - commit - Neighbors displayed will be sent

    r - reset - Reset the current filter

    s <key> - sort - sort the list by fieldname

    rs <key> - reverse sort - reverse of sort

    h - help - display this message and wait

    """
    )
    input("Press enter when done...")


def expand_numerical_range(rngstr: str) -> list[int]:
    result = set()
    filtered = re.sub(r"[^\d,-]", "", rngstr)
    if not filtered:
        raise ValueError(f"Invalid range: {rngstr}")
    for group in filtered.split(","):
        if not (span := sorted([int(i) for i in group.split("-") if i])):
            continue
        begin, end = span[0], span[-1]
        result.update(set(range(begin, end + 1)))
    return sorted(list(result))


class PrintOutputTable:
    def __init__(self, neighbors, fieldnames: list, shorten: int = SHORTEN):
        self.shorten = shorten
        self._results = neighbors
        self.fieldnames = fieldnames
        self._fieldnames = [INDEX] + fieldnames
        self._output()

    @functools.cached_property
    def _column_widths(self):
        results = {}
        for field in self._fieldnames:
            fieldlengths = []
            for r in self._results:
                value = r.get(field, "")
                shortened = helpers.debug_shorten(value, self.shorten)
                fieldlengths.append(len(str(shortened)))
            if field != INDEX:
                fieldlengths.append(len(field))
            else:
                fieldlengths.append(2)
            results[field] = max(fieldlengths) + 2
        return results

    def _print_row(self, fieldvalues):
        for field in self._fieldnames:
            value = helpers.debug_shorten(str(fieldvalues[field]), self.shorten)
            print(value.ljust(self._column_widths[field]), end="")
        print("")

    def _output(self) -> None:
        _output = []
        _output.append({fn: fn if fn != INDEX else "" for fn in self._fieldnames})
        _output.append({fn: "-" * len(fn) for fn in self._fieldnames})
        _output.extend(self._results)
        for result in _output:
            self._print_row(result)


class InteractiveNeighborFilter:
    STARTING_FIELDS = ["hostname", "local_int", "ip", "sysinfo"]
    MAPPING = {
        "interface_name": "local_int",
        "interface": "remote_int",
    }

    @functools.cached_property
    def REVERSE_MAPPING(self):
        return {v: k for k, v in self.MAPPING.items()}

    def forward_map(self, key):
        return self.MAPPING.get(key, key)

    def reverse_map(self, key):
        return self.REVERSE_MAPPING.get(key, key)

    def __init__(self):
        self._fields = self.STARTING_FIELDS.copy()
        self._skip_all = False
        self._discover_all = False
        self._sortkey = lambda nd: dict(nd).get("sysinfo")
        self._reverse = False
        self._filter = None
        self._index_filter = None
        self._exclude = None
        self._reset()

    def filter_index(self, index):
        result = index in self._index_filter
        if self._exclude:
            return not (result)
        return result

    def _reset(self):
        self._filter = pandor.AllowAll()
        self._index_filter = []
        self._exclude = True

    def _indexed_and_mapped(self, pre_filtered):
        originals = {}
        converted = []
        pre_filtered = sorted(pre_filtered, key=self._sortkey, reverse=self._reverse)
        for index, neighbor in enumerate(pre_filtered, start=1):
            originals[index] = neighbor
            if not self.filter_index(index):
                continue
            if not self._filter.filter(neighbor):
                continue
            neighbordict = dict(index=index)
            for key, value in dict(neighbor).items():
                neighbordict[self.forward_map(key)] = value
            converted.append(neighbordict)
        return (originals, converted)

    def _parse_command(self, command):
        cmd_split = command.split()
        commit = False
        if cmd_split and cmd_split[-1] == "!":
            cmd_split = cmd_split[:-1]
            commit = True
        match cmd_split:
            case ["a"]:
                self._reset()
                commit = True
                print("All neighbors allowed")
            case ["A"]:
                self._discover_all = True
                self._reset()
                commit = True
                print("All neighbors allowed going forward")
            case ["n"]:
                self._reset()
                self._exclude = False
                commit = True
                print("No neighbors allowed")
            case ["N"]:
                self._skip_all = True
                self._reset()
                self._exclude = False
                commit = True
                print("No neighbors allowed going forward")
            case ["i", *args]:
                self._reset()
                args = "".join(args)
                try:
                    self._index_filter = expand_numerical_range(args)
                    self._exclude = False
                    print(f"Including: {args}")
                except ValueError:
                    commit = False
                    print(f"Invalid range: {args}")
            case ["e", *args]:
                self._reset()
                args = "".join(args)
                try:
                    self._index_filter = expand_numerical_range(args)
                    print(f"Excluding: {args}")
                except ValueError:
                    commit = False
                    print(f"Invalid range: {args}")
            case ["s", str(key)]:
                if key not in self._fields:
                    print(f"Invalid key: {key}")
                else:
                    self._reverse = False
                    self._sortkey = lambda n: getattr(n, key, 0)
                    print(f"Sorting by: {key}")
            case ["rs", str(key)]:
                if key not in self._fields:
                    print(f"Invalid key: {key}")
                else:
                    self._reverse = True
                    self._sortkey = lambda n: getattr(n, key, 0)
                    print(f"Reverse sorting by: {key}")
            case ["f", *args]:
                self._reset()
                args = " ".join(args)
                try:
                    self._filter = pandor.AttrFilterForkFactory(args)
                    self._filter.attr = self.reverse_map(self._filter.attr)
                    print(f"Filtering by: {args}")
                except ValueError:
                    commit = False
                    print(f"Invalid filter: {args}")
            case ["h"]:
                print_long_help()
            case ["r"]:
                commit = False
                self._reset()
                print("Resetting")
            case []:
                pass
            case _:
                print(f"Unknown input: {command}")
        print("\n\n")
        return commit

    def filter(self, device, pre_filtered):
        logger.debug("%s %s - Filtering neighbors", device.hostname, device.device_ip)
        if not pre_filtered:
            logger.debug("%s %s - Empty list", device.hostname, device.device_ip)
            return pre_filtered
        if self._discover_all:
            logger.debug(
                "%s %s - Set to _discover_all", device.hostname, device.device_ip
            )
            return pre_filtered
        if self._skip_all:
            logger.debug("%s %s - Set to _skip_all", device.hostname, device.device_ip)
            return []

        originals, converted = self._indexed_and_mapped(pre_filtered)
        while True:
            print_device_info(device)
            print("")
            PrintOutputTable(converted, self._fields)
            print("")
            print_short_help()
            print("")
            commit = self._parse_command(input(PROMPT))
            originals, converted = self._indexed_and_mapped(pre_filtered)
            if commit:
                return [originals[i.get(INDEX)] for i in converted]
