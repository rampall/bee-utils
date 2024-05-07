# Bee Utils

A simple python script to fund a [bee node](https://github.com/ethersphere/bee) with [xDAI](https://docs.gnosischain.com/about/tokens/xdai/) or [xBZZ](https://gnosisscan.io/token/0xdbf3ea6f5bee45c02255b2c26a16f300502f68da/) (a.k.a "BZZ on xDai") on Gnosis.

## Install

```
git clone https://github.com/rampall/bee-utils.git
cd bee-utils
pip install -r requirements.txt
```

## Setup

### Set Environment Variables

#### Funder wallet address to send funds from
```
export FROM=0x1234...
```

#### Private Key of Funder wallet address
```
export PK=0x9876...
```

#### Bee node address to receive funds
```
export TO=0x1020...
```

#### Gnosis RPC URL
```
export GNOSIS_RPC=http://...
```

## Usage

### To fund an address with xDAI

```
# Send 1 xDAI
python3 bee_utils.py send-xdai --amount 1 --from_address $FROM --to_address $TO --pk $PK --rpc $GNOSIS_RPC
```

### To fund an address with xBZZ

```
# Send 10 xBZZ
python3 bee_utils.py send-xbzz --amount 1 --from_address $FROM --to_address $TO --pk $PK --rpc $GNOSIS_RPC
```