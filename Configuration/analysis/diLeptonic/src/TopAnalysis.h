#ifndef TopAnalysis_h
#define TopAnalysis_h

#include "AnalysisBase.h"

class TopAnalysis : public AnalysisBase
{
    
    // Histograms
    TH2 *h_GenRecoLeptonpT,*h_GenRecoAntiLeptonpT,*h_GenRecoLeptonEta,*h_GenRecoAntiLeptonEta, *h_GenRecoLLBarMass, *h_GenRecoLLBarpT;
    TH2 *h_GenRecoBJetpT,*h_GenRecoAntiBJetpT, *h_GenRecoBJetEta,*h_GenRecoAntiBJetEta, *h_GenRecoBJetRapidity, *h_GenRecoAntiBJetRapidity;//, *h_GenRecoBJetE, *h_GenRecoAntiBJetE;;
    TH2 *h_GenRecoToppT,*h_GenRecoAntiToppT,*h_GenRecoTopRapidity,*h_GenRecoAntiTopRapidity, *h_GenRecoTTBarMass, *h_GenRecoTTBarpT, *h_GenRecoTTBarRapidity;
    TH2 *h_GenRecoMet;
    
    TH1 *h_NJetMatching;

    TH1D *TTh1_postZcut, *Allh1_postZcut, *Zh1_postZcut;
    TH1D *TTh1_post2jets, *Allh1_post2jets, *Zh1_post2jets;
    TH1D *TTh1_postMET, *Allh1_postMET, *Zh1_postMET;
    TH1D *TTh1_post1btag, *Allh1_post1btag, *Zh1_post1btag;
    TH1D *TTh1_postKinReco, *Allh1_postKinReco, *Zh1_postKinReco;
    
    TH1 *Looseh1, *Allh1, *Zh1, *TTh1, *h_GenAll, *h_jetMulti, *h_jetMulti_noBTag,
      *h_jetMulti_diLep, *h_BjetMulti, *h_BjetMulti_noBTag,*h_jetMultiXSec,*h_jetMultiAll, 
         *h_jetMultiNoPU, *h_jetMultiVisTop, *h_VisGenAll, *h_diLepMassFull, 
         *h_diLepMassFull_fullSel;

    TH1 *h_HypTTBarMass, *h_HypTTBarRapidity, *h_HypTTBarpT;
    TH1 *h_HypLLBarMass, *h_HypLLBarpT;
    TH1 *h_HypMet;

    TH1 *h_VisGenTTBarMass,*h_VisGenTTBarRapidity,*h_VisGenTTBarpT;
    TH1 *h_VisGenTopRapidity,*h_VisGenAntiTopRapidity;
    TH1 *h_VisGenLLBarMass,*h_VisGenLLBarpT;
    TH1 *h_VisGenMet;

    TH1 *h_RecoTTBarMass, *h_RecoTTBarRapidity,*h_RecoTTBarpT;
    TH1 *h_RecoToppT,*h_RecoAntiToppT,*h_RecoTopRapidity,*h_RecoAntiTopRapidity;
    TH1 *h_RecoLLBarMass, *h_RecoLLBarpT;
    TH1 *h_RecoLeptonpT,*h_RecoAntiLeptonpT,*h_RecoLeptonEta,*h_RecoAntiLeptonEta;
    TH1 *h_RecoBJetpT,*h_RecoAntiBJetpT, *h_RecoBJetRapidity,*h_RecoAntiBJetRapidity,*h_RecoBJetEta,*h_RecoAntiBJetEta;
    TH1 *h_RecoMet;
    
    TH2 *h_GenRecoHT;
    TH1 *h_VisGenHT, *h_HypHT, *h_RecoHT;

    TH1 *h_vertMulti, *h_vertMulti_noPU, *h_MET;

    TH1 *h_jetpT,*h_jetHT;
    TH1 *h_MuonpT, *h_MuonEta;
    TH1 *h_ElectronpT, *h_ElectronEta;
    TH1 *h_LeptonpT, *h_LeptonEta;
    TH1 *h_AntiLeptonpT, *h_AntiLeptonEta;
    TH1 *h_LeptonpT_diLep, *h_LeptonEta_diLep;
    TH1 *h_AntiLeptonpT_diLep, *h_AntiLeptonEta_diLep;

    TH1 *h_MuonpT_postMETcut, *h_MuonEta_postMETcut;
    TH1 *h_ElectronpT_postMETcut, *h_ElectronEta_postMETcut;
    TH1 *h_LeptonpT_postMETcut, *h_LeptonEta_postMETcut;
    TH1 *h_AntiLeptonpT_postMETcut, *h_AntiLeptonEta_postMETcut;
    
    TH1 *h_leptonPtBeforeKinReco, *h_leptonEtaBeforeKinReco;
    TH1 *h_leptonPtAfterKinReco, *h_leptonEtaAfterKinReco;
    TH1 *h_METBeforeKinReco, *h_METAfterKinReco;
    TH1 *h_bjetetaBeforeKinReco, *h_bjetetaAfterKinReco;
    
    TH1 *h_HypAntiToppT, *h_HypAntiTopEta, *h_HypAntiTopMass,*h_HypAntiTopRapidity;
    TH1 *h_HypToppT, *h_HypTopEta,*h_HypTopMass, *h_HypTopRapidity;
    
    TH1 *h_HypNeutrinopT, *h_HypAntiNeutrinopT;
    TH1 *h_RecoNeutrinopT, *h_RecoAntiNeutrinopT;
    TH1 *h_VisGenNeutrinopT, *h_VisGenAntiNeutrinopT;
    TH2 *h_GenRecoNeutrinopT, *h_GenRecoAntiNeutrinopT;
    
    TH1 *h_HypAntiBJetpT, *h_HypAntiBJetEta, *h_HypAntiBJetRapidity;
    TH1 *h_HypBJetpT, *h_HypBJetEta, *h_HypBJetRapidity;

    TH1 *h_HypAntiLeptonpT, *h_HypAntiLeptonEta;
    TH1 *h_HypLeptonpT, *h_HypLeptonEta;

    TH1 *h_step3, *h_step4, *h_step5,*h_step6,*h_step7,*h_step8,*h_step9;

    TH1 *h_VisGenAntiToppT, *h_VisGenAntiTopEta;
    TH1 *h_VisGenToppT, *h_VisGenTopEta;

    TH1 *h_VisGenAntiBJetpT, *h_VisGenAntiBJetEta, *h_VisGenAntiBJetRapidity;
    TH1 *h_VisGenBJetpT, *h_VisGenBJetEta, *h_VisGenBJetRapidity;

    TH1 *h_VisGenAntiBQuarkpT, *h_VisGenAntiBQuarkEta, *h_VisGenAntiBQuarkRapidity;
    TH1 *h_VisGenBQuarkpT, *h_VisGenBQuarkEta, *h_VisGenBQuarkRapidity;

    TH1 *h_VisGenAntiLeptonpT, *h_VisGenAntiLeptonEta;
    TH1 *h_VisGenLeptonpT, *h_VisGenLeptonEta;

    TH2 *h_GenRecoLLBarDPhi, *h_GenRecoLeptonantiBjetMass, *h_GenRecoAntiLeptonBjetMass, *h_GenRecoJetMult;
    TH1 *h_VisGenLLBarDPhi,  *h_VisGenLeptonantiBjetMass,  *h_VisGenAntiLeptonBjetMass,  *h_VisGenJetMult;
    TH1 *h_HypLLBarDPhi,     *h_HypLeptonantiBjetMass,     *h_HypAntiLeptonBjetMass,     *h_HypJetMult;
    TH1 *h_RecoLLBarDPhi,    *h_RecoLeptonantiBjetMass,    *h_RecoAntiLeptonBjetMass,    *h_RecoJetMult;

    TH1 *h_HypToppTLead,    *h_HypToppTNLead,    *h_HypTopRapidityLead, *h_HypTopRapidityNLead, *h_HypTopMassLead, *h_HypTopMassNLead;
    TH1 *h_HypLeptonpTLead, *h_HypLeptonpTNLead, *h_HypLeptonEtaLead,   *h_HypLeptonEtaNLead;
    TH1 *h_HypBJetpTLead,   *h_HypBJetpTNLead,   *h_HypBJetEtaLead,     *h_HypBJetEtaNLead;

    TH1 *h_RecoToppTLead,    *h_RecoToppTNLead,    *h_RecoTopRapidityLead, *h_RecoTopRapidityNLead, *h_RecoTopMassLead, *h_RecoTopMassNLead;
    TH1 *h_RecoLeptonpTLead, *h_RecoLeptonpTNLead, *h_RecoLeptonEtaLead,   *h_RecoLeptonEtaNLead;
    TH1 *h_RecoBJetpTLead,   *h_RecoBJetpTNLead,   *h_RecoBJetEtaLead,     *h_RecoBJetEtaNLead;

    TH1 *h_VisGenToppTLead,    *h_VisGenToppTNLead,    *h_VisGenTopRapidityLead, *h_VisGenTopRapidityNLead, *h_VisGenTopMassLead, *h_VisGenTopMassNLead;
    TH1 *h_VisGenLeptonpTLead, *h_VisGenLeptonpTNLead, *h_VisGenLeptonEtaLead,   *h_VisGenLeptonEtaNLead;
    TH1 *h_VisGenBJetpTLead,   *h_VisGenBJetpTNLead,   *h_VisGenBJetEtaLead,     *h_VisGenBJetEtaNLead;

    TH2 *h_GenRecoToppTLead,    *h_GenRecoToppTNLead,    *h_GenRecoTopRapidityLead, *h_GenRecoTopRapidityNLead, *h_GenRecoTopMassLead, *h_GenRecoTopMassNLead;
    TH2 *h_GenRecoLeptonpTLead, *h_GenRecoLeptonpTNLead, *h_GenRecoLeptonEtaLead,   *h_GenRecoLeptonEtaNLead;
    TH2 *h_GenRecoBJetpTLead,   *h_GenRecoBJetpTNLead,   *h_GenRecoBJetEtaLead,     *h_GenRecoBJetEtaNLead;

    
//     //Begin: Plots for Carmen
//     TH1 *h_RecoLeadingJetpT,    *h_RecoNLeadingJetpT,    *h_RecoLeadingJetEta,    *h_RecoNLeadingJetEta;
//     TH1 *h_HypLeadingJetpT,     *h_HypNLeadingJetpT,     *h_HypLeadingJetEta,     *h_HypNLeadingJetEta;
//     TH2 *h_GenRecoLeadingJetpT, *h_GenRecoLeadingJetEta, *h_GenRecoNLeadingJetpT, *h_GenRecoNLeadingJetEta;
//     TH1 *h_VisGenLeadingJetpT,  *h_VisGenLeadingJetEta,  *h_VisGenNLeadingJetpT,  *h_VisGenNLeadingJetEta;
// 
//     //Begin: Plots for Carmen
//     TH1 *h_RecoExtraJetpT,  *h_HypExtraJetpT, *h_VisGenExtraJetpT, *h_RecoExtraJetEta, *h_HypExtraJetEta, *h_VisGenExtraJetEta;
//     TH1 *h_RecoExtraJetpT2, *h_HypExtraJetpT2, *h_VisGenExtraJetpT2, *h_RecoExtraJetEta2, *h_HypExtraJetEta2, *h_VisGenExtraJetEta2;
//     TH1 *h_RecoExtraJetpT3, *h_HypExtraJetpT3, *h_VisGenExtraJetpT3, *h_RecoExtraJetEta3, *h_HypExtraJetEta3, *h_VisGenExtraJetEta3;
//     TH1 *h_RecoExtraJetpT4, *h_HypExtraJetpT4, *h_VisGenExtraJetpT4, *h_RecoExtraJetEta4, *h_HypExtraJetEta4, *h_VisGenExtraJetEta4;
//     TH2 *h_GenRecoExtraJetpT, *h_GenRecoExtraJetEta, *h_GenRecoExtraJetpT2, *h_GenRecoExtraJetEta2, *h_GenRecoExtraJetpT3, *h_GenRecoExtraJetEta3, *h_GenRecoExtraJetpT4, *h_GenRecoExtraJetEta4;
// 
//     TH1 *h_RecoJetMultpt40, *h_HypJetMultpt40, *h_VisGenJetMultpt40, *h_RecoJetMultpt60, *h_HypJetMultpt60, *h_VisGenJetMultpt60;
//     TH2 *h_GenRecoJetMultpt40, *h_GenRecoJetMultpt60, *h_GenRecoJetMultQ0, *h_GenRecoJetMultTotal;
//     //End: Plots for Carmen
    

    // ++++ Control Plots ++++
    TH1 *h_AllLeptonEta_step0, *h_AllLeptonpT_step0, *h_AllJetsEta_step0, *h_AllJetspT_step0;
    TH1 *h_AllLeptonEta_step1, *h_AllLeptonpT_step1, *h_AllJetsEta_step1, *h_AllJetspT_step1;
    TH1 *h_AllLeptonEta_step2, *h_AllLeptonpT_step2, *h_AllJetsEta_step2, *h_AllJetspT_step2;
    TH1 *h_AllLeptonEta_step3, *h_AllLeptonpT_step3, *h_AllJetsEta_step3, *h_AllJetspT_step3;
    TH1 *h_AllLeptonEta_step4, *h_AllLeptonpT_step4, *h_AllJetsEta_step4, *h_AllJetspT_step4;
    TH1 *h_AllLeptonEta_step5, *h_AllLeptonpT_step5, *h_AllJetsEta_step5, *h_AllJetspT_step5;
    TH1 *h_AllLeptonEta_step6, *h_AllLeptonpT_step6, *h_AllJetsEta_step6, *h_AllJetspT_step6;
    TH1 *h_AllLeptonEta_step7, *h_AllLeptonpT_step7, *h_AllJetsEta_step7, *h_AllJetspT_step7;
    TH1 *h_AllLeptonEta_step8, *h_AllLeptonpT_step8, *h_AllJetsEta_step8, *h_AllJetspT_step8;
    TH1 *h_LeptonEta_step0, *h_LeptonpT_step0, *h_JetsEta_step0, *h_JetspT_step0;
    TH1 *h_LeptonEta_step1, *h_LeptonpT_step1, *h_JetsEta_step1, *h_JetspT_step1;
    TH1 *h_LeptonEta_step2, *h_LeptonpT_step2, *h_JetsEta_step2, *h_JetspT_step2;
    TH1 *h_LeptonEta_step3, *h_LeptonpT_step3, *h_JetsEta_step3, *h_JetspT_step3;
    TH1 *h_LeptonEta_step4, *h_LeptonpT_step4, *h_JetsEta_step4, *h_JetspT_step4;
    TH1 *h_LeptonEta_step5, *h_LeptonpT_step5, *h_JetsEta_step5, *h_JetspT_step5;
    TH1 *h_LeptonEta_step6, *h_LeptonpT_step6, *h_JetsEta_step6, *h_JetspT_step6;
    TH1 *h_LeptonEta_step7, *h_LeptonpT_step7, *h_JetsEta_step7, *h_JetspT_step7;
    TH1 *h_LeptonEta_step8, *h_LeptonpT_step8, *h_JetsEta_step8, *h_JetspT_step8;
    TH1 *h_LeptonMult_step0, *h_JetsMult_step0, *h_BJetsMult_step0;
    TH1 *h_LeptonMult_step1, *h_JetsMult_step1, *h_BJetsMult_step1;
    TH1 *h_LeptonMult_step2, *h_JetsMult_step2, *h_BJetsMult_step2;
    TH1 *h_LeptonMult_step3, *h_JetsMult_step3, *h_BJetsMult_step3;
    TH1 *h_LeptonMult_step4, *h_JetsMult_step4, *h_BJetsMult_step4;
    TH1 *h_LeptonMult_step5, *h_JetsMult_step5, *h_BJetsMult_step5;
    TH1 *h_LeptonMult_step6, *h_JetsMult_step6, *h_BJetsMult_step6;
    TH1 *h_LeptonMult_step7, *h_JetsMult_step7, *h_BJetsMult_step7;
    TH1 *h_LeptonMult_step8, *h_JetsMult_step8, *h_BJetsMult_step8;    

    
public:
    
    virtual void Begin(TTree*);
    virtual void SlaveBegin(TTree*);
    virtual void SlaveTerminate();
    virtual void Terminate();
    virtual Bool_t Process(Long64_t entry);
    virtual void SetClosureTest(TString closure, double slope);
    
private:
    double calculateClosureTestWeight();
    
    ClassDef(TopAnalysis, 0);
};

#endif


