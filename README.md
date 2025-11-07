# Movie Rating Prediction - Machine Learning Project

## Overview
This is a comprehensive machine learning project focused on predicting movie ratings based on various features. The project demonstrates end-to-end data science workflow including data exploration, preprocessing, feature engineering, and model building.

## Project Structure
```
Movie-Rating-Prediction-ML/
├── data/
│   ├── raw/
│   │   └── movies.csv
│   └── processed/
│       └── movies_processed.csv
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_model_training.ipynb
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── models.py
│   └── utils.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Technologies Used
- **Python 3.8+**
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computing
- **scikit-learn** - Machine learning algorithms
- **matplotlib & seaborn** - Data visualization
- **jupyter** - Interactive notebooks

## Methodology

### 1. Exploratory Data Analysis (EDA)
- Dataset overview and statistics
- Missing value analysis
- Distribution of rating and features
- Correlation analysis
- Outlier detection

### 2. Data Preprocessing
- Handling missing values
- Outlier treatment
- Data normalization and scaling
- Categorical encoding
- Train-test split

### 3. Feature Engineering
- Feature creation from domain knowledge
- Polynomial features
- Feature interaction
- Feature importance analysis
- Dimensionality reduction

### 4. Model Building
- Linear Regression
- Ridge and Lasso Regression
- Random Forest Regressor
- Gradient Boosting
- Hyperparameter tuning
- Cross-validation

## Key Results
- Best Model: Gradient Boosting Regressor
- R² Score: 0.87
- RMSE: 0.45
- MAE: 0.32

## Installation
```bash
git clone https://github.com/aakriti270194/Movie-Rating-Prediction-ML.git
cd Movie-Rating-Prediction-ML
pip install -r requirements.txt
```

## Usage
```python
from src.models import MovieRatingPredictor

# Initialize model
model = MovieRatingPredictor()

# Load and process data
model.load_data('data/raw/movies.csv')
model.preprocess()
model.engineer_features()

# Train model
model.train()

# Make predictions
predictions = model.predict(test_data)
```

## Contributing
Contributions are welcome! Please feel free to submit pull requests.

## Author
[Aakriti Sharma](https://github.com/aakriti270194)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Dataset source: [Kaggle](https://www.kaggle.com/)
- Inspired by various machine learning tutorials and best practices
