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
        self.coexpr_matrix = None
        self.nxgraph = None

        print("Reading Coexpressions From: {}".format(coexpr_file))
        self.coexpr_matrix = self._load_coexpr_matrix(coexpr_file)
        # Read network in any format supported by networkx
        # https://networkx.readthedocs.io/en/stable/reference/readwrite.html
        print("Reading Graph/network From: {}".format(network_file))
        self.nxgraph = self._load_graph_from_file(network_file)

    def _load_coexpr_matrix(self, coexpr_file_name):
        try:
            return np.load(file=coexpr_file_name,
                           mmap_mode="r",
                           allow_pickle=False,
                           fix_imports=False)
        except IOError:
            print("Coexpression file either doesn't exist" +
                  " or could not be read.")
        except ValueError:
            print("The coexpression file contains an object array," +
                  " but allow_pickle=False given.")

    def _load_graph_from_file(self, network_file):
        # print("Read a graph in any compatible format " +
        #       "and store it in a network graph object.")
        try:
            return nx.read_adjlist(file=network_file)
        except OSError as oerr:
            print("The Graph file either doesn't exist, or could not be read.")
            print(oerr)
        except ValueError:
            # if there's a reading error, let's first try GraphML format before
            # reporting an error.
            try:
                return.read_graphml(file=network_file)
            except ValueError as verr:
                print("There was a problem reading the file as an" +
                      " adjacency list or as a GraphML file.")
                print(verr)

    def _ecc(self):
        print("Calculate edge clustering coefficients for " +
              "all edges in the nxgraph")
        if (self.nxgraph is not None) and (type(self.nxgraph) == nx.Graph):
            for e in self.nxgraph.edges():
                self.nxgraph[e[0]][e[1]]['ecc'] = self._ecc_single(e)

    def _ecc_single(self, e):
        print("Calculate edge clustering coefficient for " +
              " a given edge e in the nxgraph.")
        numerator = len(list(nx.common_neighbors(self.nxgraph,
                                                 e[0],
                                                 e[1]))) + 1
        denominator = min(self.nxgraph.degree(e[0]), self.nxgraph.degree(e[1]))
        return (numerator / (denominator * 1.0))

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
