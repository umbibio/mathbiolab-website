---
date: 2023-11-03
categories:
  - Computational Biology
  - Bayesian Methods
  - Genomics
  - Transcriptomics
authors:
  - aarriojas
  - spalatano
  - jmacoska
  - kzarringhalam
journal: NAR Genomics and Bioinformatics
doi: 10.1093/nargab/lqad106
---

# A Bayesian noisy logic model for inference of transcription factor activity from single cell and bulk transcriptomic data

**Authors**: Arriojas A, Patalano S, Macoska J, Zarringhalam K

**Journal**: NAR Genomics and Bioinformatics, 5(4), lqad106 (2023)

**DOI**: [10.1093/nargab/lqad106](https://doi.org/10.1093/nargab/lqad106)


<!-- more -->

## Abstract

Transcription factors (TFs) play a crucial role in regulating gene expression, but inferring their activities from transcriptomic data remains challenging. Here, we present NLBayes, a Bayesian noisy logic framework for the inference of TF activities from both bulk and single-cell RNA sequencing data. Our approach models the complex regulatory interactions between TFs and their target genes using a probabilistic Boolean logic framework that accounts for the inherent noise and uncertainty in gene expression data. NLBayes incorporates prior knowledge of TF-target relationships and uses Markov Chain Monte Carlo (MCMC) sampling to infer the posterior distributions of TF activities. Through extensive validation on simulated data and applications to real datasets, we demonstrate that NLBayes outperforms existing methods in accuracy, robustness to noise, and interpretability. We apply NLBayes to analyze TF activities in prostate cancer progression and treatment response, revealing key regulators and their dynamics. Furthermore, our model's capability to handle single-cell data allows for the identification of cell type-specific TF activities and regulatory patterns. NLBayes provides a powerful and versatile tool for the systems-level analysis of transcriptional regulation in complex biological processes and diseases.

## Key Points

- Novel Bayesian framework for inferring transcription factor activities
- Handles both bulk RNA-seq and single-cell RNA-seq data
- Integrates prior knowledge of regulatory relationships
- Provides uncertainty quantification through posterior distributions
- Application to cancer progression reveals key regulatory dynamics
- Open-source implementation with user-friendly interfaces

## Supporting Materials

- [**NLBayes Web Application**](https://umbibio.math.umb.edu/nlbayes)
- [**R Package**](https://github.com/umbibio/nlbayes-rcran)
- [**Python Package**](https://github.com/umbibio/nlbayes-python)
- [**Datasets (PRJNA881605)**](https://www.ncbi.nlm.nih.gov/sra/?term=PRJNA881605)
- [**Reproducibility Data (Zenodo)**](https://doi.org/10.5281/zenodo.10116663)

## Citation

```bibtex
@article{arriojas2023bayesian,
  title={A Bayesian noisy logic model for inference of transcription factor activity from single cell and bulk transcriptomic data},
  author={Arriojas, Argenis and Patalano, Stefan and Macoska, Jill and Zarringhalam, Kourosh},
  journal={NAR Genomics and Bioinformatics},
  volume={5},
  number={4},
  pages={lqad106},
  year={2023},
  publisher={Oxford University Press},
  doi={10.1093/nargab/lqad106}
}
```
