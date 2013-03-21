#include <iostream>
#include <fstream>
#include <TString.h>
#include <TFile.h>
#include <TTree.h>
#include <TProof.h>
#include <TSelector.h>
#include <TObjString.h>
#include "TopAnalysis.h"
#include "PUReweighter.h"
#include "CommandLineParameters.h"
#include "utils.h"

///determine the path to the PU distribution files, depending on systematic
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

const TString pdfDirName(int pdf_no) {
    TString result("PDF_");
    if (pdf_no == 0) result += "CENTRAL";
    else result += TString::Format("%d", (pdf_no+1)/2) + "_" + (pdf_no % 2 ? "UP" : "DOWN");
    return result;
}

void load_Analysis(TString validFilenamePattern, 
                   TString givenChannel, 
                   TString systematic,
                   int specific_PDF,
                   int dy,
                   TString closure,
                   double slope
                  )
{   
    ifstream infile ("selectionList.txt");
    if (!infile.good()) { 
        std::cerr << "Error! Please check the selectionList.txt file!\n\n"; 
        exit(773); 
    }
    
    AnalysisBase *selector = new TopAnalysis();
    PUReweighter *pu = new PUReweighter();
    pu->setMCDistrSum12("S10");
    pu->setDataTruePUInput(getPUPath(systematic).c_str());
    selector->SetPUReweighter(pu);

    int filecounter = 0;
    while(!infile.eof()){
        TString filename;
        infile >> filename;
        if (filename == "" || filename[0] == '#') continue; //empty line? --> skip
        if (!filename.Contains(validFilenamePattern)) continue;

        //channel selection for later BTag eff
        std::cout << std::endl;
        std::cout << "PROCESSING File " << ++filecounter << " ("<< filename << ") from selectionList.txt\n";
        std::cout << std::endl;

        TFile file(filename);
        if (file.IsZombie()) { std::cerr << "Cannot open " << filename << std::endl; return; }

        TObjString *channel_file = dynamic_cast<TObjString*>(file.Get("writeNTuple/channelName"));
        TObjString *systematics_from_file = dynamic_cast<TObjString*>(file.Get("writeNTuple/systematicsName"));
        TObjString *samplename = dynamic_cast<TObjString*>(file.Get("writeNTuple/sampleName"));
        TObjString *o_isSignal = dynamic_cast<TObjString*>(file.Get("writeNTuple/isSignal"));
        TObjString *o_isMC = dynamic_cast<TObjString*>(file.Get("writeNTuple/isMC"));
        TH1* weightedEvents = dynamic_cast<TH1*>(file.Get("EventsBeforeSelection/weightedEvents"));
        if (!channel_file || !systematics_from_file || !o_isSignal || !o_isMC || !samplename) { 
            std::cout << "Error: info about sample missing!" << std::endl; 
            return;  
        }
        bool isSignal = o_isSignal->GetString() == "1";
        bool isMC = o_isMC->GetString() == "1";
        
        if (!isMC && systematic != "") {
            std::cout << "Sample is DATA, so not running again for systematic variation\n";
            continue;
        }
        
        if (systematic == "PDF" && (!isSignal || !(systematics_from_file->GetString() == "Nominal"))) {
            std::cout << "Skipping file: is not signal or not nominal -- and running PDFs\n";
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
        
        for (const auto& channel : channels) {
            TString btagFile = "BTagEff/Nominal/" + channel + "/" 
                + channel + "_ttbarsignalplustau.root";
            TString outputfilename { filename };
            if (outputfilename.Contains('/')) {
                Ssiz_t last = outputfilename.Last('/');
                outputfilename = outputfilename.Data() + last + 1;
            }
            if (!outputfilename.Contains(channel + "_")) outputfilename.Prepend(channel + "_");
            //outputfile is now channel_filename.root
            
            selector->SetBTagFile(btagFile);
            selector->SetChannel(channel);
            selector->SetSignal(isSignal);
            selector->SetMC(isMC);
            selector->SetTrueLevelDYChannel(dy);
            if (dy) {
                if (outputfilename.First("_dy") == kNPOS) { 
                    std::cerr << "DY variations must be run on DY samples!\n";
                    std::cerr << outputfilename << " must start with 'channel_dy'\n";
                    std::exit(1);
                }
                outputfilename.ReplaceAll("_dy", TString("_dy").Append(dy == 11 ? "ee" : dy == 13 ? "mumu" : "tautau"));
            }
            if (systematic == "") {
                selector->SetSystematic(systematics_from_file->GetString());
            } else {
                selector->SetSystematic(systematic);
            }
            selector->SetWeightedEvents(weightedEvents);
            selector->SetSamplename(samplename->GetString(), systematics_from_file->GetString());
            selector->SetOutputfilename(outputfilename);
            selector->SetRunViaTau(0);
            selector->SetClosureTest(closure, slope);

            TTree *tree = dynamic_cast<TTree*>(file.Get("writeNTuple/NTuple"));
            if (! tree) { std::cerr << "Error: Tree not found!\n"; exit(854); }
            
            TChain chain("writeNTuple/NTuple");
            chain.Add(filename);
            // chain.SetProof(); //will work from 5.34 onwards
            
            if (systematic == "PDF") {
                TH1* pdfWeights = dynamic_cast<TH1*>(file.Get("EventsBeforeSelection/pdfEventWeights"));
                if (!pdfWeights) { std::cerr << "Error: pdfEventWeights histo missing!\n"; exit(831); }
                for (int pdf_no = 0; pdfWeights->GetBinContent(pdf_no+1) > 0; ++pdf_no) {
                    if (specific_PDF >=0 && pdf_no != specific_PDF) continue;
                    selector->SetSystematic(pdfDirName(pdf_no));
                    //weightedEvents->SetBinContent(1, pdfWeights->GetBinContent(pdf_no+1));
                    selector->SetWeightedEvents(weightedEvents);
                    selector->SetPDF(pdf_no);
                    chain.Process(selector);
                }
            } else {
                chain.Process(selector);
                if (isSignal && closure == "") {
                    selector->SetRunViaTau(1);
                    outputfilename.ReplaceAll("signalplustau", "bgviatau");
                    selector->SetOutputfilename(outputfilename);
                    chain.Process(selector);
                }
            }
        }
        file.Close();
    }
}

int main(int argc, char** argv) {
    CLParameter<std::string> opt_f("f", "Restrict to filename pattern, e.g. ttbar", false, 1, 1);
    CLParameter<std::string> opt_s("s", "Run with a systematic that runs on the nominal ntuples, e.g. 'PDF', 'PU_UP' or 'TRIG_DOWN'", false, 1, 1);
    CLParameter<int> opt_pdfno("pdf", "Run a certain PDF systematic only, sets -s PDF. Use e.g. --pdf n, where n=0 is central, 1=variation 1 up, 2=1down, 3=2up, 4=2down, ...", false, 1, 1);
    CLParameter<std::string> opt_c("c", "Specify a certain channel (ee, emu, mumu). No channel specified = run on all channels", false, 1, 1,
            [](const std::string &ch){return ch == "" || ch == "ee" || ch == "emu" || ch == "mumu";});
    CLParameter<int> opt_dy("d", "Drell-Yan mode (11 for ee, 13 for mumu, 15 for tautau)", false, 1, 1,
            [](int dy){return dy == 11 || dy == 13 || dy == 15;});
    CLParameter<std::string> opt_closure("closure", "Enable the closure test. Valid: pttop|ytop|nominal", false, 1, 1,
            [](const std::string &c){return c == "pttop" || c == "ytop" || c == "nominal";});
    CLParameter<double> opt_closureSlope("slope", "Slope for closure test, use -0.01 to 0.01 for pt and -0.4 to 0.4", false, 1, 1,
            [](double s){return abs(s) < 1;});
                                         
    CLAnalyser::interpretGlobal(argc, argv);
    
    TString validFilenamePattern = opt_f.isSet() ? opt_f[0] : "";
    TString syst = opt_s.isSet() ? opt_s[0] : "";
    TString channel = opt_c.isSet() ? opt_c[0] : "";
    int dy = opt_dy.isSet() ? opt_dy[0] : 0;
    TString closure = opt_closure.isSet() ? opt_closure[0] : "";    
    double slope = 0;
    if (closure != "" && closure != "nominal") {
        if (!opt_closureSlope.isSet()) {
            std::cerr << "closure test: need slope!\n"; exit(1);
        } else {
            slope = opt_closureSlope[0];
        }
    }
    int pdf_no = -1;
    if (opt_pdfno.isSet()) {
        pdf_no = opt_pdfno[0];
        if (pdf_no >= 0)
            std::cout << "Running PDF variation: " << pdfDirName(pdf_no) << "\n";
        if (!(syst == "" || syst == "PDF")) {
            std::cout << "Insonsistent systematic parameter: " << syst << " cannot be used with PDF systematic!\n";
            std::exit(1);
        }
        syst = "PDF";
    }
    
//     TProof* p = TProof::Open(""); // not before ROOT 5.34
    load_Analysis(validFilenamePattern, channel, syst, pdf_no, dy, closure, slope);
//     delete p;
}