# Data Download
This repo contains scripts for downloading datasets and knowledge files of all tasks in [ELEVATER](https://computer-vision-in-the-wild.github.io/ELEVATER/). In this repo, we provide a central hub to all the datasets along with our collected knowledge files to facilitate future end-to-end training on ELEVATER benchmark. Note that:

- Our software toolkit supports automatic dataset downloading, and knowledge files are a part of toolkit.
- Please refer to the original license of the each dataset, and this benchmark is for academic research purpose.


## Image Classification

```Shell
pip install vision-datasets>=0.2.0
cd classification
```

Download all datasets

```Shell
python download_datasets.py --ds all
```

Download a specific dataset

```Shell
python download_datasets.py --ds `DATASET_NAME`

# `DATASET_NAME` should be one of ['caltech-101', 'cifar-10', 'cifar-100', 'country211', 'dtd', 'eurosat_clip', 'fer-2013', 'fgvc-aircraft-2013b-variants102', 'food-101', 'gtsrb', 'hateful-memes', 'kitti-distance', 'mnist', 'oxford-flower-102', 'oxford-iiit-pets', 'patch-camelyon', 'ping-attack-on-titan-plus', 'ping-whiskey-plus', 'rendered-sst2', 'resisc45_clip', 'stanford-cars', 'voc-2007-classification']
```

Download knowledge files

```Shell
python download_knowledge.py
```

## Object Detection
```Shell
cd detection
```

Download all datasets
```
python download.py
```

Download a specific dataset
```
python download.py --dataset_names `DATASET_NAME`
```

Knowledge files are already included in the repo
```
detection/*yaml
```
