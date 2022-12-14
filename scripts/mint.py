from brownie_tokens import MintableForkToken
from scripts.helpers import *

import os


def mint(token, account, amount):
    token = MintableForkToken(token.address)

    token._mint_for_testing(account, amount)

    return token.balanceOf(account)


def main():
    usdc = Contract('arb_usdc')
    whale = accounts[0]
    amount = 1_000_000 * 10**usdc.decimals()

    amount_minted = mint(usdc, whale, amount)
    print(f"Minted {amount_minted / 10**usdc.decimals()} {usdc.name()} to {whale.address}")
