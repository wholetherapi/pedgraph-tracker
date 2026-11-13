import argparse
import yaml

from src.model import Model


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', default='configs/default.yaml')
    args = parser.parse_args()
    cfg = yaml.safe_load(open(args.config))
    print('training with', cfg)


if __name__ == '__main__':
    main()
