
# Introduction
This repo contains a template for a package. It was created as part of a great
Datacamp course. It also has a `supporting instructions` notebook that guides some
of the steps taken during the course. `cookiecutter` most of this automatically. 

#### ToDo
Add more text to the `supporting instructions` to cover all of the files used.

## impyrial

A package for converting between imperial unit lengths and weights.

This package was created for the [datacamp](`https://www.datacamp.com`) course "Developing Python Packages".

### Features

- Convert lengths between miles, yards, feet and inches.
- Convert weights between hundredweight, stone, pounds and ounces.

### Usage

```
import impyrial

# Convert 500 miles to feet
impyrial.length.convert_unit(500, from_unit='yd', to_unit='ft')  # returns 1500.0

# Convert 100 ounces to pounds
impyrial.weight.convert_unit(100, from_unit='oz', to_unit='lb')  # returns 6.25
```