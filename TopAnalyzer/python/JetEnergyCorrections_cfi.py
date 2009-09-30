import FWCore.ParameterSet.Config as cms

analyzeJetEnergyCorrections = cms.EDAnalyzer("JetEnergyCorrectionsAnalyzer",
    ## input collection                             
    src = cms.InputTag("ttSemiLepEvent"),
    ## event weight
    weight = cms.InputTag("eventWeight"),
    ## use the weight or not                             
    useWeight = cms.bool(False),
    ## analyzer specific configurables
    analyze   = cms.PSet(
      ## hypothesis key
      hypoKey = cms.string("kGenMatch")
    )    
)



