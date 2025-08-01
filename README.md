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
[Open the GEE script here](https://code.earthengine.google.com/978e963cffcdf94f9502d9399da77497)

### Accessing and running the script

1. Open the script link above in the Google Earth Engine Code Editor.

2. Import the `focus-counties.csv` file from this repository into your Google Earth Engine assets and name it `focus_counties`.  

3. In your GEE script, adapt the import statement as follows:
   ```javascript
   var countiesList = ee.FeatureCollection("projects/fromglc/assets/focus_counties");
   ```

3. Run the script to visualize suitability maps and export outputs to your Google Drive.



