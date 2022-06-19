import os
import argparse
import urllib.request

parser = argparse.ArgumentParser(description='Download ELEVATER image classification benchmark datasets.')
parser.add_argument('--ds', default='all', help='Dataset to download.', type=str)
parser.add_argument('--knowledge', default='all', help='Knowledge source type: [wiki, wordnet, gpt3].', type=str)
parser.add_argument('--output_dir', default='./data', help='Output directory.', type=str)

args = parser.parse_args()

ALL_DATASETS = ['caltech-101', 'cifar-10', 'cifar-100', 'country211', 'dtd', 'eurosat_clip', 'fer-2013', 'fgvc-aircraft-2013b-variants102', 'food-101', 'gtsrb', 'hateful-memes', 'kitti-distance', 'mnist', 'oxford-flower-102', 'oxford-iiit-pets', 'patch-camelyon', 'ping-attack-on-titan-plus', 'ping-whiskey-plus', 'rendered-sst2', 'resisc45_clip', 'stanford-cars', 'voc-2007-classification']

ALL_KNOWLEDGE = ['wiki', 'wordnet', 'gpt3']

assert args.ds == 'all' or args.ds in ALL_DATASETS, f"Datasets should be one of: {ALL_DATASETS}.  Use `--ds all` to download all datasets"

def download_exec(fpath, fname):
    output_dir = f'{args.output_dir}/{fpath}'
    os.makedirs(output_dir, exist_ok=True)
    urllib.request.urlretrieve(f'https://elevater.blob.core.windows.net/resources/{fpath}/{fname}?sp=r&st=2022-06-08T05:41:38Z&se=2023-06-08T13:41:38Z&spr=https&sv=2021-06-08&sr=c&sig=TEPxyA1%2Fxu6wu7v4zFcJ7O8O7VGSWwXmZDiVyt9Xx7U%3D', f'{output_dir}/{fname}')

def download(ds, knowledge):
    print(f'Downloading dataset: {ds}...')
    if knowledge in ['wiki', 'wordnet']:
        fname = f'{ds}_knowledge.tsv'
        fpath = 'knowledge/external'
    elif knowledge == 'gpt3':
        fname = f'GPT3_{ds}.tsv'
        fpath = 'knowledge/gpt3'
    else:
        raise ValueError(f'Unknown knowledge source: {knowledge}')
    download_exec(fpath, fname)
    print(f'Dataset download finishes: {ds}.')

def download_spawn(knowledge):
    print('===========================================')
    print(f'Downloading {knowledge} knowledge...')
    if args.ds != "all":
        download(args.ds, knowledge)
    else:
        for ds in ALL_DATASETS:
            download(ds, knowledge)
    print(f'Knowledge download finishes: {knowledge}.')
    print('===========================================')

if args.knowledge != "all":
    download_spawn(args.knowledge)
else:
    for knowledge in ALL_KNOWLEDGE:
        download_spawn(knowledge)
