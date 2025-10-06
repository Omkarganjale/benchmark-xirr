# XIRR Benchmarking API

A RESTful API for calculating Extended Internal Rate of Return (XIRR) for investment portfolios with benchmark comparison capabilities. This service allows users to calculate the annualized return of their investments and compare them against standard market benchmarks like NIFTY 50.

## Features

- Calculate XIRR for custom cash flows and dates
- Compare portfolio performance against market benchmarks
- Support for multiple benchmark indices (NIFTY, NIFTY50, etc.)
- Absolute return calculation for benchmarks
- Caching mechanism for improved performance
- Comprehensive error handling and input validation
- RESTful API with JSON responses
- Detailed logging

## Tech Stack

- **Backend Framework**: Flask (Python)
- **Database**: SQLite (with SQLAlchemy ORM)
- **Financial Calculations**: pyxirr
- **Market Data**: yfinance (Yahoo Finance API)
- **Data Validation**: Marshmallow
- **Logging**: Python logging module
- **Environment Management**: python-dotenv

## Prerequisites

- Python 3.8+
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd benchmark-xirr
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Copy the `.env.example` file to `.env` and modify as needed:
   ```bash
   cp .env.example .env
   ```

2. Environment variables:
   ```
   DEBUG=True
   HOST=0.0.0.0
   PORT=5000
   LOG_LEVEL=INFO
   SQLALCHEMY_DATABASE_URI=sqlite:///Database.db
   ```

## Running the Application

1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. The API will be available at `http://localhost:5000`

## API Endpoints

### 1. Calculate XIRR

Calculate XIRR for given cash flows and compare with benchmarks.

- **Endpoint**: `POST /api/calculate`
- **Request Body**:
  ```json
  {
    "cashflows": [1000, 2000, 3000],
    "dates": ["2022-01-01", "2022-02-01", "2022-03-01"],
    "benchmarks": ["NIFTY", "NIFTY50"]
  }
  ```
  
  - `cashflows`: List of cash flows (positive for investments, negative for withdrawals)
  - `dates`: List of corresponding dates in YYYY-MM-DD format
  - `benchmarks`: List of benchmark indices to compare against (optional)

- **Success Response (200 OK)**:
  ```json
  {
    "status": "success",
    "data": {
      "portfolio": {
        "xirr": 12.34
      },
      "benchmarks": {
        "NIFTY": {
          "absoluteReturns": 3150.50,
          "xirr": 10.25
        },
        "NIFTY50": {
          "absoluteReturns": 3200.75,
          "xirr": 10.50
        }
      }
    }
  }
  ```

### 2. Health Check

Check if the API is running.

- **Endpoint**: `GET /api/health`
- **Success Response (200 OK)**:
  ```json
  {
    "status": "success",
    "data": {
      "status": "healthy",
      "version": "1.0.0"
    }
  }
  ```

## Project Structure

```
benchmark-xirr/
├── .bruno/                  # API testing collections
├── enums/                   # Enumerations
│   ├── BenchmarkTicker.py   # Supported benchmark tickers
│   └── ResponseStatus.py    # API response statuses
├── models/                  # Database models
│   ├── BaseModel.py         # Base model class
│   ├── BenchmarkRecord.py   # Benchmark data model
│   └── CacheRange.py        # Caching model
├── schemas/                 # Data validation schemas
│   └── XirrCalculationRequestSchema.py
├── services/                # Business logic
│   ├── CachingService.py    # Caching service
│   ├── CalculationService.py# XIRR calculation logic
│   ├── FinancialDataService.py # Market data service
│   └── ValidationService.py # Input validation
├── util/                    # Utility functions
│   └── ResponseUtil.py      # API response formatter
├── views/                   # API endpoints
│   ├── ApiStateView.py      # API state management
│   ├── CalculateView.py     # XIRR calculation endpoint
│   └── HealthCheckView.py   # Health check endpoint
├── .env.example             # Example environment variables
├── .flaskenv                # Flask environment variables
├── app.py                   # Application entry point
├── config.py                # Configuration settings
└── requirements.txt         # Python dependencies
```

## Error Handling

The API returns appropriate HTTP status codes and error messages in the following format:

```json
{
  "status": "error",
  "message": "Detailed error message"
}
```

## Testing

API tests are available in the `.bruno` directory and can be run using [Bruno](https://www.usebruno.com/).

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [pyxirr](https://github.com/apervilon/pyxirr) - XIRR calculation library
- [yfinance](https://pypi.org/project/yfinance/) - Market data provider
- [Marshmallow](https://marshmallow.readthedocs.io/) - Data validation and serialization
