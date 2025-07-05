# StockPulse – Stock Price Tracker on AWS

StockPulse is a lightweight Python-based stock price tracker that runs on an AWS EC2 instance. It uses shell scripting and cron to automatically fetch live stock prices at regular intervals. API keys are securely managed using a `.gitignore` file.

## Features

- Python script to fetch real-time stock prices using an API
- Shell script for automation
- Cron job to schedule execution every 5 minutes
- Git-based deployment
- API key management using `.gitignore`
- Hosted on an AWS EC2 instance

## Project Structure

stockpulse/
├── app.py           # Python script to fetch stock prices
├── config.py        # Stores API key (not committed)
├── fetch.sh         # Shell script to run app.py and log output
├── stock_log.txt    # Log file for tracking results
└── .gitignore       # Ignores config.py and logs in Git

## Requirements

- Python 3
- Git
- Apache2 or Nginx (Apache used)
- AWS EC2 (Ubuntu)
- A free API key from a stock data provider (e.g., Finnhub or Alpha Vantage)

##  Setup Instructions

### 1. Clone the repository on your EC2 instance

```bash
cd /var/www/html
sudo git clone https://github.com/yourusername/stockpulse.git
cd stockpulse


