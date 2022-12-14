import pytest
import os

from brownie import *
from brownie_tokens import MintableForkToken

from scripts.helpers import load_contract


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    pass

# wallets

@pytest.fixture(scope="module")
def ce():
    return accounts.at(os.getenv("CE_MM"), force=True) 


@pytest.fixture(scope="module")
def rp():
    return accounts.at(os.getenv("RP_HRDWLT"), force=True)


@pytest.fixture(scope="module")
def alice(accounts):
    return accounts[0]


@pytest.fixture(scope="module")
def bob(accounts):
    return accounts[1]


@pytest.fixture(scope="module")
def whale(accounts):
    return accounts[2]

@pytest.fixture(scope="module")
def rich_whale(whale, usdc, gmx, esgmx):
    usdc._mint_for_testing(whale, 1_000_000 * 10**usdc.decimals())
    gmx._mint_for_testing(whale, 1000 * 10**gmx.decimals())
    esgmx._mint_for_testing(whale, 1000 * 10**esgmx.decimals())

    return whale 

# coins

@pytest.fixture(scope="module")
def usdc():
    return MintableForkToken('arb_usdc')


@pytest.fixture(scope="module")
def gmx():
    return MintableForkToken('arb_gmx')


@pytest.fixture(scope="module")
def rewards_router():
    return load_contract('arb_gmx_rewards_router')


@pytest.fixture(scope="module")
def fsglp(rewards_router):
    return load_contract(rewards_router.stakedGlpTracker())


@pytest.fixture(scope="module")
def sgmx(rewards_router):
    return load_contract(rewards_router.stakedGmxTracker())


@pytest.fixture(scope="module")
def esgmx(rewards_router):
    return MintableForkToken(rewards_router.esGmx())


@pytest.fixture(scope="module")
def glp_manager(rewards_router):
    return load_contract(rewards_router.glpManager())


@pytest.fixture(scope="module")
def glp_vester(rewards_router):
    return load_contract(rewards_router.glpVester())


@pytest.fixture(scope="module")
def gmx_vester(rewards_router):
    return load_contract(rewards_router.gmxVester())






