from .gget_ref import ref
from .gget_search import search
from .gget_info import info
from .gget_seq import seq
from .gget_muscle import muscle
from .gget_blast import blast
from .gget_blat import blat
from .gget_enrichr import enrichr
from .gget_archs4 import archs4
from .gget_alphafold import alphafold
from .gget_setup import setup
from .gget_pdb import pdb
from .gget_gpt import gpt
from .gget_cellxgene import cellxgene
from .gget_chembl import chembl
from .gget_uniprot import uniprot

import logging
logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.INFO,
    datefmt="%c",
)
# Mute numexpr threads info
logging.getLogger("numexpr").setLevel(logging.WARNING)

__version__ = "0.28.0"
__author__ = "jeremie kalfon"
__email__ = "jkalfon@whitelabgx.com"
