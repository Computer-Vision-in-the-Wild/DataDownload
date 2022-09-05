import pathlib
import argparse

from vision_datasets import DatasetHub
from vision_datasets.common.dataset_downloader import DatasetDownloader
from vision_datasets.common import Usages

parser = argparse.ArgumentParser(description='Download ELEVATER image classification benchmark datasets.')
parser.add_argument('--ds', default='caltech-101', help='Dataset to download.', type=str)
parser.add_argument('--output_dir', default='./data', help='Output directory.', type=str)

args = parser.parse_args()

ALL_DATASETS = ['caltech-101', 'cifar-10', 'cifar-100', 'country211', 'dtd', 'eurosat_clip', 'fer-2013', 'fgvc-aircraft-2013b-variants102', 'food-101', 'gtsrb', 'hateful-memes', 'kitti-distance', 'mnist', 'oxford-flower-102', 'oxford-iiit-pets', 'patch-camelyon', 'rendered-sst2', 'resisc45_clip', 'stanford-cars', 'voc-2007-classification']

assert args.ds == 'all' or args.ds in ALL_DATASETS, f"Datasets should be one of: {ALL_DATASETS}.  Use `--ds all` to download all datasets"

hub = DatasetHub(pathlib.Path('./resources/vision_datasets.json').read_text())
downloader = DatasetDownloader('https://cvinthewildeus.blob.core.windows.net/datasets', hub.dataset_registry)

def download(ds):
    print(f'Downloading dataset: {ds}...')
    downloader.download(ds, target_dir=args.output_dir, purposes=[Usages.TRAIN_PURPOSE, Usages.VAL_PURPOSE, Usages.TEST_PURPOSE])
    print(f'Dataset download finishes: {ds}.')

if args.ds != "all":
    download(args.ds)
else:
    for ds in ALL_DATASETS:
        download(ds)
