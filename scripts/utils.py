from brownie_tokens import MintableForkToken
from brownie import *

import os

from scripts.helpers import load_contract


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
