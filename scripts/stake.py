from brownie import * 

from scripts.mint import mint
from scripts.helpers import load_contract


def stake_glp(account, token, amount_in, rewards_router):
    # approve token transfer and stake for glp
    token.approve(rewards_router.glpManager(), amount_in, {'from': account})
    rewards_router.mintAndStakeGlp(token, amount_in, 0, 0, {'from': account})

    fsglp = Contract(rewards_router.stakedGlpTracker())
    return fsglp.balanceOf(account) 


def stake_gmx(account, amount_in, rewards_router, gmx):
    # approve token transfer and stake
    staked_gmx_tracker = Contract(rewards_router.stakedGmxTracker())
    gmx.approve(staked_gmx_tracker, amount_in, {'from': account})
    rewards_router.stakeGmx(amount_in, {'from': account})

    return staked_gmx_tracker.stakedAmounts(account)


def stake_esgmx(account, amount_in, rewards_router, esgmx):
    # stake 
    rewards_router.stakeEsGmx(amount_in, {'from': account})

    staked_gmx_tracker = Contract(rewards_router.stakedGmxTracker())

    return staked_gmx_tracker.stakedAmounts(account)


def main():
    # globals
    print("Loading global variables")
    whale = accounts[0]
    rewards_router = load_contract('arb_gmx_rewards_router')
    staked_gmx_tracker = Contract(rewards_router.stakedGmxTracker())

    usdc = Contract('arb_usdc')
    usd_amount = 1_000_000 * 10**usdc.decimals()

    gmx = Contract('arb_gmx')
    gmx_amount = 1_000 * 10**gmx.decimals()

    esgmx = Contract(rewards_router.esGmx())
    esgmx_amount = 1_000 * 10**esgmx.decimals()

    # start staking
    print("Minting and staking GLP...")
    chain.snapshot() # stake glp
    _ = mint(usdc, whale, usd_amount)
    staked_amount = stake_glp(whale, usdc, usd_amount, rewards_router)
    print(f"{whale} paid ${usd_amount / 10**usdc.decimals():,.2f} to stake {staked_amount / 10**18:,.3f} GLP")
    print()
    chain.revert() 

    print("Staking GMX...")
    chain.snapshot() # stake gmx 
    _ = mint(gmx, whale, gmx_amount)
    staked_amount = stake_gmx(whale, gmx_amount, rewards_router, gmx)
    print(f"{whale} staked {gmx_amount / 10**gmx.decimals():,.2f} GMX") 
    print()
    chain.revert()

    print("Staking esGMX...")
    chain.snapshot() # stake esGmx 
    _ = mint(esgmx, whale, esgmx_amount)
    staked_amount = stake_esgmx(whale, esgmx_amount, rewards_router, esgmx)
    print(f"{whale} staked {esgmx_amount / 10**esgmx.decimals():,.2f} esGMX") 

