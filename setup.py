from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    scripts=['src/inference_test/nodes/inference.py'             
             ],
    packages=['inference_test'],
    package_dir={'': 'src'},
    requires= ['rospy']
)

setup(**setup_args)