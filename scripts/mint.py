from brownie_tokens import MintableForkToken
from scripts.helpers import *

import os


def mint(amount, amount2):
    ce, rp = accounts.at(os.getenv("CE_MM"), force=True), accounts.at(os.getenv("RP_HRDWLT")) 

    usdc = MintableForkToken('arb_usdc')
    
    usdc._mint_for_testing(ce, amount * 10 ** usdc.decimals())
    usdc._mint_for_testing(rp, amount2 * 10 ** usdc.decimals())

    gmx = MintableForkToken('arb_gmx')

    gmx._mint_for_testing(ce, amount * 10 ** gmx.decimals())
    gmx._mint_for_testing(rp, amount2 * 10 ** gmx.decimals())


def main():
    amount = 100_000 * 10**6
    amount2 = 1_000 * 10**18

    mint(amount, amount2)

