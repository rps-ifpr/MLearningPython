import setuptools
import six

setuptools.setup (
    name = "pip_test", # Substitua por seu próprio nome de usuário
    version = "0.0.1",
    author = "Exemplo de autor",
    author_email = "autor @ example.com ",
    description =" Um pequeno pacote de exemplo ",
    long_description =" long_description ",
    long_description_content_type =" text / markdown ",
    url ="",
    packages = setuptools.find_packages (),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '> = 3.6 ',
)