import levinpower

import numpy as np
import matplotlib.pyplot as plt
import time


if __name__ == "__main__":
    '''
    pk = np.load("./../data/pk.npz")
    kernels = np.load("./../data/kernels.npz")
    background = np.load("./../data/background.npz")


# Prepare example input, this can be any corresponding lists and arrays from your code.
    k_pk = pk["k"]
    z_pk = pk["z"]
    power_spectrum = pk["pk_nl"].flatten()
    number_count = kernels["kernels_cl"].shape[0]
    backgound_z = background["z"]
    background_chi = background["chi"]
    chi_kernels = kernels["chi_cl"]
    kernels = np.concatenate(
        (kernels["kernels_cl"].T, kernels["kernels_sh"].T), axis=1)

# Setup the class with precomputed bessel functions (take a few moments)
    print(kernels.shape,power_spectrum.shape)
    lp = levinpower.LevinPower(True, number_count,
                          backgound_z, background_chi,
                          chi_kernels, kernels,
                          k_pk, z_pk, power_spectrum)

    ell = np.arange(2, 4000, 1)
    t0 = time.time()
    # actually calculate the Cls, returns a list for galaxy clustering, ggl and cosmic shear
    # Each one is again a list of n_tomo_tracer_A (n_tomo_tracer_B+1)/2 entries with the length
    # len(ell). The (0,0) bin corresponds to 0 and the (0,2) bin to 2 etc.
    Cl_gg, Cl_gs, Cl_ss = lp.compute_C_ells(ell)
    t1 = time.time()
    total = t1-t0
    print(total)
 
 
    plt.plot(ell, Cl_gg[0])
    # updating the kernls, spectrum, background (is the same here, but could change)
    lp.init_splines(backgound_z, background_chi,
                    chi_kernels, kernels, k_pk, z_pk, power_spectrum)
    Cl_gg, Cl_gs, Cl_ss = lp.compute_C_ells(ell)
    plt.plot(ell, Cl_gg[0], "--")
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
    '''
    

    number_count = 10
    number_count_sh = 5
    nz = 150
    zmin = 0
    zmax = 4
    kmax = 10
    kmin = 1e-4
    nk_per_decade = 20
    background_z = z_pk = np.linspace(zmin, zmax, nz)
    z_pk = background_z
    #cosmo = ccl.Cosmology(Omega_c=0.305, Omega_b=0.0466,
    #          h=0.695, n_s=0.901, sigma8=0.76,
    #          transfer_function=‘bbks’) # simple cosmology for quick chi-range computation
    h = 0.7
    h3 = 0.7**3
    sf = 1. / (1. + background_z)
    background_chi = chi_kernels = z_pk
    kernels = np.ones([len(background_chi), number_count+number_count_sh])
    dlk = np.log10(kmax) - np.log10(kmin)
    k_pk = np.logspace(np.log10(kmin), np.log10(kmax), int(dlk * nk_per_decade))
    k_pk *= h
    power_spectrum = np.array([k_pk for sfi in sf]).flatten() # uncomment if things look crazy with P(k) of ones -- prob not too slow
    print(kernels.shape,power_spectrum.shape)
    #power_spectrum = np.ones([len(background_z), len(k_pk)]).flatten()
    #print(‘Running non-Limber Bessel function pre-computation (will take some time | %s threads)’%os.environ[‘OMP_NUM_THREADS’])
    lp = levinpower.LevinPower(True, number_count,
           background_z, background_chi,
           chi_kernels, kernels,
           k_pk, z_pk, power_spectrum)
    import pdb; pdb.set_trace()