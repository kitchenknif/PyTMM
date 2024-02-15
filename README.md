# PyTMM
Transfer Matrix Method implementation &amp; RefractiveIndex.info database (2015-05-24) browser

Citations: [![DOI](https://zenodo.org/badge/39225589.svg)](https://zenodo.org/badge/latestdoi/39225589)

## RefractiveIndex.info module as a separate package:
[https://github.com/toftul/refractiveindex](https://github.com/toftul/refractiveindex)

## Documentation
Extended documentation can be found at  [kitchenknif.github.io/PyTMM](https://kitchenknif.github.io/PyTMM)


## Installation &amp; Basic Usage
By default the RefractiveIndex module thinks that the RefractiveIndex.info database is installed in your home folder. If this is okay, the database can be used as follows:

    catalog = RefractiveIndex()
    mat = catalog.getMaterial('main', 'Si', 'Aspnes')
    # wavelength in nanometers
    n = mat.getRefractiveIndex(500))
    n = mat.getExtinctionCoefficient(500))

If you want to have the database in a different folder, you just need to specify the path to the RefractiveIndex database:

    catalog = RefractiveIndex("./path/to/folder/with/RefractiveIndex/database")
    mat = catalog.getMaterial('main', 'Si', 'Aspnes')
    n = mat.getRefractiveIndex(500))  # wavelength in nanometers

By default, the database is downloaded automatically on first use. If you do not want that, use `RefractiveIndex(auto_download=False)`.

Examples of using the transferMatrix module can be found in

    .
    +-- _PyTMM
    |   +-- examples


## Dependencies
- numpy
- scipy
- pyyaml
- matplotlib (for plotting)
