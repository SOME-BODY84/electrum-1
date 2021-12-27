# -*- coding: utf-8 -*-
#
#
# Electrum - lightweight Bitcoin client
# Electrum - lightweight Bitcoin client
# Copyright (C) 2018 The Electrum developers
# Copyright (C) 2018 The Electrum developers
#
#
# Permission is hereby granted, free of charge, to any person
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# subject to the following conditions:
#
#
# The above copyright notice and this permission notice shall be
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# included in all copies or substantial portions of the Software.
#
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# SOFTWARE.
from .networks import *
from .networks import *
GIT_REPO_URL = "https://github.com/spesmilo/electrum"
GIT_REPO_URL = "https://github.com/spesmilo/electrum"
GIT_REPO_ISSUES_URL = "https://github.com/spesmilo/electrum/issues"
GIT_REPO_ISSUES_URL = "https://github.com/spesmilo/electrum/issues"
networks = {
networks = {
    'Bitcoin': BitcoinMainnet,
    'Bitcoin': BitcoinMainnet,
    'Bitcoin-Mainnet': BitcoinMainnet,
    'Bitcoin-Mainnet': BitcoinMainnet,
    'Bitcoin-Testnet': BitcoinTestnet,
    'Bitcoin-Testnet': BitcoinTestnet,
    'Bitcoin-Regtest': BitcoinRegtest,
    'Bitcoin-Regtest': BitcoinRegtest,
    'Bitcoin-Simnet': BitcoinSimnet,
    'Bitcoin-Simnet': BitcoinSimnet,
    'Crowncoin': CrowncoinMainnet,
    'Crowncoin-Mainnet': CrowncoinMainnet,
    'Namecoin': NamecoinMainnet,
    'Namecoin-Mainnet': NamecoinMainnet,
}
}


net = networks['Bitcoin']
net = networks['Bitcoin']
def select_network(network='Bitcoin'):
def select_network(network='Bitcoin'):
    if not network in networks:
    if not network in networks:
        raise Exception('Invalid Network. Available: {}'.format(
        raise Exception('Invalid Network. Available: {}'.format(
            list(networks.keys())))
            list(networks.keys())))
    global net
    global net
    net = networks.get(network, 'Bitcoin')
    net = networks.get(network, 'Bitcoin')
    return
return
