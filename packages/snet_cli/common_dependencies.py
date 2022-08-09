from setuptools.command.develop import develop as _develop
from setuptools.command.install import install as _install


common_dependencies = [
    'eth-hash==0.3.3',
    'eth-utils==2.0.0',
    'eth-rlp==0.3.0',
    'grpcio-tools==1.19.0',
    'jsonrpcclient==2.5.2',
    'web3==4.8.3',
    'mnemonic==0.18',
    'pycoin==0.80',
    'rlp==1.0.1',
    'pyyaml==4.2b1',
    'ipfsapi==0.4.2.post1',
    'rfc3986==1.1.0',
    'pymultihash==0.8.2',
    'base58==1.0.2',
    'argcomplete==1.9.4',
    'grpcio-health-checking==1.19.0',
    'jsonschema==3.2.0'
]


def install_and_compile_proto():
    import snet.snet_cli
    from snet.snet_cli.utils.utils import compile_proto as compile_proto
    from pathlib import Path
    proto_dir = Path(__file__).absolute().parent.joinpath(
        "snet", "snet_cli", "resources", "proto")
    dest_dir = Path(snet.snet_cli.__file__).absolute(
    ).parent.joinpath("resources", "proto")
    print(proto_dir, "->", dest_dir)
    for fn in proto_dir.glob('*.proto'):
        print("Compiling protobuf", fn)
        compile_proto(proto_dir, dest_dir, proto_file=fn)


class develop(_develop):
    """Post-installation for development mode."""

    def run(self):
        _develop.run(self)
        self.execute(install_and_compile_proto, (),
                     msg="Compile protocol buffers")


class install(_install):
    """Post-installation for installation mode."""

    def run(self):
        _install.run(self)
        self.execute(install_and_compile_proto, (),
                     msg="Compile protocol buffers")
