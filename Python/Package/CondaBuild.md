# Conda build

## meta.yaml
https://docs.conda.io/projects/conda-build/en/latest/resources/define-metadata.html

```
{% set name = "pkg" %}
{% set version = "1.0.0" %}

package:
  name: {{ name }}
  version: {{ version }}

source:
  path: ../
  url: https://github.com/usr/pkg

outputs:

  - name: {{ name }}
    build:
      noarch: python
      number: 0
      script: python -m pip install --no-deps --ignore-installed .
    requirements:
      host:
        - python
        - pip
      run:
        - python
    about:
      home: https://github.com/usr/pkg
      summary: 'My python pkg'
  
  - name: {{ name }}.test
    requirements:
      run:
        - python
    test:
      source_files:
        - tests        
    about:
      home: https://github.com/usr/pkg
      summary: 'My python pkg'  
```
