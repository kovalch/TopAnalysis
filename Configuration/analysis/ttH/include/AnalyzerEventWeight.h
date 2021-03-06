#ifndef AnalyzerEventWeight_h
#define AnalyzerEventWeight_h

#include <vector>
#include <map>

class TString;
class TH1;

#include "AnalyzerBase.h"

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








/// Playground class, test here whatever you want to test
class AnalyzerEventWeight : public AnalyzerBase{
    
public:
    
    /// Constructor
    AnalyzerEventWeight(const std::vector<TString>& selectionStepsNoCategories,
                        const std::vector<TString>& stepsForCategories =std::vector<TString>(),
                        const JetCategories* jetCategories =0);
    
    /// Destructor
    ~AnalyzerEventWeight(){}
    
    
    
private:
    
    /// Book all histograms for given selection step
    virtual void bookHistos(const TString& step, std::map<TString, TH1*>& m_histogram);
    
    /// Fill all histograms for given selection step
    virtual void fillHistos(const RecoObjects& recoObjects, const CommonGenObjects& commonGenObjects,
                            const TopGenObjects& topGenObjects, const HiggsGenObjects& higgsGenObjects,
                            const KinRecoObjects& kinRecoObjects,
                            const tth::RecoObjectIndices& recoObjectIndices, const tth::GenObjectIndices& genObjectIndices,
                            const tth::GenLevelWeights& genLevelWeights, const tth::RecoLevelWeights& recoLevelWeights,
                            const double& weight, const TString& step,
                            std::map<TString, TH1*>& m_histogram);
};





#endif







