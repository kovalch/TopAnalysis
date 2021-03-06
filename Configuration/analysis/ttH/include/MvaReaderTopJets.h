#ifndef MvaReaderTopJets_h
#define MvaReaderTopJets_h

class TString;
namespace TMVA{
    class Reader;
}

#include "MvaReaderBase.h"

class MvaVariablesBase;





/// Class for reading MVA weights for assignment of top jets from file,
/// based on set of MVA input variables per event
class MvaReaderTopJets : public MvaReaderBase{
    
public:
    
    /// Constructor which sets MVA weights and creating TMVA Reader
    MvaReaderTopJets(const TString& mvaMethod);
    
    /// Destructor
    ~MvaReaderTopJets(){};
    
    
    
private:
    
    /// Set the MVA input variables for the MVA reader
    virtual void bookVariables(TMVA::Reader* const mvaWeightsReader, MvaVariablesBase*& mvaVariables)const;
    
    /// Read the MVA input variables into the pointer associated to the MVA reader
    virtual void readVariables(MvaVariablesBase* const mvaVariables, const MvaVariablesBase* const mvaVariablesTmp)const;
};







#endif







