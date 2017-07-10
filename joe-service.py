####
#
# JOE SANDBOX McAfee TIE integration
#

# DO NOT CHANGE
server = "https://jbxcloud.joesecurity.org/index.php/api/"

## Joe Reputation to McAfee Reputation
joeMcAfee= {"-1":"unkown","0":"not_set","1":"most_likely_malicious","2":"known_malicious"}

# Timeout for the HTTP request, in seconds
timeout = 6

# ------------------------------

import os
import sys
import time
import traceback
import logging
from dxlclient.client import DxlClient
from dxlclient.client_config import DxlClientConfig
#from dxlclient.message import Message, Request

from dxltieclient import TieClient
from dxltieclient.constants import HashType, TrustLevel, FileProvider, ReputationProp, CertProvider, CertReputationProp, CertReputationOverriddenProp

# Import common logging and configuration
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

# Enable logging, this will also direct built-in DXL log messages.
# See - https://docs.python.org/2/howto/logging-cookbook.html
log_formatter = logging.Formatter('%(asctime)s %(name)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)

logger = logging.getLogger()
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)

## DXL Client Configuration
CONFIG_FILE_NAME = "/vagrant/dxlclient.config"

# Create DXL configuration from file
config = DxlClientConfig.create_dxl_config_from_file(CONFIG_FILE_NAME)
CONFIG_FILE = os.path.dirname(os.path.abspath(__file__)) + "/" + CONFIG_FILE_NAME

## Check if it is a SHA1
def is_sha1(maybe_sha):
    if len(maybe_sha) != 40:
        return False
    try:
        sha_int = int(maybe_sha, 16)
    except ValueError:
        return False
    return True

## Check if it is a SHA256
def is_sha256(maybe_sha):
    if len(maybe_sha) != 64:
        return False
    try:
        sha_int = int(maybe_sha, 16)
    except ValueError:
        return False
    return True

## Check if it is an MD5
def is_md5(maybe_md5):
    if len(maybe_md5) != 32:
        return False
    try:
        md5_int = int(maybe_md5, 16)
    except ValueError:
        return False
    return True

## Map McAfee Trust Level from trustlevel string provided
def getTrustLevel(trustlevelStr):
    trustlevelStr = trustlevelStr.lower()
    if trustlevelStr == 'known_trusted':
        return TrustLevel.KNOWN_TRUSTED
    elif trustlevelStr == 'known_trusted_install':
        return TrustLevel.KNOWN_TRUSTED_INSTALLER
    elif trustlevelStr == 'most_likely_trusted':
        return TrustLevel.MOST_LIKELY_TRUSTED
    elif trustlevelStr == 'might_be_trusted':
        return TrustLevel.MIGHT_BE_TRUSTED
    elif trustlevelStr == 'unknown':
        return TrustLevel.UNKNOWN
    elif trustlevelStr == 'might_be_malicious':
        return TrustLevel.MIGHT_BE_MALICIOUS
    elif trustlevelStr == 'most_likely_malicious':
        return TrustLevel.MOST_LIKELY_MALICIOUS
    elif trustlevelStr == 'known_malicious':
        return TrustLevel.KNOWN_MALICIOUS
    elif trustlevelStr == 'not_set':
        return TrustLevel.NOT_SET
    return -1

## Set the TIE reputation of a file via MD5, SHA1, or SHA256 hash
def setReputation(trustlevelStr, md5, sha1, sha256, filenameStr, commentStr):
    trustlevelInt = getTrustLevel(trustlevelStr)

    if md5 == None and sha1 == None and sha256 == None:
        print "no file hash"
    else:
        ### Verify SHA1 string
        if sha1 != "":
            if not is_sha1(sha1):
               print "invalid sha1"

        ### Verify SHA256 string
        if sha256 != "":
            if not is_sha1(sha1):
                print "invalid sha256"

        if md5 != "":
            if not is_md5(md5):
                print "invalid md5"

    # Create the client
    with DxlClient(config) as client:

        # Connect to the fabric
        client.connect()

        # Create the McAfee Threat Intelligence Exchange (TIE) client
        tie_client = TieClient(client)

        if trustlevelInt != -1:
            # Set the Enterprise reputation for notepad.exe to Known Trusted
            tie_client.set_file_reputation(
                trustlevelInt , {
                    HashType.MD5: md5,
                    HashType.SHA1: sha1,
                    HashType.SHA256: sha256
                },
                filename=filenameStr,
                comment=commentStr)
        else:
            print "invalid trust level",
            trustlevel = trustlevelStr

def convertInterval(pollMins):
    print "Polling set to " + str(pollMins) + " Minutes"

    if pollMins != None:
        pollMins = float(pollMins)
        return pollMins * 60
    else:
        return 0.0

# Get Environment Variables
apiKey = os.environ.get('JOE_KEY')
pollInterval = convertInterval(os.environ.get('JOE_POLL'))  ## Get Joe Polling Interval and convert to floating seconds

if pollInterval == 0:
    print "Polling Interval Needs to be set in environment variable JOE_POLL"
    exit(0)

try:
    import requests
    from requests.exceptions import ConnectionError
except ImportError:
    print "Error: Please install the Python 'requests' package via pip"
    sys.exit()

def getJoeList():
    analysisUrl = server +'analysis/list'
    #deleteUrl = server +'analysis/delete'

    params = {"apikey" : apiKey}

    # Fetch analysis metadata
    try:
        result = requests.post(analysisUrl, data = params, timeout = timeout)
        content = result.json()[0]
        trustlevelStr = "no_set"
        filenameStr = ""
        md5 = ""
        sha1 = ""
        sha256 = ""

        for key, value in content.iteritems():

            ## Comment about Joe
            commentStr = "Reputations Score from Joe Sandbox"

            ## Get filename
            if key == "filename":
                filenameStr = value

            ## Get md5
            if key == "md5":
                md5 = value

            ## Get SHA1
            if key == "sha1":
                sha1 = value

            ## Get SHA256
            if key == "sha256":
                sha256 = value

            ## Get Results of Scan
            if key == "detections":
                detectionsList = value.split(';')
                trustlevelStr = joeMcAfee[detectionsList[-2]] ## Retrieve last value in list
                setReputation(trustlevelStr, md5, sha1, sha256, filenameStr, commentStr)
            print key, " : ", value

        #print content['webid']
    except ValueError,e:
        print "API fault: " + result.text
        sys.exit()
    except:
        print "Unable to fetch analyses: " + traceback.format_exc()
        sys.exit()

def main():
    print ""
    print "--- Joe Sandbox metadata script ---"
    print ""

    while True:
        getJoeList()
        time.sleep(pollInterval)

if __name__=="__main__":
    main()
