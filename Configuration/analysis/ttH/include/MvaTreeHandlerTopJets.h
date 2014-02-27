#ifndef MvaTreeHandlerTopJets_h
#define MvaTreeHandlerTopJets_h

#include <vector>

class TString;
class TTree;

#include "MvaTreeHandlerBase.h"

class MvaVariablesBase;
class JetCategories;
class RecoObjects;
class CommonGenObjects;
class TopGenObjects;
class HiggsGenObjects;
class KinRecoObjects;
namespace tth{
    class RecoLevelWeights;
    class GenLevelWeights;
    class GenObjectIndices;
    class RecoObjectIndices;
}





/// Class for handling the trees of input variables for MVA,
/// trying to identify the jets coming from (anti)b's from (anti)tops
class MvaTreeHandlerTopJets : public MvaTreeHandlerBase{
    
public:
    
    /// Constructor for selection steps
    MvaTreeHandlerTopJets(const char* mvaInputDir,
                          const std::vector<TString>& selectionStepsNoCategories,
                          const std::vector<TString>& stepsForCategories =std::vector<TString>(),
                          const JetCategories* jetCategories =0);
    
    /// Destructor
    ~MvaTreeHandlerTopJets(){}
    
    
    
private:
    
    /// Fill all variables for given selection step
    virtual void fillVariables(const RecoObjects& recoObjects, const CommonGenObjects& commonGenObjects,
                               const TopGenObjects& topGenObjects, const HiggsGenObjects& higgsGenObjects,
                               const KinRecoObjects& kinRecoObjects,
                               const tth::RecoObjectIndices& recoObjectIndices, const tth::GenObjectIndices& genObjectIndices,
                               const tth::GenLevelWeights& genLevelWeights, const tth::RecoLevelWeights& recoLevelWeights,
                               const double& weight, const TString& step,
                               std::vector<MvaVariablesBase*>& mvaVariables);
    
    /// Create and fill branches for TTree holding the input variables for MVA
    virtual void createAndFillBranches(TTree* tree, const std::vector<MvaVariablesBase*>& v_mvaVariables);
    
    /// Import all branches from TTree
    virtual void importBranches(TTree* tree, std::vector<MvaVariablesBase*>& mvaVariables);
};





#endif







