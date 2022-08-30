from brownie import * 
from brownie_tokens import MintableForkToken

import os


def load_contract(addr):
    if addr == ZERO_ADDRESS:
        return None
    try:
        cont = Contract(addr)
    except ValueError:
        cont = Contract.from_explorer(addr)
    return cont


def mint_tokens():
    gmx._mint_for_testing(ce, 10_000 * 10**gmx.decimals())
    usdc._mint_for_testing(ce, 1_000_000 * 10**usdc.decimals())
    esgmx._mint_for_testing(ce, 10_000 * 10**esgmx.decimals())
