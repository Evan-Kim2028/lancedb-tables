# lancedb-tables
`lancedb-tables` is a python package wrapper over LanceDB that makes it easy to create and update LanceDB tables into embedded streaming OLAP data pipeline designs.

Since Lance is designed to be mutable, it is possible to create an embedded streaming pipeline using the same data source. The main advantage of this streaming approach is that it doesn't require any parquet glob file management. This reduces the complexity of setting up streaming to the same as batch processing. The other main benefit is that LanceDB leverages the [Apache Arrow Standard](https://arrow.apache.org/overview/) which makes integrations into ETL pipelines using 
[Polars](https://lancedb.github.io/lancedb/python/polars_arrow/#from-polars-dataframe) and [DuckDB](https://lancedb.github.io/lancedb/python/duckdb/) simple.

## Install with pip
`pip install lancedb-tables`

## Install from source
1. Clone the repository
2. This repository uses rye to manage dependencies and the virtual environment. To install rye, refer to this link for instructions [here](https://rye-up.com/guide/installation/). 
3. Once rye is installed, run `rye sync` to install dependencies and setup the virtual environment, which has a default name of `.venv`. 
4. Activate the virtual environment with the command `source .venv/bin/activate`.