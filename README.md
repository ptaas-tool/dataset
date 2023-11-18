# Dataset

This dataset contains a list of vulnerabilities and attacks sets. We gathered a list
of possible layer 7 attacks on APIs and then we selected which attacks can be performed
based on the given vulnerabilities.

You can get this dataset in multiple versions in ```dest``` directory.
These files are our
model dataset which we are going to work on.

```json
[
  {
    "vulnerabilities": [
      "sql raw input",
      "multi source access",
      "hardcode password"
    ],
    "attacks": [
      "sql-injection"
    ]
  }
]
```

## size

Dataset stats, based of the dest versions:

```shell
Version v0.1 (simple):
Attacks = 9, Vulnerabilities = 112, Dataset size = 500, Dataset files = 10
```

```shell
Version v0.2 (complex):
Attacks = 9, Vulnerabilities = 112, Dataset size = 1000, Dataset files = 5
```

```shell
Version v0.3 (normal):
Attacks = 9, Vulnerabilities = 112, Dataset size = 1000, Dataset files = 10
```

## contribute

In order to add new data into our dataset, run the following python script and fill the inputs:

```shell
python3 main.py 100 10 # this is the number of batches that you want to import, second is the max vulnerabilities for each batch
```
