# JVS Corups for ๐ค datasets

## Preparation 

1. Download the JVS Corpus from the official web page and extract it to this directory
    - [Shinnosuke Takamichi \(้ซ้ ๆไนไป\) \- jvs\_corpus](https://sites.google.com/site/shinnosuketakamichi/research-topics/jvs_corpus)
2. Run `fix.sh` to fix wrong file names
    - If zip file you downloaded is `md5 hash: 2987778b0ee830914bfebb97783d0c3e`
3. Run `prepare.py` to generate `all_transcripts.txt` file
4. Add `from jvs_datasets import jvs_datasets` in your python scripts
    - Need to include this directory in your `PYTHONPATH`

## Usage

```python
In [1]: from jvs_datasets import jvs_datasets
Using custom data configuration default-f40f9d93b88f3f56
Reusing dataset csv (/Users/yag_ays/.cache/huggingface/datasets/csv/default-f40f9d93b88f3f56/0.0.0/6b9057d9e23d9d8a2f05b985917a0da84d70c5dae3d22ddd8a3f22fb01c69d9e)
100%|โโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโโ| 1/1 [00:00<00:00, 508.09it/s]

In [2]: jvs_datasets[0]
Out[2]:
{'file_id': 'VOICEACTRESS100_001',
 'sentence': 'ใพใใๆฑๅฏบใฎใใใซใไบๅคงๆ็ใจๅผใฐใใใไธป่ฆใชๆ็ใฎไธญๅคฎใซ้ใใใใใจใๅคใใ',
 'path': '/Users/yag_ays/dev/speech-to-text/jvs_datasets/jvs_ver1/jvs096/parallel100/wav24kHz16bit/VOICEACTRESS100_001.wav'}
```

