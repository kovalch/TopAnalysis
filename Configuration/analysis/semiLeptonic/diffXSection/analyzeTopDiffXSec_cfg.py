import FWCore.ParameterSet.Config as cms

## ---
##   use this file to study different distributions for measurement of differential Cross Section
##   does also a monitoring of the cuts before they are applied
## ---

## ---
##    options
## ---

## allow crab to choose trigger filter for every job individually
import FWCore.ParameterSet.VarParsing as VarParsing
import sys
options = VarParsing.VarParsing ('standard')
# create object triggerTag with default value HLT of type singleton and string
options.register('triggerTag', 'HLT',VarParsing.VarParsing.multiplicity.singleton,VarParsing.VarParsing.varType.string, "chosen trigger tag")
# define the syntax you need to enter in the cfg file:
# search for arguments entered after cmsRun
if( hasattr(sys, "argv") ):
    # split arguments by comma - seperating different variables
    for args in sys.argv :
        arg = args.split(',')
        # split further by = to separate variable name and value
        for val in arg:
            val = val.split('=')
            # set variable var to value val (supposed crab syntax: var=val)
            if(len(val)==2):
                setattr(options,val[0], val[1])
print "used trigger path: TriggerResults::"+options.triggerTag

## choose jet collection and corresponding MET
if(not globals().has_key('jetType')):
    jetType =  'particleFlow' # 'Calo'

# switch to run on data and remove all gen plots (type 'MC' or 'data')
if(not globals().has_key('runningOnData')): 
    runningOnData = "MC"

# choose jet correction level shown in plots
# L3Absolute for MC, L2L3Residual for data
if(not globals().has_key('corrLevel')):
    corrLevel='L3Absolute'
print "used JEC level in jetKinematics: "+corrLevel

## run kinematic fit?
## ATTENTION: until the new parameter jetResolutionSmearFactor
## is implemented in a higher version of the TKinFitter package you
## need to check out the head:
## cvs co -r V06-07-04 TopQuarkAnalysis
## cvs up -A TopQuarkAnalysis

if(not globals().has_key('applyKinFit')):
   applyKinFit = True#  False
if(applyKinFit==True):
    print "kinFit and top reconstruction is applied - attention: slows down!!!"
if(applyKinFit==False):
    print "kinFit and top reconstruction not applied"
    
## choose whether you want a pat tuple as output
if(not globals().has_key('writeOutput')): 
    writeOutput  = False # True
    
## remove all ttbar specific gen level filter - used by other _cfg based on this file
if(not globals().has_key('removeGenTtbar')):
    removeGenTtbar = False 
if(removeGenTtbar==True):
    print "all gen level filters using ttbar decay subset are removed" 
    if(runningOnData=="MC"):
        print "selection for gen plots only via TopAnalysis.TopFilter.sequences.genSelection_cff"

## implement anti b-tagging path
if(not globals().has_key('implement0TagPath')):
    implement0TagPath = False
#if(implement0TagPath==True):
#    print "path with ==0 btagged jets included" 
#if(implement0TagPath==False):
#    print "path with ==0 btagged jets excluded"
    
## eventfilter is to select a special ttbar decay channel from ttbarSample by genmatching (ttbar MC only, other MC: choose 'all')
if(not globals().has_key('eventFilter')):
    eventFilter  = 'signal only' # 'background only' # 'all' # 'signal only' # 'semileptonic electron only' # 'dileptonic electron only' # 'dileptonic muon only' # 'fullhadronic' # 'dileptonic muon + electron only' # 'via single tau only' # 'dileptonic via tau only'
if(runningOnData=="MC"):
    print 'chosen ttbar filter:' , eventFilter

# analyze muon quantities
process = cms.Process("Selection")

## configure message logger
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

## define input
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(    
    ## add your favourite file here
    #'/store/user/wbehrenh/TTJets_TuneD6T_7TeV-madgraph-tauola/Spring11-PAT/6e6559812e09b52af172f27db20ae337/mc2pat_9_1_HFr.root'
    #'/store/user/mgoerner/WJetsToLNu_TuneD6T_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_36_1_085.root'
    #'/store/user/mgoerner/WJetsToLNu_TuneD6T_7TeV-madgraph-tauola/PAT_FALL10HH/148435cd71339b79cc0025730c13472a/fall10MC_100_1_iJg.root'
    #'/store/user/cakir/MuHad/PAT_Data2011_MuHadv1_GJSON/d006f2bc492c2b853732556b211d6e87/Data2011_GJSON_10_1_vcC.root'
    #'/store/user/henderle/TTJets_TuneD6T_7TeV-madgraph-tauola/PAT_FALL10HH/6c1c00d4602477b58cef63f182ce0614/fall10MC_14_3_M5Q.root'
    #'/store/user/dammann/TTJets_TuneD6T_7TeV-madgraph-tauola/Fall10-PAT-v2/43e23e1dee19d970b0c8344e9053309f/mcpat_21_1_JdU.root'
    #'/store/user/mgoerner/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/PAT_FALL10HH2/148435cd71339b79cc0025730c13472a/fall10MC_9_1_mFa.root'
    #'/store/user/mgoerner/Mu/PAT_Nov4RerecoL1IncludedUHH/e37a6f43ad6b01bd8486b714dc367330/DataNov4RerecoL1included_196_1_jzY.root'
    )
)

## define maximal number of events to loop over
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.source.skipEvents = cms.untracked.uint32(0)


## configure process options
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

## register TFileService
process.TFileService = cms.Service("TFileService",
    fileName = cms.string('analyzeDiffXSec_test.root')
)

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = cms.string('START38_V14::All')

## Needed for redoing the ak5GenJets
process.load("TopAnalysis.TopUtils.GenJetParticles_cff")
process.load("RecoJets.Configuration.RecoGenJets_cff")

if(runningOnData=="MC"):
    process.p0 = cms.Path(## redo genjets without mu/nu from tau
                          process.genJetParticles *
                          process.ak5GenJets
                          )
    
## ---
##    configure the cutflow scenario
## ---
## std sequence to produce the ttGenEvt
process.load("TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff")
## high level trigger filter
#(use "TriggerResults::REDIGI38X" for fall10 QCD, WW, ZZ and WZ and "TriggerResults::HLT" for the other ones)
# for all PileUp sample use "TriggerResults::REDIGI38XPU"
# for all spring11 MC use REDIGI311X
from HLTrigger.HLTfilters.hltHighLevel_cfi import *
process.hltFilter = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::"+options.triggerTag, HLTPaths = ["HLT_Mu9"], throw=False)
#process.hltFilter = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::HLT", HLTPaths = ["HLT_Mu9"], throw=False)
#process.hltFilter = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::REDIGI38X", HLTPaths = ["HLT_Mu9"], throw=False)
#process.hltFilter = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::REDIGI38XPU", HLTPaths = ["HLT_Mu9"], throw=False)
#process.hltFilter = hltHighLevel.clone(TriggerResultsTag = "TriggerResults::REDIGI311X", HLTPaths = ["HLT_Mu9"], throw=False)

## semileptonic selection
process.load("TopAnalysis.TopFilter.sequences.semiLeptonicSelection_cff")
## generator matching
process.load("TopAnalysis.TopFilter.sequences.generatorMatching_cff")
## muon selection
process.load("TopAnalysis.TopFilter.sequences.muonSelection_cff")
## jet selection
process.load("TopAnalysis.TopFilter.sequences.jetSelection_cff")
## redefine veto jets to be sure it is also replaced when running on PF
from TopAnalysis.TopFilter.sequences.jetSelection_cff import goodJets
process.vetoJets.src="goodJets"
process.vetoJets.cut=''

## tool to select muons from gen Particles and save them as new collection
process.load("TopAnalysis.TopUtils.GenCandSelector_cfi")
## generator level based collections and semileptonic selection (muon and jets)
process.load("TopAnalysis.TopFilter.sequences.genSelection_cff")

## ---
## including analysis tools
## ---
## cross section module
process.load("TopAnalysis.TopAnalyzer.MuonCrossSection_cfi")
## jet kinematics analyzer
process.load("TopAnalysis.TopAnalyzer.JetKinematics_cfi")
## muon kinematics analyzer
process.load("TopAnalysis.TopAnalyzer.MuonKinematics_cfi")
## jet quality analyzer
process.load("TopAnalysis.TopAnalyzer.JetQuality_cfi")
## muon quality analyzer
process.load("TopAnalysis.TopAnalyzer.MuonQuality_cfi")
## electron quality analyzer
process.load("TopAnalysis.TopAnalyzer.ElectronQuality_cfi")
## MET analyzer
process.load("TopAnalysis.TopAnalyzer.METKinematics_cfi")
## electron kinematics analyzer
process.load("TopAnalysis.TopAnalyzer.ElectronKinematics_cfi")
## muon jet kinematics analyzer
process.load("TopAnalysis.TopAnalyzer.MuonJetKinematics_cfi")
## muon vertex analyzer
process.load("TopAnalysis.TopAnalyzer.MuonVertexKinematics_cfi")

## ---
##    set up vertex filter
## ---
process.PVSelection = cms.EDFilter("PrimaryVertexFilter",
                                   pvSrc   = cms.InputTag('offlinePrimaryVertices'),
                                   minNdof = cms.double(4.0),
                                   maxZ    = cms.double(24.0),
                                   maxRho  = cms.double(2.0)
                                   )
## ---
##    set up filter for different ttbar decay channels
## ---
process.load("TopQuarkAnalysis.TopEventProducers.producers.TtDecaySelection_cfi")
process.ttSemiLeptonicFilter = process.ttDecaySelection.clone()
process.ttSemiLeptonicFilter.allowedTopDecays.decayBranchA.muon = True
if(not eventFilter=='all'):
    ## adapt output filename
    if(eventFilter=='signal only'):
        process.TFileService.fileName = 'analyzeDiffXSec_testSig.root'
    elif(eventFilter=='background only'):
        process.ttSemiLeptonicFilter.invert = True
    elif(eventFilter=='semileptonic electron only'):
        process.ttSemiLeptonicFilter.allowedTopDecays.decayBranchA.muon     = False
        process.ttSemiLeptonicFilter.allowedTopDecays.decayBranchA.electron = True
    elif(eventFilter=='dileptonic electron only'):
        process.ttSemiLeptonicFilter.allowedTopDecays.decayBranchA.muon     = False
        process.ttSemiLeptonicFilter.allowedTopDecays.decayBranchA.electron = True
        process.ttSemiLeptonicFilter.allowedTopDecays.decayBranchB.electron = True
    elif(eventFilter=='dileptonic muon only'):
        process.ttSemiLeptonicFilter.allowedTopDecays.decayBranchA.muon     = True
        process.ttSemiLeptonicFilter.allowedTopDecays.decayBranchB.muon     = True
    elif(eventFilter=='fullhadronic'):
        process.ttSemiLeptonicFilter.allowedTopDecays.decayBranchA.muon     = False
    elif(eventFilter=='dileptonic muon + electron only'):
        process.ttSemiLeptonicFilter.allowedTopDecays.decayBranchA.muon     = True
        process.ttSemiLeptonicFilter.allowedTopDecays.decayBranchB.electron = True
    elif(eventFilter=='dileptonic via tau only'):
        process.ttSemiLeptonicFilter.allowedTopDecays.decayBranchA.muon     = False
        process.ttSemiLeptonicFilter.allowedTopDecays.decayBranchA.tau      = True
        process.ttSemiLeptonicFilter.allowedTopDecays.decayBranchB.electron = True
        process.ttSemiLeptonicFilter.allowedTopDecays.decayBranchB.muon     = True
        process.ttSemiLeptonicFilter.allowedTopDecays.decayBranchB.tau      = True
    elif(eventFilter=='via single tau only'):
        process.ttSemiLeptonicFilter.allowedTopDecays.decayBranchA.muon     = False
        process.ttSemiLeptonicFilter.allowedTopDecays.decayBranchA.tau      = True
    else:
        raise NameError, "'"+eventFilter+"' is not a prober eventFilter name choose: 'all', 'signal only', 'background only', 'semileptonic electron only', 'dileptonic electron only', 'dileptonic muon only', 'fullhadronic', 'via single tau only', 'dileptonic via tau only' or 'dileptonic muon + electron only'"
    ## sequence with filter for decay channel and trigger selection hltFilter
    process.filterSequence = cms.Sequence(process.makeGenEvt *
                                          process.ttSemiLeptonicFilter *
                                          process.hltFilter
                                          )
## sequence without filter (only trigger selection hltFilter) - done when 'all' is chosen, removeGenTtbar=True or runningOnData = "data"
if(eventFilter=='all') or (removeGenTtbar==True) or (runningOnData=="data"):
    process.filterSequence = cms.Sequence(process.hltFilter)
     
## ---
##    set up genFilter for semileptonic muons and taus, where taus are decaying into leptons
## ---
process.ttSemiLeptonicFilterSemiTauMuon= process.ttDecaySelection.clone()
process.ttSemiLeptonicFilterSemiTauMuon.allowedTopDecays.decayBranchA.tau = True
process.ttSemiLeptonicFilterSemiTauMuon.allowedTopDecays.decayBranchA.muon= True
process.ttSemiLeptonicFilterSemiTauMuon.restrictTauDecays = cms.PSet(
    leptonic   = cms.bool(True),
    oneProng   = cms.bool(False),
    threeProng = cms.bool(False)
    )
process.genFilterSequence = cms.Sequence(process.makeGenEvt                      *
                                         process.ttSemiLeptonicFilterSemiTauMuon *
                                         process.ttSemiLeptonicFilter             )

## define ordered jets
uds0    = cms.PSet(index = cms.int32(0), correctionLevel = cms.string(corrLevel), useTree = cms.bool(False) )
uds1    = cms.PSet(index = cms.int32(1), correctionLevel = cms.string(corrLevel), useTree = cms.bool(False) )
uds2    = cms.PSet(index = cms.int32(2), correctionLevel = cms.string(corrLevel), useTree = cms.bool(False) )
uds3    = cms.PSet(index = cms.int32(3), correctionLevel = cms.string(corrLevel), useTree = cms.bool(False) )
udsAll  = cms.PSet(index = cms.int32(-1), correctionLevel = cms.string(corrLevel), useTree = cms.bool(False) )

## ---
##    Set up selection steps for muon selection
## ---
process.combinedMuonsSelection        = process.muonSelection.clone (src = 'combinedMuons'       , minNumber = 1, maxNumber = 99999999)
process.kinematicMuonsSelection       = process.muonSelection.clone (src = 'kinematicMuons'      , minNumber = 1, maxNumber = 99999999)
process.trackMuonsSelection           = process.muonSelection.clone (src = 'trackMuons'          , minNumber = 1, maxNumber = 99999999)
process.highPtMuonsSelection          = process.muonSelection.clone (src = 'highPtMuons'         , minNumber = 1, maxNumber = 99999999)
process.goldenMuonsSelection          = process.muonSelection.clone (src = 'goldenMuons'         , minNumber = 1, maxNumber = 99999999)
process.tightMuonsSelection           = process.muonSelection.clone (src = 'tightMuons'          , minNumber = 1, maxNumber = 99999999)

process.muonCuts = cms.Sequence(process.combinedMuonsSelection        +
                                process.highPtMuonsSelection          +
                                process.kinematicMuonsSelection       +
                                process.trackMuonsSelection           +
                                process.goldenMuonsSelection          +
                                process.tightMuonsSelection           +
                                process.muonSelection
                                )

## ---
##    Set up selection steps for different jet multiplicities
## ---
process.leadingJetSelectionNjets1 = process.leadingJetSelection.clone (src = 'tightLeadingPFJets', minNumber = 1)
process.leadingJetSelectionNjets2 = process.leadingJetSelection.clone (src = 'tightLeadingPFJets', minNumber = 2)
process.leadingJetSelectionNjets3 = process.leadingJetSelection.clone (src = 'tightLeadingPFJets', minNumber = 3)
process.leadingJetSelectionNjets4 = process.leadingJetSelection.clone (src = 'tightLeadingPFJets', minNumber = 4)
process.jetCuts = cms.Sequence(process.leadingJetSelectionNjets1 +
                               process.leadingJetSelectionNjets2 +
                               process.leadingJetSelectionNjets3 +
                               process.leadingJetSelectionNjets4 
                               )

## ---
##    Set up low level selection steps (sligthly above trigger) for monitoring
## ---
from TopAnalysis.TopFilter.sequences.jetSelection_cff import selectedPatJets
process.looseCentralJets = selectedPatJets.clone(src = 'selectedPatJetsAK5PF', cut = 'abs(eta) < 2.5 & pt > 30.')
process.looseJetSelectionNjets3 = process.leadingJetSelection.clone (src = 'looseCentralJets', minNumber = 3)
process.looseCuts = cms.Sequence(process.looseCentralJets*process.kinematicMuonsSelection+process.looseJetSelectionNjets3)
                               
## ---
##    Set up selection steps for different (gen)-jet multiplicities
## ---
process.leadingGenJetSelectionNjets1 = process.leadingGenJetSelection.clone (src = 'selectedGenJetCollection', minNumber = 1)
process.leadingGenJetSelectionNjets2 = process.leadingGenJetSelection.clone (src = 'selectedGenJetCollection', minNumber = 2)
process.leadingGenJetSelectionNjets3 = process.leadingGenJetSelection.clone (src = 'selectedGenJetCollection', minNumber = 3)
process.leadingGenJetSelectionNjets4 = process.leadingGenJetSelection.clone (src = 'selectedGenJetCollection', minNumber = 4)

process.genJetCuts = cms.Sequence(process.leadingGenJetSelectionNjets1 +
                                  process.leadingGenJetSelectionNjets2 +
                                  process.leadingGenJetSelectionNjets3 +
                                  process.leadingGenJetSelectionNjets4 
                                  )

## ---
##    Set up selection for b-jet multiplicity
## ---
process.btagging = process.bottomJetSelection.clone(src = 'tightBottomPFJets', minNumber = 2, maxNumber = 99999)

## kinematic contributions
## muon
process.tightMuonKinematics = process.analyzeMuonKinematics.clone (src = 'tightMuons')
process.tightMuonQuality    = process.analyzeMuonQuality.clone    (src = 'tightMuons')
process.tightMuonKinematicsTagged = process.tightMuonKinematics.clone();
process.tightMuonQualityTagged    = process.tightMuonQuality.clone();
process.kinematicMuonQualityPreSel = process.analyzeMuonQuality.clone    (src = 'kinematicMuons')
process.goldenMuonQualityPreSel    = process.analyzeMuonQuality.clone    (src = 'goldenMuons'   )
process.tightMuonKinematicsPreSel  = process.analyzeMuonKinematics.clone (src = 'tightMuons'    )
process.tightMuonQualityPreSel     = process.analyzeMuonQuality.clone    (src = 'tightMuons'    )

## jets
process.tightLead_0_JetKinematics = process.analyzeJetKinematics.clone (src = 'tightLeadingPFJets', analyze = uds0 )
process.tightLead_1_JetKinematics = process.analyzeJetKinematics.clone (src = 'tightLeadingPFJets', analyze = uds1 )
process.tightLead_2_JetKinematics = process.analyzeJetKinematics.clone (src = 'tightLeadingPFJets', analyze = uds2 )
process.tightLead_3_JetKinematics = process.analyzeJetKinematics.clone (src = 'tightLeadingPFJets', analyze = uds3 )
process.tightJetKinematics  = process.analyzeJetKinematics.clone(src = 'tightLeadingPFJets', analyze = udsAll)
process.tightJetQuality     = process.analyzeJetQuality.clone   (src = 'tightLeadingPFJets')
process.bottomJetKinematics = process.analyzeJetKinematics.clone(src = 'tightBottomPFJets', analyze = udsAll)
process.tightJetKinematicsPreSel = process.analyzeJetKinematics.clone(src = 'tightLeadingPFJets', analyze = udsAll)
process.tightJetQualityPreSel    = process.analyzeJetQuality.clone   (src = 'tightLeadingPFJets')

process.tightLead_0_JetKinematicsTagged = process.tightLead_0_JetKinematics.clone()
process.tightLead_1_JetKinematicsTagged = process.tightLead_1_JetKinematics.clone()
process.tightLead_2_JetKinematicsTagged = process.tightLead_2_JetKinematics.clone()
process.tightLead_3_JetKinematicsTagged = process.tightLead_3_JetKinematics.clone()
process.tightJetKinematicsTagged  = process.tightJetKinematics.clone()
process.tightJetQualityTagged     = process.tightJetQuality.clone()
process.bottomJetKinematicsTagged = process.bottomJetKinematics.clone()
process.bottomLead_0_JetKinematicsTagged = process.analyzeJetKinematics.clone (src = 'tightBottomPFJets', analyze = uds0 )
process.bottomLead_1_JetKinematicsTagged = process.analyzeJetKinematics.clone (src = 'tightBottomPFJets', analyze = uds1 )

## muon&jets
process.tightMuontightJetsKinematics       = process.analyzeMuonJetKinematics.clone(srcA = 'tightMuons', srcB = 'tightLeadingPFJets')
process.tightMuontightJetsKinematicsTagged = process.tightMuontightJetsKinematics.clone()
process.trackMuontightJetsKinematicsPreSel = process.analyzeMuonJetKinematics.clone(srcA = 'trackMuons', srcB = 'vetoJets')

## MET
process.analyzeMETMuon = process.analyzeMETCorrelations.clone(srcA = 'patMETs', srcB='tightMuons')
process.analyzeMETMuonTagged = process.analyzeMETMuon.clone()

## collect kinematics
process.monitorKinematicsBeforeBtagging = cms.Sequence(process.tightMuonKinematics       +
                                                       process.tightMuonQuality          +
                                                       process.tightLead_0_JetKinematics +
                                                       process.tightLead_1_JetKinematics +
                                                       process.tightLead_2_JetKinematics +
                                                       process.tightLead_3_JetKinematics +
                                                       process.tightJetKinematics        +
                                                       process.tightJetQuality           +
                                                       process.bottomJetKinematics       +
                                                       process.analyzeMETMuon            +
                                                       process.tightMuontightJetsKinematics)

process.monitorKinematicsAfterBtagging = cms.Sequence(process.tightMuonKinematicsTagged       +
                                                      process.tightMuonQualityTagged          +
                                                      process.tightLead_0_JetKinematicsTagged +
                                                      process.tightLead_1_JetKinematicsTagged +
                                                      process.tightLead_2_JetKinematicsTagged +
                                                      process.tightLead_3_JetKinematicsTagged +
                                                      process.tightJetKinematicsTagged        +
                                                      process.tightJetQualityTagged           +
                                                      process.bottomJetKinematicsTagged       +
                                                      process.analyzeMETMuonTagged            +
                                                      process.tightMuontightJetsKinematicsTagged+
                                                      process.bottomLead_0_JetKinematicsTagged  +
                                                      process.bottomLead_1_JetKinematicsTagged)
process.basicMonitoring = cms.Sequence(process.trackMuontightJetsKinematicsPreSel +
                                       process.kinematicMuonQualityPreSel         +
                                       process.goldenMuonQualityPreSel            +
                                       process.tightMuonKinematicsPreSel          +
                                       process.tightMuonQualityPreSel             +
                                       process.tightJetKinematicsPreSel           +
                                       process.tightJetQualityPreSel              )

## ---
##    configure Kinematic fit
## ---

## produce top reconstructed event
process.load('TopQuarkAnalysis.TopEventProducers.sequences.ttSemiLepEvtBuilder_cff')
## process.ttSemiLepJetPartonMatch.verbosity = 1

## choose collections
## in fitting procedure
process.kinFitTtSemiLepEventHypothesis.leps = 'tightMuons'
process.kinFitTtSemiLepEventHypothesis.jets = 'tightLeadingPFJets'
process.kinFitTtSemiLepEventHypothesis.mets = 'patMETsPF'
## in genmatch
process.ttSemiLepHypGenMatch.jets = 'tightLeadingPFJets'
process.ttSemiLepHypGenMatch.leps = 'tightMuons'
process.ttSemiLepHypGenMatch.mets = 'patMETsPF'
process.ttSemiLepHypGenMatch.jetCorrectionLevel=corrLevel
## in event hypothesis used for 
process.ttSemiLepHypKinFit.jets = 'tightLeadingPFJets'
process.ttSemiLepHypKinFit.leps = 'tightMuons'
process.ttSemiLepHypKinFit.mets = 'patMETsPF'

# maximum number of jets to be considered in the jet combinatorics
# (has to be >= 4, can be set to -1 if you want to take all)
process.kinFitTtSemiLepEventHypothesis.maxNJets = 5

# maximum number of jet combinations finally written into the event, starting from the "best"
# (has to be >= 1, can be set to -1 if you want to take all)
process.kinFitTtSemiLepEventHypothesis.maxNComb = 3

# set constraints:: 1: Whad-mass, 2: Wlep-mass, 3: thad-mass, 4: tlep-mass, 5: nu-mass, 6: equal t-masses
process.kinFitTtSemiLepEventHypothesis.constraints = [1, 2, 6]

# consider b-tagging in event reconstruction
#process.kinFitTtSemiLepEventHypothesis.bTagAlgo = "trackCountingHighEffBJetTags"
process.kinFitTtSemiLepEventHypothesis.bTagAlgo = "simpleSecondaryVertexHighEffBJetTags"

# TCHE discr.values 7TeV: 1.7, 3.3, 10.2
process.kinFitTtSemiLepEventHypothesis.minBDiscBJets     = 1.74
process.kinFitTtSemiLepEventHypothesis.maxBDiscLightJets = 1.74
process.kinFitTtSemiLepEventHypothesis.useBTagging       = True

# use larger JER in KinFit as it is obtained from data
if(runningOnData=="data") and (applyKinFit==True):
    process.kinFitTtSemiLepEventHypothesis.jetEnergyResolutionSmearFactor = 1.1

# add hypothesis
from TopQuarkAnalysis.TopEventProducers.sequences.ttSemiLepEvtBuilder_cff import *
addTtSemiLepHypotheses(process,['kKinFit'])
if(eventFilter=='signal only') and (runningOnData=="MC"):
    if(applyKinFit==True):
        print 'kinfit: processing ttbar SG MC - build genmatch'
else:
    removeTtSemiLepHypGenMatch(process)
    if(applyKinFit==True):
        print 'kinfit: processing bkg or data - genmatch removed'

## keep only events with unambigues parton matches
## (no other partons exist in dR=0.3 cone) 
## attention: improves purity but reduces efficiency
if(eventFilter=='signal only') and (runningOnData=="MC"):
    process.ttSemiLepJetPartonMatch.algorithm = "unambiguousOnly"
    #process.ttSemiLepJetPartonMatch.algorithm = "totalMinDist"
    process.ttSemiLepJetPartonMatch.useMaxDist = True
    ## set number of jets considered in jet-parton matching
    process.ttSemiLepJetPartonMatch.maxNJets=-1
    ## choose jet collection considered in jet-parton matching
    process.ttSemiLepJetPartonMatch.jets='tightLeadingPFJets'
    
## ---
##    configure KinFit Analyzers
## ---

## kinfit succeeded?
process.load("TopQuarkAnalysis.TopEventProducers.producers.TtSemiLepEvtFilter_cfi")
process.filterRecoKinFit  = process.ttSemiLepEventFilter.clone( cut = cms.string("isHypoValid('kKinFit')"  ) )
process.filterMatchKinFit = process.ttSemiLepEventFilter.clone( cut = cms.string("isHypoValid('kGenMatch')") )

## ## configure top reconstruction analyzers & define PSets
## a) for top reconstruction analyzer
process.load("TopAnalysis.TopAnalyzer.TopKinematics_cfi")
## 1)  plots built from event hypothesis kinFit after reco selection
recoKinFit        = cms.PSet(hypoKey=cms.string('kKinFit'  ), useTree=cms.bool(True),
                             matchForStabilityAndPurity=cms.bool(False), ttbarInsteadOfLepHadTop = cms.bool(False),
                             maxNJets = process.kinFitTtSemiLepEventHypothesis.maxNJets)
process.analyzeTopRecoKinematicsKinFit = process.analyzeTopRecKinematics.clone(analyze=recoKinFit)
## 2)  same as 1) but for top/antitop instead of leptonic/hadronic top
recoKinFitTopAntitop = cms.PSet(hypoKey=cms.string('kKinFit'  ), useTree=cms.bool(True),
                                matchForStabilityAndPurity=cms.bool(False), ttbarInsteadOfLepHadTop = cms.bool(True),
                                maxNJets = process.kinFitTtSemiLepEventHypothesis.maxNJets)
process.analyzeTopRecoKinematicsKinFitTopAntitop = process.analyzeTopRecKinematics.clone(analyze=recoKinFitTopAntitop)
## 3)  plots built from event hypothesis of objects from genmatch to partons (ttSemiLepJetPartonMatch) after reco selection
recoGenMatch      = cms.PSet(hypoKey=cms.string('kGenMatch'), useTree=cms.bool(True),
                             matchForStabilityAndPurity=cms.bool(False), ttbarInsteadOfLepHadTop = cms.bool(False),
                             maxNJets = process.kinFitTtSemiLepEventHypothesis.maxNJets)
process.analyzeTopRecoKinematicsGenMatch      = process.analyzeTopRecKinematics.clone(analyze=recoGenMatch)
## 4) plots built from parton level objects
## a)  after phase space selection
genTtbarSemiMu    = cms.PSet(hypoKey=cms.string("None"     ), useTree=cms.bool(True),
                             matchForStabilityAndPurity=cms.bool(False), ttbarInsteadOfLepHadTop = cms.bool(False),
                             maxNJets = process.kinFitTtSemiLepEventHypothesis.maxNJets)
process.analyzeTopPartonLevelKinematics = process.analyzeTopGenKinematics.clone(analyze=genTtbarSemiMu)
## b) without phase space selection
process.analyzeTopPartonLevelKinematicsPhaseSpace = process.analyzeTopGenKinematics.clone(analyze=genTtbarSemiMu)

## configure Kin Fit performance analyzers
process.load("TopAnalysis.TopAnalyzer.HypothesisKinFit_cfi"    )
hypoKinFit = cms.PSet(hypoKey = cms.string("kKinFit"),
                      wantTree = cms.bool(True),
                      maxNJets = process.kinFitTtSemiLepEventHypothesis.maxNJets)
process.analyzeHypoKinFit = process.analyzeHypothesisKinFit.clone(analyze=hypoKinFit)
#process.load("TopAnalysis.TopAnalyzer.HypothesisKinFitMET_cfi" )
#process.analyzeHypoKinFitMET  = process.analyzeHypothesisKinFitMET.clone (srcA = "ttSemiLepEvent", srcB = "patMETs"         )
#process.load("TopAnalysis.TopAnalyzer.HypothesisKinFitJets_cfi")
#process.analyzeHypoKinFitJets = process.analyzeHypothesisKinFitJets.clone(srcA = "ttSemiLepEvent", srcB = "tightLeadingPFJets")
#process.load("TopAnalysis.TopAnalyzer.HypothesisKinFitMuon_cfi")
#process.analyzeHypoKinFitMuon = process.analyzeHypothesisKinFitMuon.clone(srcA = "ttSemiLepEvent", srcB = "tightMuons"      )

## ---
##    collect KinFit Analyzers depending on sample processed
## ---
## dummy to avoid empty sequences
process.dummy = process.hltFilter.clone()
## check if kinFit should be included in main path
if(applyKinFit==True):
    ## case 1: MC sample
    if(runningOnData=="MC"):
        ## case 1a): ttbar semileptonic mu-signal
        if(eventFilter=='signal only'):
            process.kinFit    = cms.Sequence(process.makeTtSemiLepEvent                      +
                                             process.analyzeTopRecoKinematicsKinFit          +
                                             process.analyzeTopRecoKinematicsKinFitTopAntitop+
                                             process.analyzeTopRecoKinematicsGenMatch        +
                                             process.analyzeHypoKinFit                       +
                                             process.filterRecoKinFit                        +
                                             process.filterMatchKinFit
                                             )
            process.kinFitGen           = cms.Sequence(process.analyzeTopPartonLevelKinematics          )
            process.kinFitGenPhaseSpace = cms.Sequence(process.analyzeTopPartonLevelKinematicsPhaseSpace)
            
        ## case 1b): other MC
        else:
            process.kinFit    = cms.Sequence(process.makeTtSemiLepEvent                      +
                                             process.analyzeTopRecoKinematicsKinFitTopAntitop+
                                             process.analyzeTopRecoKinematicsKinFit          +
                                             process.filterRecoKinFit                        
                                             )
            process.kinFitGen           = cms.Sequence(process.dummy)
            process.kinFitGenPhaseSpace = cms.Sequence(process.dummy)
    ## case 2: data sample
    elif(runningOnData=="data"):
        process.kinFit    = cms.Sequence(process.makeTtSemiLepEvent                      +
                                         process.analyzeTopRecoKinematicsKinFit          +
                                         process.analyzeTopRecoKinematicsKinFitTopAntitop+
                                         process.filterRecoKinFit                        
                                         )
        process.kinFitGen           = cms.Sequence(process.dummy)
        process.kinFitGenPhaseSpace = cms.Sequence(process.dummy)
    else:
         print "choose runningOnData= data or MC"
else:
    process.kinFit              = cms.Sequence(process.dummy)
    process.kinFitGen           = cms.Sequence(process.dummy)
    process.kinFitGenPhaseSpace = cms.Sequence(process.dummy)

## ---
##    run the final sequences
## ---
## standard sequence for cross section analyis and detailed cut monitoring
process.p1 = cms.Path(
                      ## gen event selection (decay channel) and the trigger selection (hltFilter)
                      process.filterSequence                        *
                      ## PV event selection
                      process.PVSelection                           *
                      ## introduce some collections
                      process.semiLeptonicSelection                 *
                      ## muon selection
                      process.muonCuts                              *
                      ## veto on additional leptons
                      process.secondMuonVeto                        *
                      process.electronVeto                          *
                      ## jet selection
                      process.jetCuts                               *
                      ## monitor kinematics before b-tagging
                      process.monitorKinematicsBeforeBtagging       *
                      ## b-tagging
                      process.btagging                              *
                      ## monitor kinematics after b-tagging
                      process.monitorKinematicsAfterBtagging        *
                      ## apply kinematic fit
                      process.kinFit
                      )
if(applyKinFit==False or eventFilter!="signal only"):
    process.p1.remove(process.dummy)
if(runningOnData=="data"):
    process.p1.remove(process.isolatedGenMuons)
    process.p1.remove(process.semiLeptGenCollections)

## loose selection and monitoring of some basic distributions
process.p2 = cms.Path(## gen event selection (decay channel) and the trigger selection (hltFilter)
                      process.filterSequence                        *
                      ## PV event selection
                      process.PVSelection                           *
                      ## introduce some collections
                      process.semiLeptonicSelection                 *
                      ## loose selection (slightly above mu17TriCentralJet30 Trigger)
                      process.looseCuts                             *
                      ## basic monitoring
                      process.basicMonitoring
                      )

## std analysis with generator objects as input for efficiency determination
## no phase space cuts
if(runningOnData=="MC"):
    print "running on Monte Carlo, gen-plots produced"
    process.p3 = cms.Path(
                          ## gen event selection: semileptonic (muon & tau->lepton)
                          ## tau->Mu if eventFilter=='background only' and
                          ## process.ttSemiLeptonicFilter.invert = True
                          process.genFilterSequence                     *
                          ## introduce some collections
                          process.isolatedGenMuons                      *
                          process.semiLeptGenCollections                *
                          ## investigate top reconstruction
                          process.kinFitGen
                          )
    ## delete gen filter
    if(removeGenTtbar==True):    
        process.p3.remove(process.genFilterSequence)
    ## delete dummy sequence
    if(applyKinFit==False or eventFilter!="signal only"):
        process.p3.remove(process.dummy)
else:
    process.p3 = cms.Path(process.dummy)
    
## std analysis with generator objects as input for efficiency determination
## phase space cuts for muon and jets
if(runningOnData=="MC"):
    process.s4 = cms.Sequence(
                              ## introduce some collections
                              process.isolatedGenMuons                      *
                              process.semiLeptGenCollections                *
                              ## muon selection
                              process.genMuonSelection                      *
                              ## jet selection
                              process.genJetCuts                            *
                              ## investigate top reconstruction
                              process.kinFitGenPhaseSpace
                              )
    process.p4 = cms.Path(
                          ## gen event selection: semileptonic (muon & tau->lepton)
                          ## tau->Mu if eventFilter=='background only' and
                          ## process.ttSemiLeptonicFilter.invert = True
                          process.genFilterSequence                      *
                          ## sequence with gen selection and histograms
                          process.s4
                          )
    ## delete gen filter
    if(removeGenTtbar==True):    
        process.p4.remove(process.genFilterSequence)
    ## delete dummy sequence
    if(applyKinFit==False or eventFilter!="signal only"):
        process.p4.remove(process.dummy)
elif(runningOnData=="data"):
    process.p4 = cms.Path(process.dummy)
    print "running on data, no gen-plots"
else:
    print "choose runningOnData= data or MC, creating no gen-plots"
## Output Module Configuration
if(writeOutput):
    from PhysicsTools.PatAlgos.patEventContent_cff import *
    process.out = cms.OutputModule("PoolOutputModule",
                                   fileName = cms.untracked.string('patTuple_selectedNjets4.root'),
                                   # save only events passing the full path
                                   SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p1') ),
                                   #save output (comment to keep everything...)
                                   outputCommands = cms.untracked.vstring('drop *') 
                                   )
    process.out.outputCommands += patEventContentNoCleaning
    process.out.outputCommands += patExtraAodEventContent
    process.outpath = cms.EndPath(process.out)
## switch to SSV btagging
from PhysicsTools.PatAlgos.tools.helpers import massSearchReplaceAnyInputTag
massSearchReplaceAnyInputTag(process.p1, 'tightBottomPFJets', 'simpleSecondaryVertexHighEffBJets')
process.simpleSecondaryVertexHighEffBJets.src="goodJetsPF30"
process.p1.replace(process.semiLeptonicSelection, process.semiLeptonicSelection*process.simpleSecondaryVertexHighEffBJets)

## switch to PF objects
if(jetType=="particleFlow"):
    pathlist = [process.p1, process.p2, process.p3, process.p4]
    for path in pathlist:  
        massSearchReplaceAnyInputTag(path, 'tightLeadingJets', 'tightLeadingPFJets')
        massSearchReplaceAnyInputTag(path, 'tightBottomJets' , 'tightBottomPFJets' )
        massSearchReplaceAnyInputTag(path, 'goodJets'        , 'goodJetsPF30'      )
        massSearchReplaceAnyInputTag(path, 'centralJets'     , 'centralJetsPF30'   )
        massSearchReplaceAnyInputTag(path, 'reliableJets'    , 'reliableJetsPF30'  )
        massSearchReplaceAnyInputTag(path, 'noEtaJets'       , 'noEtaJetsPF30'     )
        massSearchReplaceAnyInputTag(path, 'noPtJets'        , 'noPtJetsPF'        )
        massSearchReplaceAnyInputTag(path, 'patMETs'         , 'patMETsPF'         )
        path.remove(process.centralJets)
        path.remove(process.reliableJets)
        path.remove(process.goodJets)
        path.remove(process.tightLeadingJets)
        path.remove(process.tightBottomJets)
