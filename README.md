# DSR Reader
This program finds an Ethereum account's DS-Proxy and then reads its DSR balance from the Pot contract.

## Prerequisite
- Git
- [Python v3.6.6](https://www.python.org/downloads/release/python-366/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
    - This project requires *virtualenv* to be installed if you want to use Maker's python tools. This helps with making sure that you are running the right version of python and checks that all of the pip packages that are installed in the **install.sh** are in the right place and have the right versions.
- [X-code](https://apps.apple.com/ca/app/xcode/id497799835?mt=12) (for Macs)

## Getting Started (Installation)

1. **Clone the `dsr-reader` repository and switch into its directory:**
```
git clone https://github.com/ith-harvey/dsr-reader.git
cd dsr-reader
```
2. **Initializing the git submodules that will bring in both the pymaker and the pyexchange library.**
```
git submodule update --init --recursive
```
3. **Check to make sure you have the correct version (Python 3.6.6) of Python by running:**
```
python3 -V
```
4. **To set up the virtual environment and install requirements, run the following script:**
```
./install.sh
```

## Start command
```
bin/dsr-interface [network] [Ethereum address]
```
