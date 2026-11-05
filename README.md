# SAILHAB Professional Website Monitor

A Python-based website monitoring tool that checks multiple websites,
measures response times, identifies HTTP errors, and generates CSV reports.

## Features

- Monitor multiple websites automatically.
- Check HTTP response status codes.
- Measure website response times.
- Detect connection failures and HTTP errors.
- Calculate monitoring success rates.
- Generate CSV reports for record keeping.

## Requirements

- Python 3
- requests library

## Installation

Install the required library:

    python -m pip install requests

## Configuration

Add website addresses to websites.txt, one per line.

Example:

    https://example.com
    https://google.com
    https://github.com

## Run

    python monitor.py

## Reports

The program automatically generates:

    monitor_report.csv

The report includes timestamps, website addresses, HTTP statuses,
response times, and monitoring results.

## Project Status

Working prototype tested on Android Termux.

## Important

This tool performs basic availability checks. It does not guarantee
continuous uptime or replace professional infrastructure monitoring.
