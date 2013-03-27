#include <iostream>
#include <fstream>

#include <TString.h>
#include <TFile.h>
#include <TTree.h>
#include <TProof.h>
#include <TSelector.h>
#include <TObjString.h>
#include <TChain.h>
#include <TH1.h>

#include "HiggsAnalysis.h"
#include "../../diLeptonic/src/utils.h"
#include "../../diLeptonic/src/PUReweighter.h"
#include "../../diLeptonic/src/CommandLineParameters.h"


//determine the path to the PU distribution files, depending on systematic
const std::string getPUPath(TString systematic) {
    std::string pu_path(CMSSW_BASE());
    if (systematic == "PU_UP") {
        pu_path.append("/src/TopAnalysis/TopUtils/data/Data_PUDist_12fb_sysUp.root");
        std::cout << "using pilup-up distribution\n";
    } else if (systematic == "PU_DOWN") {
        pu_path.append("/src/TopAnalysis/TopUtils/data/Data_PUDist_12fb_sysDown.root");
        std::cout << "using pilup-down distribution\n";
    } else {
        pu_path.append("/src/TopAnalysis/TopUtils/data/Data_PUDist_12fb.root");
        if (systematic != "") {
            std::cout << "Using Nominal PU distribution for " << systematic << " systematic!\n";
        }
    }
    return pu_path;
}


void load_HiggsAnalysis(TString validFilenamePattern, 
                   TString givenChannel, 
                   TString systematic, 
                   int dy
                   )
{   
    ifstream infile ("selectionList.txt");
    if (!infile.good()) { 
        std::cerr << "Error! Please check the selectionList.txt file!\n" << std::endl; 
        exit(773); 
    }
    
    HiggsAnalysis* selector = new HiggsAnalysis();
    PUReweighter* pu = new PUReweighter();
    pu->setMCDistrSum12("S10");
    pu->setDataTruePUInput(getPUPath(systematic).c_str());
    selector->SetPUReweighter(pu);

    int filecounter = 0;
    while(!infile.eof()){
        
        // Access nTuple input filename from selectionList
        TString filename;
        infile >> filename;
        if (filename == "" || filename[0] == '#') continue; //empty line? --> skip
        if (!filename.Contains(validFilenamePattern)) continue;
        std::cout << std::endl;
        std::cout << "PROCESSING File " << ++filecounter << " ("<< filename << ") from selectionList.txt" << std::endl;
        std::cout << std::endl;
        
        // Open nTuple file
        TFile file(filename);
        if (file.IsZombie()){
            std::cerr << "Cannot open " << filename << std::endl;
            return;
        }
        
        // Access information about samples, stored in the nTuples
        TObjString *channel_file = dynamic_cast<TObjString*>(file.Get("writeNTuple/channelName"));
        TObjString *systematics_from_file = dynamic_cast<TObjString*>(file.Get("writeNTuple/systematicsName"));
        TObjString *samplename = dynamic_cast<TObjString*>(file.Get("writeNTuple/sampleName"));
        TObjString *o_isSignal = dynamic_cast<TObjString*>(file.Get("writeNTuple/isSignal"));
        TObjString *o_isHiggsSignal = dynamic_cast<TObjString*>(file.Get("writeNTuple/isHiggsSignal"));
        TObjString *o_isMC = dynamic_cast<TObjString*>(file.Get("writeNTuple/isMC"));
        TH1* weightedEvents = dynamic_cast<TH1*>(file.Get("EventsBeforeSelection/weightedEvents"));
        if (!channel_file || !systematics_from_file || !o_isSignal || !o_isMC || !samplename) { 
            std::cout << "Error: info about sample missing!" << std::endl; 
            return;  
        }
        
        // Configure information about samples
        bool isSignal = o_isSignal->GetString() == "1";
        bool isMC = o_isMC->GetString() == "1";
        bool isHiggsSignal(false);
        if(o_isHiggsSignal && o_isHiggsSignal->GetString()=="1")isHiggsSignal = true;
        bool isHiggsInclusive(false);
        if(isHiggsSignal && samplename->GetString()=="ttbarhiggsinclusive")isHiggsInclusive = true;
        
        if (!isMC && systematic != "") {
            std::cout << "Sample is DATA, so not running again for systematic variation\n";
            continue;
        }
        
        //determine the channels to run over
        std::vector<TString> channels;
        //is the "mode" (=channel) given in the file?
        if (channel_file->GetString() != "") {
            channels.push_back(channel_file->GetString());
        } else {
            if (givenChannel != "") {
                channels.push_back(givenChannel);
            } else {
                channels.push_back("emu");
                channels.push_back("ee");
                channels.push_back("mumu");
            }
        }
        
        // Loop over channels and run selector
        for(const auto& channel : channels){
            
            // Set output file name
            TString outputfilename(filename);
            if (outputfilename.Contains('/')) {
                Ssiz_t last = outputfilename.Last('/');
                outputfilename = outputfilename.Data() + last + 1;
            }
            if (!outputfilename.BeginsWith(channel + "_")) outputfilename.Prepend(channel + "_");
            //outputfile is now channel_filename.root
            if (dy) {
                if (outputfilename.First("_dy") == kNPOS) { 
                    std::cerr << "DY variations must be run on DY samples!\n";
                    std::cerr << outputfilename << " must start with 'channel_dy'\n";
                    std::exit(1);
                }
                outputfilename.ReplaceAll("_dy", TString("_dy").Append(dy == 11 ? "ee" : dy == 13 ? "mumu" : "tautau"));
            }
            if(isHiggsInclusive)outputfilename.ReplaceAll("inclusive", "inclusiveOther");
            
            // Configure selector
            selector->SetBTagFile("");
            selector->SetChannel(channel);
            selector->SetSignal(isSignal);
            selector->SetHiggsSignal(isHiggsSignal);
            selector->SetMC(isMC);
            selector->SetTrueLevelDYChannel(dy);
            if (systematic == "") {
                selector->SetSystematic(systematics_from_file->GetString());
            } else {
                selector->SetSystematic(systematic);
            }
            selector->SetWeightedEvents(weightedEvents);
            selector->SetSamplename(samplename->GetString(), systematics_from_file->GetString());
            selector->SetOutputfilename(outputfilename);
            selector->SetRunViaTau(0);
            selector->SetHiggsInclusiveSample(isHiggsInclusive);
            selector->SetHiggsInclusiveSeparation(false);
            
            // Check whether nTuple can be found
            TTree *tree = dynamic_cast<TTree*>(file.Get("writeNTuple/NTuple"));
            if (!tree){
                std::cerr << "Error: Tree not found!\n";
                exit(854);
            }
            
            // Set up nTuple chain and run selector
            TChain chain("writeNTuple/NTuple");
            chain.Add(filename);
            // chain.SetProof(); //will work from 5.34 onwards
            chain.Process(selector);
            
            // For splitting of ttbarsignal in component with intermediate taus and without
            if(isSignal && !isHiggsSignal) {
                selector->SetRunViaTau(1);
                outputfilename.ReplaceAll("signalplustau", "bgviatau");
                selector->SetOutputfilename(outputfilename);
                chain.Process(selector);
            }
            
            // For splitting of ttH inclusive decay in H->bb and other decays
            if(isHiggsInclusive){
                selector->SetHiggsInclusiveSeparation(true);
                outputfilename.ReplaceAll("Other", "Bbbar");
                selector->SetOutputfilename(outputfilename);
                chain.Process(selector);
            }
        }
        file.Close();
    }
}

int main(int argc, char** argv) {
    CLParameter<std::string> opt_f("f", "Restrict to filename pattern, e.g. ttbar", false, 1, 1);
    CLParameter<std::string> opt_s("s", "Run with a systematic that runs on the nominal ntuples, e.g. 'PU_UP' or 'TRIG_DOWN'", false, 1, 1);
    CLParameter<std::string> opt_c("c", "Specify a certain channel (ee, emu, mumu). No channel specified = run on all channels", false, 1, 1,
            [](const std::string &ch){return ch == "" || ch == "ee" || ch == "emu" || ch == "mumu";});
    CLParameter<int> opt_dy("d", "Drell-Yan mode (11 for ee, 13 for mumu, 15 for tautau)", false, 1, 1,
            [](int dy){return dy == 11 || dy == 13 || dy == 15;});
                                         
    CLAnalyser::interpretGlobal(argc, argv);
    
    TString validFilenamePattern = opt_f.isSet() ? opt_f[0] : "";
    TString syst = opt_s.isSet() ? opt_s[0] : "";
    TString channel = opt_c.isSet() ? opt_c[0] : "";
    int dy = opt_dy.isSet() ? opt_dy[0] : 0;
    
//     TProof* p = TProof::Open(""); // not before ROOT 5.34
    load_HiggsAnalysis(validFilenamePattern, channel, syst, dy);
//     delete p;
}