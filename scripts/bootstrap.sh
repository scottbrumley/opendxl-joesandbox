#!/usr/bin/env bash

#set -e

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
