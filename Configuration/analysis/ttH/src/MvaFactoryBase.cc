#include <vector>
#include <iostream>
#include <fstream>

#include <TFile.h>
#include <TTree.h>
#include <TString.h>
#include <TCut.h>
#include <TMVA/Tools.h>
#include <TMVA/Config.h>
#include <TMVA/Factory.h>

#include "MvaFactoryBase.h"
#include "MvaVariablesBase.h"
#include "mvaSetup.h"
#include "higgsUtils.h"





MvaFactoryBase::MvaFactoryBase(const TString& mvaOutputDir, const TString& weightFileDir,
                               const TString& treeFileName):
mvaOutputDir_(mvaOutputDir),
weightFileDir_(weightFileDir),
treeFileName_(treeFileName)
{
    // Check if input file exists
    std::ifstream inputFileStream(treeFileName);
    if(!inputFileStream.is_open()){
        std::cerr<<"ERROR in constructor of MvaFactoryBase! File containing the MVA input trees not found: "<<treeFileName
                 <<"\n...break\n"<<std::endl;
        exit(1);
    }
    inputFileStream.close();
}



void MvaFactoryBase::train(const std::vector<mvaSetup::MvaSet>& v_mvaSet)const
{
    std::cout<<"--- Beginning MVA training\n";
    
    // Open input file
    TFile* treeFile = TFile::Open(treeFileName_);
    
    // Loop over the steps/categories and train MVAs
    for(const auto& mvaSet : v_mvaSet){
        const TString mergedStepName = tth::stepName(mvaSet.step_, mvaSet.v_category_);
        this->trainMva(treeFile, mvaSet, mergedStepName);
    }
    
    // Cleanup
    treeFile->Close();
    
    std::cout<<"=== Finishing MVA training\n\n";
}



void MvaFactoryBase::trainMva(TFile* const, const mvaSetup::MvaSet&, const TString&)const
{
    // WARNING: this is empty template method, overwrite for inherited class
    
    std::cerr<<"ERROR! Dummy method trainMva() in MvaFactoryBase is called, but overridden one should be used\n"
             <<"...break\n"<<std::endl;
    exit(568);
}



void MvaFactoryBase::runMva(const char* const methodPrefix, const TCut& cutSignal, const TCut& cutBackground,
                            TTree* const treeTraining, TTree* const treeTesting,
                            const std::vector<mvaSetup::MvaConfig>& v_mvaConfig,
                            const TString& stepName)const
{
    
    // Get a TMVA instance
    TMVA::Tools::Instance();
    
    // Create a ROOT output file for TMVA
    TString mvaOutputFilename(mvaOutputDir_);
    mvaOutputFilename.Append(methodPrefix);
    mvaOutputFilename.Append(stepName);
    mvaOutputFilename.Append(".root");
    TFile* outputFile = TFile::Open(mvaOutputFilename, "RECREATE");
    
    // Set the output directory for the weights (if not specified, default is "weights")
    TString mvaOutputWeightsFilename(mvaOutputDir_);
    mvaOutputWeightsFilename.Append(weightFileDir_);
    (TMVA::gConfig().GetIONames()).fWeightFileDir = mvaOutputWeightsFilename;
    
    // Create the factory
    TMVA::Factory* factory(0);
    TString factoryName(methodPrefix);
    factoryName.Append(stepName);
    factory = new TMVA::Factory(factoryName, outputFile, "!V:!Silent");
    
    // Configure the factory
    this->configureFactory(factory, cutSignal, cutBackground, treeTraining, treeTesting);
    
    // Book the MVA methods (e.g. boosted decision tree with specific setup)
    for(const auto& mvaConfig : v_mvaConfig){
        const TString methodTitle(mvaConfig.methodAppendix_);
        factory->BookMethod(mvaConfig.mvaType_,
                            methodTitle,
                            mvaConfig.options_);
    }
    
    // Run factory
    factory->TrainAllMethods();
    factory->TestAllMethods();
    factory->EvaluateAllMethods();
    
    // Cleanup
    outputFile->Close();
    delete factory;
}



void MvaFactoryBase::configureFactory(TMVA::Factory* const,
                                      const TCut&, const TCut&,
                                      TTree* const, TTree* const)const
{
    // WARNING: this is empty template method, overwrite for inherited class
    
    std::cerr<<"ERROR! Dummy method configureFactory() in MvaFactoryBase is called, but overridden one should be used\n"
             <<"...break\n"<<std::endl;
    exit(568);
}



void MvaFactoryBase::addVariable(TMVA::Factory* const factory, const MvaVariableInt& variable)const
{
    factory->AddVariable(variable.name().data(), *variable.type());
}



void MvaFactoryBase::addVariable(TMVA::Factory* const factory, const MvaVariableFloat& variable)const
{
    factory->AddVariable(variable.name().data(), *variable.type());
}



void MvaFactoryBase::addSpectator(TMVA::Factory* const factory, const MvaVariableInt& variable)const
{
    factory->AddSpectator(variable.name().data(), *variable.type());
}



void MvaFactoryBase::addSpectator(TMVA::Factory* const factory, const MvaVariableFloat& variable)const
{
    factory->AddSpectator(variable.name().data(), *variable.type());
}










