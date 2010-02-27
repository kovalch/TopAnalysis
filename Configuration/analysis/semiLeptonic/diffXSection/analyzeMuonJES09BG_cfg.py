## ---
##    this configfile does the same like analyzeMuonDiffXSec_cfg.py
##    but with a JES shift of -10% and for ttbar BG (filtered on gen level)
## ---

## get the mother file
execfile("/afs/naf.desy.de/user/g/goerner/semileptonic341/analyzeMuonDiffXSecBG_cfg.py")

## get JES-shifting module
process.load("TopAnalysis.TopUtils.JetEnergyScale_cfi")
# set input collection- needed while running on pat tuples
process.scaledJetEnergy.inputJets = "selectedLayer1Jets"
# JES -10%
process.scaledJetEnergy.scaleFactor = 0.9

## include module to create JES-shifted collection
process.p1.replace(process.semiLeptonicSelection,
                   process.scaledJetEnergy * process.semiLeptonicSelection)

## change monitoring to shifted collection
process.p1.replace(process.unshiftedJets,
                   process.shiftedJets)

## change input collection to JES-shifted collection 
process.centralJets.src = "scaledJetEnergy:selectedLayer1Jets"
process.reliableJets.src = "scaledJetEnergy:selectedLayer1Jets"
process.goodJets.src = "scaledJetEnergy:selectedLayer1Jets"

## change output name 
process.TFileService.fileName = 'analyzeDiffXSecJES09_testBkg.root'
