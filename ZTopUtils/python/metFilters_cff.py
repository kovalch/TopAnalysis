import FWCore.ParameterSet.Config as cms


## following the recommendation from
#  https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFilters
#  also includes a bool combiner configured for these filters
# 
#  If you want to apply the filters (filter events) use the metFilters
#  sequence. If you want to store booleans (or the combined one) without
#  skipping events, use the metFiltersIgnore sequence.
#  Please note, that storing the boolean for the CSCHaloFilter does not work!


## The iso-based HBHE noise filter ___________________________________________||
from CommonTools.RecoAlgos.HBHENoiseFilter_cfi import *

## The iso-based HBHE noise filter ___________________________________________||
from CommonTools.RecoAlgos.HBHENoiseFilterResultProducer_cfi import *


## The CSC beam halo tight filter ____________________________________________||
from RecoMET.METAnalyzers.CSCHaloFilter_cfi import *

## The HCAL laser filter _____________________________________________________||
from RecoMET.METFilters.hcalLaserEventFilter_cfi import *

## The ECAL dead cell trigger primitive filter _______________________________||
from RecoMET.METFilters.EcalDeadCellTriggerPrimitiveFilter_cfi import *

## The EE bad SuperCrystal filter ____________________________________________||
from RecoMET.METFilters.eeBadScFilter_cfi import *

## The ECAL laser correction filter
from RecoMET.METFilters.ecalLaserCorrFilter_cfi import *

## The Good vertices collection needed by the tracking failure filter ________||
goodVertices = cms.EDFilter(
    "VertexSelector",
    filter = cms.bool(False),
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string("!isFake && ndof > 4 && abs(z) <= 24 && position.rho < 2")
    )

## The tracking failure filter _______________________________________________||
from RecoMET.METFilters.trackingFailureFilter_cfi import *

## The tracking POG filters __________________________________________________||
from RecoMET.METFilters.trackingPOGFilters_cff import *
## NOTE: to make tagging mode of the tracking POG filters (three of them), please do:
##    manystripclus53X.taggedMode = cms.untracked.bool(True)
##    manystripclus53X.forcedValue = cms.untracked.bool(False)
##    toomanystripclus53X.taggedMode = cms.untracked.bool(True)
##    toomanystripclus53X.forcedValue = cms.untracked.bool(False)
##    logErrorTooManyClusters.taggedMode = cms.untracked.bool(True)
##    logErrorTooManyClusters.forcedValue = cms.untracked.bool(False)
## Also the stored boolean for the three filters is opposite to what we usually
## have for other filters, i.e., true means rejected bad events while false means 
## good events.

from TopAnalysis.ZTopUtils.boolcombiner_cfi import *

combinedbools.mustBeFalse = ['manystripclus53X',
                             'toomanystripclus53X',
                             'logErrorTooManyClusters']

combinedbools.mustBeTrue = [cms.InputTag('HBHENoiseFilterResultProducer','HBHENoiseFilterResult'),
                            #'CSCTightHaloFilter', ###no bool return!!
                            'hcalLaserEventFilter',
                            'EcalDeadCellTriggerPrimitiveFilter',
                            'trackingFailureFilter',
                            'eeBadScFilter',
                            'ecalLaserCorrFilter']


metFilters = cms.Sequence(
    HBHENoiseFilter *
    CSCTightHaloFilter *
    hcalLaserEventFilter *
    EcalDeadCellTriggerPrimitiveFilter *
    goodVertices * trackingFailureFilter *
    eeBadScFilter *
    ecalLaserCorrFilter *
    trkPOGFilters #*
    #combinedbools
    )

ignoreMetFilters = cms.Sequence(
    cms.ignore(HBHENoiseFilterResultProducer) * #produces HBHENoiseFilterResult
    cms.ignore(CSCTightHaloFilter) *
    cms.ignore(hcalLaserEventFilter) *
    cms.ignore(EcalDeadCellTriggerPrimitiveFilter) *
    cms.ignore(goodVertices) *  cms.ignore(trackingFailureFilter) *
    cms.ignore(eeBadScFilter) *
    cms.ignore(ecalLaserCorrFilter) *
    #trkPOGFilters: give negative output
    cms.ignore(manystripclus53X) *
    cms.ignore(toomanystripclus53X) *
    cms.ignore(logErrorTooManyClusters) *
    combinedbools
    )
