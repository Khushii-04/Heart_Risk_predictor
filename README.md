# Heart Disease Risk Predictor

This project predicts the risk of heart disease based on various health parameters using machine learning.

## Features

- Interactive web app built with Streamlit
- Machine learning model trained on heart disease dataset
- Real-time prediction with probability scores

## Files

- `Heart_Risk.ipynb`: Jupyter notebook with data analysis, model training, and evaluation
- `app.py`: Streamlit web application for predictions
- `heart.csv`: Dataset used for training
- `model.pkl`: Trained machine learning model

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Khushii-04/Heart_Risk_predictor.git
   cd Heart_Risk_predictor
   ```

2. Install dependencies:
   ```bash
   pip install streamlit pandas scikit-learn
   ```

## Usage

### Running the Web App

To run the Streamlit web application:

```bash
streamlit run app.py
```

This will start the app on `http://localhost:8501`. Open this URL in your browser to use the heart disease risk predictor.

### Running the Notebook

To explore the data analysis and model training:

1. Open `Heart_Risk.ipynb` in Jupyter Notebook or VS Code
2. Run the cells to see the analysis and train the model

## Model Details

The model is a Random Forest classifier trained on features like age, cholesterol, blood pressure, etc. It predicts the probability of heart disease risk.
