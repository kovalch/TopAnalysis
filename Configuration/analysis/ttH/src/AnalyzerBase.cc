#define AnalysisHistograms_cxx

#include <iostream>
#include <algorithm>
#include <cstdlib>

#include <TH1.h>
#include <TH1D.h>
#include <TString.h>
#include <TSelectorList.h>

#include "AnalyzerBase.h"
#include "analysisStructs.h"
#include "JetCategories.h"
#include "higgsUtils.h"
#include "../../common/include/analysisObjectStructs.h"
#include "../../common/include/analysisUtils.h"
#include "../../common/include/classes.h"





// --------------------------- Methods for AnalysisHistogramBase ---------------------------------------------



AnalyzerBase::AnalyzerBase(const TString& prefix,
                           const std::vector<TString>& selectionStepsNoCategories,
                           const std::vector<TString>& stepsForCategories,
                           const JetCategories* jetCategories):
prefix_(prefix),
selectionSteps_(selectionStepsNoCategories),
stepsForCategories_(stepsForCategories),
jetCategories_(jetCategories),
selectorList_(0)
{
    if(!jetCategories_ && stepsForCategories_.size()>0){
        std::cerr<<"ERROR in constructor for AnalysisHistogramsBase! "
                 <<"No jet categories passed, but request for category-wise selection steps\n...break\n"<<std::endl;
        exit(234);
    }
    if(jetCategories_ && stepsForCategories_.size()==0){
        std::cerr<<"ERROR in constructor for AnalysisHistogramsBase! "
                 <<"Jet categories passed, but no category-wise selection steps defined\n...break\n"<<std::endl;
        exit(235);
    }
}



void AnalyzerBase::book(TSelectorList* output)
{
    // Set pointer to output, so that histograms are owned by it
    selectorList_ = output;
    
    // Book histograms for steps not separated in JetCategories
    for(const auto& stepShort : selectionSteps_){
        const TString step = tth::stepName(stepShort);
        this->addStep(step);
    }
    
    // Book histograms for steps exclusive in each JetCategory
    for(const auto& stepShort : stepsForCategories_){
        for(int category = 0; category<jetCategories_->numberOfCategories(); ++category){
            const TString step = tth::stepName(stepShort, category);
            this->addStep(step);
        }
    }
    
    // Book overview plot for each step divided in JetCategories
    for(const auto& stepShort : stepsForCategories_){
        const TString step = tth::stepName(stepShort);
        std::map<TString, TH1*>& m_histogram = m_stepHistograms_[step+"jetCategories"].m_histogram_;
        const int numberOfCategories(jetCategories_->numberOfCategories());
        TString name = "jetCategories";
        m_histogram[name] = this->store(new TH1D(prefix_+name+step, "Jet categories;# jets/b-jets; # events", numberOfCategories, 0, numberOfCategories));
        const std::vector<TString> v_binLabel(jetCategories_->binLabels());
        for(std::vector<TString>::const_iterator i_binLabel = v_binLabel.begin(); i_binLabel != v_binLabel.end(); ++i_binLabel){
            const TString binLabel(*i_binLabel);
            int position = std::distance(v_binLabel.begin(), i_binLabel) +1;
            m_histogram[name]->GetXaxis()->SetBinLabel(position, binLabel);
        }
    }
    
    // Cleanup
    selectorList_ = 0;
}



void AnalyzerBase::addStep(const TString& step)
{
    // Check whether step already exists
    if(this->checkExistence(step)){
        std::cout<<"Warning in addStep()! Selection step already contained: "<<step
                 <<"\n...skip this one\n";
        return;
    }

    // Book the histograms of the specific analyser
    std::map<TString, TH1*>& m_histogram = m_stepHistograms_[step].m_histogram_;
    this->bookHistos(step, m_histogram);
}



bool AnalyzerBase::checkExistence(const TString& step)const
{
    return m_stepHistograms_.find(step) != m_stepHistograms_.end();
}



void AnalyzerBase::bookHistos(const TString&, std::map<TString, TH1*>&)
{
    // WARNING: this is empty template method, overwrite for inherited histogram class
    
    std::cerr<<"ERROR! Dummy method bookHistos() in AnalysisHistogramBase is called, but overridden one should be used\n"
             <<"...break\n"<<std::endl;
    exit(567);
}



void AnalyzerBase::fill(const RecoObjects& recoObjects, const CommonGenObjects& commonGenObjects,
                        const TopGenObjects& topGenObjects, const HiggsGenObjects& higgsGenObjects,
                        const KinRecoObjects& kinRecoObjects,
                        const tth::RecoObjectIndices& recoObjectIndices, const tth::GenObjectIndices& genObjectIndices,
                        const tth::GenLevelWeights& genLevelWeights, const tth::RecoLevelWeights& recoLevelWeights,
                        const double& weight, const TString& stepShort)
{
    // Number of selected jets and bjets
    const int numberOfJets = recoObjectIndices.jetIndices_.size();
    const int numberOfBjets = recoObjectIndices.bjetIndices_.size();
    
    // Set up step name and check if step exists
    const bool stepInCategory = stepShort.Contains("_cate");
    const TString step = stepInCategory ? stepShort : tth::stepName(stepShort);
    const bool stepExists(this->checkExistence(step));
    if(!stepInCategory && jetCategories_){
        const int categoryId = jetCategories_->categoryId(numberOfJets, numberOfBjets);
        
        // Fill the jetCategories histogram
        const TString stepForJetCategories = step + "jetCategories";
        if(this->checkExistence(stepForJetCategories)){
            std::map<TString, TH1*>& m_histogram = m_stepHistograms_[stepForJetCategories].m_histogram_;
            TString name = "jetCategories";
            m_histogram[name]->Fill(categoryId, weight);
        }
        
        // Here check the individual jet categories
        const TString fullStepName = tth::stepName(stepShort, categoryId);
        this->fill(recoObjects, commonGenObjects,
                   topGenObjects, higgsGenObjects,
                   kinRecoObjects,
                   recoObjectIndices, genObjectIndices,
                   genLevelWeights, recoLevelWeights,
                   weight, fullStepName);
    }
    if(!stepExists) return;
    
    // Fill the histograms of the specific analyser
    std::map<TString, TH1*>& m_histogram = m_stepHistograms_[step].m_histogram_;
    this->fillHistos(recoObjects, commonGenObjects,
                     topGenObjects, higgsGenObjects,
                     kinRecoObjects,
                     recoObjectIndices, genObjectIndices,
                     genLevelWeights, recoLevelWeights,
                     weight, step,
                     m_histogram);
}



void AnalyzerBase::fillHistos(const RecoObjects&, const CommonGenObjects&,
                              const TopGenObjects&, const HiggsGenObjects&,
                              const KinRecoObjects&,
                              const tth::RecoObjectIndices&, const tth::GenObjectIndices&,
                              const tth::GenLevelWeights&, const tth::RecoLevelWeights&,
                              const double&, const TString&,
                              std::map<TString, TH1*>&)
{
    // WARNING: this is empty template method, overwrite for inherited histogram class
    
    std::cerr<<"ERROR! Dummy method fillHistos() in AnalysisHistogramBase is called, but overridden one should be used\n"
             <<"...break\n"<<std::endl;
    exit(568);
}



void AnalyzerBase::clear()
{
    for(auto stepHistograms : m_stepHistograms_){
        stepHistograms.second.m_histogram_.clear();
    }
    m_stepHistograms_.clear();
    selectorList_ = 0;
}







// --------------------------- Methods for EventYieldHistograms ---------------------------------------------



AnalyzerEventYields::AnalyzerEventYields(const std::vector<TString>& selectionStepsNoCategories,
                                         const std::vector<TString>& stepsForCategories,
                                         const JetCategories* jetCategories):
AnalyzerBase("events_", selectionStepsNoCategories, stepsForCategories, jetCategories)
{
    std::cout<<"--- Beginning setting up event yield histograms\n";
    std::cout<<"=== Finishing setting up event yield histograms\n\n";
}



void AnalyzerEventYields::bookHistos(const TString& step, std::map<TString, TH1*>& m_histogram)
{
    TString name;
    
    name = "weighted";
    m_histogram[name] = this->store(new TH1D(prefix_+name+step,"event yield;;# events",8,0,8));
    m_histogram[name]->Sumw2();
}



void AnalyzerEventYields::fillHistos(const RecoObjects&, const CommonGenObjects&,
                                     const TopGenObjects&, const HiggsGenObjects&,
                                     const KinRecoObjects&,
                                     const tth::RecoObjectIndices&, const tth::GenObjectIndices&,
                                     const tth::GenLevelWeights&, const tth::RecoLevelWeights&,
                                     const double& weight, const TString&,
                                     std::map<TString, TH1*>& m_histogram)
{
    TString name;
    
    name = "weighted";
    m_histogram[name]->Fill(1., weight);
}









// --------------------------- Methods for DyScalingHistograms ---------------------------------------------



AnalyzerDyScaling::AnalyzerDyScaling(const std::vector<TString>& selectionSteps, const TString& looseStep):
AnalyzerBase("dyScaling_", selectionSteps),
looseStep_(looseStep)
{
    std::cout<<"--- Beginning setting up Drell-Yan scaling histograms\n";
    if(std::find(selectionSteps_.begin(), selectionSteps_.end(), looseStep_) == selectionSteps_.end()){
        std::cerr<<"ERROR in constructor of DyScalingHistograms!"
                 <<"Could not find in selection steps the step specified for loose histogram: "<<looseStep_
                 <<"\n...break\n"<<std::endl;
        exit(987);
    }
    std::cout<<"=== Finishing setting up Drell-Yan scaling histograms\n\n";
}



void AnalyzerDyScaling::bookHistos(const TString& step, std::map<TString, TH1*>& m_histogram)
{
    const TString looseStep = tth::stepName(looseStep_) + "zWindow";
    if(step == looseStep){
        m_histogram["h_loose"] = this->bookHisto(m_histogram["h_loose"], prefix_+"Looseh1");
    }
    
    if(step.Contains("zWindow")){
        m_histogram["h_zWindow"] = this->bookHisto(m_histogram["h_zWindow"], prefix_+"Zh1"+step);
    }
    else{
        m_histogram["h_all"] = this->bookHisto(m_histogram["h_all"], prefix_+"Allh1"+step);
        m_histogram["h_zVeto"] = this->bookHisto(m_histogram["h_zVeto"], prefix_+"TTh1"+step);
        this->bookHistos(step + "zWindow", m_stepHistograms_[step + "zWindow"].m_histogram_);
    }
}



TH1* AnalyzerDyScaling::bookHisto(TH1* histo, const TString& name)
{
    histo = this->store(new TH1D(name,"Dilepton Mass; m_{ll}; events",40,0,400));
    return histo;
}



void AnalyzerDyScaling::fillHistos(const RecoObjects& recoObjects, const CommonGenObjects&,
                                   const TopGenObjects&, const HiggsGenObjects&,
                                   const KinRecoObjects&,
                                   const tth::RecoObjectIndices& recoObjectIndices, const tth::GenObjectIndices&,
                                   const tth::GenLevelWeights&, const tth::RecoLevelWeights&,
                                   const double& weight, const TString& step,
                                   std::map<TString, TH1*>& m_histogram)
{
    const int leadingLeptonIndex = recoObjectIndices.leadingLeptonIndex_;
    const int nLeadingLeptonIndex = recoObjectIndices.nLeadingLeptonIndex_;
    
    // FIXME: should use one common function in HiggsAnalysis and here
    //bool hasLeptonPair(false);
    if(leadingLeptonIndex!=-1 && nLeadingLeptonIndex!=-1){
        ;//hasLeptonPair = true;
    }
    else return;
    
    const LV dilepton = recoObjects.allLeptons_->at(leadingLeptonIndex) + recoObjects.allLeptons_->at(nLeadingLeptonIndex);
    const double dileptonMass = dilepton.M();
    const bool isZregion = dileptonMass>76. && dileptonMass<106.;
    
    
    // Fill histograms
    const TString looseStep = tth::stepName(looseStep_) + "zWindow";
    if(step == looseStep) m_stepHistograms_[looseStep].m_histogram_["h_loose"]->Fill(dileptonMass, weight);
    
    if(step.Contains("zWindow")){
        m_histogram["h_zWindow"]->Fill(dileptonMass, weight);
        TString stepNoZ(step);
        stepNoZ.ReplaceAll("zWindow", "");
        m_stepHistograms_[stepNoZ].m_histogram_["h_all"]->Fill(dileptonMass, weight);
    }
    else if(!isZregion){
        m_histogram["h_zVeto"]->Fill(dileptonMass, weight);
        m_histogram["h_all"]->Fill(dileptonMass, weight);
    }
}









// --------------------------- Methods for HfFracScalingHistograms ---------------------------------------------



AnalyzerHfFracScaling::AnalyzerHfFracScaling(const std::vector<TString>& selectionSteps):
AnalyzerBase("hfFracScaling_", selectionSteps)
{
    std::cout<<"--- Beginning setting up Heavy-Flavour Fraction scaling histograms\n";
    std::cout<<"=== Finishing setting up Heavy-Flavour Fraction scaling histograms\n\n";
}



void AnalyzerHfFracScaling::bookHistos(const TString& step, std::map<TString, TH1*>& m_histogram)
{
    TString name = "btag_multiplicity";
    m_histogram[name] = this->store(new TH1D(prefix_+name+step, "B-tagged jet multiplicity; N b-tags; events",10,0,10));
    name = "btag_discriminatorSum";
    m_histogram[name] = this->store(new TH1D(prefix_+name+step, "Sum of b-tag discriminants; Sum of b-tags; # events",30,0.,15.));
}



void AnalyzerHfFracScaling::fillHistos(const RecoObjects& recoObjects, const CommonGenObjects&,
                                   const TopGenObjects&, const HiggsGenObjects&,
                                   const KinRecoObjects&,
                                   const tth::RecoObjectIndices& recoObjectIndices, const tth::GenObjectIndices&,
                                   const tth::GenLevelWeights&, const tth::RecoLevelWeights&,
                                   const double& weight, const TString&,
                                   std::map<TString, TH1*>& m_histogram)
{
    const std::vector<int>& jetIndices = recoObjectIndices.jetIndices_;
    const int nBJets = recoObjectIndices.bjetIndices_.size();
    const std::vector<double>& jetsBtagDiscriminant = *recoObjects.jetBTagCSV_;
    double bTag_sum = 0.;
    for(size_t jetId = 0; jetId < jetIndices.size(); ++jetId) {
        bTag_sum += jetsBtagDiscriminant.at(jetId);
    }
    m_histogram["btag_multiplicity"]->Fill(nBJets, weight);
    m_histogram["btag_discriminatorSum"]->Fill(bTag_sum, weight);
}







