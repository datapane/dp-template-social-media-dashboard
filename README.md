
# Datapane template: <template_name>

This is a Datapane template.

It can be used as a starting point for creating a Datapane report that <template_description>.

# 🚧 Datapane template development 🚧

*This sub-section should be removed.*

## The template file

When Datapane downloads a template it looks for `template.py`.

The template can be notebook-first, in which case we can convert a `template.ipynb` to `template.py` with the following command:

`jupyter nbconvert --to script 'template.ipynb'`

## Assets

Materials such as images, datasets, and asset generating code, should be included in the `./assets` directory.

This includes markdown files that are to be loaded into the report.

## Dependencies

This template may require additional third-party packages. A full list of required packages should be included in `pyproject.toml`

## README and repository

Datapane template repo names should begin with `dp-template-`, e.g. `dp-template-classifier-dashboard`.

Update this README to include template-specific content within the `<template_*>` placeholders.

# Download the template

The template can be downloaded directly in archive file format, or directly through the Datapane package with the following command:

`datapane template dp-<template_slug>`

# Dependencies

This template may require additional third-party packages. A full list of required packages can be found in `pyproject.toml`
 
 # Contributions

 This template is open-source and accepts contributions!

# How to create a new Datapane template

Visit [datapane/dp-template](https://github.com/datapane/dp-template-classifier-dashboard) for instructions on how to create a new Datapane template.