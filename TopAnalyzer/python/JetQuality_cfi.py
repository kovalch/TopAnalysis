import FWCore.ParameterSet.Config as cms

analyzeJetQuality = cms.EDAnalyzer("JetQualityAnalyzer",
    ## input collection                             
    src = cms.InputTag("selectedLayer1Jets"),
    ## event weight
    weight = cms.InputTag("eventWeight"),
    ## use the weight or not                             
    useWeight = cms.bool(False),
    ## special parameters for jet quality analysis
    analyze   = cms.PSet(
      ## fill histograms for 1.,2.,3.,... leading
      ## jet? -1 corresponds to 'all'
      index  = cms.int32(-1),
      ## flavor tag for the flavor dependend JEC monitor
      ## plots; the form is expected as described in
      ## SWGuidePATDataFormats#pat_JetCorrFactors
      flavor = cms.string("uds")
    )
)



