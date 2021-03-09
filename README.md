# Calculating the non-Limber expression for the angular power spectrum using the Levin integration. 

The non-Limber integral which is computed for each element of the angular power spectrum is, for clustering:
<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{200}&space;C_\ell&space;=&space;\frac{2}{\pi}&space;\int_0^\infty&space;d\chi_1&space;K(\chi_1)&space;\int_0^\infty&space;d\chi_2&space;K(\chi_2)&space;\int_0^\infty&space;dk&space;\,&space;k^2&space;P_\delta(k,z_1,z_2)j_\ell(k&space;\chi_1)j_\ell(k&space;\chi_2)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{200}&space;C_\ell&space;=&space;\frac{2}{\pi}&space;\int_0^\infty&space;d\chi_1&space;K(\chi_1)&space;\int_0^\infty&space;d\chi_2&space;K(\chi_2)&space;\int_0^\infty&space;dk&space;\,&space;k^2&space;P_\delta(k,z_1,z_2)j_\ell(k&space;\chi_1)j_\ell(k&space;\chi_2)" title="" /></a>

for cosmic shear:
<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{200}&space;C_\ell&space;=&space;\frac{2}{\pi}&space;\frac{(\ell&space;&plus;2)!}{(\ell-2)!}&space;\int_0^\infty&space;d\chi_1&space;K(\chi_1)&space;\int_0^\infty&space;d\chi_2&space;K(\chi_2)&space;\int_0^\infty&space;dk&space;\,&space;k^2&space;P_\delta(k,z_1,z_2)\frac{j_\ell(k&space;\chi_1)}{(k\chi_1)^2}\frac{j_\ell(k&space;\chi_2)}{(k&space;\chi_2)^2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{200}&space;C_\ell&space;=&space;\frac{2}{\pi}&space;\frac{(\ell&space;&plus;2)!}{(\ell-2)!}&space;\int_0^\infty&space;d\chi_1&space;K(\chi_1)&space;\int_0^\infty&space;d\chi_2&space;K(\chi_2)&space;\int_0^\infty&space;dk&space;\,&space;k^2&space;P_\delta(k,z_1,z_2)\frac{j_\ell(k&space;\chi_1)}{(k\chi_1)^2}\frac{j_\ell(k&space;\chi_2)}{(k&space;\chi_2)^2}" title="{}" /></a>

and for galaxy-galaxy lensing (assuming quantities labeled with '1' are associated with shear and '2' with number counts):
<a href="https://www.codecogs.com/eqnedit.php?latex=\dpi{200}&space;C_\ell&space;=&space;\frac{2}{\pi}&space;\sqrt{\frac{(\ell&space;&plus;2)!}{(\ell-2)!}}&space;\int_0^\infty&space;d\chi_1&space;K(\chi_1)&space;\int_0^\infty&space;d\chi_2&space;K(\chi_2)&space;\int_0^\infty&space;dk&space;\,&space;k^2&space;P_\delta(k,z_1,z_2)\frac{j_\ell(k&space;\chi_1)}{(k\chi_1)^2}j_\ell(k&space;\chi_2)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\dpi{200}&space;C_\ell&space;=&space;\frac{2}{\pi}&space;\sqrt{\frac{(\ell&space;&plus;2)!}{(\ell-2)!}}&space;\int_0^\infty&space;d\chi_1&space;K(\chi_1)&space;\int_0^\infty&space;d\chi_2&space;K(\chi_2)&space;\int_0^\infty&space;dk&space;\,&space;k^2&space;P_\delta(k,z_1,z_2)\frac{j_\ell(k&space;\chi_1)}{(k\chi_1)^2}j_\ell(k&space;\chi_2)" title="" /></a>

where K is in each case the kernel for the appropriate tracer and <img src="https://render.githubusercontent.com/render/math?math=P_\delta"> is the non-linear matter power spectrum. We assume that <img src="https://render.githubusercontent.com/render/math?math=P_\delta(k,z_1,z_2) = \sqrt{P_\delta(k,z_1)P_\delta(k,z_2)}">.


## Compiling
The code is compiled by typing make install. In the main directory there is another makefile for an example main. The documentation can be created via doxygen -g doxyfile followed by doxygen doxyfile .
Only standard libraries and the GSL are needed.

For the python module, `pip install .` (or `pip install -e .` for a `develop` install) should do the trick. An up-to-date version of `pip` (10+) is required. You might have to install pybind11, but this should work automatically.

##  Running the code
There exists a python test file showing which things one should pass to the constructor of the class. In principle the class needs to be initialized once. This is especially true if the Bessel functions are precomputed since this would generate unnecessary overhead. If you want to update the spectra, the weights or anything, you should just call the init_splines method to set up the new splines without touching the Bessel functions.

The arguments in the constructor are:
* precompute: if set True, Besselfunctions are precomputed, speeds up the calculation.
* number_count: the first `<number_count>` entries are treated as the galaxy clustering, while the remaining are treated as cosmic shear. 

