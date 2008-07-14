#include "TopAnalysis/TopAnalyzer/plugins/IsolationAnalyzer.h"
#include "DataFormats/PatCandidates/interface/MET.h"
//#include "DataFormats/METReco/interface/MET.h"
//#include "DataFormats/METReco/interface/METCollection.h"
//#include "DataFormats/METReco/interface/METFwd.h"
//#include "DataFormats/METReco/interface/CaloMETCollection.h"
//#include "DataFormats/METReco/interface/CaloMET.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "AnalysisDataFormats/TopObjects/interface/TtGenEvent.h"

using std::cout;
using std::endl;
using reco::GenParticle;
using edm::LogInfo;

IsolationAnalyzer::IsolationAnalyzer(const edm::ParameterSet& cfg) :
	muons_(cfg.getParameter<edm::InputTag>("muons")),
			met_(cfg.getParameter<edm::InputTag>("missingEt")),
			ttgen_(cfg.getParameter<edm::InputTag>("genEvent")),
			jets_(cfg.getParameter<edm::InputTag>("jets")),
			ptBins_(cfg.getParameter<std::vector<double> >("ptBins")) {
	edm::Service<TFileService> fs;
	if ( !fs) {
		throw edm::Exception( edm::errors::Configuration,
				"TFile Service is not registered in cfg file" );
	}

	//for each ptBin new IsolationMonitor
	isomon_ = new IsolationMonitor();
	for (unsigned int x=0; x< ptBins_.size()-1; x++) {
		std::stringstream had, semi;
		double t = ptBins_.at(x);
		had << "thad_" << t;
		semi << "tsemi_" <<t;
		IsolationMonitor *temph = new IsolationMonitor(had.str());
		IsolationMonitor *temps = new IsolationMonitor(semi.str());
		hmonitors_.push_back(temph);
		smonitors_.push_back(temps);
	}
	thadpt_ = fs->make<TH1F>("hadrTopPt", "hadrTopPt", 100, 0., 600.);
	tleppt_ = fs->make<TH1F>("leprTopPt", "leprTopPt", 100, 0., 600.);
	hcaloCorr_ = fs->make<TH1F>("hadTopCaloCorr", "hadTopCaloCorr",
			ptBins_.size()-1, 0., ptBins_.size()-1*1.0);
	lcaloCorr_ = fs->make<TH1F>("lepTopCaloCorr", "lepTopCaloCorr",
			ptBins_.size()-1, 0., ptBins_.size()-1*1.0);
	htrackCorr_ = fs->make<TH1F>("hadTopTrackCorr", "hadTopTrackCorr",
			ptBins_.size()-1, 0., ptBins_.size()-1*1.0);
	ltrackCorr_ = fs->make<TH1F>("lepTopTrackCorr", "lepTopTrackCorr",
			ptBins_.size()-1, 0., ptBins_.size()-1*1.0);
	minDPhiMETJet_ = fs->make<TH1F>("minDeltaPhiMETJets", "minDeltaPhiMETJets",
			100, 0., 4.);
	dPhiMETjet1_ = fs->make<TH1F>("deltaPhiMetJet1", "deltaPhiMetJet1", 80, -4.,
			4.);
	dPhiMETjet2_ = fs->make<TH1F>("deltaPhiMetJet2", "deltaPhiMetJet2", 80, -4.,
			4.);
	dPhiMETjet3_ = fs->make<TH1F>("deltaPhiMetJet3", "deltaPhiMetJet3", 80, -4.,
			4.);
	dPhiMETjet4_ = fs->make<TH1F>("deltaPhiMetJet4", "deltaPhiMetJet4", 80, -4.,
			4.);
	dPhiMETmuon_ = fs->make<TH1F>("deltaPhiMetleadingMuon", "deltaPhiMetMuon",
			80, -4., 4.);
}

IsolationAnalyzer::~IsolationAnalyzer() {
}

void IsolationAnalyzer::analyze(const edm::Event& evt,
		const edm::EventSetup& setup) {

	//	const reco::MET *met;
//	const reco::CaloMET *met;
	const pat::MET *met;
	// Get Reconstructed MET
//	edm::Handle<reco::CaloMETCollection> hmetcol;
	edm::Handle<std::vector<pat::MET> > metH;
	evt.getByLabel(met_, metH);
//	const reco::CaloMETCollection *metcol = hmetcol.product();
	met = &(*metH)[0];
	

	//get muons
	//	edm::Handle<TopMuonCollection> muons;
	//	evt.getByLabel(muons_, muons);

	edm::Handle<std::vector<pat::Muon> > muons;
	evt.getByLabel(muons_, muons);

	//the event
	edm::Handle<TtGenEvent> genEvt;
	evt.getByLabel(ttgen_, genEvt);

	edm::Handle<double> weightHandle;
	evt.getByLabel("weight", "weight", weightHandle);

	double weight = *weightHandle;
	LogInfo("ControlOutput") << "weight:  " << weight << endl;

	edm::Handle<TopJetCollection> jets;
	evt.getByLabel("selectedLayer1TopJets", jets);

	TtGenEvent event = *genEvt;
	//	cout << "semi? : " << event.isSemiLeptonic() << endl;
	const reco::GenParticle* thad = event.hadronicDecayTop();
	const reco::GenParticle* tlep = event.leptonicDecayTop();

	if (tlep) {
		tleppt_->Fill(tlep->pt(), weight);
		//		cout << "tl pt: " << tlep->pt() << endl;		
	}

	if (thad) {
		thadpt_->Fill(thad->pt(), weight);
		//		cout << "th pt: " << thad->pt() << endl;
	}

	int size = muons->size();
	//	cout <<"suize : " << size << endl;
	double dp1, dp2, dp3, dp4 = 0;
	if (jets->size() < 4) {
		TopJetCollection::const_iterator jet = jets->begin();
		dp1 = deltaPhi(met->phi(), jet->phi());
		cout << "1st jet-met dPhi: " << dp1 << endl;

		++jet;
		dp2 = deltaPhi(met->phi(), jet->phi());
		cout << "2nd jet-met dPhi: " << dp2 << endl;

		++jet;
		dp3 = deltaPhi(met->phi(), jet->phi());
		cout << "3rd jet-met dPhi: " << dp3 << endl;

		++jet;
		dp4 = deltaPhi(met->phi(), jet->phi());
		cout << "4st jet-met dPhi: " << dp4 << endl;
	}
	double mindp = 0;
	mindp = min(dp1, dp2);
	mindp = min(mindp, dp3);
	mindp = min(mindp, dp4);

	minDPhiMETJet_->Fill(mindp, weight);
	dPhiMETjet1_->Fill(dp1, weight);
	dPhiMETjet2_->Fill(dp2, weight);
	dPhiMETjet3_->Fill(dp3, weight);
	dPhiMETjet4_->Fill(dp4, weight);
	for (int i = 0; i < size; ++i) {
		pat::Muon mu = (pat::Muon)(* muons)[i];
		isomon_->fill(mu, *met, weight);
		if (i == 0)
			dPhiMETmuon_->Fill(deltaPhi(mu.phi(), met->phi()));
		//in bins:
		for (unsigned int i=0; i < ptBins_.size()-1; i++) {
			if (thad && tlep) {
				if (thad->pt() >= ptBins_[i] && thad->pt() < ptBins_[i+1])
					hmonitors_[i]->fill(mu, *met, weight);
				if (tlep->pt() >= ptBins_[i] && tlep->pt() < ptBins_[i+1])
					smonitors_[i]->fill(mu, *met, weight);
			}
		}
		//TODO: find a way to get trackIsolation and caloIsolation
		LogInfo("ControlOutput") << "trackIso: " << mu.trackIso() << endl;
		LogInfo("ControlOutput") << "caloIso: " << mu.caloIso() << endl;
	}
	LogInfo("ControlOutput") << "MET: " << met->pt() << endl;

}

void IsolationAnalyzer::beginJob(const edm::EventSetup&) {

}

void IsolationAnalyzer::endJob() {

	isomon_->printCorrelation();
	cout << smonitors_.size() << endl;
	for (unsigned int x = 0; x< smonitors_.size(); x++) {
		hcaloCorr_->SetBinContent(x+1,
				hmonitors_[x]->getCaloCorrelationFactor());
		lcaloCorr_->SetBinContent(x+1,
				smonitors_[x]->getCaloCorrelationFactor());
		htrackCorr_->SetBinContent(x+1,
				hmonitors_[x]->getTrackCorrelationFactor());
		ltrackCorr_->SetBinContent(x+1,
				smonitors_[x]->getTrackCorrelationFactor());

		std::stringstream xlabel;
		xlabel << ptBins_.at(x) << "-" << ptBins_.at(x+1);
		hcaloCorr_->GetXaxis()->SetBinLabel(x+1, xlabel.str().c_str());
		lcaloCorr_->GetXaxis()->SetBinLabel(x+1, xlabel.str().c_str());
		htrackCorr_->GetXaxis()->SetBinLabel(x+1, xlabel.str().c_str());
		ltrackCorr_->GetXaxis()->SetBinLabel(x+1, xlabel.str().c_str());

		smonitors_[x]->printCorrelation();
		hmonitors_[x]->printCorrelation();
	}
}

