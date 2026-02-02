# Energy Price Prediction

A machine learning project for predicting energy prices using both Ordinary Least Squares (OLS) regression and Artificial Neural Network (ANN) models. The project uses a microservices architecture deployed via Docker containers.

Created by Antea Bendo and Eleni Sklaveniti as part of the course __‘M. Grum: Advanced AI-based Application Systems’__ by the
__‘Junior Chair for Business Information Science, esp. AI-based Application Systems’__ at University of Potsdam.

## Overview

This system predicts energy prices by analyzing historical data spanning two years (January 1, 2024 to January 1, 2026). The data is retrieved via API and split into 80% training and 20% testing datasets. The project supports two prediction models:

- **OLS (Ordinary Least Squares)**: Statistical linear regression model
- **ANN (Artificial Neural Network)**: Deep learning model using TensorFlow/Keras Sequential Model

## Architecture

The project is organized into four Docker-based microservices:

### 1. **knowledgeBase**
Stores trained models and their configurations:
- `currentAiSolution.keras` - Trained ANN model
- `currentOlsSolution.xml` - Trained OLS model

### 2. **activationBase**
Contains the input data for predictions:
- `current_activation.csv` - Features for current predictions (time, price_lag, target_price)

### 3. **codeBase**
Executes the prediction scripts:
- `apply_ann_solution.py` - Runs ANN predictions
- `apply_ols_solution.py` - Runs OLS predictions

### 4. **learningBase**
Handles model training and data preparation:
- Fetches data from API (2-year historical data)
- Splits data (80/20 train/test)
- Trains both OLS and ANN models

## Prerequisites

- Docker Desktop (for macOS users, ensure you're running on Apple Silicon/ARM64 architecture)
- Docker Compose
- External Docker volume: `ai_system`

## Setup

### 1. Create the shared volume

```bash
docker volume create ai_system
```

### 2. Build individual Docker images

Each component has its own Dockerfile. They call be pulled from dockerhub with the following commands if needed. 

```bash
docker pull anteab/activationbase_energy_prediction

docker pull anteab/learningbase_energy_prediction 

docker pull anteab/knowledgebase_energy_prediction

docker pull anteab/codebase_energy_prediction
```

## Usage

### Running Individual Services

Each service has its own `docker-compose.yml` file and can be run independently:

```bash

docker compose -f images/activaitonbase_energy_prediction/docker-compose.yml up

docker compose -f images/learningbase_energy_prediction/docker-compose.yml up

docker compose -f images/knowledgebase_energy_prediction/docker-compose.yml up

docker compose -f images/codebase_energy_prediction/docker-compose.yml up

```

### Running Complete Prediction Scenarios

#### OLS Prediction

```bash
docker compose -f scenarios/apply_ols_solution/docker-compose.yml up
```

This will:
1. Load the knowledge base (OLS model)
2. Load the activation data
3. Execute OLS prediction
4. Output predicted vs real values

#### ANN Prediction

```bash
docker compose -f scenarios/apply_ann_solution/docker-compose.yml up
```

This will:
1. Load the knowledge base (ANN model)
2. Load the activation data
3. Execute ANN prediction
4. Output predicted vs real values

## Model Features

Both models use the following input features:
- **time**: Timestamp or time index
- **price_lag**: Prior day price (lagged feature)

Target variable:
- **target_price**: The energy price to predict

## Data Flow

1. **Training Phase** (learningBase):
    - Fetch 2 years of historical energy price data
    - Split into 80% training, 20% testing
    - Train OLS and ANN models
    - Save models to knowledgeBase

2. **Prediction Phase** (codeBase):
    - Load trained model from knowledgeBase
    - Load input features from activationBase
    - Generate predictions
    - Compare with actual values

## Dependencies

### Python Libraries
- **TensorFlow/Keras**: For ANN model
- **statsmodels**: For OLS regression
- **NumPy**: Numerical computations
- **Pandas**: Data manipulation
- **joblib**: Model serialization

## Troubleshooting

### "File not found" errors
- Verify the shared volume `ai_system` exists: `docker volume ls`
- Check file paths use absolute paths (e.g., `/tmp/knowledgeBase/`)
- Ensure proper capitalization (Linux is case-sensitive)

## Output Example

```
OLS Prediction happened
Real Value: -1.82551288
Prediction: -1.8234567

ANN Prediction happened
Real Value: -1.82551288
Prediction: -1.8255
```

## License

This project is licensed under the [**GNU Affero General Public License v3.0 (AGPL-3.0)**](https://www.gnu.org/licenses/agpl-3.0.en.html) .