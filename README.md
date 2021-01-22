# What is this for

`attach-ext` extracts attachment from EML file.

## Setup

```
pip install git+https://github.com/hirachan/attach-ext -U
```

## Extract attachments

```
attach-ext EMLFILE.eml
```

You can also set more emls.

```
attach-ext EMLFILE1.eml EMLFILE2.eml
```

## The Outputs

Outputs will be created under `output` directory.
Directory named as same as original EML file will be created under it.
