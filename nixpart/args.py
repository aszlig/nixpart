import os
import argparse


def handle_nixos_config(path):
    fullpath = os.path.abspath(path)
    if not os.path.exists(fullpath):
        msg = "{} does not exist.".format(fullpath)
        raise argparse.ArgumentTypeError(msg)
    return fullpath


def parse_args(args=None):
    desc = "Declaratively create partitions and filesystems"
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument(
        '-v', '--verbose', dest='verbosity', action='count', default=0,
        help="Print what's going on, use multiple times to increase verbosity"
    )

    parser.add_argument(
        '-X', '--xml', dest='is_xml', action='store_true',
        help="The provided NixOS configuration file is in XML format"
    )

    parser.add_argument(
        'nixos_config', type=handle_nixos_config,
        help="A NixOS configuration file"
    )

    return parser.parse_args(args=args)