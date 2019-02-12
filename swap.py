import sys
import Bio.SeqIO
import Bio.SeqRecord
import re
import fastplaststuff

def readallRecordsList(fastaFname):
    allRecordsList = []
    for seqRecord in Bio.SeqIO.parse(fastaFname, 'fasta'):
        allRecordsList.append(seqRecord)
    return allRecordsList

def swapGeneAndOrganismPosition(allRecordsList):
    for seqRecord in allRecordsList:
        fastPlastStyleID = seqRecord.id
        names = fastplaststuff.geneAndOrganismSeparator(fastPlastStyleID)
        paftoolsStyleID = fastplaststuff.Names(names.gene, names.organism).makeTargetsFileFormattedID()
        seqRecord.id = paftoolsStyleID
        #print(paftoolsStyleID)

fastaFname = sys.argv[1]
targetsFastaFname = sys.argv[2]
allRecordsList = readallRecordsList(fastaFname)

swapGeneAndOrganismPosition(allRecordsList)

Bio.SeqIO.write(allRecordsList, targetsFastaFname, 'fasta')


#fastPlastStyleID = swapGeneAndOrganismPosition(allRecordsList)
#print(fastPlastStyleID)

#names = fastplaststuff.geneAndOrganismSeparator(fastPlastStyleID)
#print(names)

#n = fastplaststuff.Names(names.gene, names.organism).makeTargetsFileFormattedID()
#print(n)

#formatIDsToTargetsFile(allRecordsList)
