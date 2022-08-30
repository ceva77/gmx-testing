from brownie import *


def test_stake_glp(whale, usdc, fsglp, rewards_router):
    # check initial balances
    assert usdc.balanceOf(whale) == 0
    assert fsglp.balanceOf(whale) == 0

    # mint, approve, and mint and stake
    usdc._mint_for_testing(whale, 100_000 * 10**usdc.decimals())
    usdc.approve(rewards_router.glpManager(), 100_000 * 10**usdc.decimals(), {'from': whale})
    rewards_router.mintAndStakeGlp(usdc, usdc.balanceOf(whale), 0, 0, {'from': whale})
    
    # check final balances
    assert usdc.balanceOf(whale) == 0
    assert fsglp.balanceOf(whale) > 0


def test_stake_gmx(whale, gmx, rewards_router, sgmx):
    # mint gmx
    amount = 1_000 * 10**gmx.decimals()
    gmx._mint_for_testing(whale, amount)

    # check initial balances
    assert sgmx.balanceOf(whale) == 0
    assert gmx.balanceOf(whale) == amount

    # approve and stake
    gmx.approve(sgmx, amount, {'from': whale})
    rewards_router.stakeGmx(amount, {'from': whale})

    # check final balances
    assert gmx.balanceOf(whale) == 0
    assert sgmx.stakedAmounts(whale) == amount 


def test_stake_esgmx(whale, esgmx, rewards_router, sgmx):
    # mint esGMX
    amount = 1_000 * 10**esgmx.decimals()
    esgmx._mint_for_testing(whale, amount)

    # check initial balances
    assert sgmx.balanceOf(whale) == 0
    assert esgmx.balanceOf(whale) == amount

    # approve and stake
    esgmx.approve(sgmx, amount, {'from': whale})
    rewards_router.stakeEsGmx(amount, {'from': whale})

    # check final balances
    assert esgmx.balanceOf(whale) == 0
    assert sgmx.stakedAmounts(whale) == amount 

    
