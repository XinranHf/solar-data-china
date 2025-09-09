# Solar Data China

This repository contains code and data for analyzing solar energy trends in China.

## Overview

This project was developed as part of a Summer 2025 internship. The goal is to collect, process, and analyze solar energy data from various sources in China, providing insights into production, capacity, and regional trends.

## Features

- Data collection from public and proprietary sources
- Data cleaning and preprocessing
- Visualization of solar energy trends
- Statistical analysis and reporting

## Getting Started

1. Clone this repository.
2. Install the required dependencie
```
pip install -r requirements.txt
```
3. Follow the instructions in the `notebooks/` directory to run analyses.

## Google Earth Engine (GEE) Scripts

This project includes a Google Earth Engine script hosted at:
[Sampling 1](https://code.earthengine.google.com/8a5ec307976e95411467d00c411095dd)
[Sampling 2](https://code.earthengine.google.com/21336bb49b7734bce6d2e186ac416349)
[Landcover](https://code.earthengine.google.com/1be46db2d38545db6dd1352aeb33e022)


### Accessing and running the script

1. Open the script link above in the Google Earth Engine Code Editor.

2. Import the `focus-counties.csv` file from this repository into your Google Earth Engine assets and name it `focus_counties`.  

3. In your GEE script, adapt the import statement as follows:
   ```javascript
   var countiesList = ee.FeatureCollection("projects/fromglc/assets/focus_counties");
   ```

3. Run the script to visualize suitability maps and export outputs to your Google Drive.

## Repository Structure 

solar-data-china/
│
├── data/ # Datasets
│ ├── raw_data/         # Original raw datasets
│ └── data_processed/   # Cleaned and preprocessed datasets
│
├── GEE_exports/        # Outputs exported from Google Earth Engine
├── Google_my_Maps/     # Manual mappings created with Google My Maps
│
├── scripts/            # Python scripts 
│ ├── analysis/         # Comparative analysis of datasets 
│ ├── data_processing/  # Data cleaning, preprocessing, and transformations
│ ├── mapdata/          # Administrative boundaries and shapefile handling
│ ├── model/            # Training and evaluation of ML models
│ ├── satellite_image/  # Preprocessing of satallite_image
│ └── scan/             # Detection and segmentation experiments
│
├── requirements.txt # Python dependencies
└── README.md # Main documentation


