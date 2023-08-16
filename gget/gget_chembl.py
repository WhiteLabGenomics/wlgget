import logging

import psycopg2
import pandas as pd
import pandas.io.sql as sqlio

# Add and format time stamp in logging messages
logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.INFO,
    datefmt="%c",
)
# Mute numexpr threads info
logging.getLogger("numexpr").setLevel(logging.WARNING)


def chembl(chembl_id, resource="chembl", identifier=None, assay_id=None, save=False):
    """
    
    """
    #TODO: put as setup
    #! wget https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/chembl_33_postgresql.tar.gz -O ../data/chembl_33_postgresql.tar.gz
    #! tar -xvf chembl_33_postgresql.tar.gz
    #! conda install -c conda-forge postgresql
    #! initdb -D ~/postgresdata
    #! postgres -D ~/postgresdata
    #! createuser -s postgres
    #! psql -U postgres
    #! create database chembl_33;
    #! \q

    #get this file loc

    os.system("pg_restore --no-owner -h localhost -p 5432 -U postgres -d chembl_33 chembl_33_postgresql.dmp")

    con = psycopg2.connect(database="chembl_33", user="postgres", password="", host="127.0.0.1", port="5432")
    print("Database opened successfully")
    resources = [
        "chembl",
        "assays",
        "assay_detail",
    ]

    if ressource == "assays":
        quer = """
SELECT DISTINCT
  m.chembl_id                      AS compound_chembl_id,
  act.standard_type,
  act.standard_relation,
  act.standard_value,
  act.standard_units,
  t.chembl_id                      AS target_chembl_id,
  t.pref_name                      AS target_name,
  t.target_type,
  d.doc_id,
  cs.accession                     AS accession
FROM compound_structures s
  RIGHT JOIN molecule_dictionary m ON s.molregno = m.molregno
  JOIN compound_records r ON m.molregno = r.molregno
  JOIN docs d ON r.doc_id = d.doc_id
  JOIN activities act ON r.record_id = act.record_id
  JOIN assays a ON act.assay_id = a.assay_id
  JOIN target_dictionary t ON a.tid = t.tid
  JOIN target_components tc ON t.tid = tc.tid
  JOIN component_sequences cs ON tc.component_id = cs.component_id
        """
        if identifier is not None:
            quer += "\nAND cs.accession = '"+identifier+"';"
        if limit is not None:
            quer += "\nLIMIT 100000"
        

    dat = sqlio.read_sql_query(quer, con)
    return dat