import sys
import Bio.SeqIO
import Bio.SeqRecord
import re

def readSeqRecordList(fastaFname):
    allRecordsList = []
    for seqRecord in Bio.SeqIO.parse(fastaFname, 'fasta'):
        allRecordsList.append(seqRecord)
    #print(allRecordsList)
    return allRecordsList

def formatIDsToTargetsFile(seqRecordList):
    for seqRecord in seqRecordList:
        geneAndOrganismList = seqRecord.id.split('[_]') #IN PLACE PROCESSING!
        print(len(geneAndOrganismList))
        if len(geneAndOrganismList) != 2:
            raise Exception('length is greater than 2: %s' % seqRecord.id)
            #unusualNames = seqRecord.id +'\n'
            #sys.stderr.write(unusualNames)
        geneName = geneAndOrganismList[0]
        organismName = geneAndOrganismList[1]
        formattedID = '%s-%s' % (organismName, geneName)
        #print(formattedID)
        seqRecord.id = formattedID

def writeNamesWithMoreThanOneUnderscoreToStderr(seqRecordList):
    for seqRecord in seqRecordList:
        geneAndOrganismList = seqRecord.id.split('_')
        if len(geneAndOrganismList) != 2:
            unusualNames = seqRecord.id +'\n'
            sys.stderr.write(unusualNames)
            #print(unusualNames)

fastaFname = sys.argv[1]
seqRecordList = readSeqRecordList(fastaFname)
#formatIDsToTargetsFile(seqRecordList)
writeNamesWithMoreThanOneUnderscoreToStderr(seqRecordList)
#targetsFastaFname = sys.argv[2]
#Bio.SeqIO.write(seqRecordList, targetsFastaFname, 'fasta')