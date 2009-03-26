import FWCore.ParameterSet.Config as cms

from TopAnalysis.TopAnalyzer.MuonAnalyzer_cfi import analyzeMuon
## ---------------------------------------Muon eta  |  Muon pt  |   Jet eta |  Jet pt   | muon iso  |  
fullLepMuon00 = analyzeMuon.clone()    ##     -     |     -     |     -     |     -     |     -     | 
fullLepMuon10 = analyzeMuon.clone()    ##     x     |     -     |     -     |     -     |     -     | 
fullLepMuon20 = analyzeMuon.clone()    ##     x     |     x     |     -     |     -     |     -     |   
fullLepMuon01 = analyzeMuon.clone()    ##     -     |     -     |     x     |     -     |     -     |    
fullLepMuon02 = analyzeMuon.clone()    ##     -     |     -     |     x     |     x     |     -     | 
fullLepMuon11 = analyzeMuon.clone()    ##     x     |     -     |     x     |     -     |     -     | 
fullLepMuon12 = analyzeMuon.clone()    ##     x     |     -     |     x     |     x     |     -     |  
fullLepMuon21 = analyzeMuon.clone()    ##     x     |     x     |     x     |     -     |     -     |  
fullLepMuon22 = analyzeMuon.clone()    ##     x     |     x     |     x     |     x     |     -     |  
fullLepMuon32 = analyzeMuon.clone()    ##     x     |     x     |     x     |     x     |     x     |  

## put any extra configuration here:

from TopAnalysis.TopAnalyzer.JetAnalyzer_cfi  import analyzeJets
## ---------------------------------------Muon eta  |  Muon pt  | Jets eta  |  Jets pt  | muon iso  |  
fullLepJets00 = analyzeJets.clone()    ##     -     |     -     |     -     |     -     |     -     |   
fullLepJets10 = analyzeJets.clone()    ##     x     |     -     |     -     |     -     |     -     |    
fullLepJets20 = analyzeJets.clone()    ##     x     |     x     |     -     |     -     |     -     |    
fullLepJets01 = analyzeJets.clone()    ##     -     |     -     |     x     |     -     |     -     |    
fullLepJets02 = analyzeJets.clone()    ##     -     |     -     |     x     |     x     |     -     |    
fullLepJets11 = analyzeJets.clone()    ##     x     |     -     |     x     |     -     |     -     |    
fullLepJets12 = analyzeJets.clone()    ##     x     |     -     |     x     |     x     |     -     |   
fullLepJets21 = analyzeJets.clone()    ##     x     |     x     |     x     |     -     |     -     |   
fullLepJets22 = analyzeJets.clone()    ##     x     |     x     |     x     |     x     |     -     |  
fullLepJets32 = analyzeJets.clone()    ##     x     |     x     |     x     |     x     |     x     |  

## put any extra configuration here:  

## import selection cuts here
from TopAnalysis.TopFilter.selections.fullLepMuonSelection_step1_cff import *

from TopAnalysis.TopFilter.filters.EtaEventFilter_cfi       import filterMuonEta
filterFullLep10 = filterMuonEta.clone()
from TopAnalysis.TopFilter.filters.EtaEventFilter_cfi       import filterJetsEta
filterFullLep01 = filterJetsEta.clone()
from TopAnalysis.TopFilter.filters.PtEventFilter_cfi        import filterMuonPt
filterFullLep20 = filterMuonPt.clone()
from TopAnalysis.TopFilter.filters.PtEventFilter_cfi        import filterJetsPt
filterFullLep02 = filterJetsPt.clone()
from TopAnalysis.TopFilter.filters.IsolationEventFilter_cfi import filterMuonIsolation
filterFullLep30 = filterMuonIsolation.clone()

## put any extra configuration here:
filterFullLep10.cuts = fullLepMuonEta
filterFullLep01.cuts = fullLepJetsEta
filterFullLep20.cuts = fullLepMuonPt
filterFullLep02.cuts = fullLepJetsPt
filterFullLep30.cuts = fullLepCombIsolation

## define sequences
selectFullMuonMuonKinematics = cms.Sequence(fullLepMuon00 + fullLepJets00 *
                                            filterFullLep10 *
                                            fullLepMuon10 + fullLepJets10 *
                                            filterFullLep20 *
                                            fullLepMuon20 + fullLepJets20 
                                           )

selectFullMuonJetsKinematics = cms.Sequence(fullLepMuon00 + fullLepJets00 *
                                            filterFullLep01 *
                                            fullLepMuon01 + fullLepJets01 *
                                            filterFullLep02 *
                                            fullLepMuon02 + fullLepJets02 
                                           )

selectFullMuonMuonIsolation  = cms.Sequence(fullLepMuon22 + fullLepJets22 * 
                                            filterFullLep30 *
                                            fullLepMuon32 + fullLepJets32
                                           )

selectFullLepMuon = cms.Sequence(fullLepMuon00 + fullLepJets00 *
                                 filterFullLep10 *
				 fullLepMuon10 + fullLepJets10 *
                                 filterFullLep20 *
                                 fullLepMuon20 + fullLepJets20 * 
				 filterFullLep01 *
                                 fullLepMuon21 + fullLepJets21 *
				 filterFullLep02 *
                                 fullLepMuon22 + fullLepJets22 *
				 filterFullLep30 *
                                 fullLepMuon32 + fullLepJets32 
                                )



