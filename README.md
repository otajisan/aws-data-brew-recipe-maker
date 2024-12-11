# aws-data-brew-recipe-maker

AWS Glue Data Brew Recipe maker

- Create a Data Brew recipe to extract values registered in a column of type json.

# Usage

- input file

```json
{
  "key1": "value1",
  "key2": "value2"
}
```

- Run the script

```bash
./run.sh example.json example
```

- Then, the output will be like this:

```json
[
  {
    "Action": {
      "Operation": "EXTRACT_VALUE",
      "Parameters": {
        "path": "key1",
        "sourceColumn": "example",
        "targetColumn": "example_key1"
      }
    }
  },
  {
    "Action": {
      "Operation": "EXTRACT_VALUE",
      "Parameters": {
        "path": "key2",
        "sourceColumn": "example",
        "targetColumn": "example_key2"
      }
    }
  }
]
```