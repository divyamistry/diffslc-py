from diffslcpy import diffslc
from optparse import OptionParser


def main():
    usage = 'usage: %prog [options] arg'
    parser = OptionParser(usage)
    parser.add_option(
        "-c", "--coexpr_file", dest="coexprfile", default="coexpression.expr", help="File containing the gene coexpression matrix. [%default]"
    )
    parser.add_option(
        "-g", "--graph_file", dest="netfile", default="graph.gml", help="File containing the PPI network in a format that NetworkX understands. [%default]"
    )
    (options, args) = parser.parse_args()
    ds = diffslc.DiffSLc(options.coexprfile, options.netfile)
    ds.centrality()
