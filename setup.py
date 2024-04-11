# Submodule init to make models and key functionality available
from setuptools import setup
import os
os.path.dirname(os.path.abspath(__file__))

setup(
    name='hypercloud',
    packages=[
        'hypercloud',
        'hypercloud.models',
        'hypercloud.utils',
        'hypercloud.settings',
        'hypercloud.losses',
        'hypercloud.datasets'
    ],
    package_dir={
        'hypercloud': 'hypercloud',
        'hypercloud.models': 'hypercloud/models',
        'hypercloud.utils': 'hypercloud/utils',
        'hypercloud.settings': 'hypercloud/settings',
        'hypercloud.losses': 'hypercloud/losses',
        'hypercloud.datasets': 'hypercloud/datasets',
    },
    install_requires={
        'pyinn' @ 'git+https://github.com/mateuuszzzzz/pyinn/tree/cupy-fix@cupy-fix',
        'plyfile==0.8.1',
        'scikit-learn==0.22.1',
        'scipy==1.7.3',
        'torch==1.12.1',
        'pandas==0.25.3',
        'numpy==1.21.16',
        'matplotlib==3.1.12',
        'h5py==2.10.0',
    },
    description='Auxiliary package to make HyperCloud code accessible from Gaussian Mesh Splatting (GaMeS).',
)
