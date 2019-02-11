import unittests
import re

class Names(object):
    """Wrapper class for gene name and organism name attributes"""

    def __init__(self, gene, organism):
        self.gene = gene
        self.organism = organism

def geneAndOrganismSeparator(fastPlastStyleID):
    gene = re.match('^[a-z]{,}[0-9]{,}[_][a-z]{,}[0-9]{,}[_]{,}[0-9]{,}', )
    organism = re.match('[0-9]{,}') #at end $
    names = Names(gene, organism)
    return names

class NamesTestCase(unittest.TestCase):

    def test_Names(self):
        fastPlastStyleIDSimple = 'rpl36_58'
        fastPlastStyleIDUnusual = 'ycf3_exon3_60'
        namesSimple = geneAndOrganismSeparator(fastPlastStyleIDSimple)
        self.assert('rpl36', namesSimple.gene, 'incorrect gene name')
        self.assert('58', namesSimple.organism, 'incorrect organism name')
        namesUnusual = geneAndOrganismSeparator(fastPlastStyleIDUnusual)
        self.assert('ycf3_exon3', namesUnusual.gene, 'incorrect gene name')
        self.assert('60', namesUnusual.organism, 'incorrect organism name')

if __name__== '__main__':
    unittest.main()
