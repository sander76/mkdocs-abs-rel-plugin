# Mkdocs absolute to relative link converter

Mkdocs officially only supports relative links. While this makes sense there are situation where it is useful to make use of absolute links. For example when creating a document with absolute links to an image folder. 
If that file is to be moved later on, links are kept intact.

## Installation

```bash
pip install mkdocs-abs-rel-plugin
```


## Usage

In your `mkdocs.yml` file add `abs-to-rel` to the plugins entry:

```yaml
plugins:
  - abs-to-rel
```