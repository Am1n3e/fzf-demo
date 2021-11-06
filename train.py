import logging
import argparse

logger = logging.getLogger(__name__)


def _parse_args():
    arg_parser = argparse.ArgumentParser(description='Train a model')
    arg_parser.add_argument('data_file_path')

    return arg_parser.parse_args()


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")

    args = _parse_args()

    logging.info('Training using: %s', args.data_file_path)


if __name__ == '__main__':
       main()
