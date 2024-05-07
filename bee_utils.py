import click
import json
from web3 import Web3

with open("./abi.json") as f:
    info_json = json.load(f)
bzz_abi = info_json["bzz"]

@click.group()
def cli():
    pass

@cli.command()
@click.option('--rpc', prompt='Gnosis RPC URL', help='Gnosis RPC URL')
@click.option('--from_address', prompt='From address', help='Sender account address')
@click.option('--pk', prompt='Private key', help='Sender account private key')
@click.option('--to_address', prompt='To address', help='Recipient account address')  
@click.option('--amount', prompt='Amount', type=float, help='Amount of xDAI to send')
def send_xdai(rpc, from_address, pk, to_address, amount):
    w3 = Web3(Web3.HTTPProvider(rpc))
    nonce =  w3.eth.get_transaction_count(from_address)
    # Build transaction
    tx = {
        'nonce': nonce,
        'to': to_address,
        'value': w3.to_wei(amount, 'ether'),
        'type': 2,
        'gas': 200000,
        'maxFeePerGas': 2000000000,
        'maxPriorityFeePerGas': 1000000000,
        'chainId': 100
    }
    
    # Sign transaction
    signed_tx = w3.eth.account.sign_transaction(tx, pk)
    
    # Send transaction
    print(f'Signed TX.\nSending {amount} xDAI from {from_address} to {to_address}...')
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print("Transaction Hash:", w3.to_hex(tx_hash))

@cli.command()
@click.option('--rpc', prompt='Gnosis RPC URL', help='Gnosis RPC URL')
@click.option('--from_address', prompt='From address', help='Sender account address')
@click.option('--pk', prompt='Private key', help='Sender account private key')
@click.option('--to_address', prompt='To address', help='Recipient account address')
@click.option('--amount', prompt='Amount', type=int, help='Amount of BZZ to send')
def send_xbzz(rpc, from_address, pk, to_address, amount):
    w3 = Web3(Web3.HTTPProvider(rpc))
    value = amount * 10000000000000000
    print(rpc, from_address, pk, to_address, amount, f"{value}")
    bzz_address = '0xdBF3Ea6F5beE45c02255B2c26a16F300502F68da' # BZZ token contract address
    bzz_contract = w3.eth.contract(address=bzz_address, abi=bzz_abi)

    # Build the transaction
    nonce =  w3.eth.get_transaction_count(from_address)
    tx = bzz_contract.functions.transfer(to_address, value).build_transaction({
        'from': from_address,
        'nonce': nonce,
        'type': 2,
        'gas': 200000,
        'maxFeePerGas': 2000000000,
        'maxPriorityFeePerGas': 1000000000,
        'chainId': 100
    })

    # Sign transaction
    signed_tx = w3.eth.account.sign_transaction(tx, pk)
    
    # Send transaction
    print(f'Sending {amount} xBZZ ({value} wei) from {from_address} to {to_address}...')
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print("Transaction Hash:", w3.to_hex(tx_hash))

if __name__ == '__main__':
    cli()
