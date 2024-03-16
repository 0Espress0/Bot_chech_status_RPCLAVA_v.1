from web3 import Web3
import time
# Create by Espresso "https://twitter.com/zicza10"
# Ethereum node RPC endpoint
rpc_endpoint = 'https://eth1.lava.build/lava-referer-xxxxxxxxxxxxxxxxxxxxx' #<< Change your LAVA RPC

# Ethereum wallet address to check balance
wallet_address = '0x0000000000000000000000000000000000000000' #<< Change your Wallet


# Connect to Ethereum node
web3 = Web3(Web3.HTTPProvider(rpc_endpoint))

def check_node_status():
    try:
        # Get syncing status
        syncing = web3.eth.syncing

        if syncing:
            print("Node is syncing...")
            print("Current block:", syncing['currentBlock'])
            print("Highest block:", syncing['highestBlock'])
        else:
            print("Node is up to date.")
    except Exception as e:
        print("Error while checking node status:", e)

def check_wallet_balance():
    try:
        balance_wei = web3.eth.get_balance(wallet_address)
        balance_eth = balance_wei / 10**18  # Convert Wei to Ether
        print("Wallet balance:", balance_eth, "ETH")
    except Exception as e:
        print("Error while checking wallet balance:", e)

while True:
    check_node_status()
    check_wallet_balance()
    # Sleep for 10 seconds before checking again
    time.sleep(10)
