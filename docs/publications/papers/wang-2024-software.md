---
tags:
  - Software
  - Network Analysis
  - Systems Biology
  - 2024
authors:
  - Wang R
  - Smith J
  - Chen M
date: 2024-03-10
pub_type: software
repo_url: https://github.com/mathbiolab/netViz
doi: 10.5281/zenodo.1234567
---

# netViz: An R package for network visualization and analysis

**Authors**: Wang R, Smith J, Chen M

**Version**: 1.2.0 (March 2024)

**DOI**: [10.5281/zenodo.1234567](https://doi.org/10.5281/zenodo.1234567)

**Repository**: [GitHub - mathbiolab/netViz](https://github.com/mathbiolab/netViz)

## Overview

netViz is an R package for comprehensive network visualization and analysis, designed specifically for biological networks such as protein-protein interaction networks, gene regulatory networks, and metabolic networks. The package provides a suite of tools for network construction, visualization, analysis, and integration with various data types such as gene expression, proteomics, and metabolomics data.

## Key Features

- **Flexible network construction**: Create networks from various data formats including edge lists, adjacency matrices, and common network file formats.
- **Interactive visualization**: Produce publication-quality static visualizations or interactive web-based visualizations with customizable layouts, styles, and annotations.
- **Network analysis**: Calculate centrality measures, identify network modules, perform pathway enrichment analysis, and detect differentially connected nodes between conditions.
- **Data integration**: Overlay and visualize multi-omics data on network structures to reveal relationships and patterns.
- **Statistical testing**: Perform statistical tests to identify significant network features and compare network properties across conditions.
- **Extensible architecture**: Easily integrate with other R packages in the Bioconductor ecosystem.

## Installation

```r
# Install from CRAN
install.packages("netViz")

# Or install the development version from GitHub
# install.packages("devtools")
devtools::install_github("mathbiolab/netViz")
```

## Example Usage

```r
library(netViz)

# Load example data
data(example_network)

# Create a basic network visualization
plot_network(example_network)

# Identify network modules
modules <- detect_modules(example_network, method = "louvain")

# Visualize modules with different colors
plot_network(example_network, modules = modules)

# Perform pathway enrichment on modules
enrichment <- module_enrichment(modules, database = "KEGG")
```

## Citation

Wang R, Smith J, Chen M (2024). "netViz: An R package for network visualization and analysis." *Journal of Open Source Software*, 9(95), 4567. https://doi.org/10.21105/joss.04567
