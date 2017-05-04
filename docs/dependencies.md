#Requirements

### For Repo
* Put your broker certs in the brokercerts/ directory [Certificate Setup](./cert_setup.md)
* Put your client certificates in the certs/ directory [Certificate Setup](./cert_setup.md)
* Edit dxlclient.config and add your Broker(s)

### For Automated Environment
1. Download Vagrant https://www.vagrantup.com/downloads.html
2. Run installer for Vagrant
3. Download Virtualbox https://www.virtualbox.org/wiki/Downloads?replytocom=98578
4. Run installer for Virtualbox
3. Download Git https://git-scm.com/downloads

### Environment Variables
* Create a file named scripts/env.sh
* Make executable chmod +x scripts/env.sh
```
#!/bin/bash

joeAPI="Your API Key" # Joe API Key to allow you're web requests
joePOLL=15  # Joe Sandbox polling time in Minutes

sudo echo "export JOE_KEY='${joeAPI}'" | sudo tee -a /etc/environment
sudo echo "export JOE_POLL='${joePOLL}'" | sudo tee -a /etc/environment

```