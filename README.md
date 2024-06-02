# Retirement Calculator

A Streamlit application for calculating retirement savings. This application allows users to input their current age, retirement age, current savings, annual savings, estimated annual return, and target savings to calculate their estimated savings at retirement age, any shortfall or overage, suggestions for adjusting annual savings, and progress towards the target savings.

## Features

- Input fields for current age, retirement age, current savings, annual savings, estimated annual return, and target savings.
- Calculates estimated savings at retirement age.
- Provides shortfall or overage between estimated savings and target savings.
- Suggests how much to increase or decrease annual savings to reach target savings.
- Indicates progress towards target savings.

## Requirements

- Python 3.8+
- Poetry
- Streamlit

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/retirement_calculator.git
   cd retirement_calculator
   ```

2. Install the dependencies using Poetry:

   ```bash
   poetry install
   ```

## Usage

1. Run the Streamlit application:

   ```bash
   poetry run streamlit run retirement_calculator.py
   ```

2. Open your web browser and navigate to `http://localhost:8501` to use the application.

## Project Structure

```
retirement_calculator/
├── functions.py
├── poetry.lock
├── pyproject.toml
└── retirement_calculator.py
```

- `functions.py`: Contains the non-Streamlit functions for calculating savings and adjustments.
- `retirement_calculator.py`: Main Streamlit application file.
- `pyproject.toml`: Poetry configuration file.
- `poetry.lock`: Poetry lock file.

## License

This project is licensed under the MIT License.
