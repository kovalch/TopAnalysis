#define HiggsAnalysis_cxx

#include <iostream>
#include <cmath>
#include <cstdlib>
#include <utility>
#include <algorithm>

#include <TTree.h>
#include <TString.h>
#include <TFile.h>
#include <TSystem.h>
#include <Math/VectorUtil.h>

#include "HiggsAnalysis.h"
#include "higgsUtils.h"
#include "analysisStructs.h"
#include "AnalyzerBase.h"
#include "MvaTreeHandlerBase.h"
#include "MvaTreePlotterBase.h"
#include "../../common/include/analysisUtils.h"
#include "../../common/include/analysisObjectStructs.h"
#include "../../common/include/classes.h"
#include "../../common/include/ScaleFactors.h"





/// Lepton eta selection (absolute value)
constexpr double LeptonEtaCUT = 2.4;

/// Lepton pt selection in GeV
constexpr double LeptonPtCut = 20.;

/// Jet eta selection (absolute value)
constexpr double JetEtaCUT = 2.4;

/// Jet pt selection in GeV
constexpr double JetPtCUT = 30.;

/// Leading 2 jet pt selection in GeV (For cut based approach)
constexpr double Lead2JetPtCUT = JetPtCUT;


/// B-tag working point
/// Available options: 
///  csvl_wp (0.244) 
///  csvm_wp (0.679)
///  csvt_wp (0.898)
constexpr BtagScaleFactors::workingPoints BtagWP = BtagScaleFactors::csvl_wp;


/// MET selection for same-flavour channels (ee, mumu)
constexpr double MetCUT = 40.;










HiggsAnalysis::HiggsAnalysis(TTree*):
inclusiveHiggsDecayMode_(-999),
additionalBjetMode_(-999)
{}



HiggsAnalysis::~HiggsAnalysis()
{}



void HiggsAnalysis::Begin(TTree*)
{
    // Defaults from AnalysisBase
    AnalysisBase::Begin(0);

    // Set up selection steps of MVA tree handlers
    for(MvaTreeHandlerBase* mvaTreeHandler : v_mvaTreeHandler_){
        if(mvaTreeHandler) mvaTreeHandler->book();
    }
}




void HiggsAnalysis::Terminate()
{
    // Produce b-tag efficiencies
    // FIXME: Shouldn't we also clear b-tagging efficiency histograms if they are produced ?
    if(this->makeBtagEfficiencies()) this->btagScaleFactors()->produceEfficiencies();

    // Do everything needed for MVA
    for(MvaTreeHandlerBase* mvaTreeHandler : v_mvaTreeHandler_){
        if(mvaTreeHandler){
            // Produce and write tree
            mvaTreeHandler->writeTrees(static_cast<std::string>(this->outputFilename()),
                                        Channel::convertChannel(static_cast<std::string>(this->channel())),
                                        Systematic::convertSystematic(static_cast<std::string>(this->systematic())));
            //mvaTreeHandler->writeTrees(fOutput);

            // Create and store control plots in fOutput
            MvaTreePlotterBase* mvaTreePlotter = mvaTreeHandler->setPlotter(mvaTreeHandler->stepMvaVariablesMap());
            mvaTreePlotter->plotVariables(fOutput);

            // Cleanup
            mvaTreePlotter->clear();
            delete mvaTreePlotter;
            mvaTreeHandler->clear();
        }
    }
    
    
    // Defaults from AnalysisBase
    AnalysisBase::Terminate();
}



void HiggsAnalysis::SlaveBegin(TTree *)
{
    // Defaults from AnalysisBase
    AnalysisBase::SlaveBegin(0);
    
    // Set b-tagging working point
    this->btagScaleFactors()->setWorkingPoint(BtagWP);
    
    // Book histograms for b-tagging efficiencies
    if(this->makeBtagEfficiencies()) this->btagScaleFactors()->bookHistograms(fOutput);
    
    // Book histograms of all analyzers
    this->bookAll();
}



void HiggsAnalysis::SlaveTerminate()
{
    this->clearAll();

    // Defaults from AnalysisBase
    AnalysisBase::SlaveTerminate();
}



Bool_t HiggsAnalysis::Process(Long64_t entry)
{
    // Defaults from AnalysisBase
    if(!AnalysisBase::Process(entry)) return kFALSE;


    // Use utilities without namespaces
    using namespace common;


    // Entry for object structs are not yet read, so reset
    this->resetObjectStructEntry();


    // Define the selection steps as strings
    std::string selectionStep("");


    //===CUT===
    // this is step0a, no cut application
    selectionStep = "0a";
    
    // Create dummies for objects, non-dummies are created only as soon as needed
    const RecoObjects recoObjectsDummy;
    const CommonGenObjects commonGenObjectsDummy;
    const KinRecoObjects kinRecoObjectsDummy;
    const TopGenObjects topGenObjectsDummy;
    const HiggsGenObjects higgsGenObjectsDummy;

    // Set up dummies for weights and indices, as needed for generic functions
    const tth::GenObjectIndices genObjectIndicesDummy({}, {}, {}, {}, {}, {}, -1, -1, -1, -1, -1, -1, -1, -1);
    const tth::RecoObjectIndices recoObjectIndicesDummy({}, {}, {}, -1, -1, -1, -1, -1, -1, {}, {}, {});
    const tth::GenLevelWeights genLevelWeightsDummy(0., 0., 0., 0., 0.);
    const tth::RecoLevelWeights recoLevelWeightsDummy(0., 0., 0., 0., 0.);
    
    // ++++ Control Plots ++++
    
    this->fillAll(selectionStep,
                  recoObjectsDummy, commonGenObjectsDummy,
                  topGenObjectsDummy, higgsGenObjectsDummy,
                  kinRecoObjectsDummy,
                  genObjectIndicesDummy, recoObjectIndicesDummy,
                  genLevelWeightsDummy, recoLevelWeightsDummy,
                  1.);



    //===CUT===
    // this is step0b, select events on generator level and access true level weights
    selectionStep = "0b";

    // Separate DY dilepton decays in lepton flavours
    if(this->failsDrellYanGeneratorSelection(entry)) return kTRUE;

    // Separate dileptonic ttbar decays via tau
    //if(this->failsTopGeneratorSelection(entry)) return kTRUE;

    // Separate inclusive ttH sample in decays H->bbbar and others
    const int higgsDecayMode = this->higgsDecayMode(entry);
    if(this->failsHiggsGeneratorSelection(higgsDecayMode)) return kTRUE;

    // Separate tt+bb from tt+other
    if(this->failsAdditionalJetFlavourSelection(entry)) return kTRUE;

    // Correct for the MadGraph branching fraction being 1/9 for dileptons (PDG average is .108)
    const double weightMadgraphCorrection = this->madgraphWDecayCorrection(entry);

    // Get weight due to pileup reweighting
    const double weightPU = this->weightPileup(entry);

    // Get weight due to generator weights
    const double weightGenerator = this->weightGenerator(entry);

    // Get true level weights
    const double trueLevelWeightNoPileup = weightGenerator*weightMadgraphCorrection;
    const double trueLevelWeight = trueLevelWeightNoPileup*weightPU;

    const tth::GenLevelWeights genLevelWeights(weightMadgraphCorrection, weightPU, weightGenerator,
                                               trueLevelWeightNoPileup, trueLevelWeight);

    // ++++ Control Plots ++++

    this->fillAll(selectionStep,
                  recoObjectsDummy, commonGenObjectsDummy,
                  topGenObjectsDummy, higgsGenObjectsDummy,
                  kinRecoObjectsDummy,
                  genObjectIndicesDummy, recoObjectIndicesDummy,
                  genLevelWeights, recoLevelWeightsDummy,
                  1.);



    //===CUT===
    selectionStep = "1";

    // Check if event was triggered with the same dilepton trigger as the specified analysis channel
    if(this->failsDileptonTrigger(entry)) return kTRUE;



    // === FULL RECO OBJECT SELECTION === (can thus be used at each selection step)

    // Access reco objects, and common generator objects
    const RecoObjects& recoObjects = this->getRecoObjects(entry);
    const CommonGenObjects& commonGenObjects = this->getCommonGenObjects(entry);

    // Get allLepton indices, apply selection cuts and order them by pt (beginning with the highest value)
    const VLV& allLeptons = *recoObjects.allLeptons_;
    const std::vector<int>& lepPdgId = *recoObjects.lepPdgId_;
    std::vector<int> allLeptonIndices = initialiseIndices(allLeptons);
    selectIndices(allLeptonIndices, allLeptons, LVeta, LeptonEtaCUT, false);
    selectIndices(allLeptonIndices, allLeptons, LVeta, -LeptonEtaCUT);
    selectIndices(allLeptonIndices, allLeptons, LVpt, LeptonPtCut);
    orderIndices(allLeptonIndices, allLeptons, LVpt);
    //const int numberOfAllLeptons = allLeptonIndices.size();

    // Get indices of leptons and antiLeptons separated by charge, and get the leading ones if they exist
    std::vector<int> leptonIndices = allLeptonIndices;
    std::vector<int> antiLeptonIndices = allLeptonIndices;
    selectIndices(leptonIndices, lepPdgId, 0);
    selectIndices(antiLeptonIndices, lepPdgId, 0, false);
    const int numberOfLeptons = leptonIndices.size();
    const int numberOfAntiLeptons = antiLeptonIndices.size();
    const int leptonIndex = numberOfLeptons>0 ? leptonIndices.at(0) : -1;
    const int antiLeptonIndex = numberOfAntiLeptons>0 ? antiLeptonIndices.at(0) : -1;

    // In case of an existing opposite-charge dilepton system,
    // get their indices for leading and next-to-leading lepton
    int leadingLeptonIndex(-1);
    int nLeadingLeptonIndex(-1);
    if(numberOfLeptons>0 && numberOfAntiLeptons>0){
        leadingLeptonIndex = leptonIndex;
        nLeadingLeptonIndex = antiLeptonIndex;
        orderIndices(leadingLeptonIndex, nLeadingLeptonIndex, allLeptons, LVpt);
    }
    const bool hasLeptonPair = this->hasLeptonPair(leadingLeptonIndex, nLeadingLeptonIndex, lepPdgId);

    // Get two indices of the two leptons in the right order for trigger scale factor, if existing
    int leptonXIndex(leadingLeptonIndex);
    int leptonYIndex(nLeadingLeptonIndex);
    if(hasLeptonPair){
        //in ee and mumu channel leptonX must be the highest pt lepton, i.e. this is already correct
        // in emu channel leptonX must be electron
        if(std::abs(lepPdgId.at(leptonXIndex)) != std::abs(lepPdgId.at(leptonYIndex))){
            orderIndices(leptonYIndex, leptonXIndex, lepPdgId, true);
        }
    }

    // Get dilepton system, if existing
    const LV dummyLV(0.,0.,0.,0.);
    const LV dilepton(hasLeptonPair ? allLeptons.at(leadingLeptonIndex)+allLeptons.at(nLeadingLeptonIndex) : dummyLV);

    // Get jet indices, apply selection cuts and order them by pt (beginning with the highest value)
    const VLV& jets = *recoObjects.jets_;
    std::vector<int> jetIndices = initialiseIndices(jets);
    selectIndices(jetIndices, jets, LVeta, JetEtaCUT, false);
    selectIndices(jetIndices, jets, LVeta, -JetEtaCUT);
    selectIndices(jetIndices, jets, LVpt, JetPtCUT);
    orderIndices(jetIndices, jets, LVpt);
    const int numberOfJets = jetIndices.size();
    const bool has2Jets = numberOfJets > 1 && jets.at(jetIndices.at(0)).pt() >= Lead2JetPtCUT && jets.at(jetIndices.at(1)).pt() >= Lead2JetPtCUT;

    // Fill a vector with all jet pair indices, while sorting each pair by the jet charge:
    // first entry is antiBIndex i.e. with higher jet charge, second entry is bIndex
    //const std::vector<double>& jetChargeGlobalPtWeighted = *recoObjects.jetChargeGlobalPtWeighted_;
    const std::vector<double>& jetChargeRelativePtWeighted = *recoObjects.jetChargeRelativePtWeighted_;
    const tth::IndexPairs& jetIndexPairs = this->chargeOrderedJetPairIndices(jetIndices, jetChargeRelativePtWeighted);

    // Get b-jet indices, apply selection cuts
    // and apply b-tag efficiency MC correction using random number based tag flipping
    // and order b-jets by btag discriminator (beginning with the highest value)
    const std::vector<double>& jetBTagCSV = *recoObjects.jetBTagCSV_;
    const std::vector<int>& jetPartonFlavour = *commonGenObjects.jetPartonFlavour_;
    std::vector<int> bjetIndices = jetIndices;
    selectIndices(bjetIndices, jetBTagCSV, (double)this->btagScaleFactors()->getWPDiscrValue());
    this->retagJets(bjetIndices, jetIndices, jets, jetPartonFlavour, jetBTagCSV);
    orderIndices(bjetIndices, jetBTagCSV);
    const int numberOfBjets = bjetIndices.size();
    const bool hasBtag = numberOfBjets > 0;

    // Get MET
    const LV& met = *recoObjects.met_;
    const bool hasMetOrEmu = this->channel()=="emu" || met.pt()>MetCUT;

    const tth::RecoObjectIndices recoObjectIndices(allLeptonIndices,
                                                   leptonIndices, antiLeptonIndices,
                                                   leptonIndex, antiLeptonIndex,
                                                   leadingLeptonIndex, nLeadingLeptonIndex,
                                                   leptonXIndex, leptonYIndex,
                                                   jetIndices, jetIndexPairs,
                                                   bjetIndices);
    
    
    // Determine all reco level weights
    const double weightLeptonSF = this->weightLeptonSF(leadingLeptonIndex, nLeadingLeptonIndex, allLeptons, lepPdgId);
    const double weightTriggerSF = this->weightTriggerSF(leptonXIndex, leptonYIndex, allLeptons);
    const double weightNoPileup = trueLevelWeightNoPileup*weightTriggerSF*weightLeptonSF;
    // We do not apply a b-tag scale factor
    //const double weightBtagSF = ReTagJet ? 1. : this->weightBtagSF(jetIndices, jets, jetPartonFlavour);
    constexpr double weightBtagSF = 1.;

    // The weight to be used for filling the histograms
    double weight = weightNoPileup*weightPU;


    tth::RecoLevelWeights recoLevelWeights(weightLeptonSF, weightTriggerSF, weightBtagSF,
                                           weightNoPileup, weight);


    // ++++ Control Plots ++++

    this->fillAll(selectionStep,
                  recoObjects, commonGenObjects,
                  topGenObjectsDummy, higgsGenObjectsDummy,
                  kinRecoObjectsDummy,
                  genObjectIndicesDummy, recoObjectIndices,
                  genLevelWeights, recoLevelWeights,
                  1.);



    //===CUT===
    selectionStep = "2";

    // we need an OS lepton pair matching the trigger selection...
    if (!hasLeptonPair) return kTRUE;

    // ++++ Control Plots ++++

    this->fillAll(selectionStep,
                  recoObjects, commonGenObjects,
                  topGenObjectsDummy, higgsGenObjectsDummy,
                  kinRecoObjectsDummy,
                  genObjectIndicesDummy, recoObjectIndices,
                  genLevelWeights, recoLevelWeights,
                  weight);



    //===CUT===
    selectionStep = "3";

    // ...with at least 20 GeV invariant mass
    if(dilepton.M() < 20.) return kTRUE;

    const bool isZregion = dilepton.M() > 76 && dilepton.M() < 106;
    //const KinRecoObjects& kinRecoObjects = this->getKinRecoObjects(entry);
    //const KinRecoObjects& kinRecoObjects = this->getKinRecoObjectsOnTheFly(leptonIndex, antiLeptonIndex, jetIndices,
    //                                                                       allLeptons, jets, jetBTagCSV, met);
    const KinRecoObjects& kinRecoObjects = kinRecoObjectsDummy;
    //const bool hasSolution = kinRecoObjects.valuesSet_;



    // ++++ Control Plots ++++

    this->fillAll(selectionStep,
                  recoObjects, commonGenObjects,
                  topGenObjectsDummy, higgsGenObjectsDummy,
                  kinRecoObjects,
                  genObjectIndicesDummy, recoObjectIndices,
                  genLevelWeights, recoLevelWeights,
                  weight);



    // ****************************************
    //handle inverted Z cut
    // Z window plots need to be filled here, in order to rescale the contribution to data
    if(isZregion){
        selectionStep = "4zWindow";

        this->fillAll(selectionStep,
                      recoObjects, commonGenObjects,
                      topGenObjectsDummy, higgsGenObjectsDummy,
                      kinRecoObjects,
                      genObjectIndicesDummy, recoObjectIndices,
                      genLevelWeights, recoLevelWeights,
                      weight);

        if(has2Jets){
            selectionStep = "5zWindow";

            this->fillAll(selectionStep,
                          recoObjects, commonGenObjects,
                          topGenObjectsDummy, higgsGenObjectsDummy,
                          kinRecoObjects,
                          genObjectIndicesDummy, recoObjectIndices,
                          genLevelWeights, recoLevelWeights,
                          weight);

            if(hasMetOrEmu){
                selectionStep = "6zWindow";

                this->fillAll(selectionStep,
                              recoObjects, commonGenObjects,
                              topGenObjectsDummy, higgsGenObjectsDummy,
                              kinRecoObjects,
                              genObjectIndicesDummy, recoObjectIndices,
                              genLevelWeights, recoLevelWeights,
                              weight);

                if(hasBtag){
                    selectionStep = "7zWindow";

                    // FIXME: do not use b-tag scale factor
                    //fullWeights *= weightBtagSF;

                    this->fillAll(selectionStep,
                                  recoObjects, commonGenObjects,
                                  topGenObjectsDummy, higgsGenObjectsDummy,
                                  kinRecoObjects,
                                  genObjectIndicesDummy, recoObjectIndices,
                                  genLevelWeights, recoLevelWeights,
                                  weight);
                }
            }
        }
    }



    //=== CUT ===
    selectionStep = "4";

    //Exclude the Z window
    if(this->channel()!="emu" && isZregion) return kTRUE;

    // ++++ Control Plots ++++

    this->fillAll(selectionStep,
                  recoObjects, commonGenObjects,
                  topGenObjectsDummy, higgsGenObjectsDummy,
                  kinRecoObjects,
                  genObjectIndicesDummy, recoObjectIndices,
                  genLevelWeights, recoLevelWeights,
                  weight);



    //=== CUT ===
    selectionStep = "5";

    //Require at least two jets
    if(!has2Jets) return kTRUE;

    // ++++ Control Plots ++++

    this->fillAll(selectionStep,
                  recoObjects, commonGenObjects,
                  topGenObjectsDummy, higgsGenObjectsDummy,
                  kinRecoObjects,
                  genObjectIndicesDummy, recoObjectIndices,
                  genLevelWeights, recoLevelWeights,
                  weight);



    //=== CUT ===
    selectionStep = "6";

    //Require MET > 40 GeV in non-emu channels
    if(!hasMetOrEmu) return kTRUE;

    // ++++ Control Plots ++++

    this->fillAll(selectionStep,
                  recoObjects, commonGenObjects,
                  topGenObjectsDummy, higgsGenObjectsDummy,
                  kinRecoObjects,
                  genObjectIndicesDummy, recoObjectIndices,
                  genLevelWeights, recoLevelWeights,
                  weight);

    // Fill the b-tagging efficiency plots
    if(this->makeBtagEfficiencies()){
        this->btagScaleFactors()->fillHistograms(jetIndices, jetBTagCSV, jets, jetPartonFlavour, weight);
        return kTRUE;
    }

    

    //=== CUT ===
    selectionStep = "7";

    //Require at least one b tagged jet
    if(!hasBtag) return kTRUE;

    weight *= weightBtagSF;



    // === FULL GEN OBJECT SELECTION ===

    // Access top generator object struct, and higgs generator object struct
    const TopGenObjects& topGenObjects = this->getTopGenObjects(entry);
    const HiggsGenObjects& higgsGenObjects = this->getHiggsGenObjects(entry);
    
    // Match for all genJets all B hadrons
    std::vector<std::vector<int> > genJetBhadronIndices;
    std::vector<int> genBjetIndices;
    std::vector<int> genJetMatchedRecoBjetIndices;
    if(topGenObjects.valuesSet_){
        const VLV& allGenJets = *commonGenObjects.allGenJets_;
        genJetBhadronIndices = this->matchBhadronsToGenJets(allGenJets, topGenObjects);
        genBjetIndices = this->genBjetIndices(genJetBhadronIndices);
        genJetMatchedRecoBjetIndices = this->matchRecoToGenJets(jetIndices, jets, genBjetIndices, allGenJets);
    }
    
    // Match for all genJets all C hadrons
    std::vector<std::vector<int> > genJetChadronIndices;
    std::vector<int> genCjetIndices;
    std::vector<int> genJetMatchedRecoCjetIndices;
    if(topGenObjects.valuesSet_){
        const VLV& allGenJets = *commonGenObjects.allGenJets_;
        genJetChadronIndices = this->matchChadronsToGenJets(allGenJets, topGenObjects);
        genCjetIndices = this->genCjetIndices(genJetBhadronIndices, genJetChadronIndices);
        genJetMatchedRecoCjetIndices = this->matchRecoToGenJets(jetIndices, jets, genCjetIndices, allGenJets);
    }
    
    // Jet matchings for ttbar system
    int genBjetFromTopIndex(-1);
    int genAntiBjetFromTopIndex(-1);
    int matchedBjetFromTopIndex(-1);
    int matchedAntiBjetFromTopIndex(-1);
    if(topGenObjects.valuesSet_){
        genBjetFromTopIndex = this->genBjetIndex(topGenObjects, 6);
        genAntiBjetFromTopIndex = this->genBjetIndex(topGenObjects, -6);
        matchedBjetFromTopIndex = genBjetFromTopIndex>=0 ? genJetMatchedRecoBjetIndices.at(genBjetFromTopIndex) : -1;
        matchedAntiBjetFromTopIndex = genAntiBjetFromTopIndex>=0 ? genJetMatchedRecoBjetIndices.at(genAntiBjetFromTopIndex) : -1;
    }
    
    // Jet matchings for Higgs system
    int genBjetFromHiggsIndex(-1);
    int genAntiBjetFromHiggsIndex(-1);
    int matchedBjetFromHiggsIndex(-1);
    int matchedAntiBjetFromHiggsIndex(-1);
    if(topGenObjects.valuesSet_ && higgsDecayMode == 5){
        genBjetFromHiggsIndex = this->genBjetIndex(topGenObjects, 25);
        genAntiBjetFromHiggsIndex = this->genBjetIndex(topGenObjects, -25);
        matchedBjetFromHiggsIndex = genBjetFromHiggsIndex>=0 ? genJetMatchedRecoBjetIndices.at(genBjetFromHiggsIndex) : -1;
        matchedAntiBjetFromHiggsIndex = genAntiBjetFromHiggsIndex>=0 ? genJetMatchedRecoBjetIndices.at(genAntiBjetFromHiggsIndex) : -1;
    }
    
    
    const tth::GenObjectIndices genObjectIndices(genBjetIndices,
                                                 genJetBhadronIndices,
                                                 genJetMatchedRecoBjetIndices,
                                                 genCjetIndices,
                                                 genJetChadronIndices,
                                                 genJetMatchedRecoCjetIndices,
                                                 genBjetFromTopIndex, genAntiBjetFromTopIndex,
                                                 matchedBjetFromTopIndex, matchedAntiBjetFromTopIndex,
                                                 genBjetFromHiggsIndex, genAntiBjetFromHiggsIndex,
                                                 matchedBjetFromHiggsIndex, matchedAntiBjetFromHiggsIndex);



    // ++++ Control Plots ++++

    this->fillAll(selectionStep,
                  recoObjects, commonGenObjects,
                  topGenObjects, higgsGenObjects,
                  kinRecoObjects,
                  genObjectIndices, recoObjectIndices,
                  genLevelWeights, recoLevelWeights,
                  weight);



    return kTRUE;
}



tth::IndexPairs HiggsAnalysis::chargeOrderedJetPairIndices(const std::vector<int>& jetIndices,
                                                           const std::vector<double>& jetCharges)
{
    tth::IndexPairs result;
    if(jetIndices.size() < 2) return result;

    // Loop over all jet combinations
    for(std::vector<int>::const_iterator i_jetIndex = jetIndices.begin(); i_jetIndex != --(jetIndices.end()); ++i_jetIndex){
        std::vector<int>::const_iterator incrementIterator(i_jetIndex);
        ++incrementIterator;
        for(std::vector<int>::const_iterator j_jetIndex = incrementIterator; j_jetIndex != jetIndices.end(); ++j_jetIndex){
            // Get the indices of b and anti-b jet defined by jet charge
            int bIndex = *i_jetIndex;
            int antiBIndex = *j_jetIndex;
            common::orderIndices(antiBIndex, bIndex, jetCharges);

            result.push_back(std::make_pair(antiBIndex, bIndex));
        }
    }

    return result;
}



std::vector<std::vector<int> > HiggsAnalysis::matchBhadronsToGenJets(const VLV& allGenJets, const TopGenObjects& topGenObjects)const
{
    std::vector<std::vector<int> > result = std::vector<std::vector<int> >(allGenJets.size());
    
    const std::vector<int>& genBHadJetIndex(*topGenObjects.genBHadJetIndex_);
    for(size_t iHadron = 0; iHadron < genBHadJetIndex.size(); ++iHadron){
        const int& jetIndex = genBHadJetIndex.at(iHadron);
        // Protect against hadrons not clustered to any jet
        if(jetIndex == -1) continue;
        result.at(jetIndex).push_back(iHadron);
    }
    
    return result;
}



std::vector<std::vector<int> > HiggsAnalysis::matchChadronsToGenJets(const VLV& allGenJets, const TopGenObjects&)const
{
    std::vector<std::vector<int> > result = std::vector<std::vector<int> >(allGenJets.size());
    
    // FIXME: Loop over all c hadrons and assign them to the jet where they are clustered to
    // FIXME: requires future ntuple branches for c hadrons
    
    return result;
}



std::vector<int> HiggsAnalysis::genBjetIndices(const std::vector<std::vector<int> >& genJetBhadronIndices)const
{
    std::vector<int> result;
    
    for(size_t iJet = 0; iJet < genJetBhadronIndices.size(); ++iJet){
        if(genJetBhadronIndices.at(iJet).size()) result.push_back(iJet);
    }
    
    return result;
}



std::vector<int> HiggsAnalysis::genCjetIndices(const std::vector<std::vector<int> >& genJetBhadronIndices,
                                               const std::vector<std::vector<int> >& genJetChadronIndices)const
{
    if(genJetBhadronIndices.size() != genJetChadronIndices.size()){
        std::cerr<<"ERROR in HiggsAnalysis::genCjetIndices! Input vectors are of different size: "
                 <<genJetBhadronIndices.size()<<" , "<<genJetChadronIndices.size()
                 <<"\n...break\n"<<std::endl;
        exit(489);
    }
    
    std::vector<int> result;
    
    for(size_t iJet = 0; iJet < genJetChadronIndices.size(); ++iJet){
        // First exclude b jets, for remaining ones assign c jets
        if(genJetBhadronIndices.at(iJet).size()) continue;
        if(genJetChadronIndices.at(iJet).size()) result.push_back(iJet);
    }
    
    return result;
}



int HiggsAnalysis::genBjetIndex(const TopGenObjects& topGenObjects, const int pdgId)const
{
    int result(-1);
    
    const std::vector<int>& genBHadFlavour(*topGenObjects.genBHadFlavour_);
    const std::vector<int>& genBHadJetIndex(*topGenObjects.genBHadJetIndex_);
    
    bool alreadyFound(false);
    for(size_t iBHadron=0; iBHadron<genBHadFlavour.size(); ++iBHadron){
        const int flavour = genBHadFlavour.at(iBHadron);
        if(flavour != pdgId) continue;
        
        // Assigning jet index of corresponding hadron. Set to -2 if >1 hadrons found for the same flavour
        if(alreadyFound) return -2;
        result = genBHadJetIndex.at(iBHadron);
        alreadyFound = true;
    }
    
    return result;
}



int HiggsAnalysis::matchRecoToGenJet(const std::vector<int>& jetIndices, const VLV& jets, const int genJetIndex, const VLV& genJets)const{
    
    if(genJetIndex < 0) return -1;
    const LV& genJet = genJets.at(genJetIndex);
    
    int result(-999);
    
    // Find closest jet and its distance in deltaR
    double deltaRJet(999.);
    for(const auto& index : jetIndices){
        double deltaR = ROOT::Math::VectorUtil::DeltaR(genJet, jets.at(index));
        if(deltaR < deltaRJet){
            deltaRJet = deltaR;
            result = index;
        }
    }
    
    // Call a jet matched if it is close enough, and has similar pt
    if(deltaRJet>0.4) return -2;
    if(result >= 0){
        const double ptRecoJet = jets.at(result).pt();
        const double ptJet = genJet.pt();
        const double deltaPtRel = (ptJet - ptRecoJet)/ptJet;
        if(deltaPtRel<-0.4 || deltaPtRel>0.6) return -3;
    }
    
    return result;
}



std::vector<int> HiggsAnalysis::matchRecoToGenJets(const std::vector<int>& jetIndices, const VLV& jets,
                                                   const std::vector<int>& genJetIndices, const VLV& allGenJets)const
{
    // Set all values to -1
    std::vector<int> result = std::vector<int>(allGenJets.size(), -1);
    
    for(const int index : genJetIndices){
        result.at(index) = this->matchRecoToGenJet(jetIndices, jets, index, allGenJets);
    }
    
    return result;
}



void HiggsAnalysis::SetInclusiveHiggsDecayMode(const int inclusiveHiggsDecayMode)
{
    inclusiveHiggsDecayMode_ = inclusiveHiggsDecayMode;
}



void HiggsAnalysis::SetAdditionalBjetMode(const int additionalBjetMode)
{
    additionalBjetMode_ = additionalBjetMode;
}




void HiggsAnalysis::SetAllAnalyzers(std::vector<AnalyzerBase*> v_analyzer)
{
    v_analyzer_ = v_analyzer;
}



void HiggsAnalysis::SetAllTreeHandlers(std::vector<MvaTreeHandlerBase*> v_mvaTreeHandler)
{
    v_mvaTreeHandler_ = v_mvaTreeHandler;
}



bool HiggsAnalysis::failsHiggsGeneratorSelection(const int higgsDecayMode)const
{
    if(inclusiveHiggsDecayMode_ == -999) return false;
    
    // Separate ttH events from inclusve decay into H->bbbar and other decays
    if(inclusiveHiggsDecayMode_==0 && higgsDecayMode==5) return true;
    if(inclusiveHiggsDecayMode_==5 && higgsDecayMode!=5) return true;
    return false;
}



bool HiggsAnalysis::failsAdditionalJetFlavourSelection(const Long64_t& entry)const
{
    if(additionalBjetMode_ == -999) return false;
    
    // Use the full sample for creating btag efficiencies
    if(this->makeBtagEfficiencies()) return false;
    
    // FIXME: this is a workaround as long as there is no specific additional jet flavour info written to nTuple
    const TopGenObjects& topGenObjects = this->getTopGenObjects(entry);
    const CommonGenObjects& commonGenObjects = this->getCommonGenObjects(entry);

    float signalJetPt_min = 20.;
    float signalJetEta_max = 2.5;
    
    // Identifying unique gen b-jets from top
    std::vector<int> genBJetIdFromTop;
    for(size_t iHad=0; iHad<topGenObjects.genBHadJetIndex_->size(); iHad++) {
        if(std::abs(topGenObjects.genBHadFlavour_->at(iHad)) != 6) continue;
        int genJetId = topGenObjects.genBHadJetIndex_->at(iHad);
        if(genJetId<0) continue;
        if(std::find(genBJetIdFromTop.begin(), genBJetIdFromTop.end(), genJetId) != genBJetIdFromTop.end()) continue;
        if(commonGenObjects.allGenJets_->at(genJetId).Pt()<signalJetPt_min || std::fabs(commonGenObjects.allGenJets_->at(genJetId).Eta())>signalJetEta_max) continue;
        
        genBJetIdFromTop.push_back(genJetId);
    }   // End of loop over all b-hadrons
    const unsigned int nTopBjets = genBJetIdFromTop.size();
    
    
    if((additionalBjetMode_==2 || additionalBjetMode_==1) && nTopBjets<2) return true;
    if(additionalBjetMode_==0 && nTopBjets<2) return false;

    
    // Identifying additional b-jets not from top
    std::vector<int> genAddBJetIdNotFromTop;
    for(size_t iHad=0; iHad<topGenObjects.genBHadJetIndex_->size(); iHad++) {
        if(topGenObjects.genBHadFromTopWeakDecay_->at(iHad)!=0) continue;
        int genJetId = topGenObjects.genBHadJetIndex_->at(iHad);
        if(genJetId<0) continue;
        if(std::find(genBJetIdFromTop.begin(), genBJetIdFromTop.end(), genJetId) != genBJetIdFromTop.end()) continue;
        if(commonGenObjects.allGenJets_->at(genJetId).Pt()<signalJetPt_min || std::fabs(commonGenObjects.allGenJets_->at(genJetId).Eta())>signalJetEta_max) continue;
        if(std::find(genAddBJetIdNotFromTop.begin(), genAddBJetIdNotFromTop.end(), genJetId) != genAddBJetIdNotFromTop.end()) continue;
        
        genAddBJetIdNotFromTop.push_back(genJetId);
    }   // End of loop over all b-hadrons

    const unsigned int nExtraBjets = genAddBJetIdNotFromTop.size();

    if(additionalBjetMode_==2 && nExtraBjets>=2) return false;
    if(additionalBjetMode_==1 && nExtraBjets==1) return false;
    if(additionalBjetMode_==0 && nExtraBjets==0) return false;

    return true;
}



void HiggsAnalysis::fillAll(const std::string& selectionStep,
                            const RecoObjects& recoObjects, const CommonGenObjects& commonGenObjects,
                            const TopGenObjects& topGenObjects, const HiggsGenObjects& higgsGenObjects,
                            const KinRecoObjects& kinRecoObjects,
                            const tth::GenObjectIndices& genObjectIndices, const tth::RecoObjectIndices& recoObjectIndices,
                            const tth::GenLevelWeights& genLevelWeights, const tth::RecoLevelWeights& recoLevelWeights,
                            const double& defaultWeight)const
{
    for(AnalyzerBase* analyzer : v_analyzer_){
        if(analyzer) analyzer->fill(recoObjects, commonGenObjects,
                                    topGenObjects, higgsGenObjects,
                                    kinRecoObjects,
                                    recoObjectIndices, genObjectIndices,
                                    genLevelWeights, recoLevelWeights,
                                    defaultWeight, selectionStep);
    }
    
    for(MvaTreeHandlerBase* mvaTreeHandler : v_mvaTreeHandler_){
        if(mvaTreeHandler) mvaTreeHandler->fill(recoObjects, commonGenObjects,
                                                topGenObjects, higgsGenObjects,
                                                kinRecoObjects,
                                                recoObjectIndices, genObjectIndices,
                                                genLevelWeights, recoLevelWeights,
                                                defaultWeight, selectionStep);
    }
}



void HiggsAnalysis::bookAll()
{
    for(AnalyzerBase* analyzer : v_analyzer_){
        if(analyzer) analyzer->book(fOutput);
    }
}



void HiggsAnalysis::clearAll()
{
    for(AnalyzerBase* analyzer : v_analyzer_){
        if(analyzer) analyzer->clear();
    }
}








