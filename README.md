# pedgraph-tracker

Reference implementation for **"Graph-Associative Tracking of Dense Pedestrian Crowds"** (Computer Vision and Image Understanding).

This repository contains the complete training and evaluation pipeline used in the
paper: dataset loaders, the model, the training loop, the evaluation script and the
released metrics.

## Contents

```
configs/
  default.yaml
src/
  __init__.py
  assoc.py
train.py
eval.py
results/
  metrics.md
requirements.txt
```

## Quick start

```
pip install -r requirements.txt
python train.py --config configs/default.yaml
python eval.py --checkpoint checkpoints/best.pt
```

The released checkpoint reproduces the numbers in `results/metrics.md`.

## Citation

```bibtex
@inproceedings{pedgraph-tracker2026,
  title={Graph-Associative Tracking of Dense Pedestrian Crowds},
  booktitle={Computer Vision and Image Understanding},
  year={2026}
  
}
```
