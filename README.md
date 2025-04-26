# Currency Exchange Rate Notifier

A Python script that checks if today's exchange rate is favorable compared to recent averages and sends an SMS notification via Twilio if it's a good time to convert currency.

## Features

- Fetches 30 days of historical exchange rate data from [Resenje.org Kurs API](https://kurs.resenje.org)
- Compares today's rate against:
  - 7-day (1 week) average
  - 30-day (1 month) average
- Sends SMS alerts via Twilio when the rate is above thresholds
- Configurable for different currencies and threshold percentages

## Prerequisites

- Python 3.x
- Twilio account (for SMS notifications)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Luka582/SMS_exchange_notification.git