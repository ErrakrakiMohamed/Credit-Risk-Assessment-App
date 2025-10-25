# Credit Risk Assessment App

![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![Last Updated](https://img.shields.io/badge/last_updated-February_2025-green.svg)

A Streamlit-based web application designed to evaluate loan approval odds using a pre-trained Artificial Neural Network (ANN) model. This project leverages machine learning to analyze financial data and provide personalized predictions and improvement tips based on user inputs.

## Features

- **Personalized Assessment**: Input your financial details (income, credit score, loan amount, etc.) to get a tailored loan approval probability
- **Dynamic Visualization**: Interactive Plotly chart displaying approval odds with color-coded thresholds (low, medium, high)
- **Improvement Tips**: Receive actionable suggestions to enhance your loan approval chances
- **Educational Content**: Learn about factors influencing loan decisions via "How It Works" and "About" tabs
- **Local Data Privacy**: Data is processed in-browser and not stored or shared


## Installation

follow the installation instructions below to run the app locally.

### Prerequisites

- Python 3.9 or higher
- Git (for version control)

### Setup Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ErrakrakiMohamed/Credit-Risk-Assessment-App
   cd Credit-Risk-Assessment
   ```

2. **Create a Virtual Environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Required Files**
   
   Ensure the following files are in your project directory:
   - `credit_risk_model.pkl` (pre-trained ANN model)
   - `minmax_scaler.pkl` (pre-trained scaler)

## Usage

### Running the App

Start the Streamlit application:
```bash
streamlit run app.py
```

Open your browser and navigate to `http://localhost:8501`.

### Interacting with the App

1. Navigate to the **Assessment** tab to enter your financial details
2. Click **"Predict Approval Odds"** to see your approval probability and personalized tips
3. Explore the **How It Works** and **About** tabs for additional information
4. Adjust input values (income, credit score, etc.) to see how they impact the prediction


## Dependencies

All dependencies are listed in `requirements.txt`:

```
streamlit==1.36.0
pandas==2.2.2
numpy==1.26.4
tensorflow==2.16.2
scikit-learn==1.5.1
joblib==1.4.2
plotly==5.22.0
```

## Model Information

The application uses an Artificial Neural Network (ANN) trained on LendingClub data (2007-2018) to predict loan approval probabilities. The model considers multiple financial factors including:

- Annual income
- Credit score
- Loan amount
- Employment length
- Debt-to-income ratio
- Credit history length

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes and commit: `git commit -m "Description of changes"`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

Please ensure your code adheres to the project's style and includes appropriate documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

- **GitHub**: [https://github.com/my](https://github.com/my)
- **Issues**: For questions or support, feel free to open an issue on the GitHub repository

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/), [TensorFlow](https://www.tensorflow.org/), and [Plotly](https://plotly.com/)
- Trained on LendingClub historical loan data (2007-2018)
- Inspired by the need for accessible financial risk assessment tools

---

**Note**: This application is for educational purposes only and should not be used as the sole basis for financial decisions. Always consult with financial professionals for loan and credit advice.
