from setuptools import setup

setup(
    name="pre_commit_ansible-inventory",
    url="https://github.com/MartinVedani/pre-commit-ansible-inventory",
    author="Slightly adapted from Mikko Salmi",
    author_email="martin.vedani@gmail.com",
    version=open("VERSION", "r").read().strip(),
    install_requires=["ansible-base==2.10.17"],
    license="MIT",
    packages=["pre_commit_hooks"],
    entry_points={
        "console_scripts": [
            "ansible-inventory-wrapper = pre_commit_hooks.ansible_inventory_wrapper:main",
        ]
    },
)
