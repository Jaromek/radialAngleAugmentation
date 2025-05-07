# radialAngleAugmentation 📊

This project provides tools for data augmentation and numerical analysis on various datasets. It includes utilities for generating, processing, and visualizing data, as well as comparing different oversampling methods. 

---

## 📁 Project Structure

- **📓 augmentationProcess.ipynb**  
  The main notebook demonstrating the data augmentation process step by step, including visualizations and explanations. 

- **🛠 augmentationFiles/**  
  Python modules implementing the core logic:
  - `Augmentation.py` – logic for augmenting points. 
  - `Coordinate.py` – class representing a point in space (Cartesian and polar coordinates). 
  - `DataUtils.py` – utilities for normalization, outlier removal, center of mass calculation, etc. 
  - `SectionUtils.py` – section and subsection division, Section, SubSection, SectionGroup classes. 
  - `radiousAngleMethod.py` – implementation of the RAM (Radius Angle Method). 
- **📚 articleNotebooks/**  
  Notebooks and scripts for comparative analysis:
  - `numericalResultsCheck.ipynb` – comparison of RAM, SMOTE, ADASYN, ROS on various datasets (wine, cancer, blobs). 
  - `numericalResults.py` – functions for summarizing results. 
  - `plotting.py` – functions for data and results visualization. 

- **🖼 images/**  
  Visualization results:
  - `augmentationPlot/` – augmentation plots (e.g., blobs, cancer). 
  - `correlationMatrix/` – correlation matrices. 
  - `methodPlot/`, `poprawione/` – additional comparative plots. 

---

## 🚀 Quick Start

1. Install required libraries:  
    ```sh
    pip install -r requirements.txt
    ```  
2. Open and run the [`augmentationProcess.ipynb`](augmentationProcess.ipynb) notebook in Jupyter Notebook or VS Code.   
3. Explore and modify the code in the [`augmentationFiles/`](augmentationFiles/) folder and analyze results in the [`articleNotebooks/`](articleNotebooks/). 

---

## ✨ Key Features

- **Data Augmentation**: Section and subsection division, generation of new points in polar space.   
- **Oversampling Methods Comparison**: RAM, SMOTE, ADASYN, ROS. 
- **Visualization**: Plots in Cartesian and polar coordinates, correlation matrices. 

---

## 📦 Example Usage

The [`augmentationProcess.ipynb`](augmentationProcess.ipynb) notebook contains a complete pipeline:  
1. Data loading and normalization  
2. Section and subsection division  
3. Point augmentation  
4. Results visualization 

---

## 📝 Licence

Project intended for scientific and educational purposes. 

---

> Have fun exploring radialAngleAugmentation! 
