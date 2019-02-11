import unittest
import re

class Names(object):
    """Wrapper class for gene name and organism name attributes"""

    def __init__(self, gene, organism):
        self.gene = gene
        self.organism = organism

def geneAndOrganismSeparator(fastPlastStyleID):
    m = re.match('([^-]+)_([0-9]+)$', fastPlastStyleID)
    if m is not None:
        gene = m.group(1)
        organism = m.group(2)
    names = Names(gene, organism)
    return names

class NamesTestCase(unittest.TestCase):

    def test_Names(self):
        fastPlastStyleIDSimple = 'rpl36_58'
        fastPlastStyleIDUnusual = 'ycf3_exon3_60'
        namesSimple = geneAndOrganismSeparator(fastPlastStyleIDSimple)
        self.assertEqual('rpl36', namesSimple.gene, 'incorrect gene name')
        self.assertEqual('58', namesSimple.organism, 'incorrect organism name')
        namesUnusual = geneAndOrganismSeparator(fastPlastStyleIDUnusual)
        self.assertEqual('ycf3_exon3', namesUnusual.gene, 'incorrect gene name')
        self.assertEqual('60', namesUnusual.organism, 'incorrect organism name')

if __name__== '__main__':
    unittest.main()
