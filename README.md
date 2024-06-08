# safeurl_decoder
Python SDK for decoding safeurls from Barracuda, Cisco, Proofpoint, Microsoft, etc. and opening them in the default browser.

## Install
```
git clone https://github.com/purusoni/safeurl_decoder_and_opener.git
cd safeurl_decoder_and_opener/

python setup.py install
```

## CLI Usage
```
$ safeurl-decode
usage: safeurl-decode [-h] [--debug] [url]

Decode a SafeURL and open it in the default browser.

positional arguments:
  url         The SafeURL to decode and open.

optional arguments:
  -h, --help  show this help message and exit
  --debug     Print debugging information.
```

## Python 
```
from safeurl_decoder import SafeURL

r = SafeURL().decode('https://www.google.com')
print(r)

# https://www.google.com
```
