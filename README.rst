DiffSLc
-------

To use DiffSLc's python implementaiton, simply import it as package:

>>> from diffslcpy import diffslc
>>> print diffslc.DiffSLc

Or use the command line tool:

.. code-block::

    $ diffslcpy-cl --help
    Usage: diffslcpy-cl [options] arg
    
    Options:
    -h, --help            show this help message and exit
    -c COEXPRFILE, --coexpr_file=COEXPRFILE
                          File containing the gene coexpression matrix.
                          [coexpression.expr]
    -g NETFILE, --graph_file=NETFILE
                          File containing the PPI network in NetworkX adjacency
                            list or GraphML format. [graph.graphml]

--

Additional instructions:

- The coexpression matrix is optional if the edges in the graph already have `coexpr` attribute that holds the coexpression value.

- If both, a coexpression matrix and a network file, are provided, the values in coexpression matrix will overwrite the `coexpr` edge attribute of the network. 

- If both, a coexpression matrix and a network file, are provided, the mapping between network nodes and corresponding row/column names in the coexpression matrix must be the same. DiffSLc will look for coexpression values in the coexpression matrix based on the network node names.

- If you do not have a mapping between your graph nodes and the data you used to create coexpression matrix, there is detailed information provided in the diffslc repository [README's section 3a and 3b](https://github.com/divyamistry/diffslc#step-3a-mapping-between-dip-interactor-and-yg_s98-netaffx-annotations) (and the associated source code mentioned therein).
