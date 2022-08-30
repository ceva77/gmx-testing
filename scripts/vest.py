from brownie import *


def stake_glp():
    whale = accounts[0]
    usdc = Contract('arb_usdc')
    rewards_router = Contract('arb_gmx_rewards_router')

    # mint, approve, and mint and stake
    usdc._mint_for_testing(whale, 100_000 * 10**usdc.decimals())
    usdc.approve(rewards_router.glpManager(), 100_000 * 10**usdc.decimals(), {'from': whale})
    rewards_router.mintAndStakeGlp(usdc, usdc.balanceOf(whale), 0, 0, {'from': whale})


def main():
    stake_glp()
