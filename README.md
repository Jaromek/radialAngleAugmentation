# DataScientificProject

This project provides tools for data augmentation and numerical analysis on 2D datasets. It includes utilities for generating, processing, and visualizing data, as well as comparing various oversampling methods.

## Project Structure

- **augmentationProcess.ipynb**  
  The main notebook demonstrating the data augmentation process step by step, including visualizations and explanations.

- **augmentationFiles/**  
  Python modules implementing the core logic:
  - `Augmentation.py` – logic for augmenting points.
  - `Coordinate.py` – class representing a point in space (Cartesian and polar coordinates).
  - `DataUtils.py` – utilities for normalization, outlier removal, center of mass calculation, etc.
  - `SectionUtils.py` – section and subsection division, Section, SubSection, SectionGroup classes.
  - `radiousAngleMethod.py` – implementation of the RAM (Radius Angle Method).
  - `__pycache__/` – Python cache files.

- **articleNotebooks/**  
  Notebooks and scripts for comparative analysis:
  - `metodyNumeryczneSprawdzenia.ipynb` – comparison of RAM, SMOTE, ADASYN, ROS on various datasets (wine, cancer, blobs).
  - `numericalResults.py` – functions for summarizing results.
  - `plotting.py` – functions for data and results visualization.

- **images/**  
  Visualization results:
  - `augmentationPlot/` – augmentation plots (e.g., blobs, cancer).
  - `correlationMatrix/` – correlation matrices.
  - `methodPlot/`, `poprawione/` – additional comparative plots.

## Quick Start

1. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```
2. Open and run the [`augmentationProcess.ipynb`](augmentationProcess.ipynb) notebook in Jupyter Notebook or VS Code.
3. Explore and modify the code in the [`augmentationFiles/`](augmentationFiles/) folder and analyze results in [`articleNotebooks/`](articleNotebooks/).

## Key Features

- **Data Augmentation**: Section and subsection division, generation of new points in polar space.
- **Oversampling Methods Comparison**: RAM, SMOTE, ADASYN, ROS.
- **Visualization**: Plots in Cartesian and polar coordinates, correlation matrices.

## Example Usage

The [`augmentationProcess.ipynb`](augmentationProcess.ipynb) notebook contains a complete pipeline:
- Data loading and normalization
- Section and subsection division
- Point augmentation
- Visualization of results

## Authors

This project is intended for scientific and educational purposes.

---

For implementation details, see the source files in the [`augmentationFiles/`](augmentationFiles/) directory.
