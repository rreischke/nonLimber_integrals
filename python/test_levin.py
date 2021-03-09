import levinpower

import numpy as np
import matplotlib.pyplot as plt
import time


if __name__ == "__main__":
    pk = np.load("./../data/pk.npz")
    kernels = np.load("./../data/kernels.npz")
    background = np.load("./../data/background.npz")

    k_pk = pk["k"]
    z_pk = pk["z"]
    power_spectrum = pk["pk_nl"].flatten()
    number_count = kernels["kernels_cl"].shape[0]
    backgound_z = background["z"]
    background_chi = background["chi"]
    chi_kernels = kernels["chi_cl"]
    kernels = np.concatenate(
        (kernels["kernels_cl"].T, kernels["kernels_sh"].T), axis=1)

    lp = levinpower.LevinPower(True, number_count,
                          backgound_z, background_chi,
                          chi_kernels, kernels,
                          k_pk, z_pk, power_spectrum)

    ell = np.arange(2, 4000, 1)
    t0 = time.time()
    Cl_gg, Cl_gs, Cl_ss = lp.compute_C_ells(ell)
    t1 = time.time()
    total = t1-t0
    print(total)
    plt.plot(ell, Cl_gg[0])
    lp.init_splines(backgound_z, background_chi,
                    chi_kernels, kernels, k_pk, z_pk, power_spectrum)
    Cl_gg, Cl_gs, Cl_ss = lp.compute_C_ells(ell)
    plt.plot(ell, Cl_gg[0], "--")
    plt.xscale('log')
    plt.yscale('log')
    plt.show()