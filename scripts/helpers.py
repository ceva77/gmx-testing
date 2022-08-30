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

def load_all():
    gmx = MintableForkToken('arb_gmx')
    usdc = MintableForkToken('arb_usdc')

    rewards_router = load_contract('arb_gmx_rewards_router')

    glp = load_contract(rewards_router.glp())
    fsglp = load_contract(rewards_router.stakedGlpTracker())
    sgmx = load_contract(rewards_router.stakedGmxTracker())
    esgmx = MintableForkToken(rewards_router.esGmx())

    glp_manager = load_contract(rewards_router.glpManager())
    glp_vester = load_contract(rewards_router.glpVester())
    gmx_vester = load_contract(rewards_router.gmxVester())

    ce = accounts.at(os.getenv("CE_MM"), force = True)
    rp = accounts.at(os.getenv("RP_HRDWLT"), force = True)

def mint_tokens():
    gmx._mint_for_testing(ce, 10_000 * 10**gmx.decimals())
    usdc._mint_for_testing(ce, 1_000_000 * 10**usdc.decimals())
    esgmx._mint_for_testing(ce, 10_000 * 10**esgmx.decimals())
