from brownie_tokens import MintableForkToken
from brownie import *

from scripts.mint import mint


def test_mint(ce, rp, alice, bob):
    usdc = MintableForkToken('arb_usdc')
    gmx = MintableForkToken('arb_gmx')

    assert usdc.balanceOf(ce) == 0
    assert usdc.balanceOf(rp) == 0
    
    assert gmx.balanceOf(ce) == 0
    assert gmx.balanceOf(rp) == 0
    
    # mint
    amount = 100_000
    amount2 = 50_000
    usdc._mint_for_testing(ce, amount * 10**usdc.decimals())
    usdc._mint_for_testing(rp, amount2 * 10**usdc.decimals())

    gmx._mint_for_testing(ce, amount * 10**gmx.decimals())
    gmx._mint_for_testing(rp, amount2 * 10**gmx.decimals())
    
    assert usdc.balanceOf(ce) == amount * 10 ** usdc.decimals() 
    assert usdc.balanceOf(rp) == amount2 * 10 ** usdc.decimals() 
    
    assert gmx.balanceOf(ce) == amount * 10 ** gmx.decimals() 
    assert gmx.balanceOf(rp) == amount2 * 10 ** gmx.decimals() 
