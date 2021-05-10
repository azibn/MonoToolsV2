from setuptools import setup
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

extrafiles =['data/tables/GKSPCPapTable1_Final.txt',
             'data/tables/BolMag_interpolations.models',
             'data/tables/Cheops_Quad_LDs.txt',
             'data/tables/KeplerLDlaws.txt',
             'data/tables/tess_lc_locations.csv',
             'data/tables/GKSPCPapTable2_Final.txt',
             'data/tables/logprob_array_kip.txt',
             'data/tables/logprob_array_flat.txt',
             'data/tables/logprob_array_apo.txt',
             'data/tables/emarg_array_flat.txt',
             'data/tables/tessLDs.txt',
             'data/tables/emarg_array_vve.txt',
             'data/tables/emarg_array_kip.txt',
             'data/tables/interpolated_functions_for_vcirc.pkl',
             'data/tables/tces_per_cadence.txt',
             'data/tables/emarg_array_apo.txt',
             'data/tables/logprob_array_vve.txt',
             'data/tables/LogMePriorFromRe.txt',
             'data/tables/Cheops_Quad_LDs_AllFeHs.txt',
             'tests/test_fit.py',
             'stellar/Densities_as_found_by_starpars.csv',
             'stellar/__init__.py',
             'stellar/LAMOST_5_res_all.numbers',
             'stellar/apjaa8b0ft3_mrt.txt',
             'stellar/cks_gaia_bright_xmatch.txt',
             'stellar/KepASstars.txt',
             'stellar/BolMag',
             'stellar/isoclassify/LICENSE',
             'stellar/isoclassify/requirements.txt',
             'stellar/isoclassify/__init__.py',
             'stellar/isoclassify/README.md',
             'stellar/isoclassify/huber17scripts/tgas_combined_obs.txt',
             'stellar/isoclassify/huber17scripts/ini',
             'stellar/isoclassify/huber17scripts/apokasc_direct.py',
             'stellar/isoclassify/huber17scripts/apokasc_grid.py',
             'stellar/isoclassify/bin/isoclassify',
             'stellar/isoclassify/isoclassify/__init__.py',
             'stellar/isoclassify/isoclassify/pipeline.py',
             'stellar/isoclassify/isoclassify/direct/getmesabc.py',
             'stellar/isoclassify/isoclassify/direct/classify.py',
             'stellar/isoclassify/isoclassify/direct/__init__.py',
             'stellar/isoclassify/isoclassify/direct/asfgrid.py',
             'stellar/isoclassify/isoclassify/grid/temp',
             'stellar/isoclassify/isoclassify/grid/plot.py',
             'stellar/isoclassify/isoclassify/grid/classify.py',
             'stellar/isoclassify/isoclassify/grid/__init__.py',
             'stellar/isoclassify/isoclassify/grid/example-bc.ipynb',
             'stellar/isoclassify/isoclassify/grid/pdf.py',
             'stellar/isoclassify/isoclassify/grid/priors.py',
             'stellar/isoclassify/isoclassify/grid/match.py',
             'stellar/isoclassify/examples/example.csv',
             'stellar/isoclassify/examples/grid.ipynb',
             'stellar/isoclassify/examples/direct.ipynb']

setuptools.setup(
    name='MonoTools',
    version='0.1.3',
    description='A package for detecting, vetting and modelling transiting exoplanets on uncertain periods',
    url='https://github.com/hposborn/MonoTools',
    author='Hugh P. Osborn',
    author_email='hugh.osborn@space.unibe.ch',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='BSD 2-clause',
    project_urls={
        "Bug Tracker": "https://github.com/hposborn/MonoTools/issues",
    },
    packages=setuptools.find_packages(),
    package_data={'MonoTools': extrafiles},
    install_requires=['matplotlib',
                      'numpy',
                      'pandas',
                      'scipy',
                      'astropy',
                      'astroquery',
                      'batman-package==2.4.7',
                      'lightkurve==1.11.0',
                      'arviz==0.11',
                      'Theano==1.0.4',
                      'pymc3==3.8',
                      'exoplanet==0.3.2',
                      'celerite',
                      'requests',
                      'urllib3',
                      'lxml',
                      'httplib2',
                      'h5py',
                      'ipython',
                      'bokeh',
                      'corner',
                      'transitleastsquares',
                      'eleanor',
                      'seaborn',
                      'iteround',
                      ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
    ],
)
