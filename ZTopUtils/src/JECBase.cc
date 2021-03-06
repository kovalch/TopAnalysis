#include "../interface/JECBase.h"
#include <stdexcept>
#include "unistd.h"

namespace ztop {

void JECBase::copyFrom(const ztop::JECBase & old) {
	totalunc_ = 0;
	is2012_ = old.is2012_;
	if (!old.pathToFile_.empty())
		setFile(old.pathToFile_, true); // JECUncertainties... don't provide a copy contructor..
	noupdown_ = old.noupdown_;
	sources_ = old.sources_;
}

JECBase::JECBase(const ztop::JECBase & old) {
	copyFrom(old);
}

JECBase & JECBase::operator =(const ztop::JECBase & old) {
	copyFrom(old);
	return *this;
}

JECBase::~JECBase() {

	if (totalunc_)
		delete totalunc_;
	for (unsigned int i = 0; i < vsrc_.size(); i++) {
		if (vsrc_.at(i))
			delete vsrc_.at(i);
	}

}

void JECBase::setFile(std::string pathToFile, bool quiet) {
	if (pathToFile.empty()) {
		std::cout << "JECBase::setFile: path empty!" << std::endl;
		std::exit (EXIT_FAILURE);
	}
	std::ifstream check_file(pathToFile.data());
	if (!check_file.good()) {
		std::cout << "JECBase::setFile: cannot open file!" << pathToFile
				<< std::endl;
		std::exit (EXIT_FAILURE);
	}
	if (!quiet)
		std::cout << "setting JEC uncertainties file to: " << pathToFile
		<< std::endl;
	pathToFile_ = pathToFile;

	//delete old JEC

	if (totalunc_)
		delete totalunc_;
	for (unsigned int i = 0; i < vsrc_.size(); i++) {
		if (vsrc_[i])
			delete vsrc_[i];
	}
	vsrc_.clear();

	const int nsrc = 16;
	const char* srcnames[nsrc] = { "Absolute", //0                         //uncorr
			"HighPtExtra",    //1
			"SinglePion",     //2
			"Flavor",         //3
			"Time",           //4
			"RelativeJEREC1", //5
			"RelativeJEREC2", //6
			"RelativeJERHF",  //7
			"RelativeStatEC2",  //8
			"RelativeStatHF", //9
			"RelativeFSR",    //10
			"PileUpDataMC",   //11                         //uncorr
			"PileUpOOT",      //12
			"PileUpPt",       //13
			"PileUpBias",     //14                         //uncorr
			"PileUpJetRate" }; //15

	const int nsrc12 = 41;
	const char* srcnames12[nsrc12] = {
			"AbsoluteStat", //0
			"AbsoluteScale", //1
			"AbsoluteFlavMap", //2
			"AbsoluteMPFBias", //3
			"HighPtExtra",     //4
			"SinglePionECAL",  //5
			"SinglePionHCAL",  //6
			"FlavorQCD", 		//7
			"Time",				//8
			"RelativeJEREC1", 	//9
			"RelativeJEREC2", 	//10
			"RelativeJERHF",	//11
			"RelativePtBB",		//12
			"RelativePtEC1", 	//13
			"RelativePtEC2", 	//14
			"RelativePtHF", 	//15
			"RelativeFSR",		//16
			"RelativeStatEC2", 	//17
			"RelativeStatHF",	//18
			"PileUpDataMC",		//19
			"PileUpPtBB", 		//20
			"PileUpPtEC", 		//21
			"PileUpPtHF",		//22
			"PileUpBias",		//23
			"SubTotalPileUp",	//24
			"SubTotalRelative",	//25
			"SubTotalPt",		//26
			"SubTotalMC",		//27
			"Total",			//28
			"TotalNoFlavor",	//29
			"FlavorZJet",		//30
			"FlavorPhotonJet",	//31
			"FlavorPureGluon",	//32
			"FlavorPureQuark",	//33
			"FlavorPureCharm",	//34
			"FlavorPureBottom", //35
			"CorrelationGroupMPFInSitu", //36
			"CorrelationGroupIntercalibration", //37
			"CorrelationGroupbJES", //38
			"CorrelationGroupFlavor", //39
			"CorrelationGroupUncorrelated",//40
	};

	if (is2012_) {
		for (int isrc = 0; isrc < nsrc12; isrc++) {
			const char *name = srcnames12[isrc];
			bool got = true;
			JetCorrectionUncertainty *unc = 0;
			try {
				unc = new JetCorrectionUncertainty(
						JetCorrectorParameters(pathToFile.data(), name));
			}
			catch(std::runtime_error &rte) {
				std::cout << "JECBase::setFile: Uncertainty for source " << name
						<< " not found! Skipping" << std::endl;
				got = false;
				sleep(2);
			}
			if (got)
				vsrc_.push_back(unc);
		}
	} else {
		for (int isrc = 0; isrc < nsrc; isrc++) {
			const char *name = srcnames[isrc];
			bool got = true;
			JetCorrectionUncertainty *unc = 0;
			try {
				unc = new JetCorrectionUncertainty(
						JetCorrectorParameters(pathToFile.data(), name));
			}
			catch(std::runtime_error &rte) {
				std::cout << "JECBase::setFile: Uncertainty for source " << name
						<< " not found! Skipping" << std::endl;
				got = false;
				sleep(2);
			}
			if (got)
				vsrc_.push_back(unc);
		}
	}
	totalunc_ = new JetCorrectionUncertainty(
			JetCorrectorParameters(pathToFile.data(), "Total"));
}

void JECBase::setSystematics(std::string set) {
	if (set == "up") {
		noupdown_ = 1;
		std::cout << "JECBase::setSystematics: Systematics set to: " << set
				<< std::endl;
	} else if (set == "down") {
		noupdown_ = -1;
		std::cout << "JECBase::setSystematics: Systematics set to: " << set
				<< std::endl;
	} else if (set == "no") {
		noupdown_ = 0;
		std::cout << "JECBase::setSystematics: Systematics set to: " << set
				<< std::endl;
	} else {
		std::cout << "JECBase::setSystematics: String " << set
				<< " not allowed. available options: up, down, no" << std::endl;
	}
}

void JECBase::applyJECUncertainties(float & pt, float& eta, float & phi, float& m) {

	if (noupdown_ == 0) // no variation
		return;

	if (!(totalunc_)) { // nothing set. exit?!?
		std::cout << "JECBase::applyJECUncertainties: no inputfile set, exit"
				<< std::endl;
		throw std::logic_error(
				"JECBase::applyJECUncertainties: no inputfile set, exit");
	}

	bool up = false;
	if (noupdown_ > 0)
		up = true;

	double dunc = 0;

	if (sources_.size() < 1) { //total
		totalunc_->setJetPt(pt);
		totalunc_->setJetEta(eta);
		dunc = totalunc_->getUncertainty(up);
	} else if (sources_.size() <= vsrc_.size()) {
		for (unsigned int i = 0; i < sources_.size(); i++) {
			if (sources_[i] < vsrc_.size()) { //for a spec source
				JetCorrectionUncertainty *unc = vsrc_[sources_[i]];
				unc->setJetPt(pt);
				unc->setJetEta(eta);
				double uncert = unc->getUncertainty(up);
				dunc = sqrt(dunc * dunc + uncert * uncert);
			} else {
				std::cout << "JECBase::applyJECUncertainties: source "
						<< sources_[i] << " doesn't exist." << std::endl;
			}
		}
	} else {
		std::cout
		<< "JECBase::applyJECUncertainties: too many sources; must be below "
		<< vsrc_.size() - 1 << "." << std::endl;
	}
	if (up){
		pt*=  (1 + dunc);
		m*=  (1 + dunc);
	}
	else{
		pt*=  (1 - dunc);
		m*=  (1 - dunc);
	}
}
}

