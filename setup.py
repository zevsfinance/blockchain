from setuptools import setup

dependencies = [
    "blspy==1.0.2",  # Signature library
    "Zevsvdf==1.0.2",  # timelord and vdf verification
    "Zevsbip158==1.0",  # bip158-style wallet filters
    "Zevspos==1.0.3",  # proof of space
    "clvm==0.9.6",
    "clvm_rs==0.1.7",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.7",  # Binary data management library
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the Zevs processes readable names
    "sortedcontainers==2.3.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspython==2.1.0",  # Query DNS seeds
]

upnp_dependencies = [
    "miniupnpc==2.1",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
]

kwargs = dict(
    name="Zevs-blockchain",
    author="Mariano Sorgente",
    author_email="mariano@Zevs.net",
    description="Zevs blockchain full node, farmer, timelord, and wallet.",
    url="https://Zevs.net/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="Zevs blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "Zevs",
        "Zevs.cmds",
        "Zevs.consensus",
        "Zevs.daemon",
        "Zevs.full_node",
        "Zevs.timelord",
        "Zevs.farmer",
        "Zevs.harvester",
        "Zevs.introducer",
        "Zevs.plotting",
        "Zevs.protocols",
        "Zevs.rpc",
        "Zevs.server",
        "Zevs.simulator",
        "Zevs.types.blockchain_format",
        "Zevs.types",
        "Zevs.util",
        "Zevs.wallet",
        "Zevs.wallet.puzzles",
        "Zevs.wallet.rl_wallet",
        "Zevs.wallet.cc_wallet",
        "Zevs.wallet.did_wallet",
        "Zevs.wallet.settings",
        "Zevs.wallet.trading",
        "Zevs.wallet.util",
        "Zevs.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "Zevs = Zevs.cmds.Zevs:main",
            "Zevs_wallet = Zevs.server.start_wallet:main",
            "Zevs_full_node = Zevs.server.start_full_node:main",
            "Zevs_harvester = Zevs.server.start_harvester:main",
            "Zevs_farmer = Zevs.server.start_farmer:main",
            "Zevs_introducer = Zevs.server.start_introducer:main",
            "Zevs_timelord = Zevs.server.start_timelord:main",
            "Zevs_timelord_launcher = Zevs.timelord.timelord_launcher:main",
            "Zevs_full_node_simulator = Zevs.simulator.start_simulator:main",
        ]
    },
    package_data={
        "Zevs": ["pyinstaller.spec"],
        "Zevs.wallet.puzzles": ["*.clvm", "*.clvm.hex"],
        "Zevs.util": ["initial-*.yaml", "english.txt"],
        "Zevs.ssl": ["Zevs_ca.crt", "Zevs_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
