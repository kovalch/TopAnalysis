#include "utils.h"

#include <cmath>
#include <string>
#include <iostream>
#include <algorithm>
#include <stdlib.h>

#include <TPad.h>
#include <TF1.h>
#include <TPaveText.h>
#include <TMath.h>
#include <TLorentzVector.h>
#include <TFile.h>
#include <THStack.h>

void LVtod4(const LV lv, double *d) {
    d[0] = lv.E();
    d[1] = lv.Px();
    d[2] = lv.Py();
    d[3] = lv.Pz();
}

std::string d2s(double d) {
    char result[100];
    if (std::abs(d) < 5) {
        sprintf(result, "%.3f", d);
        std::string s = std::string(result);
        while (s.length() > 0 && s[s.length()-1] == '0') s.erase(s.end()-1);
        if (s.length() > 0 && s[s.length()-1] == '.') s.erase(s.end()-1);
        return s;
    } else {
        sprintf(result, "%.0f", d);
        return std::string(result);
    }
}

void drawRatio(const TH1* histNumerator, const TH1* histDenominator, 
               const Double_t ratioMin, const Double_t ratioMax, 
               const TStyle &myStyle, int verbose, const std::vector<double> err)
{
    // this function draws a pad with the ratio of 'histNumerator' and 'histDenominator'
    // the range of the ratio is 'ratioMin' to 'ratioMax'
    // to the systematic variation "sys" of the enumerator "systematicVariation"
    // per default only the gaussian error of the 'histNumerator' is considered:
    // (error(bin i) = sqrt(histNumerator->GetBinContent(i))/histDenominator->GetBinContent(i))
    // if 'err_' is present and its size equals the number of bins in the histos,
    // its valus are considered as error for the ratio
    // NOTE: x Axis is transferred from histDenominator to the bottom of the canvas
    // modified quantities: none
    // used functions: none
    // used enumerators: none

    // check that histos have the same binning
    if(histNumerator->GetNbinsX()!=histDenominator->GetNbinsX()){
        std::cout << "error when calling drawRatio - histos have different number of bins" << std::endl;
        return;
    }
    if(verbose>1){
        std::cout << "building ratio plot of " << histNumerator->GetName();
        std::cout << " and " << histDenominator->GetName() << std::endl;
    }
    // create ratio
    TH1* ratio = (TH1*)histNumerator->Clone();
    ratio->Divide(histDenominator);
    // calculate error for ratio
    // a) from err_
    if(err.size()==(unsigned int)histNumerator->GetNbinsX()){
        if(verbose>0) std::cout << "ratio error from vector" << std::endl;
        for(int bin=1; bin<=histNumerator->GetNbinsX(); bin++){
            ratio->SetBinError(bin, err[bin-1]);
        }
    }
    else{
        // b) default: only gaussian error of histNumerator
        if(verbose>0) std::cout << "ratio error from statistical error of " << histNumerator->GetName() << " only" << std::endl;
        for(int bin=1; bin<=histNumerator->GetNbinsX(); bin++){
            ratio->SetBinError(bin, sqrt(histNumerator->GetBinContent(bin))/histDenominator->GetBinContent(bin));
        }
    }
    // get some values from old pad
    //Int_t    logx = gPad->GetLogx();
    //Double_t left = gPad->GetLeftMargin();
    //Double_t right = gPad->GetRightMargin();

    Int_t    logx  = myStyle.GetOptLogx();
    Double_t left  = myStyle.GetPadLeftMargin();
    Double_t right = myStyle.GetPadRightMargin();

    // y:x size ratio for canvas
    double canvAsym = 4./3.;
    // ratio size of pad with plot and pad with ratio
    double ratioSize = 0.36;
    // change old pad
    gPad->SetBottomMargin(ratioSize);
    gPad->SetRightMargin(right);
    gPad->SetLeftMargin(left);
    gPad->SetBorderMode(0);
    gPad->SetBorderSize(0);
    gPad->SetFillColor(10);
    // create new pad for ratio plot
    TPad *rPad;
    rPad = new TPad("rPad","",0,0,1,ratioSize+0.001);
#ifdef DILEPTON_MACRO
    rPad->SetFillColor(10);
#else
    rPad->SetFillStyle(0);
    rPad->SetFillColor(0);
#endif
    rPad->SetBorderSize(0);
    rPad->SetBorderMode(0);
    rPad->Draw();
    rPad->cd();
    rPad->SetLogy(0);
    rPad->SetLogx(logx);
    rPad->SetTicky(1);
    // configure ratio plot
    double scaleFactor = 1./(canvAsym*ratioSize);
    ratio->SetStats(kFALSE);
    ratio->SetTitle("");
    ratio->SetMaximum(ratioMax);
    ratio->SetMinimum(ratioMin);
    ratio->SetLineWidth(1);
    // configure axis of ratio plot
    ratio->GetXaxis()->SetTitleSize(histNumerator->GetXaxis()->GetTitleSize()*scaleFactor*1.3);
    ratio->GetXaxis()->SetTitleOffset(histNumerator->GetXaxis()->GetTitleOffset()*0.9);
    ratio->GetXaxis()->SetLabelSize(histNumerator->GetXaxis()->GetLabelSize()*scaleFactor*1.4);
    ratio->GetXaxis()->SetTitle(histNumerator->GetXaxis()->GetTitle());
    ratio->GetXaxis()->SetNdivisions(histNumerator->GetNdivisions());
    ratio->GetYaxis()->CenterTitle();
    ratio->GetYaxis()->SetTitle("#frac{N_{data}}{N_{MC}}");
    ratio->GetYaxis()->SetTitleSize(histNumerator->GetYaxis()->GetTitleSize()*scaleFactor);
    ratio->GetYaxis()->SetTitleOffset(histNumerator->GetYaxis()->GetTitleOffset()/scaleFactor);
    ratio->GetYaxis()->SetLabelSize(histNumerator->GetYaxis()->GetLabelSize()*scaleFactor);
    ratio->GetYaxis()->SetLabelOffset(histNumerator->GetYaxis()->GetLabelOffset()*3.3);
    ratio->GetYaxis()->SetTickLength(0.03);
    ratio->GetYaxis()->SetNdivisions(505);
    ratio->GetXaxis()->SetRange(histNumerator->GetXaxis()->GetFirst(), histNumerator->GetXaxis()->GetLast());
    // delete axis of initial plot
    histNumerator->GetXaxis()->SetLabelSize(0);
    histNumerator->GetXaxis()->SetTitleSize(0);
    // draw ratio plot
    ratio->DrawClone("p e X0");
    ratio->SetMarkerSize(1.2);
    ratio->DrawClone("p e X0 same");
    rPad->SetTopMargin(0.0);
    rPad->SetBottomMargin(0.15*scaleFactor);
    rPad->SetRightMargin(right);
    gPad->SetLeftMargin(left);
    gPad->RedrawAxis();
    // draw grid
    //rPad->SetGrid(1,1);

    // draw a horizontal lines on a given histogram
    // a) at 1
    Double_t xmin = ratio->GetXaxis()->GetXmin();
    Double_t xmax = ratio->GetXaxis()->GetXmax();
    TString height = ""; height += 1;
    TF1 *f = new TF1("f", height, xmin, xmax);
    f->SetLineStyle(1);
    f->SetLineWidth(1);
    f->SetLineColor(kBlack);
    f->Draw("L same");
    // b) at upper end of ratio pad
    TString height2 = ""; height2 += ratioMax;
    TF1 *f2 = new TF1("f2", height2, xmin, xmax);
    f2->SetLineStyle(1);
    f2->SetLineWidth(1);
    f2->SetLineColor(kBlack);
    f2->Draw("L same");
}


void setHHStyle(TStyle& HHStyle)
{
    const int fontstyle=42;
    HHStyle.SetPalette(1);
        
    // ==============
    //  Canvas
    // ==============
            
    HHStyle.SetCanvasBorderMode(0);
    HHStyle.SetCanvasColor(kWhite);
    HHStyle.SetCanvasDefH(600); //Height of canvas
    HHStyle.SetCanvasDefW(600); //Width of canvas
    HHStyle.SetCanvasDefX(0);   //Position on screen
    HHStyle.SetCanvasDefY(0);
            
    // ==============
    //  Pad
    // ==============
            
    HHStyle.SetPadBorderMode(0);
    // HHStyle.SetPadBorderSize(Width_t size = 1);
    HHStyle.SetPadColor(kWhite);
    HHStyle.SetPadGridX(false);
    HHStyle.SetPadGridY(false);
    HHStyle.SetGridColor(0);
    HHStyle.SetGridStyle(3);
    HHStyle.SetGridWidth(1);
            
    // ==============
    //  Frame
    // ==============
            
    HHStyle.SetFrameBorderMode(0);
    HHStyle.SetFrameBorderSize(1);
    HHStyle.SetFrameFillColor(0);
    HHStyle.SetFrameFillStyle(0);
    HHStyle.SetFrameLineColor(1);
    HHStyle.SetFrameLineStyle(1);
    HHStyle.SetFrameLineWidth(1);
            
    // ==============
    //  Histo
    // ==============

    HHStyle.SetErrorX(0.0);
    HHStyle.SetEndErrorSize(0);
            
    // HHStyle.SetHistFillColor(1);
    // HHStyle.SetHistFillStyle(0);
    // HHStyle.SetHistLineColor(1);
    HHStyle.SetHistLineStyle(0);
    HHStyle.SetHistLineWidth(1);
    // HHStyle.SetLegoInnerR(Float_t rad = 0.5);
    // HHStyle.SetNumberContours(Int_t number = 20);

    // HHStyle.SetErrorMarker(20);
            
    HHStyle.SetMarkerStyle(20);
            
    // ==============
    //  Fit/function
    // ==============
            
    HHStyle.SetOptFit(1);
    HHStyle.SetFitFormat("5.4g");
    HHStyle.SetFuncColor(2);
    HHStyle.SetFuncStyle(1);
    HHStyle.SetFuncWidth(1);
            
    // ==============
    //  Date
    // ============== 
            
    HHStyle.SetOptDate(0);
    // HHStyle.SetDateX(Float_t x = 0.01);
    // HHStyle.SetDateY(Float_t y = 0.01);
            
    // =====================
    //  Statistics Box
    // =====================
            
    HHStyle.SetOptFile(0);
    HHStyle.SetOptStat(0); // To display the mean and RMS:   SetOptStat("mr");
    HHStyle.SetStatColor(kWhite);
    HHStyle.SetStatFont(fontstyle);
    HHStyle.SetStatFontSize(0.025);
    HHStyle.SetStatTextColor(1);
    HHStyle.SetStatFormat("6.4g");
    HHStyle.SetStatBorderSize(1);
    HHStyle.SetStatH(0.1);
    HHStyle.SetStatW(0.15);
    // HHStyle.SetStatStyle(Style_t style = 1001);
    // HHStyle.SetStatX(Float_t x = 0);
    // HHStyle.SetStatY(Float_t y = 0);
            
    // ==============
    //  Margins
    // ==============

    HHStyle.SetPadTopMargin(0.1);
    HHStyle.SetPadBottomMargin(0.15);
    HHStyle.SetPadLeftMargin(0.20);
    HHStyle.SetPadRightMargin(0.05);
            
    // ==============
    //  Global Title
    // ==============
            
    HHStyle.SetOptTitle(0);
    HHStyle.SetTitleFont(fontstyle);
    HHStyle.SetTitleColor(1);
    HHStyle.SetTitleTextColor(1);
    HHStyle.SetTitleFillColor(10);
    HHStyle.SetTitleFontSize(0.05);
    // HHStyle.SetTitleH(0); // Set the height of the title box
    // HHStyle.SetTitleW(0); // Set the width of the title box
    // HHStyle.SetTitleX(0); // Set the position of the title box
    // HHStyle.SetTitleY(0.985); // Set the position of the title box
    // HHStyle.SetTitleStyle(Style_t style = 1001);
    // HHStyle.SetTitleBorderSize(2);
            
    // ==============
    //  Axis titles
    // ==============
            
    HHStyle.SetTitleColor(1, "XYZ");
    HHStyle.SetTitleFont(fontstyle, "XYZ");
    HHStyle.SetTitleSize(0.04, "XYZ");
    // HHStyle.SetTitleXSize(Float_t size = 0.02); // Another way to set the size?
    // HHStyle.SetTitleYSize(Float_t size = 0.02);
    HHStyle.SetTitleXOffset(1.25);
    HHStyle.SetTitleYOffset(1.6);
    // HHStyle.SetTitleOffset(1.1, "Y"); // Another way to set the Offset
            
    // ==============
    //  Axis Label
    // ==============
            
    //HHStyle.SetLabelColor(1, "XYZ");
    HHStyle.SetLabelFont(fontstyle, "XYZ");
    HHStyle.SetLabelOffset(0.007, "XYZ");
    HHStyle.SetLabelSize(0.04, "XYZ");
            
    // ==============
    //  Axis
    // ==============
            
    HHStyle.SetAxisColor(1, "XYZ");
    HHStyle.SetStripDecimals(kTRUE);
    HHStyle.SetTickLength(0.03, "XYZ");
    HHStyle.SetNdivisions(510, "XYZ");
    HHStyle.SetPadTickX(1);  // To get tick marks on the opposite side of the frame
    HHStyle.SetPadTickY(1);
            
    // Change for log plots:
    HHStyle.SetOptLogx(0);
    HHStyle.SetOptLogy(0);
    HHStyle.SetOptLogz(0);
            
    // ==============
    //  Text
    // ==============
            
    HHStyle.SetTextAlign(11);
    HHStyle.SetTextAngle(0);
    HHStyle.SetTextColor(1);
    HHStyle.SetTextFont(fontstyle);
    HHStyle.SetTextSize(0.05);
            
    // =====================
    //  Postscript options:
    // =====================
            
    HHStyle.SetPaperSize(20.,20.);
    // HHStyle.SetLineScalePS(Float_t scale = 3);
    // HHStyle.SetLineStyleString(Int_t i, const char* text);
    // HHStyle.SetHeaderPS(const char* header);
    // HHStyle.SetTitlePS(const char* pstitle);
            
    // HHStyle.SetBarOffset(Float_t baroff = 0.5);
    // HHStyle.SetBarWidth(Float_t barwidth = 0.5);
    // HHStyle.SetPaintTextFormat(const char* format = "g");
    // HHStyle.SetPalette(Int_t ncolors = 0, Int_t* colors = 0);
    // HHStyle.SetTimeOffset(Double_t toffset);
    // HHStyle.SetHistMinimumZero(kTRUE);
}


///////////////////////////////////////////

TObject *RootFileReader::GetObj(const char * filename, const char * histoname, bool allowNonexisting) {
    auto& file = fileMap[filename];
    if (!file) {
        file = TFile::Open(filename);
        if (!file) {
            if (allowNonexisting) return nullptr;
            std::cerr << "\n\n******************* ERROR ******************* ERROR ******************* ERROR *******************\n\n"
                      << "The file " << filename << " does not exist, thus cannot get histogram " << histoname 
                      << "\n\n******************* ERROR ******************* ERROR ******************* ERROR *******************\n"
                      << std::endl;
            exit(1);
        }
        ++opened[filename];
    } else {
        fileOrder.erase(std::remove_if(begin(fileOrder), end(fileOrder), 
                                        [=](const TString &str){ return str == filename;}),
                        end(fileOrder));
    }
    
    fileOrder.push_back(filename);
    ++accessed[filename];
    //at max, keep 20 files open
    if (fileMap.size() > 20) {
        //delete 0th element
        delete fileMap[fileOrder[0]];
        fileMap.erase(fileOrder[0]);
        fileOrder.erase(fileOrder.begin());
    }
    TObject* result = file->Get(histoname);
    TH1* as_histo = dynamic_cast<TH1*>(result);
    if (as_histo) as_histo->SetDirectory(file);
    return result;
}


std::vector<TString> RootFileReader::findHistos(const char* filename, const char* histonameBegin){
    
    TFile* file = TFile::Open(filename);
    if (!file) {
        std::cerr << "\n\n******************* ERROR ******************* ERROR ******************* ERROR *******************\n\n"
                  << "The file " << filename << " does not exist, thus cannot search for histogram beginning with " << histonameBegin 
                  << "\n\n******************* ERROR ******************* ERROR ******************* ERROR *******************\n"
                  << std::endl;
        exit(1);
    }
    std::vector<TString> result;
    TList* histoList = file->GetListOfKeys();
    for(int i=0; i<histoList->GetSize(); ++i){
        TObject* i_histoList = histoList->At(i);
        TString* histoName(0);
        histoName = new TString(i_histoList->GetName());
        if(histoName->BeginsWith(histonameBegin)){
            //std::cout<<"\n\tName of object: "<<*histoName<<"\n\n";
            result.push_back(*histoName);
        }
    }
    return result;
}


RootFileReader::~RootFileReader()
{
//     std::cout << "Deleting RootFileReader\n";
//     for (const auto& i : fileMap) {
//         delete i.second;
//     }
//     for (const auto& i : accessed) {
//         std::cout << "accessed: " << i.first << " " << i.second << std::endl;
//     }
//     for (const auto& i : opened) {
//         std::cout << "opened: " << i.first << " " << i.second << std::endl;
//     }
//     
}

RootFileReader* RootFileReader::getInstance() {
    static RootFileReader instance;
    return &instance;
}

/////////////////////////////////////////////////////////


const TLorentzVector LVtoTLV(const LV& lv) {
    return TLorentzVector(lv.X(), lv.Y(), lv.Z(), lv.T());
}

const LV TLVtoLV(const TLorentzVector& lv) {
    LV result; 
    result.SetXYZT(lv.X(), lv.Y(), lv.Z(), lv.T());
    return result;
}

/** Sum the histograms in a stack and
 * return the sum in a new TH1
 */
TH1* SummedStackHisto(const THStack *stack)
{
    TList *l { stack->GetHists() }; //the TList is owned by the stack
    if (l->GetEntries() == 0) return 0;
    TH1* result = (TH1*) l->At(0)->Clone();
    for (int i = 1; i < l->GetEntries(); ++i) {
        result->Add((TH1*)l->At(i));
    }
    return result;
}

/** Calculate the median of a histogram
 * 
 */
double Median(TH1 * h1)
{ 
   int n = h1->GetXaxis()->GetNbins();
   std::vector<double>  x(n);
   h1->GetXaxis()->GetCenter( &x[0] );
   TH1D* h1D = dynamic_cast<TH1D*>(h1);
   if (!h1D) { std::cerr << "Median needs a TH1D!\n"; exit(7); }
   const double * y = h1D->GetArray(); 
   // exclude underflow/overflows from bin content array y
   return TMath::Median(n, &x[0], &y[1]); 
}

/// return CMSSW_BASE environment variable as string, with error checking
const std::string CMSSW_BASE()
{
    const char *cmssw_base = getenv("CMSSW_BASE");
    if (!cmssw_base) {
        std::cerr << "Error! Environmental variable CMSSW_BASE not set!\n"
                  << "Please run cmsenv first.\n"
                  << "When running without CMSSW, you still need this variable so that the\n"
                  << "certain files can be found.\n";
        std::exit(1);            
    }
    std::string result(cmssw_base);
    return result;
}

const TString DATA_PATH()
{
    TString result(CMSSW_BASE());
    result.Append("/src/TopAnalysis/Configuration/analysis/diLeptonic/data");
    return result;
}