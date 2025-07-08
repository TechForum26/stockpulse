# StockPulse – Stock Price Tracker on AWS

StockPulse is a lightweight Python-based stock price tracker that runs on an AWS EC2 instance. It uses shell scripting and cron to automatically fetch live stock prices at regular intervals. API keys are securely managed using a `.gitignore` file.

## Features

- Python script to fetch real-time stock prices using an API
- Shell script for automation
- Cron job to schedule execution every 5 minutes
- Git-based deployment
- API key management using `.gitignore`
- Hosted on an AWS EC2 instance

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
```

## 2. Add your API key

```bash
API_KEY = "your-api-key-here"
```
Make sure this file is not committed by verifying .gitignore includes:

```bash
config.py
stock_log.txt
```
## 3. Test the script

```bash
python3 app.py
```

## 4. Set up the automation script

```bash
#!/bin/bash
cd /var/www/html/stockpulse
python3 app.py >> stock_log.txt
echo "Fetched at $(date)" >> stock_log.txt
```
Make it executable:
```bash
chmod +x fetch.sh
```

## 5. Set up the cron job

```bash
crontab -e
```

Add the following line to run every 5 minutes:

```bash
*/5 * * * * /var/www/html/stockpulse/fetch.sh
```


## License

This project is for educational and personal portfolio use only.
