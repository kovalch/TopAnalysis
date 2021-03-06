import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
import sys
import os



####################################################################
## Global job options

REPORTEVERY = 100
WANTSUMMARY = True



####################################################################
## Define the process

from PhysicsTools.PatAlgos.patTemplate_cfg import *
process = cms.Process("topDileptonNtuple")
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(WANTSUMMARY)
)
process.options.allowUnscheduled = cms.untracked.bool(True)
#SimpleMemoryCheck = cms.Service("SimpleMemoryCheck",ignoreTotal = cms.untracked.int32(1) )



####################################################################
## Set up command line options

options = VarParsing.VarParsing ('standard')
options.register('runOnMC', True, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.bool, "decide to run on MC or data")
options.register('runOnAOD', True, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.bool, "run on AOD")
options.register('globalTag', '', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "which globalTag should be used")
options.register('mode', '', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "which type of analysis to run")
options.register('samplename', '', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "which sample to run over")
options.register('inputScript', '', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "python file with input source")
options.register('outputFile', '', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "root output file")
options.register('systematicsName', 'Nominal', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "type of systematics")
options.register('json', '', VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string, "limit to certain lumis")
options.register('skipEvents', 0, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.int, "skip N events")
options.register('includePDFWeights', False, VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.bool, "include the PDF weights *slow!!!*")

## Get and parse the command line arguments
if( hasattr(sys, "argv") ):
    for args in sys.argv :
        arg = args.split(',')
        for val in arg:
            val = val.split('=')
            if(len(val)==2):
                setattr(options,val[0], val[1])



####################################################################
## Set up samplename

if options.samplename == '':
    print 'cannot run without specifying a samplename'
    exit(8888)

if options.samplename == 'data':
    options.runOnMC = False



####################################################################
## Define input

if options.inputScript != '':
    process.load(options.inputScript)
else:
    print 'need an input script'
    exit(8889)

print "max events: ", options.maxEvents
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

if options.skipEvents > 0:
    process.source.skipEvents = cms.untracked.uint32(options.skipEvents)

# Limit to json file (if passed as parameter)
if options.json != '':
    import FWCore.PythonUtilities.LumiList as LumiList
    import FWCore.ParameterSet.Types as CfgTypes
    myLumis = LumiList.LumiList(filename = options.json).getCMSSWString().split(',')
    process.source.lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
    process.source.lumisToProcess.extend(myLumis)



####################################################################
## Create output path

if options.outputFile == '':
    fn = options.mode + '_test.root'
else:
    fn = options.outputFile
print 'Using output file ' + fn

process.TFileService = cms.Service("TFileService",
    fileName = cms.string(fn)
)



####################################################################
## Output module for edm files (needed for PAT sequence, even if not used in EndPath)

process.load("Configuration.EventContent.EventContent_cff")
process.out = cms.OutputModule("PoolOutputModule",
    process.FEVTEventContent,
    dataset = cms.untracked.PSet(dataTier = cms.untracked.string('RECO')),
    fileName = cms.untracked.string("eh.root"),
)



####################################################################
## Set up sample-specific flags for individual treatment in nTuple production

zGenInfo = False
topfilter = False
topSignal = False
higgsSignal = False
alsoViaTau = False
ttbarZ = False
containsWs = False

if options.samplename == 'ttbarsignal':
    topfilter = True
    topSignal = True
    viaTau = False
    containsWs = True
elif options.samplename == 'ttbarsignalviatau':
    topfilter = True
    topSignal = True
    viaTau = True
    containsWs = True
elif options.samplename == 'ttbarsignalplustau':
    topfilter = True
    topSignal = True
    viaTau = False
    alsoViaTau = True
    containsWs = True
elif options.samplename == 'ttbarbg':
    topfilter = True
    containsWs = True
elif options.samplename == 'dy1050' or options.samplename == 'dy50inf':
    zGenInfo = True
elif options.samplename == 'ttbarhiggstobbbar':
    topfilter = True
    topSignal = True
    viaTau = False
    alsoViaTau = True
    higgsSignal = True
elif options.samplename == 'ttbarhiggsinclusive':
    topfilter = True
    topSignal = True
    viaTau = False
    alsoViaTau = True
    higgsSignal = True
    containsWs = True
elif options.samplename == 'gghiggstozzto4l' or options.samplename == 'vbfhiggstozzto4l':
    zGenInfo = True
    higgsSignal = True
elif options.samplename == 'ttbarz':
    topfilter = True
    topSignal = True
    viaTau = False
    alsoViaTau = True
    ttbarZ = True
    containsWs = True
elif options.samplename in [
        'singletop', 'singleantitop',
        'wjets', 'ww', 'wz',
        'wwz', 'www', 'wwg',
        'ttww', 'ttg', 'ttbarw']:
    containsWs = True
elif options.samplename in [
        'data', 'zz', 'zzz',
        'qcdmu15', 'qcdem2030', 'qcdem3080', 'qcdem80170',
        'qcdbcem2030', 'qcdbcem3080', 'qcdbcem80170']:
    # No special treatment needed, put here to avoid typos
    pass
else:
    print "Error: Unknown samplename!"
    exit(8)

signal = topSignal or higgsSignal or zGenInfo



####################################################################
## Configure message logger

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = REPORTEVERY



####################################################################
## Geometry and Detector Conditions

process.load("Configuration.Geometry.GeometryDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")

if options.globalTag != '':
    print "Setting global tag to the command-line value"
    process.GlobalTag.globaltag = cms.string( options.globalTag )
else:
    print "Determine global tag automatically"
    if options.runOnMC:
        process.GlobalTag.globaltag = cms.string('POSTLS170_V6::All')
    else:
        process.GlobalTag.globaltag = cms.string('FT53_V21A_AN6::All')

print "Using global tag: ", process.GlobalTag.globaltag



####################################################################
## HCAL Noise filter

process.load('CommonTools/RecoAlgos/HBHENoiseFilter_cfi')
process.HBHENoiseFilter.minIsolatedNoiseSumE = cms.double(999999.)
process.HBHENoiseFilter.minNumIsolatedNoiseChannels = cms.int32(999999)
process.HBHENoiseFilter.minIsolatedNoiseSumEt = cms.double(999999.)



####################################################################
## Beam scraping filter

process.scrapingFilter = cms.EDFilter("FilterOutScraping",
    applyfilter = cms.untracked.bool(True),
    debugOn     = cms.untracked.bool(False),
    numtrack    = cms.untracked.uint32(10),
    thresh      = cms.untracked.double(0.25)
    )



####################################################################
## ECAL laser correction filter

process.load("RecoMET.METFilters.ecalLaserCorrFilter_cfi")



####################################################################
## Primary vertex filtering

from PhysicsTools.SelectorUtils.pvSelector_cfi import pvSelector
process.goodOfflinePrimaryVertices = cms.EDFilter(
    "PrimaryVertexObjectFilter",
    filterParams = pvSelector.clone(minNdof = cms.double(4.0), maxZ = cms.double(24.0)),
    src = cms.InputTag('offlinePrimaryVertices')
    )
if signal:
    process.goodOfflinePrimaryVertices.filter = cms.bool(False)




####################################################################
## Trigger filtering

# Get the central diLepton trigger lists, and set up filter
from TopAnalysis.TopFilter.sequences.diLeptonTriggers_cff import *
process.load("TopAnalysis.TopFilter.filters.TriggerFilter_cfi")
process.filterTrigger.TriggerResults = cms.InputTag('TriggerResults', '', 'HLT')
process.filterTrigger.printTriggers = False
if options.mode == 'mumu':
    process.filterTrigger.hltPaths  = mumuTriggers
elif options.mode == 'emu':
    process.filterTrigger.hltPaths  = emuTriggers
elif options.mode == 'ee':
    process.filterTrigger.hltPaths  = eeTriggers
else:
    process.filterTrigger.hltPaths = eeTriggers + emuTriggers + mumuTriggers
    
#print "Printing triggers: ", process.filterTrigger.printTriggers



####################################################################
## Prefilter sequence

if options.runOnMC:
    process.prefilterSequence = cms.Sequence(
        process.filterTrigger)
else:
    process.prefilterSequence = cms.Sequence(
        process.filterTrigger *
        process.HBHENoiseFilter *
        process.scrapingFilter *
        process.ecalLaserCorrFilter)



####################################################################
## Jet corrections

if options.runOnMC:
    jetCorr = ('AK5PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'])
else:
    jetCorr = ('AK5PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual'])



####################################################################
## PF2PAT sequence

pfpostfix = "PFlow"

# PF2PAT
# Parameter checkClosestZVertex = False needs to be set to False when using PF Jets with Charged Hadron Subtraction, see https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyCorrections#JetEnCorPFnoPU2012
process.load("PhysicsTools.PatAlgos.patSequences_cff")
from PhysicsTools.PatAlgos.tools.pfTools import *
usePF2PAT(process, runPF2PAT=True, jetAlgo='AK5', runOnMC=options.runOnMC, postfix=pfpostfix, jetCorrections=jetCorr, pvCollection=cms.InputTag('goodOfflinePrimaryVertices'), typeIMetCorrections=True)
getattr(process, 'pfPileUp'+pfpostfix).checkClosestZVertex = False



####################################################################
## Set up selections for PF2PAT & PAT objects: Electrons

# Basic selection for PF2PAT
#getattr(process, 'pfSelectedElectrons'+pfpostfix).cut = 'pt > 5 && gsfTrackRef.isNonnull && gsfTrackRef.trackerExpectedHitsInner.numberOfHits <= 0'  # it couldn't find pfSelectedElectrons

# Switch isolation cone to 0.3 and set cut to 0.15
#getattr(process, 'pfIsolatedElectrons'+pfpostfix).doDeltaBetaCorrection = True   # Not really a 'deltaBeta' correction, but it serves # it couldn't find doDeltaBetaCorrection 
getattr(process, 'pfIsolatedElectrons'+pfpostfix).deltaBetaIsolationValueMap = cms.InputTag("elPFIsoValuePU03PFId"+pfpostfix)
getattr(process, 'pfIsolatedElectrons'+pfpostfix).isolationValueMapsCharged = cms.VInputTag(cms.InputTag("elPFIsoValueCharged03PFId"+pfpostfix))
getattr(process, 'pfIsolatedElectrons'+pfpostfix).isolationValueMapsNeutral = cms.VInputTag(cms.InputTag("elPFIsoValueNeutral03PFId"+pfpostfix), cms.InputTag("elPFIsoValueGamma03PFId"+pfpostfix))
#getattr(process, 'pfIsolatedElectrons'+pfpostfix).isolationCut = 0.15 # it couldn't find isolationCut

getattr(process, 'patElectrons'+pfpostfix).isolationValues = cms.PSet(
    pfChargedHadrons = cms.InputTag("elPFIsoValueCharged03PFId"+pfpostfix),
    pfChargedAll = cms.InputTag("elPFIsoValueChargedAll03PFId"+pfpostfix),
    pfPUChargedHadrons = cms.InputTag("elPFIsoValuePU03PFId"+pfpostfix),
    pfNeutralHadrons = cms.InputTag("elPFIsoValueNeutral03PFId"+pfpostfix),
    pfPhotons = cms.InputTag("elPFIsoValueGamma03PFId"+pfpostfix)
)

# Electron ID
getattr(process, 'selectedPatElectrons'+pfpostfix).cut = 'electronID("eidLoose") > 0.5 && passConversionVeto'



####################################################################
## Set up selections for PF2PAT & PAT objects: Muons

# Basic selection for PF2PAT
#getattr(process, 'pfSelectedMuons'+pfpostfix).cut = 'pt > 5' \  # couldn't find pfSelectedMuons
#                                                    '&& muonRef.isNonnull()' \    
#                                                    '&& (muonRef.isGlobalMuon() || muonRef.isTrackerMuon())'   

# Switch isolation cone to 0.3 and set cut to 0.15
#getattr(process, 'pfIsolatedMuons'+pfpostfix).doDeltaBetaCorrection = True   # couldn't find doDeltaBetaCorrection
getattr(process, 'pfIsolatedMuons'+pfpostfix).deltaBetaIsolationValueMap = cms.InputTag("muPFIsoValuePU03"+pfpostfix, "", "")
#getattr(process, 'pfIsolatedMuons'+pfpostfix).isolationValueMapsCharged = [cms.InputTag("muPFIsoValueCharged03"+pfpostfix)]  # couldn't find isolationValueMapsCharged
#getattr(process, 'pfIsolatedMuons'+pfpostfix).isolationValueMapsNeutral = [cms.InputTag("muPFIsoValueNeutral03"+pfpostfix), cms.InputTag("muPFIsoValueGamma03"+pfpostfix)]   # couldn't find isolationValueMapsNeutral
#getattr(process, 'pfIsolatedMuons'+pfpostfix).isolationCut = 0.15   # couldn't find isolationCut

getattr(process, 'patMuons'+pfpostfix).isolationValues = cms.PSet(
    pfNeutralHadrons = cms.InputTag("muPFIsoValueNeutral03"+pfpostfix),
    pfChargedAll = cms.InputTag("muPFIsoValueChargedAll03"+pfpostfix),
    pfPUChargedHadrons = cms.InputTag("muPFIsoValuePU03"+pfpostfix),
    pfPhotons = cms.InputTag("muPFIsoValueGamma03"+pfpostfix),
    pfChargedHadrons = cms.InputTag("muPFIsoValueCharged03"+pfpostfix)
)

# Muon selection
getattr(process, 'selectedPatMuons'+pfpostfix).cut = 'isPFMuon && pt > 20 && abs(eta) < 2.4'



####################################################################
## Set up selections for PF2PAT & PAT objects: Jets

#getattr(process, 'patJetCorrFactors'+pfpostfix).rho = cms.InputTag("kt6PFJets", "rho", "RECO")  # problems with "kt6PFJets", "rho"

# Set to true to access b-tagging information in PAT jets
applyPostfix(process, "patJets", pfpostfix).addTagInfos = True

# Jet selection
getattr(process, 'selectedPatJets'+pfpostfix).cut = 'abs(eta)<5.4'



####################################################################
## Configure jet energy resolution, and use corrected electrons, and propagate to MET

process.load("TopAnalysis.TopUtils.JetEnergyScale_cfi")
process.scaledJetEnergy.inputElectrons = "selectedPatElectrons"+pfpostfix
process.scaledJetEnergy.inputJets = "selectedPatJets"+pfpostfix
process.scaledJetEnergy.inputMETs = "patMETs"+pfpostfix
process.scaledJetEnergy.JECUncSrcFile = cms.FileInPath("TopAnalysis/Configuration/analysis/common/data/Summer13_V4_DATA_UncertaintySources_AK5PFchs.txt")
process.scaledJetEnergy.scaleType = "abs"   # abs = 1, jes:up, jes:down

if options.runOnMC:
    process.scaledJetEnergy.resolutionEtaRanges  = cms.vdouble(0, 0.5, 0.5, 1.1, 1.1, 1.7, 1.7, 2.3, 2.3, 5.4)
    process.scaledJetEnergy.resolutionFactors    = cms.vdouble(1.052, 1.057, 1.096, 1.134, 1.288) # JER standard
else:
    process.scaledJetEnergy.resolutionEtaRanges  = cms.vdouble(0, -1)
    process.scaledJetEnergy.resolutionFactors    = cms.vdouble(1.0) # JER standard



####################################################################
## Build Final Collections

# Electrons
from PhysicsTools.PatAlgos.selectionLayer1.electronSelector_cfi import *
process.selectedPatElectronsAfterScaling = selectedPatElectrons.clone(
    src = 'scaledJetEnergy:selectedPatElectrons'+pfpostfix,
    cut = 'pt > 20 && abs(eta) < 2.5'
)

# Muons
from PhysicsTools.PatAlgos.selectionLayer1.muonSelector_cfi import *

# Electrons and muons dxy and dz selection
from TopAnalysis.TopUtils.LeptonVertexSelector_cfi import *
process.leptonVertexSelector = leptonVertexSelector.clone()
process.leptonVertexSelector.electrons = "selectedPatElectronsAfterScaling"
process.leptonVertexSelector.muons = "selectedPatMuons"+pfpostfix
process.leptonVertexSelector.electronDxyMax = 0.04

# Jets
from PhysicsTools.PatAlgos.selectionLayer1.jetSelector_cfi import *
process.load("TopAnalysis.TopFilter.filters.JetIdFunctorFilter_cfi")
process.goodIdJets.jets = cms.InputTag("scaledJetEnergy:selectedPatJets"+pfpostfix)
process.goodIdJets.jetType = cms.string('PF')
process.goodIdJets.version = cms.string('FIRSTDATA')
process.goodIdJets.quality = cms.string('LOOSE')
process.hardJets = selectedPatJets.clone(src = 'goodIdJets', cut = 'pt > 12 & abs(eta) < 2.4') 

process.finalCollectionsSequence = cms.Sequence(
    process.scaledJetEnergy *
    process.selectedPatElectronsAfterScaling *
    process.leptonVertexSelector *
    process.goodIdJets * 
    process.hardJets
    )



####################################################################
## Define which collections (including which corrections) to be used in nTuple

isolatedElectronCollection = "leptonVertexSelector"

isolatedMuonCollection = "leptonVertexSelector"

jetCollection = "hardJets"

jetForMetUncorrectedCollection = "selectedPatJets"+pfpostfix
jetForMetCollection = "scaledJetEnergy:"+jetForMetUncorrectedCollection

metCollection = "scaledJetEnergy:patMETs"+pfpostfix

mvaMetCollection = "patMEtMVA"

genJetCollection = "ak5GenJetsPlusBCHadron"

genMetCollection = "genMetTrue"

genLevelBJetProducerInput = "produceGenLevelBJets"

genBHadronMatcherInput = "matchGenBCHadronB"
genCHadronMatcherInput = "matchGenBCHadronC"



####################################################################
## Preselection based on final input collections

# Filter on events containing dilepton system of opposite charge and above m(ll) > 12 GeV
from TopAnalysis.TopFilter.filters.DileptonPreselection_cfi import *
process.dileptonPreselection = dileptonPreselection.clone(
    electrons = isolatedElectronCollection,
    muons = isolatedMuonCollection,
    filterCharge = -1,
    filterChannel = options.mode,
    excludeMasses = (-999., 12.),
)

process.preselectionSequence = cms.Sequence(process.dileptonPreselection)



####################################################################
## Additional properties based on final input collections

# Properties for jets like jet charges
process.load("TopAnalysis.HiggsUtils.producers.JetPropertiesProducer_cfi")
process.jetProperties.src = jetCollection



####################################################################
## Separation of ttbar samples in dileptonic and other decays

if topfilter:
    process.load("TopAnalysis.TopFilter.filters.GeneratorTopFilter_cfi")
    process.generatorTopFilter.rejectNonBottomDecaysOfTops = False
    # FIXME: ttGenEvent is not working in several samples, so not possible to filter dileptonic ttbar decays...
    # FIXME: As workaround, the " or topSignal" is placed here, switching off the filtering
    if higgsSignal or ttbarZ or topSignal:
        process.generatorTopFilter.invert_selection = True
        process.generatorTopFilter.channels = ["none"] # Empty array would use some defaults
    else:
        all = ['ElectronElectron', 'ElectronElectronViaTau', 
               'MuonMuon', 'MuonMuonViaTau', 
               'ElectronMuon', 'ElectronMuonViaTau']
        if topSignal:
            process.generatorTopFilter.invert_selection = False
            if viaTau:
                process.generatorTopFilter.channels = ['ElectronElectronViaTau', 'MuonMuonViaTau', 'ElectronMuonViaTau']
            elif alsoViaTau:
                process.generatorTopFilter.channels = all
            else:
                process.generatorTopFilter.channels = ['ElectronElectron', 'ElectronMuon', 'MuonMuon']
        else:
            process.generatorTopFilter.channels = all
            process.generatorTopFilter.invert_selection = True
    process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")
    process.decaySubset.fillMode = "kME" # Status3, use kStable for Status2
    process.topSplittingSequence = cms.Sequence(
        process.makeGenEvt *
        process.generatorTopFilter)
else:
    process.topSplittingSequence = cms.Sequence()



####################################################################
## Sample-specific sequences for generator level information

if zGenInfo:
    process.load("TopAnalysis.HiggsUtils.producers.GenZDecay_cfi")
    process.zGenSequence = cms.Sequence(process.genZDecay)
else:
    process.zGenSequence = cms.Sequence()

if topSignal:
    process.load("TopAnalysis.TopUtils.sequences.GenHFHadronMatching_cff")

    process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi") # Supplies PDG ID to real name resolution of MC particles
    process.load("TopAnalysis.TopUtils.GenLevelBJetProducer_cfi")
    process.produceGenLevelBJets.deltaR = 5.0
    process.produceGenLevelBJets.noBBbarResonances = True
    process.produceGenLevelBJets.genJets = process.matchGenBCHadronB.genJets

    process.genMatchSequence = cms.Sequence(
        process.genBCHadronMatchingSequence *
        process.produceGenLevelBJets
    )
else:
    process.genMatchSequence = cms.Sequence()

if higgsSignal:
    process.load("TopAnalysis.HiggsUtils.filters.GeneratorHiggsFilter_cfi")
    process.generatorHiggsFilter.channels = ["none"]
    process.generatorHiggsFilter.invert_selection = True
    process.load("TopAnalysis.HiggsUtils.sequences.higgsGenEvent_cff")
    process.decaySubsetHiggs.fillMode = "kME" # Status3, use kStable for Status2
    process.higgsGenSequence = cms.Sequence(
        process.makeGenEvtHiggs *
        process.generatorHiggsFilter
    )
else:
    process.higgsGenSequence = cms.Sequence()



####################################################################
## W decay modes for MadGraph samples, in order to correct branching ratios

madgraphSample = False
process.madgraphWDecaySequence = cms.Sequence()
if containsWs:
    if options.inputScript.find("_madgraph_") == -1:
        pass
    else:
        madgraphSample = True
        process.load("TopAnalysis.TopUtils.MadgraphWDecayProducer_cfi")
        process.madgraphWDecaySequence = cms.Sequence(process.madgraphWDecayProducer)



####################################################################
## Include PDF weights for systematic signal samples

if options.includePDFWeights:
    if not topSignal:
        print "PDF variations only supported for the signal"
        exit(5615)
    process.pdfWeights = cms.EDProducer("PdfWeightProducer",
        # Fix POWHEG if buggy (this PDF set will also appear on output,
        # so only two more PDF sets can be added in PdfSetNames if not "")
        #FixPOWHEG = cms.untracked.string("cteq66.LHgrid"),
        GenTag = cms.untracked.InputTag("genParticles"),
        PdfInfoTag = cms.untracked.InputTag("generator"),
        PdfSetNames = cms.untracked.vstring(
            "CT10.LHgrid"
            #"cteq66.LHgrid"
            #, "MRST2006nnlo.LHgrid"
            #, "NNPDF10_100.LHgrid"
            #"cteq6mE.LHgrid"
            # ,"cteq6m.LHpdf"
            #"cteq6m.LHpdf"
        ))
else:
    process.pdfWeights = cms.Sequence()



####################################################################
## Write ntuple

from TopAnalysis.TopAnalyzer.NTupleWriter_cfi import writeNTuple

writeNTuple.sampleName = options.samplename
writeNTuple.channelName = options.mode
writeNTuple.systematicsName = options.systematicsName
writeNTuple.isMC = options.runOnMC
writeNTuple.isTtbarSample = topSignal
writeNTuple.isHiggsSample = higgsSignal
writeNTuple.isZSample = zGenInfo
writeNTuple.isMadgraphSample = madgraphSample

writeNTuple.includeTrigger = False
writeNTuple.includePdfWeights = options.includePDFWeights
writeNTuple.saveHadronMothers = False
writeNTuple.saveCHadronParticles = False

writeNTuple.electrons = isolatedElectronCollection
writeNTuple.muons = isolatedMuonCollection
writeNTuple.jets = jetCollection
writeNTuple.jetsForMet = jetForMetCollection
writeNTuple.jetsForMetUncorrected = jetForMetUncorrectedCollection
writeNTuple.met = metCollection
writeNTuple.mvaMet = mvaMetCollection

writeNTuple.genJets = genJetCollection
writeNTuple.genMet = genMetCollection
writeNTuple.pdfWeights = "pdfWeights:CT10"

writeNTuple.BHadJetIndex = cms.InputTag(genLevelBJetProducerInput, "BHadJetIndex")
writeNTuple.AntiBHadJetIndex = cms.InputTag(genLevelBJetProducerInput, "AntiBHadJetIndex")
writeNTuple.BHadrons = cms.InputTag(genLevelBJetProducerInput, "BHadrons")
writeNTuple.AntiBHadrons = cms.InputTag(genLevelBJetProducerInput, "AntiBHadrons")
writeNTuple.BHadronFromTopB = cms.InputTag(genLevelBJetProducerInput, "BHadronFromTopB")
writeNTuple.AntiBHadronFromTopB = cms.InputTag(genLevelBJetProducerInput, "AntiBHadronFromTopB")
writeNTuple.BHadronVsJet = cms.InputTag(genLevelBJetProducerInput, "BHadronVsJet")
writeNTuple.AntiBHadronVsJet = cms.InputTag(genLevelBJetProducerInput, "AntiBHadronVsJet")

writeNTuple.genBHadPlusMothers = cms.InputTag(genBHadronMatcherInput, "genBHadPlusMothers")
writeNTuple.genBHadPlusMothersIndices = cms.InputTag(genBHadronMatcherInput, "genBHadPlusMothersIndices")
writeNTuple.genBHadIndex = cms.InputTag(genBHadronMatcherInput, "genBHadIndex")
writeNTuple.genBHadFlavour = cms.InputTag(genBHadronMatcherInput, "genBHadFlavour")
writeNTuple.genBHadJetIndex = cms.InputTag(genBHadronMatcherInput, "genBHadJetIndex")
writeNTuple.genBHadFromTopWeakDecay = cms.InputTag(genBHadronMatcherInput, "genBHadFromTopWeakDecay")
writeNTuple.genBHadLeptonIndex = cms.InputTag(genBHadronMatcherInput, "genBHadLeptonIndex")
writeNTuple.genBHadLeptonHadronIndex = cms.InputTag(genBHadronMatcherInput, "genBHadLeptonHadronIndex")
writeNTuple.genBHadLeptonViaTau = cms.InputTag(genBHadronMatcherInput, "genBHadLeptonViaTau")

writeNTuple.genCHadPlusMothers = cms.InputTag(genCHadronMatcherInput, "genCHadPlusMothers")
writeNTuple.genCHadPlusMothersIndices = cms.InputTag(genCHadronMatcherInput, "genCHadPlusMothersIndices")
writeNTuple.genCHadIndex = cms.InputTag(genCHadronMatcherInput, "genCHadIndex")
writeNTuple.genCHadFlavour = cms.InputTag(genCHadronMatcherInput, "genCHadFlavour")
writeNTuple.genCHadJetIndex = cms.InputTag(genCHadronMatcherInput, "genCHadJetIndex")
writeNTuple.genCHadFromTopWeakDecay = cms.InputTag(genCHadronMatcherInput, "genCHadFromTopWeakDecay")
writeNTuple.genCHadBHadronId = cms.InputTag(genCHadronMatcherInput, "genCHadBHadronId")
writeNTuple.genCHadLeptonIndex = cms.InputTag(genCHadronMatcherInput, "genCHadLeptonIndex")
writeNTuple.genCHadLeptonHadronIndex = cms.InputTag(genCHadronMatcherInput, "genCHadLeptonHadronIndex")
writeNTuple.genCHadLeptonViaTau = cms.InputTag(genCHadronMatcherInput, "genCHadLeptonViaTau")

process.writeNTuple = writeNTuple.clone()

if signal:
    process.ntupleInRecoSeq = cms.Sequence()
else:
    process.ntupleInRecoSeq = cms.Sequence(process.writeNTuple)



####################################################################
## Paths, one with preselection, one without for signal samples

# Path containing selections
path = cms.Path(
    process.prefilterSequence *
    process.goodOfflinePrimaryVertices *
    process.finalCollectionsSequence *
    process.preselectionSequence *
    process.jetProperties *
    process.madgraphWDecaySequence *
    process.ntupleInRecoSeq
)

# Path keeping all events and storing generator information
pathNtuple = cms.Path(
    process.genMatchSequence *
    process.higgsGenSequence *
    process.zGenSequence *
    process.goodOfflinePrimaryVertices *
    process.finalCollectionsSequence *
    process.jetProperties *
    process.madgraphWDecaySequence *
    process.writeNTuple
    )

if signal:
    process.pathNtuple = pathNtuple
else:
    process.path = path

pathnames = process.paths_().keys()



####################################################################
## Prepend the paths
## Cannot be before massSearchReplaceAnyInputTag(getattr(process, pathname), ...), else it crashes !?!

from TopAnalysis.TopAnalyzer.CountEventAnalyzer_cfi import countEvents
process.EventsBeforeSelection = countEvents.clone()
process.EventsBeforeSelection.includePDFWeights = options.includePDFWeights
process.EventsBeforeSelection.pdfWeights = "pdfWeights:CT10"

print 'prepending common sequence to paths:', pathnames
for pathname in pathnames:
    getattr(process, pathname).insert(0, cms.Sequence(
        process.pdfWeights *
        process.EventsBeforeSelection *
        process.topSplittingSequence
        ))



####################################################################
## Signal catcher for more information on errors

process.load("TopAnalysis.TopUtils.SignalCatcher_cfi")





