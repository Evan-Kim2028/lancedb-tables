# lancedb-tables
A serverless embedded streaming OLAP data pipeline that leverages historical blockchain data from [Hypersync](https://github.com/enviodev/hypersync-client-python) and mutable columnar storage format [Lance](https://lancedb.github.io/lance/).

Since Lance is designed to be mutable, it is possible to create an embedded streaming pipeline using the same data source. The main advantage of this streaming approach is that it doesn't require any parquet glob file management. This reduces the complexity of streaming to the same as batch processing. The other main benefit is that LanceDB has tight integration with both
[Polars](https://lancedb.github.io/lancedb/python/polars_arrow/#from-polars-dataframe) and [DuckDB](https://lancedb.github.io/lancedb/python/duckdb/). LanceDB accepts polars dataframes as
data inputs, which allows for a more flexible ETL pipeline, allowing polars to be used as a preprocessing tool. 

There is a lot of flexibility to query from ths database - such as querying larger than memory or using an embedded OLAP engine like DuckDB for faster speed and SQL API because LanceDB leverages the [Apache Arrow Standard](https://arrow.apache.org/overview/)

## Installation
`pip install lancedb-tables`