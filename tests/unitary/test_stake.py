from brownie import *

from scripts.stake import stake_glp, stake_gmx, stake_esgmx
from scripts.mint import *


def test_stake_glp(rich_whale, usdc, fsglp, rewards_router):
    whale = rich_whale

    staked_amount = stake_glp(whale, usdc, usdc.balanceOf(whale), rewards_router)

    # check final balances
    assert usdc.balanceOf(whale) == 0
    assert fsglp.balanceOf(whale) > 0 
    assert staked_amount > 0


def test_stake_gmx(rich_whale, gmx, rewards_router, sgmx):
    whale = rich_whale

    staked_amount = stake_gmx(whale, gmx.balanceOf(whale), rewards_router, gmx)

    # check final balances
    assert gmx.balanceOf(whale) == 0
    assert sgmx.stakedAmounts(whale) == staked_amount 


def test_stake_esgmx(rich_whale, esgmx, rewards_router, sgmx):
    whale = rich_whale

    staked_amount = stake_esgmx(whale, esgmx.balanceOf(whale), rewards_router, esgmx)

    # check final balances
    assert esgmx.balanceOf(whale) == 0
    assert sgmx.stakedAmounts(whale) == staked_amount 

    
