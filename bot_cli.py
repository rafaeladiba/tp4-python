from argparse import ArgumentParser, Namespace

def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "-c", "--config", help="Config file", required=True, dest="config"
    )
    return parser.parse_args()