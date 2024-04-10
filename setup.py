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
    description='Auxiliary package to make HyperCloud code accessible from Gaussian Mesh Splatting (GaMeS).',
)
