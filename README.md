# Async Netwok Monitor
This is alightweight asynchronous network monitoring tool written in python

## Features(requirements)
- Monitors multiple network services concurrently using asyncio
- Checks TCP connectivity to specified hosts and ports
- Handles connection errors and timeouts
- Logs results with timestamps to network.log
- Repeats checks every 60 seconds

## Monitored Services
- Google DNS: 8.8.8.8:53
- Cloudflare HTTPS: 1.1.1.1:443
- Local SSH: 127.0.0.1:22

## Why Asyncio?
Asyncio allows multiple network connections to be checked concurrently instead of waiting for each service. 
This improves efficiency when monitoring several hosts.

## Running as a systemd service
On a Linux system with systemd create a service unit that runs monitor.py using python3 then set the working directory to the project folder and configure automatic restart.
On WSL2 systemd must be enabled before using systemctl
