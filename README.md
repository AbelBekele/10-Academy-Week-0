# Welcome to Week-0 Task-5 of 10 Academy's intensive training program!

## Overview

This repository seamlessly merges Data Science and ML Engineering, featuring MLOps, analysis pipelines, and frontend-backend integration. Explore time series analysis, message classification, feature stores, and more. Master Software Engineering and MLOps concepts while building ML models with React and Tailwind CSS on the frontend, and Flask on the backend. Contribute to this dynamic blend of technologies—happy coding!
## Table of Contents

- [Project Title](#Welcome-to-Week-0-Task-2-of-10-Academy's-intensive-training-program!)
  - [Overview](#overview)
  - [Goals to Achieve](#goals-to-achieve)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Branches](#branches)
    - [Commits](#commits)
    - [Code Organization](#code-organization)
    - [Notebooks](#notebooks)
        - [Day 1 Analysis](#day-1-analysis)
        - [Day 2 Analysis](#day-2-analysis)
  - [Analysis results](#analysis-results)
      - [Histogram of the time difference](#histogram-of-the-time-difference)
      - [Message classification, topic modelling, and sentiment analysis](#message-classification-topic-modelling-and-sentiment-analysis)
  - [Contributing](#contributing)
  - [License](#license)


## Goals to Achieve

- **MLOps & Pipelines:** Explore MLOps components, analysis pipelines for efficient data processing.
- **Data Science Skills:** Enhance time series analysis, message classification, and statistical thinking.
- **ML Engineering Proficiency:** Implement feature stores, model versioning, monitoring, CI, Dockerization, and package building.
- **ML Model Excellence:** Build accurate, interpretable, and scalable ML models.
- **MLFlow Versioning:** Utilize MLFlow for effective model versioning, ensuring traceability and reproducibility.

## Installation

To get started with the project, follow these installation steps:

1. **Python Environment:**
    ```bash
    python -m venv your_env_name
    ```

    Replace `your_env_name` with the desired name for your environment.
    
    **Activate the environment:**

    - On Windows:

    ```bash
    .\your_env_name\scripts\activate
    ```

    - On macOS/Linux:

    ```bash
    source your_env_name/bin/activate
    ```

2. **Clone this package**
    To install the `network_analysis` package, follow these steps:

    1. Clone the repository:
        ```bash
        git clone https://github.com/AbelBekele/10-Academy-Week-0.git
        ```
    2. Navigate to the project directory:
        ```bash
        cd 10-Academy-Week-0
        ```
    
    3. Install the required dependencies:
        ```bash
        pip install -r requirements.txt
        ```


3. **Continuous Integration:**
    - CI/CD configurations are already set up. Refer to the CI/CD documentation for additional details.

## Usage

### Branches

In this repository, the branches are organized as follows:

- **main:** The main branch
    - Containing all working and updated branch pushes    

- **task-1:** The branch for Day 1 analysis.
    - **Dev Environment Setup:** Successfully set up the Python environment, Git version control, and CI/CD.
    - **Relevant Skills Demonstration:** Showcase proficiency in the CRISP-DM framework, data understanding, EDA techniques, and statistical thinking.
    - **Project Planning - EDA & Stats:** Effectively plan and execute the project using the CRISP-DM framework, perform EDA, and derive actionable insights from statistical analyses.

- **task-2:** The current branch for Day 2 analysis. 
    - 

  ```bash
  git checkout -b task-2
    ```
### Code Organization

Restructured the code by moving functions into `/src/loader.py` and `/src/utils.py`. In the analysis notebooks, used the `SlackDataLoader` from `/src/loader.py` and functions from `/src/utils.py` for data loading needs.

## Notebooks
### Day 1 Analysis
  - `/notebooks/EDA.ipynb`
### Day 2 Analysis
  - `/notebooks/Time difference analysis.ipynb`
  - `/notebooks/ML model task2.ipynb`

## Contributions
Contributions are welcome! Before contributing, please review our contribution guidelines.

##  License
This project is licensed under the MIT License.