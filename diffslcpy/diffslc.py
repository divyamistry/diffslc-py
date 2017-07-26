import networkx as nx
import numpy as np

"""
Calculate DiffSLC for all the nodes in a NetworkX graph.
It requires a gene co-expression matrix, and a NetworkX graph
where the nodes correspond to the genes in the gene
coexpression matrix.
"""


class DiffSLc:
    def __init__(self, coexpr_file, network_file):
        print("Reading Coexpressions From: {}".format(coexpr_file))
        self.coexpr_matrix = self._load_coexpr_matrix(coexpr_file)
        # Read network in any format supported by networkx
        # https://networkx.readthedocs.io/en/stable/reference/readwrite.html
        print("Reading Graph/network From: {}".format(network_file))
        self.nxgraph = self._load_graph_from_file(network_file)

    def _load_coexpr_matrix(self, coexpr_file):
        print("Read coexpression matrix and store it in a numpy matrix.")

    def _load_graph_from_file(self, network_file):
        print("Read a graph in any compatible format " +
              "and store it in a network graph object.")

    def _ecc(self):
        print("Calculate edge clustering coefficients for " +
              "given networkx graph")

    def _bdc(self):
        """
        Use a gene coexpression matrix (user provided) and
        edge clustering coefficient (Radiacchi 2004) to create
        biased degreee centrality measure for the diffslc calculation.
        """

        """
        Biased Degree Centrality gathers contributions from the
        edge clustering coefficient and the gene coexpressions
        """
        print("Calculate biased degree centrality for given networkx graph")

    def _ec(self):
        print("Calculate eigenvector centrality for the given networkx graph")

    def centrality(self):
        print("Calculate the diffslc centrality and store it as " +
              "node property in a networkx graph object")

    def beta_param(self, beta_value=0.2):
        print("Assign a value to the beta scaling parameter in the DiffSLC.")

    def omega_param(self, omega_value=0.2):
        print("Assign a value to the omega scaling parameter in the DiffSLC.")
