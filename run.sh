#!/bin/bash

input_json=$1
output_column_prefix=$2

python -m aws_data_brew_recipe_maker --input_json=$input_json --output_column_prefix=$output_column_prefix