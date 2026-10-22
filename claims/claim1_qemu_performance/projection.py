#!/usr/bin/env python3
"""Recompute the analytical eUICC dominant-cost projection (paper Section 7.2).

This is an operation-count model at a 33 MHz eUICC, not an on-card measurement.
The per-block AES figures already include data-bus transfer, engine start-up and
key scheduling. Run: python3 claims/claim1_qemu_performance/projection.py
"""
CLOCK_HZ = 33_000_000

ADD_OPS = 71_680
ADD_CYCLES = 1.0

CTR_BLOCKS = 512
CTR_CYCLES_PER_BLOCK = 77.3

CMAC_BLOCKS = 213
CMAC_CYCLES_PER_BLOCK = 124.0


def to_ms(cycles):
    return cycles / CLOCK_HZ * 1e3


def main():
    t_add = ADD_OPS * ADD_CYCLES
    t_ctr = CTR_BLOCKS * CTR_CYCLES_PER_BLOCK
    t_cmac = CMAC_BLOCKS * CMAC_CYCLES_PER_BLOCK
    total = t_add + t_ctr + t_cmac

    print("Analytical eUICC dominant-cost projection at %d MHz"
          % (CLOCK_HZ // 1_000_000))
    print("  ternary additions : %6d ops x %5.1f cyc = %9.0f cycles = %6.3f ms"
          % (ADD_OPS, ADD_CYCLES, t_add, to_ms(t_add)))
    print("  AES-CTR mask      : %6d blk x %5.1f cyc = %9.0f cycles = %6.3f ms"
          % (CTR_BLOCKS, CTR_CYCLES_PER_BLOCK, t_ctr, to_ms(t_ctr)))
    print("  AES-CMAC          : %6d blk x %5.1f cyc = %9.0f cycles = %6.3f ms"
          % (CMAC_BLOCKS, CMAC_CYCLES_PER_BLOCK, t_cmac, to_ms(t_cmac)))
    print("  total             :                       %9.0f cycles = %6.3f ms"
          % (total, to_ms(total)))


if __name__ == "__main__":
    main()
