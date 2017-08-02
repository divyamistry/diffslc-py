from diffslcpy import diffslc
from optparse import OptionParser


def main():
    usage = 'usage: %prog [options] arg'
    parser = OptionParser(usage)
    parser.add_option(
        "-c", "--coexpr_file", dest="coexprfile", default="coexpression.expr", help="File containing the gene coexpression matrix. [%default]"
    )
    parser.add_option(
        "-g", "--graph_file", dest="netfile", default="graph.graphml", help="File containing the PPI network in NetworkX adjacency list or GraphML format. [%default]"
    )
    (options, args) = parser.parse_args()
    ds = diffslc.DiffSLc(options.coexprfile, options.netfile)
    ds.centrality()
