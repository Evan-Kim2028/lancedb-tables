import datetime
from dataclasses import dataclass
import lancedb

from dataclasses import dataclass
from lancedb import DBConnection


@dataclass
class LanceTable:
    """
    Handles the orchestration of LanceDB database interactions, specifically focused on table operations
    such as creating tables, inserting, and merging data. This class facilitates connection management
    and operation execution with customizable database parameters.
    """
    # CLEANUP_TIME determines the frequency that LanceDB will clean up the database and compact the files.
    # Increase the number for less frequent cleanups and longer batch update times.
    # Scaled down for frequent operations in a demonstration
    CLEANUP_TIME: float = 86400 / 24 / 60

    # ! todo - add conn_params to a dataclass variable?

    def write_table(self, uri: str, table: str, data, merge_on: str, conn_params: dict[str, any] = None):
        """
        Writes data from a DataFrame to a specified LanceDB table. If the specified table does not exist, 
        it is created. This function supports dynamic database connection parameters.

        Parameters:
            table (str): The name of the table where the data will be written.
            data (any): The data written to the table. This can be a DataFrame or any other data structure 
                            compatible with LanceDB.
            merge_on (str): The column in the table used as the key for merging data. This column acts 
                            as the primary key or unique identifier for records during the merge operation.
            conn_params (dict[str, any], optional): A dictionary of LanceDB connection parameters that are passed 
                            to the `lancedb.connect` function. This can include parameters such as API key,
                            region, and any other specific settings required by the database connection.

        Behavior:
            The function attempts to connect to the database using the provided parameters. It then tries
            to open the specified table. If the table is found, it compacts file fragments, optimizes indices,
            and cleans up old versions before performing a merge insert operation. If the table does not exist,
            it creates a new table with the data from the DataFrame.
        """
        if conn_params is None:
            conn_params = {}
        # Try to open and merge data into existing table.
        try:
            db: DBConnection = lancedb.connect(uri, **conn_params)

            lance_tbl = db.open_table(table)
            lance_tbl.compact_files()
            # cleanup table
            lance_tbl.cleanup_old_versions(
                datetime.timedelta(seconds=self.CLEANUP_TIME))

            # merge insert data into table
            lance_tbl.merge_insert(merge_on) \
                .when_not_matched_insert_all() \
                .execute(data)

            # create scalar index
            lance_tbl.create_scalar_index(column=merge_on)

        except FileNotFoundError:
            # Handle the case where the table does not exist
            print(f"Creating table {table}")
            lance_tbl = db.create_table(name=table, data=data)

    def open_table(self, uri: str, table: str, conn_params: dict[str, any] = None):
        """
        Wrapper to open a LanceDB table
        """
        if conn_params is None:
            conn_params = {}

        db: DBConnection = lancedb.connect(uri, **conn_params)
        return db.open_table(table)
