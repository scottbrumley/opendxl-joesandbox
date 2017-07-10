#!/bin/bash

## Set your Environment variables.
joeAPI="Your API Key" # Joe API Key to allow you're web requests
joePOLL=15  # Joe Sandbox polling time in Minutes

sudo echo "export JOE_KEY='${joeAPI}'" | sudo tee -a /etc/environment
sudo echo "export JOE_POLL='${joePOLL}'" | sudo tee -a /etc/environment

sudo export JOE_KEY=${joeAPI}
sudo export JOE_POLL=${joePOLL}