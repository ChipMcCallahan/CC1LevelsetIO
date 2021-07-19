from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='CC1LevelsetIO',
    url='https://github.com/ChipMcCallahan/CC1LevelsetIO',
    author='Chip McCallahan',
    author_email='thisischipmccallahan@gmail.com',
    # Needed to actually package something
    packages=['cc1_levelset_io'],
    # Needed for dependencies
    install_requires=['cc1_levelset_proto @ git+https://github.com/ChipMcCallahan/CC1LevelsetProto.git'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='GNU General Public License v3.0',
    description='File I/O for CC1 DAT and CCX files. Converts to and from CC1LevelsetProto format.',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
