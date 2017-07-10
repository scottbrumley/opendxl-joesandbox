#!/usr/bin/env bash

#set -e

## Set your Environment variables.
joeAPI="Your API Key" # Joe API Key to allow you're web requests
joePOLL=15  # Joe Sandbox polling time in Minutes

if [[ -d "/vagrant" ]]; then
    ROOT_DIR="/vagrant/"
else
    ROOT_DIR="$(pwd)/"
fi

installRequests(){
## Installs Requests for HTTP(S) requests
    sudo pip install requests
}

setEnvironment(){
## Sets Environment variables like keys and other sensitive or environmental data
    /vagrant/scripts/env.sh
}

runProgram(){
    sudo echo "JOE_POLL={joePOLL} JOE_KEY={joeAPI} /usr/bin/python /vagrant/joe-service.py" | sudo tee -a /etc/bash.bashrc
    sudo echo "Joe Sandbox Service is Running ..."
}

function installOpenDXLTIEClient {
    ### Install Open DXL TIE Client
    echo "Installing Open DXL TIE Client"
    cd /vagrant
    sudo git clone https://github.com/opendxl/opendxl-tie-client-python.git
    cd /vagrant/opendxl-tie-client-python
    sudo python setup.py install
}

setEnvironment
installOpenDXLTIEClient
installRequests
runProgram
