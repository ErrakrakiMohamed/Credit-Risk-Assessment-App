# Credit Risk Assessment App

![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)
![React Version](https://img.shields.io/badge/react-18.x-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)
![Docker Compose](https://img.shields.io/badge/docker-compose-blue.svg)
![CI/CD](https://github.com/ErrakrakiMohamed/Credit-Risk-Assessment-App/actions/workflows/ci-cd.yml/badge.svg)

A modern, dual-container web application designed to evaluate loan approval odds using a pre-trained Machine Learning model. 

This project was recently overhauled from a monolithic Streamlit application into a professional **React + Flask** architecture, fully containerized with Docker Compose, and automated with a GitHub Actions CI/CD pipeline.

## Features

- **Modern React UI**: A beautiful, fast, and responsive Vite + React frontend with dynamic progress bars and contextual assessment cards.
- **RESTful Flask API**: A lightweight Python backend that securely loads the `.pkl` model and serves predictions via a `/predict` endpoint.
- **Microservices Architecture**: The frontend and backend are completely decoupled and run in isolated Docker containers via Docker Compose.
- **Automated CI/CD**: A GitHub Actions pipeline automatically enforces `black` code formatting, builds new Docker images, and pushes them to Docker Hub on every commit to `main`.
- **Pre-commit Hooks**: Enforces zero-tolerance Python formatting rules locally before code can even be committed.

## Installation & Local Development

This application requires **Docker** and **Docker Compose** to run locally. You no longer need to manage Python virtual environments or `npm` installations on your host machine!

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running.
- Git (for version control).

### Quick Start (Using Docker Compose)

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ErrakrakiMohamed/Credit-Risk-Assessment-App.git
   cd Credit-Risk-Assessment-App
   ```

2. **Start the Application**
   ```bash
   docker-compose up --build
   ```

3. **Access the Application**
   - **Frontend (React)**: Open your browser and navigate to `http://localhost:5173`
   - **Backend API (Flask)**: Running silently on `http://localhost:5000`

*Note: The `docker-compose.yml` file defaults to live-reload (bind mounts), meaning any edits you make to the React files or Python files locally will instantly update inside the running containers!*

## CI/CD Pipeline & GitHub Actions

This repository uses **GitHub Actions** for Continuous Integration and Continuous Deployment.

**Pipeline Workflow (`.github/workflows/ci-cd.yml`):**
1. **Linting Check**: Spins up an Ubuntu runner to verify all Python code adheres strictly to the `black` formatter. If the code is messy, the build fails.
2. **Build & Push**: If the linting passes, it logs into Docker Hub using encrypted repository secrets (`DOCKER_USERNAME` / `DOCKER_PASSWORD`).
3. **Distribution**: Rebuilds the latest `credit-risk-backend` and `credit-risk-frontend` images and pushes them live to Docker Hub.

## MLOps Pre-Commit Hook

To ensure the CI/CD pipeline doesn't fail due to formatting, this project uses a local Git hook.

### Setup Local Formatting Hook (For Contributors)
If you plan to contribute code, set up the hook locally:
```bash
# 1. Install Black
pip install black

# 2. Make the hook script executable (Mac/Linux)
chmod +x .git/hooks/pre-commit
```
Now, anytime you run `git commit`, the hook will automatically check your Python files. If they fail, fix them by running `python -m black .`

## Model Details

The application uses an Artificial Neural Network trained on LendingClub historical loan data (2007-2018). It evaluates approval risk based on:
- FICO Credit Score
- Annual income
- Loan amount
- Debt-to-income (DTI) ratio
- Revolving Balance

## Dependencies

**Backend (`requirements.txt`)**
- `Flask`
- `flask-cors`
- `pandas`
- `scikit-learn`
- `joblib`
- `black`

**Frontend (`frontend/package.json`)**
- `react` / `react-dom`
- `vite`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

- **Developer**: Mohamed Errakraki 
- **GitHub**: [ErrakrakiMohamed](https://github.com/ErrakrakiMohamed)

---

**Note**: This application is for educational purposes only and should not be used as the sole basis for financial decisions. Always consult with financial professionals for loan and credit advice.
