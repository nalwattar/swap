import sys
import Bio.SeqIO
import Bio.SeqRecord
import re
import fastplaststuff

def readSeqRecordList(fastaFname):
    allRecordsList = []
    for seqRecord in Bio.SeqIO.parse(fastaFname, 'fasta'):
        allRecordsList.append(seqRecord)
    return allRecordsList

def acquireFastPlastStyleID(seqRecordList):
    for seqRecord in seqRecordList:
        fastplastStyleID = seqRecord.id
        print(fastplaststuff.geneAndOrganismSeparator(fastplastStyleID))
        print(fastplastStyleID)

def formatIDsToTargetsFile(seqRecordList):
    for seqRecord in seqRecordList:
        if len(geneAndOrganismList) != 2:
            raise Exception('length is greater than 2: %s' % seqRecord.id)
            #unusualNames = seqRecord.id +'\n'
            #sys.stderr.write(unusualNames)
        formattedID = '%s-%s' % (organism, gene)
        seqRecord.id = formattedID

def writeNamesWithMoreThanOneUnderscoreToStderr(seqRecordList):
    for seqRecord in seqRecordList:
        geneAndOrganismList = seqRecord.id.split('_')
        if len(geneAndOrganismList) != 2:
            unusualNames = seqRecord.id +'\n'
            sys.stderr.write(unusualNames)

fastaFname = sys.argv[1]
seqRecordList = readSeqRecordList(fastaFname)
#print(seqRecordList)
acquireFastPlastStyleID(seqRecordList)
#formatIDsToTargetsFile(seqRecordList)
#targetsFastaFname = sys.argv[2]
#Bio.SeqIO.write(seqRecordList, targetsFastaFname, 'fasta')