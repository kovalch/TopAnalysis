#include "KinematicReconstruction.h"
#include <TAttLine.h>
#define printout 0
#include "KinematicReconstruction_LSroutines.h"
#include "analysisUtils.h"
#include <TLorentzVector.h>


#include <cmath>
#include <cassert>
#include <algorithm>
#include <utility>
#include <cmath>

#include <TLorentzVector.h>
#include <TMath.h>

#include "KinReco.h"
#include "utils.h"
#include "analysisUtils.h"
#include "classes.h"
// #include "TVector3.h"
#include <TRandom3.h>
#include "MeanSol.h"
#include <TH1.h>
#include <TFile.h>
#include <TString.h>


using namespace std;

void angle_rot(double alpha, double e, TLorentzVector jet, TLorentzVector & jet_sm)
{
  double px_1, py_1, pz_1; // sistema koordinat, gde impul's vdol' Oz
  
  /// Transition matrix detector -> syst1 ///
  double x1, y1, z1;
  double x2, y2, z2;
  double x3, y3, z3;
  ///
  
  
  if(fabs(jet.Px())<=e){jet.SetPx(0);}
  if(fabs(jet.Py())<=e){jet.SetPy(0);}
  if(fabs(jet.Pz())<=e){jet.SetPz(0);}
  
  
  /// Rotation in syst 1 ///
 int seed_random = (int)(( jet.Pt() - (int)(jet.Pt()) )*1000000000);
  TRandom3 r(seed_random);  ///random seed
  double phi = 2*TMath::Pi()*r.Rndm();
  pz_1 = jet.Vect().Mag()*cos(alpha);
  px_1 = - jet.Vect().Mag()*sin(alpha)*sin(phi);
  py_1 = jet.Vect().Mag()*sin(alpha)*cos(phi);  
  ///
  
  /// Transition detector <- syst1 ///
  if (jet.Py()!=0||jet.Pz()!=0)
  {
    double d = sqrt(jet.Pz()*jet.Pz() + jet.Py()*jet.Py());
    double p = jet.Vect().Mag();

    
    x1 = d/p;
    y1 = 0;
    z1 = jet.Px()/p;
    
    x2 = - jet.Px()*jet.Py()/d/p;
    y2 = jet.Pz()/d;
    z2 = jet.Py()/p;
    
    x3 = - jet.Px()*jet.Pz()/d/p;
    y3 = - jet.Py()/d;
    z3 = jet.Pz()/p;
    
    jet_sm.SetPx(x1*px_1+y1*py_1+z1*pz_1);
    jet_sm.SetPy(x2*px_1+y2*py_1+z2*pz_1);
    jet_sm.SetPz(x3*px_1+y3*py_1+z3*pz_1);
    jet_sm.SetE(jet.E());
  }
  
  if (jet.Px()==0&&jet.Py()==0&&jet.Pz()==0)
  {
    jet_sm.SetPx(jet.Px());
    jet_sm.SetPy(jet.Py());
    jet_sm.SetPz(jet.Pz());
    jet_sm.SetE(jet.E());
  }

  if (jet.Px()!=0&&jet.Py()==0&&jet.Pz()==0)
  {
    jet_sm.SetPx(pz_1);
    jet_sm.SetPy(px_1);
    jet_sm.SetPz(py_1);
    jet_sm.SetE(jet.E());
  }
  ///
  
}


KinematicReconstruction::KinematicReconstruction()
{
    isJetsMerging=false;
    //std::cout<<"--- Beginning preparation of kinematic reconstruction\n";
    this->loadData();
    //std::cout<<"=== Finishing preparation of kinematic reconstruction\n\n";
}

void KinematicReconstruction::doJetsMerging(const VLV* jets,const std::vector<double> *btags)
{
    
    isJetsMerging=true;
    
    
    alljets.clear();
    allbtags.clear();
        for (const auto& jet : *jets) {
        alljets.push_back(ttbar::LVtoTLV(jet));
    }
    for(int i=0; i<(int)btags->size(); i++) {
        allbtags.push_back(btags->at(i));
    }
    
}

void KinematicReconstruction::kinReco(const LV& leptonMinus, const LV& leptonPlus, const VLV *jets, const std::vector<double> *btags, const LV* met)
{

    gRandom->SetSeed(0);

    std::vector<struct_KinematicReconstruction> vect_sol;

    TLorentzVector leptonPlus_tlv = ttbar::LVtoTLV(leptonPlus);
    TLorentzVector leptonMinus_tlv = ttbar::LVtoTLV(leptonMinus);
    TLorentzVector met_tlv = ttbar::LVtoTLV(*met);

    
    
    //jets selection

    vector<int> b1_id;
    vector<int> b2_id;
    vector<int> nb_tag;
    std::vector<TLorentzVector> jets_tlv;
    std::vector<double> new_btags;
    
    double btag_wp=0.244;
    
if(!isJetsMerging)
{
        
    
    for (const auto& jet : *jets) {
        jets_tlv.push_back(ttbar::LVtoTLV(jet));
    }
    
    for(int i=0; i<(int)btags->size(); i++) {
//         new_btags.push_back(btags->at(i));
        
        for(int j=0; j<(int)btags->size(); j++) {
            double wi = btags->at(i);
            double wj = btags->at(j);
//                  if(i==j || (wi<0.244 && wj<0.244) || (wi<0 || wj<0))continue;
            if(i==j || (wi<btag_wp && wj<btag_wp))continue;

            if(wi>btag_wp && wj>btag_wp){nb_tag.push_back(2); }
            else{nb_tag.push_back(1); }

            b1_id.push_back(i);
            b2_id.push_back(j);
        }
    }
}
else
{
    
    //fill new jets:  logik I.
//     std::vector<TLorentzVector> new_jets_tlv;
//     std::vector<double> new_btag;
//     std::vector<int> veto_i;
//     std::vector<int> veto_j;
//         for(int i=0; i<(int)alljets.size(); i++)
//         {
//             if(allbtags.at(i)<btag_wp)continue;
//             TLorentzVector ijet=alljets.at(i);
//             
//             for(int j=0; j<(int)alljets.size(); j++)
//             {
//                  if(i==j)continue;
//                  if(allbtags.at(j)>=btag_wp)continue; 
//                 TLorentzVector jjet=alljets.at(j);
//                 double dRij=ijet.DeltaR(jjet);
//                  if(dRij>1)continue;
//                 TLorentzVector new_jet=ijet+jjet;
//                     if(new_jet.Pt()<30)continue;
//                     if(fabs(new_jet.Eta())>2.4)continue;
//                 new_jets_tlv.push_back(new_jet);
//                 new_btag.push_back(allbtags.at(i));
//                 veto_i.push_back(i);
//                 veto_j.push_back(j);
//             }   
//         }
//  
//      std::vector<int> index_i;
//      std::vector<int> index_j;
//      for(int i=0; i<(int)alljets.size(); i++)
//         {
//                 if(alljets.at(i).Pt()<30)continue;
//                 if(fabs(alljets.at(i).Eta())>2.4)continue;
//                 jets_tlv.push_back(alljets.at(i));
//                 new_btags.push_back(allbtags.at(i));
//                 index_i.push_back(i);
//                 index_j.push_back(i);
//         }
//     
//     
//     for(int i=0; i<(int)new_jets_tlv.size(); i++)
//     {
//         jets_tlv.push_back(new_jets_tlv.at(i));
//         new_btags.push_back(new_btag.at(i));
//         index_i.push_back(veto_i.at(i));
//         index_j.push_back(veto_j.at(i));
//     }
//     
//         for(int i=0; i<(int)jets_tlv.size(); i++) 
//         {
//                 for(int j=0; j<(int)jets_tlv.size(); j++) 
//                 {
//                                 if(index_i[i]==index_i[j] || index_i[i]==index_j[j] || index_j[i]==index_i[j] || index_j[i]==index_j[j])continue;                   
//                                double wi = new_btags.at(i);
//                                double wj = new_btags.at(j);
// //                                 //if(i==j || (wi<0.244 && wj<0.244) || (wi<0 || wj<0))continue;
//                                 if(i==j || (wi<btag_wp && wj<btag_wp))continue;
//                                 if(wi>btag_wp && wj>btag_wp){nb_tag.push_back(2); }
//                                 else{nb_tag.push_back(1); }
//                                 b1_id.push_back(i);
//                                 b2_id.push_back(j);
//                 }
//         }


//fill new jets:  logik II.

    std::vector<TLorentzVector> new_jets_tlv;
    std::vector<double> new_btag;
    std::vector<int> index_dR;
    int index_i;
    int index_j;
    
    for(int i=0; i<(int)alljets.size(); i++)
    {
            index_dR.push_back(-1);

    }
    
   double min_dR=1;
   do{
       min_dR=1;
       index_i=-1;
       index_j=-1;
        for(int i=0; i<(int)alljets.size(); i++)
        {
            if(alljets.at(i).Pt()<10)continue;
            if(index_dR[i]>-1)continue;
            TLorentzVector ijet=alljets.at(i);
             
            for(int j=0; j<(int)alljets.size(); j++)
            {
                if(i==j)continue;
                if(alljets.at(j).Pt()<10)continue;
                if(index_dR[j]>-1)continue;
                TLorentzVector jjet=alljets.at(j);
                
                double dRij=ijet.DeltaR(jjet);
                
                if(dRij>=1)continue;
                
                if(dRij<min_dR)
                {
                    min_dR=dRij;
                    index_i=i;
                    index_j=j;
                    
                } 
            }
        }
        if(index_i>=0)
        {
            index_dR[index_i]=index_j;
            index_dR[index_j]=index_i;
            index_i=-1;
            index_j=-1;
        }
        
      }   
     while(min_dR<1);
    
     
     vector<int> used_index;
     
     for(int i=0; i<(int)alljets.size(); i++)
     {
         bool flag=false;
         for(int k=0; k<(int)used_index.size(); k++)
         {
             if(used_index[k]==i)flag=true;
        }
        if(flag)continue;
         
        if(index_dR[i]<0)
        {
                if(alljets.at(i).Pt()<30)continue;
                if(fabs(alljets.at(i).Eta())>2.4)continue;
                jets_tlv.push_back(alljets.at(i));
                new_btags.push_back(allbtags.at(i));
                
        }
        else
        {
            if(index_dR[i]>-1)
            {
                TLorentzVector temp = alljets.at(i) + alljets.at((index_dR[i]));
                used_index.push_back(index_dR[i]);
                if(temp.Pt()<30)continue;
                if(fabs(temp.Eta())>2.4)continue;
                jets_tlv.push_back(temp);
                new_btags.push_back(allbtags.at(i)*(allbtags.at(i)>allbtags.at(index_dR[i])) + allbtags.at(index_dR[i])*(allbtags.at(index_dR[i])>allbtags.at(i)));
            }
        }
        
        
     }
     
        for(int i=0; i<(int)jets_tlv.size(); i++) 
        {
                for(int j=0; j<(int)jets_tlv.size(); j++) 
                {
                               double wi = new_btags.at(i);
                               double wj = new_btags.at(j);
//                                 //if(i==j || (wi<0.244 && wj<0.244) || (wi<0 || wj<0))continue;
                                if(i==j || (wi<btag_wp && wj<btag_wp))continue;
                                if(wi>btag_wp && wj>btag_wp){nb_tag.push_back(2); }
                                else{nb_tag.push_back(1); }
                                b1_id.push_back(i);
                                b2_id.push_back(j);
                }
        }
     
    
}    
    if(b1_id.size()<2){
        nSol=0;
        return;
    }    
   //... 
    
    
    

    ///jets loop
    /// Anya
    MeanSol meanSol(172.5);
    double max_sum_weight=0;
    int nbtag=0, isHaveSol;

    ///

    nSol=0;
    for(int ib=0; ib<(int)b1_id.size(); ib++) {
        int j1=b1_id[ib];
        int j2=b2_id[ib];
//         if((*jets)[j1].Pt()<30 || (*jets)[j2].Pt()<30)continue;
//         if(fabs((*jets)[j1].Eta())>2.4 || fabs((*jets)[j2].Eta())>2.4)continue;
        TLorentzVector l_temp, al_temp, b_temp, bbar_temp, met_temp;
        l_temp=leptonMinus_tlv;
        al_temp=leptonPlus_tlv;
        b_temp=jets_tlv.at(j1);
        bbar_temp=jets_tlv.at(j2);
        met_temp.SetXYZM(met->Px(), met->Py(), 0, 0);

        if((al_temp + b_temp).M()>180 || (l_temp + bbar_temp).M()>180)continue;

//           double b_w=new_btags.at(j1)/(1-new_btags.at(j1));
//           double bbar_w=new_btags.at(j2)/(1-new_btags.at(j2));
//             double b_w=1;
//          double bbar_w=1;

//          TRandom3 r((int)(( leptonMinus_tlv.Pt() - (int)(leptonMinus_tlv.Pt()) )*1000000000)); ///random seed
//  	gRandom->SetSeed((int)(( leptonMinus_tlv.Pt() - (int)(leptonMinus_tlv.Pt()) )*1000000000));

    TRandom3 r((int)(( jets_tlv[0].Pt() - (int)(jets_tlv[0].Pt()) )*1000000000)); ///random seed
    gRandom->SetSeed((int)(( jets_tlv[0].Pt() - (int)(jets_tlv[0].Pt()) )*1000000000));


          
        TVector3 vX_reco =  - b_temp.Vect() - bbar_temp.Vect() - l_temp.Vect() - al_temp.Vect() - met_temp.Vect();
       

        for(int sm=0; sm<100; sm++) {
            TLorentzVector b_sm=b_temp;
            TLorentzVector bbar_sm=bbar_temp;
            TLorentzVector met_sm;//=met_temp;
            TLorentzVector l_sm=l_temp;
            TLorentzVector al_sm=al_temp;
            TLorentzVector vX_sm;

            

            double fB=h_jetEres->GetRandom();//fB=1;  //sm off
            double xB=sqrt((fB*fB*b_sm.E()*b_sm.E()-b_sm.M2())/(b_sm.P()*b_sm.P()));
            double fBbar=h_jetEres->GetRandom();//fBbar=1; //sm off
            double xBbar=sqrt((fBbar*fBbar*bbar_sm.E()*bbar_sm.E()-bbar_sm.M2())/(bbar_sm.P()*bbar_sm.P()));
                           
            double fL=h_lepEres->GetRandom();//fL=1; //sm off
            double xL=sqrt((fL*fL*l_sm.E()*l_sm.E()-l_sm.M2())/(l_sm.P()*l_sm.P()));
            double faL=h_lepEres->GetRandom();//faL=1;  //sm off
            double xaL=sqrt((faL*faL*al_sm.E()*al_sm.E()-al_sm.M2())/(al_sm.P()*al_sm.P()));
                           
            b_sm.SetXYZT(b_sm.Px()*xB,b_sm.Py()*xB,b_sm.Pz()*xB,b_sm.E()*fB);
            angle_rot(h_jetAngleRes->GetRandom(),0.001,b_sm,b_sm);
                           
            bbar_sm.SetXYZT(bbar_sm.Px()*xBbar,bbar_sm.Py()*xBbar,bbar_sm.Pz()*xBbar,bbar_sm.E()*fBbar);    
            angle_rot(h_jetAngleRes->GetRandom(),0.001,bbar_sm,bbar_sm);
                                
            l_sm.SetXYZT(l_sm.Px()*xL,l_sm.Py()*xL,l_sm.Pz()*xL,l_sm.E()*fL);
            angle_rot(h_lepAngleRes->GetRandom(),0.001,l_sm,l_sm);
                           
            al_sm.SetXYZT(al_sm.Px()*xaL,al_sm.Py()*xaL,al_sm.Pz()*xaL,al_sm.E()*faL);
            angle_rot(h_lepAngleRes->GetRandom(),0.001,al_sm,al_sm);
                           
// met Pt+angle smearing
//             double fX=1;
//             double dAX=0;
//             for(int i=0;i<((int)(ptBins.size()));i++)
//             {
//                   if(vX_reco.Pt()>ptBins[i]&&vX_reco.Pt()<=ptBins[i+1])
//                   {
//                        //fX=h_metPtres[i]->GetRandom();
//                        //dAX=h_metAngleRes[i]->GetRandom();
//                        
//                        fX=1;
//                         dAX=0;
//                   }
//             }
//             double tempX= vX_reco.Px()*fX;
//             double tempY= vX_reco.Py()*fX;
//             if(r.Rndm()>0.5)dAX=-dAX;
//             vX_sm.SetXYZM(tempX*cos(dAX)-tempY*sin(dAX),tempX*sin(dAX)+tempY*cos(dAX),0,0);
//                            
// ...

//met Pt+angle smearing
            double fPx=1;
            double fPy=0;
            for(int i=0;i<((int)(ptBins.size()));i++)
            {
                  if(vX_reco.Pt()>ptBins[i]&&vX_reco.Pt()<=ptBins[i+1])
                  {
                       //fPx=h_metPxRes[i]->GetRandom();
                       //fPy=h_metPyRes[i]->GetRandom();
                       fPx=1;
                       fPy=1;
                  }
            }
            double tempX= vX_reco.Px()*fPx;
            double tempY= vX_reco.Py()*fPy;
            vX_sm.SetXYZM(tempX,tempY,0,0);
                           
       
//...
            TVector3 metV3_sm= -b_sm.Vect()-bbar_sm.Vect()-l_sm.Vect()-al_sm.Vect()-vX_sm.Vect();
            met_sm.SetXYZM(metV3_sm.Px(),metV3_sm.Py(),0,0);
            
            
            
            ///Anya
           
//            KinematicReconstruction_LSroutines tp_sm(0.0,0.0,h_wmass->GetRandom(),h_wmass->GetRandom(),(*h_nwcuts));
            KinematicReconstruction_LSroutines tp_sm(0.0,0.0,h_wmass->GetRandom(),h_wmass->GetRandom(),(*h_neuEta_w));
//              KinematicReconstruction_LSroutines tp_sm(0.0,0.0,h_wmass->GetRandom(),h_wmass->GetRandom(),hvE);
//             KinematicReconstruction_LSroutines tp_sm(0.0,0.0,h_wmass->GetRandom(),h_wmass->GetRandom(),hvE,(*h_neuEta_w));
//              KinematicReconstruction_LSroutines tp_sm(0.0,0.0,h_wmass->GetRandom(),h_wmass->GetRandom(),(*h_costheta_w),1);
            ///
            tp_sm.SetConstraints(al_sm, l_sm, b_sm, bbar_sm, met_sm.Px(), met_sm.Py());

            /// Anya
            if(tp_sm.GetNsol()>0){
            for(int i=0; i<=tp_sm.GetNsol()*0; i++) {
                   // meanSol.Add(tp_sm.GetTtSol()->at(i).top,tp_sm.GetTtSol()->at(i).topbar,tp_sm.GetTtSol()->at(i).neutrino,tp_sm.GetTtSol()->at(i).neutrinobar,1);
                  //meanSol.Add(tp_sm.GetTtSol()->at(i).top,tp_sm.GetTtSol()->at(i).topbar,tp_sm.GetTtSol()->at(i).neutrino,tp_sm.GetTtSol()->at(i).neutrinobar,(tp_sm.GetTtSol()->at(i).lepEw));//*b_w*bbar_w
                  double mbl_weight=h_mbl_w->GetBinContent(h_mbl_w->FindBin((al_sm+b_sm).M()))*h_mbl_w->GetBinContent(h_mbl_w->FindBin((l_sm+bbar_sm).M()))/100000000;
                  meanSol.Add(tp_sm.GetTtSol()->at(i).top,tp_sm.GetTtSol()->at(i).topbar,tp_sm.GetTtSol()->at(i).neutrino,tp_sm.GetTtSol()->at(i).neutrinobar,mbl_weight);//
                  //meanSol.Add(tp_sm.GetTtSol()->at(i).top,tp_sm.GetTtSol()->at(i).topbar,tp_sm.GetTtSol()->at(i).neutrino,tp_sm.GetTtSol()->at(i).neutrinobar,(tp_sm.GetTtSol()->at(i).vw));//

                   
             }
            }
            
            if(tp_sm.GetNsol()>0){isHaveSol=1; nSol++; }
            ///
///Anya comment
//             if(!(tp_sm.GetNsol()<1 || tp_sm.GetNsol()==1 || tp_sm.GetNsol()==3)) {
//                 if(tp_sm.GetTtSol()->at(0).vw>vw_max){
//                     nSol++;
//
//                     vw_max=tp_sm.GetTtSol()->at(0).vw;
//                     sol.jetB = b_temp;
//                     sol.jetBbar = bbar_temp;
//                     sol.lm = leptonMinus_tlv;
//                     sol.lp = leptonPlus_tlv;
//                     sol.met = met_temp;
//                     sol.neutrino = tp_sm.GetTtSol()->at(0).neutrino;
//                     sol.neutrinoBar = tp_sm.GetTtSol()->at(0).neutrinobar;
//                     sol.weight = tp_sm.GetTtSol()->at(0).vw;
//                     sol.Wplus = sol.lp + sol.neutrino;
//                     sol.Wminus = sol.lm + sol.neutrinoBar;
//                     sol.top = sol.Wplus + sol.jetB;
// //                     cout << "vw: " << tp_m.GetTtSol()->at(0).vw << "pt: " << sol.top.Pt() << endl;
//                     sol.topBar = sol.Wminus + sol.jetBbar;
//                     sol.ttbar = sol.top + sol.topBar;
//                     sol.jetB_index = j1;
//                     sol.jetBbar_index = j2;
//                     sol.ntags = nb_tag[ib];
//                 }
//             }
///
			}
	/*smearing*/


        if(isHaveSol) {
            if(nb_tag[ib]==nbtag) {
                if(meanSol.GetSumWeight()>max_sum_weight) {
                    max_sum_weight=meanSol.GetSumWeight();
                    meanSol.GetMeanSol(sol.top, sol.topBar, sol.neutrino, sol.neutrinoBar);
                    sol.jetB = b_temp;
                    sol.jetBbar = bbar_temp;
                    sol.lm = leptonMinus_tlv;
                    sol.lp = leptonPlus_tlv;
                    sol.met = met_temp;
                    sol.weight = 1;//chto-to chto bollshe nulya
                    sol.Wplus = sol.lp + sol.neutrino;
                    sol.Wminus = sol.lm + sol.neutrinoBar;
                    sol.ttbar = sol.top + sol.topBar;
                    sol.jetB_index = b1_id[ib];
                    sol.jetBbar_index = b2_id[ib];
                    sol.ntags = nb_tag[ib];
                }
            }
            else if(nb_tag[ib]>nbtag) {
                nbtag=nb_tag[ib];
                max_sum_weight=meanSol.GetSumWeight();
                meanSol.GetMeanSol(sol.top, sol.topBar, sol.neutrino, sol.neutrinoBar);
                sol.jetB = b_temp;
                sol.jetBbar = bbar_temp;
                sol.lm = leptonMinus_tlv;
                sol.lp = leptonPlus_tlv;
                sol.met = met_temp;
                sol.weight = 1;//chto-to chto bollshe nulya
                sol.Wplus = sol.lp + sol.neutrino;
                sol.Wminus = sol.lm + sol.neutrinoBar;
                sol.ttbar = sol.top + sol.topBar;
                sol.jetB_index = b1_id[ib];
                sol.jetBbar_index = b2_id[ib];
                sol.ntags = nb_tag[ib];
            }
        }

        meanSol.Clear();
///

    } ///end jets loop



}       // End of KinematicReconstruction constructor








int KinematicReconstruction::GetNSol()const
{
    return nSol;
}



struct_KinematicReconstruction KinematicReconstruction::GetSol()const
{
    return sol;
}

void KinematicReconstruction::loadData()
{
    
//     // W mass

    TString data_path = ttbar::DATA_PATH();
    data_path.Append("/KinReco_wmass.root");
    TFile wmassfile(data_path);
    h_wmass = (TH1F*)wmassfile.Get("W_mass");
    h_wmass->SetDirectory(0);
    wmassfile.Close();
    
    // jet resolution
    TString data_path1 = ttbar::DATA_PATH();
    data_path1.Append("/KinReco_d_angle_jet.root");
    TFile danglejetfile(data_path1);
    h_jetAngleRes = (TH1F*)danglejetfile.Get("d_angle_jet");
    h_jetEres = (TH1F*)danglejetfile.Get("fE");
    h_jetAngleRes->SetDirectory(0);
    h_jetEres->SetDirectory(0);
    danglejetfile.Close();
    //
    
    //lepton resolution
    TString data_path2 = ttbar::DATA_PATH();
    data_path2.Append("/KinReco_d_angle_lep.root");
    TFile lepangleresfile(data_path2);
    h_lepAngleRes = (TH1F*)lepangleresfile.Get("d_angle_jet");
    h_lepEres = (TH1F*)lepangleresfile.Get("fE");
    h_lepAngleRes->SetDirectory(0);
    h_lepEres->SetDirectory(0);
    lepangleresfile.Close();
    //
// 
//     //MET resolution
    
    ptBins =  {0,7,13,18,27,37,48,59,70,100,200,500,1000,1500};
    TString data_path3 = ttbar::DATA_PATH();
    data_path3.Append("/KinReco_rmshistA_dAngle_vs_Pt.root");
    TFile metangleresfile(data_path3);
    for(int i=0;i<13;i++)
    {
        char temp_name[100];
        sprintf(temp_name,"bin_%.0f_%.0f",ptBins[i],ptBins[i+1]);
        h_metAngleRes[i]=(TH1F*)metangleresfile.Get(temp_name);
        sprintf(temp_name,"metAng_bin_%.0f_%.0f",ptBins[i],ptBins[i+1]);
        h_metAngleRes[i]->SetName(temp_name);
        h_metAngleRes[i]->SetDirectory(0);
    }
    metangleresfile.Close();
    
    TString data_path4 = ttbar::DATA_PATH();
    data_path4.Append("/KinReco_rmshistA_fPt_vs_Pt.root");
    TFile metptresfile(data_path4);
    for(int i=0;i<13;i++)
    {
        char temp_name[100];
        sprintf(temp_name,"bin_%.0f_%.0f",ptBins[i],ptBins[i+1]);
        h_metPtres[i]=(TH1F*)metptresfile.Get(temp_name);
        sprintf(temp_name,"metPt_bin_%.0f_%.0f",ptBins[i],ptBins[i+1]);
        h_metPtres[i]->SetName(temp_name);
        h_metPtres[i]->SetDirectory(0);
    }
    metptresfile.Close();
    
   //met px res
    TString data_path41 = ttbar::DATA_PATH(); 
    data_path41.Append("/KinReco_rmshist_fPx_vs_Pt.root");
    TFile metpxresfile(data_path41);
    for(int i=0;i<13;i++)
    {
        char temp_name[100];
        sprintf(temp_name,"bin_%.0f_%.0f",ptBins[i],ptBins[i+1]);
        h_metPxRes[i]=(TH1F*)metpxresfile.Get(temp_name);
        sprintf(temp_name,"metPx_bin_%.0f_%.0f",ptBins[i],ptBins[i+1]);
        h_metPxRes[i]->SetName(temp_name);
        h_metPxRes[i]->SetDirectory(0);
    }
    metpxresfile.Close();
  //...   
    
  //met py res
    TString data_path42 = ttbar::DATA_PATH(); 
    data_path42.Append("/KinReco_rmshist_fPy_vs_Pt.root");
    TFile metpyresfile(data_path42);
    for(int i=0;i<13;i++)
    {
        char temp_name[100];
        sprintf(temp_name,"bin_%.0f_%.0f",ptBins[i],ptBins[i+1]);
        h_metPyRes[i]=(TH1F*)metpyresfile.Get(temp_name);
        sprintf(temp_name,"metPy_bin_%.0f_%.0f",ptBins[i],ptBins[i+1]);
        h_metPyRes[i]->SetName(temp_name);
        h_metPyRes[i]->SetDirectory(0);
    }
    metpyresfile.Close();
  //...   


    TString data_path5 = ttbar::DATA_PATH();
    data_path5.Append("/KinReco_wneutrinocuts.root");
    TFile fnw(data_path5);
    h_nwcuts = (TH1F*)fnw.Get("Eneu_true");
    h_nwcuts->SetDirectory(0);
    fnw.Close();
    
///  E 1d bins
        TString data_path6 = ttbar::DATA_PATH();
        data_path6.Append("/KinReco_wneutrino_E.root"); // no norm
//         data_path6.Append("/KinReco_wneutrino_E_normilyze.root"); // norm
        TFile frootNeut(data_path6);
        char hvE_name[20];
        
                        for(int i=0;i<6;i++)
                        {
                            sprintf(hvE_name,"Eneu_true%d",i+1);
                                    hvE[i] = (TH1F*)frootNeut.Get(hvE_name);
                                    hvE[i]->SetDirectory(0);
                        }
    frootNeut.Close();
///...

/// mbl

        TString data_path7 = ttbar::DATA_PATH();
        data_path7.Append("/KinReco_mbl.root");
        TFile fmbl(data_path7);
        h_mbl_w = (TH1F*)fmbl.Get("mbl_true");
        h_mbl_w->SetDirectory(0);
        fmbl.Close();
        
        TString data_path71 = ttbar::DATA_PATH();
        data_path71.Append("/KinReco_mbl_wrong.root");
        TFile fmbl_wrong(data_path71);
//         h_mbl_w = (TH1F*)fmbl_wrong.Get("mbl_true_wrong");
//         h_mbl_w->SetDirectory(0);
        fmbl_wrong.Close();
        
/// ...        
        
/// cos_theta*

        TString data_path8 = ttbar::DATA_PATH();
        data_path8.Append("/KinReco_costheta_true.root");
        TFile fcostheta(data_path8);
        h_costheta_w = (TH1F*)fcostheta.Get("cos_theta_true");
        h_costheta_w->SetDirectory(0);
        fcostheta.Close();
/// ...
        
/// neuEta
        TString data_path9 = ttbar::DATA_PATH();
        data_path9.Append("/KinReco_wneutrinoEta.root");
        TFile fneuEta(data_path9);
        h_neuEta_w = (TH1F*)fneuEta.Get("Etaneu_true");
        h_neuEta_w->SetDirectory(0);
        fneuEta.Close();
/// ...        
        
        
}

void KinematicReconstruction::kinReco(const LV& leptonMinus, const LV& leptonPlus, const VLV *jets, const std::vector<double> *btags, const LV* met, bool mass_loop_on)
{

    std::vector<struct_KinematicReconstruction> vect_sol;


    TLorentzVector leptonPlus_tlv = ttbar::LVtoTLV(leptonPlus);
    TLorentzVector leptonMinus_tlv = ttbar::LVtoTLV(leptonMinus);
    TLorentzVector met_tlv = ttbar::LVtoTLV(*met);

    std::vector<TLorentzVector> jets_tlv;
    for (const auto& jet : *jets) {
        jets_tlv.push_back(ttbar::LVtoTLV(jet));
    }

    vector<int> b1_id;
    vector<int> b2_id;
    vector<double> btag_ww;
    vector<int> nb_tag;

    for(int i=0; i<(int)btags->size(); i++) {
        for(int j=0; j<(int)btags->size(); j++) {
            double wi = btags->at(i);
            double wj = btags->at(j);
//             if(i==j || (wi<0.244 && wj<0.244) || (wi<0 || wj<0))continue;
            if(i==j || (wi<0.244 && wj<0.244))continue;
            btag_ww.push_back(wi + wj);

            if(wi>0.244 && wj>0.244){nb_tag.push_back(2); }
            else{nb_tag.push_back(1); }

            b1_id.push_back(i);
            b2_id.push_back(j);
        }
    }

    if(b1_id.size()<2) {
        nSol=0;
        return;
    }

    for(int i=0; i<(int)btag_ww.size() - 1; i++) {
        if(btag_ww[i]>=btag_ww[i+1]) continue;

        double aux = btag_ww[i];
        btag_ww[i] = btag_ww[i+1];
        btag_ww[i+1] = aux;
        int aix = b1_id[i];
        b1_id[i] = b1_id[i+1];
        b1_id[i+1] = aix;
        aix = b2_id[i];
        b2_id[i] = b2_id[i+1];
        b2_id[i+1] = aix;
        aix = nb_tag[i];
        nb_tag[i] = nb_tag[i+1];
        nb_tag[i+1] = aix;

        i=-1;

    }


    ///jets loop

    nSol=0;
    for(int ib=0; ib<(int)b1_id.size(); ib++) {
        int j1=b1_id[ib];
        int j2=b2_id[ib];
//         if((*jets)[j1].Pt()<30 || (*jets)[j2].Pt()<30)continue;
//         if(fabs((*jets)[j1].Eta())>2.4 || fabs((*jets)[j2].Eta())>2.4)continue;
        TLorentzVector l_temp, al_temp, b_temp, bbar_temp, met_temp;
        l_temp=leptonMinus_tlv;
        al_temp=leptonPlus_tlv;
        b_temp=jets_tlv.at(j1);
        bbar_temp=jets_tlv.at(j2);
        met_temp.SetXYZM(met->Px(), met->Py(), 0, 0);
//         if((al_temp + b_temp).M()>180 || (l_temp + bbar_temp).M()>180)continue;

        /*smearing*/
        double vw_max=0;
        if(!mass_loop_on){

//             TF1 fJet("fJet", "[0]*pow((x - 0), 0.5) + [1]");
//             fJet.SetParameters(4.18432, - 24.8944);
//
//             TF1 fLep("fLep", "[0]*pow((x - 0), 0.5) + [1]");
//             fLep.SetParameters(0.575716, - 3.11214);


            TRandom3 r(0); ///random seed

//             TF1 f1("f1", "[0] + [1]*x + [2]*x*x + [3]*x*x*x + [4]*x*x*x*x", 30, 580);
//             f1.SetParameters(1.06517e + 01, 3.58131e - 02, 7.44249e - 04, - 1.70968e - 06, 1.21316e - 09);

            double bRMS=(4.13*pow((b_temp.E() - 0), 0.5) - 27.32)/b_temp.E(); //fJet.Eval(b_temp.E())/b_temp.E(); //%
            double bbarRMS=(4.13*pow((bbar_temp.E() - 0), 0.5) - 27.32)/bbar_temp.E(); //fJet.Eval(bbar_temp.E())/bbar_temp.E(); //%
            double lRMS=(0.575716*pow((l_temp.E() - 0), 0.5) - 3.11214)/l_temp.E(); //fLep.Eval(l_temp.E())/l_temp.E(); //%
            double alRMS=(0.575716*pow((al_temp.E() - 0), 0.5) - 3.11214)/al_temp.E(); //fLep.Eval(al_temp.E())/al_temp.E(); //%


            TVector3 vX_reco =  - b_temp.Vect() - bbar_temp.Vect() - l_temp.Vect() - al_temp.Vect() - met_temp.Vect();

            double xRMS=20/vX_reco.Pt(); //%
            for(int sm=0; sm<100; sm++) {
                TLorentzVector b_sm=b_temp;
                TLorentzVector bbar_sm=bbar_temp;
                TLorentzVector met_sm=met_temp;
                TLorentzVector l_sm=l_temp;
                TLorentzVector al_sm=al_temp;


                double fB=r.Gaus(1, bRMS);
                double xB=sqrt((fB*fB*b_sm.E()*b_sm.E() - b_sm.M2())/(b_sm.P()*b_sm.P()));
                double fBbar=r.Gaus(1, bbarRMS);
                double xBbar=sqrt((fBbar*fBbar*bbar_sm.E()*bbar_sm.E() - bbar_sm.M2())/(bbar_sm.P()*bbar_sm.P()));

                double fL=r.Gaus(1, lRMS);
                double xL=sqrt((fL*fL*l_sm.E()*l_sm.E() - l_sm.M2())/(l_sm.P()*l_sm.P()));
                double faL=r.Gaus(1, alRMS);
                double xaL=sqrt((faL*faL*al_sm.E()*al_sm.E() - al_sm.M2())/(al_sm.P()*al_sm.P()));

                double xX=r.Gaus(1, xRMS);

//                 met_sm.SetXYZM(((b_sm.Px()*(1 - xB) + bbar_sm.Px()*(1 - xBbar))/(met_sm.Px()) + 1)*met_sm.Px(), ((b_sm.Py()*(1 - xB) + bbar_sm.Py()*(1 - xBbar))/(met_sm.Py()) + 1)*met_sm.Py(), 0, 0); // tollko b - jet
//                 met_sm.SetXYZM(((b_sm.Px()*(1 - xB) + bbar_sm.Px()*(1 - xBbar) + l_sm.Px()*(1 - xL) + al_sm.Px()*(1 - xaL))/(met_sm.Px()) + 1)*met_sm.Px(), ((b_sm.Py()*(1 - xB) + bbar_sm.Py()*(1 - xBbar) + l_sm.Py()*(1 - xL) + al_sm.Py()*(1 - xaL))/(met_sm.Py()) + 1)*met_sm.Py(), 0, 0); //only b - jet and lep

                met_sm.SetXYZM(((b_sm.Px()*(1 - xB) + bbar_sm.Px()*(1 - xBbar) + l_sm.Px()*(1 - xL) + al_sm.Px()*(1 - xaL) + vX_reco.Px()*(1 - xX))/(met_sm.Px()) + 1)*met_sm.Px(), ((b_sm.Py()*(1 - xB) + bbar_sm.Py()*(1 - xBbar) + l_sm.Py()*(1 - xL) + al_sm.Py()*(1 - xaL) + vX_reco.Py()*(1 - xX))/(met_sm.Py()) + 1)*met_sm.Py(), 0, 0); //all

                b_sm.SetXYZT(b_sm.Px()*xB, b_sm.Py()*xB, b_sm.Pz()*xB, b_sm.E()*fB);
                bbar_sm.SetXYZT(bbar_sm.Px()*xBbar, bbar_sm.Py()*xBbar, bbar_sm.Pz()*xBbar, bbar_sm.E()*fBbar);

                l_sm.SetXYZT(l_sm.Px()*xL, l_sm.Py()*xL, l_sm.Pz()*xL, l_sm.E()*fL);
                al_sm.SetXYZT(al_sm.Px()*xaL, al_sm.Py()*xaL, al_sm.Pz()*xaL, al_sm.E()*faL);

                KinematicReconstruction_LSroutines tp_sm(172.5, 4.8, 80.4, 0.0, 0.0);
                tp_sm.SetConstraints(al_sm, l_sm, b_sm, bbar_sm, met_sm.Px(), met_sm.Py());

                if(!(tp_sm.GetNsol()<1 || tp_sm.GetNsol()==1 || tp_sm.GetNsol()==3)) {
                    if(tp_sm.GetTtSol()->at(0).vw>vw_max) {
                        nSol++;

                        vw_max=tp_sm.GetTtSol()->at(0).vw;
                        sol.jetB = b_temp;
                        sol.jetBbar = bbar_temp;
                        sol.lm = leptonMinus_tlv;
                        sol.lp = leptonPlus_tlv;
                        sol.met = met_temp;
                        sol.neutrino = tp_sm.GetTtSol()->at(0).neutrino;
                        sol.neutrinoBar = tp_sm.GetTtSol()->at(0).neutrinobar;
                        sol.weight = tp_sm.GetTtSol()->at(0).vw;
                        sol.Wplus = sol.lp + sol.neutrino;
                        sol.Wminus = sol.lm + sol.neutrinoBar;
                        sol.top = sol.Wplus + sol.jetB;
//                         cout << "vw: " << tp_m.GetTtSol()->at(0).vw << "pt: " << sol.top.Pt() << endl;
                        sol.topBar = sol.Wminus + sol.jetBbar;
                        sol.ttbar = sol.top + sol.topBar;
                        sol.jetB_index = j1;
                        sol.jetBbar_index = j2;
                        sol.ntags = nb_tag[ib];
                    }

                }
            }
        }


        /*smearing*/
        /*mass scan*/

        if(mass_loop_on){
           for(double im=100; im<300.5; im+=1){
//                 if(1) {double im=172.5;

                KinematicReconstruction_LSroutines tp_m(im, 4.8, 80.4, 0.0, 0.0);

                tp_m.SetConstraints(al_temp, l_temp, b_temp, bbar_temp, met_temp.Px(), met_temp.Py());

//                 if(tp_m.GetNsol()<1 || tp_m.GetNsol()==1 || tp_m.GetNsol()==3) continue;
                if(tp_m.GetNsol()<1) continue;
                
                if(!(tp_m.GetTtSol()->at(0).vw>vw_max)) continue;
                
                nSol++;
                
                vw_max=tp_m.GetTtSol()->at(0).vw;
                sol.jetB = b_temp;
                sol.jetBbar = bbar_temp;
                sol.lm = leptonMinus_tlv;
                sol.lp = leptonPlus_tlv;
                sol.met = met_temp;
                sol.neutrino = tp_m.GetTtSol()->at(0).neutrino;
                sol.neutrinoBar = tp_m.GetTtSol()->at(0).neutrinobar;
                sol.weight = tp_m.GetTtSol()->at(0).vw;
                sol.Wplus = sol.lp + sol.neutrino;
                sol.Wminus = sol.lm + sol.neutrinoBar;
                sol.top = sol.Wplus + sol.jetB;
//                 cout << "vw: " << tp_m.GetTtSol()->at(0).vw << "pt: " << sol.top.Pt() << endl;
                sol.topBar = sol.Wminus + sol.jetBbar;
                sol.ttbar = sol.top + sol.topBar;
                sol.jetB_index = j1;
                sol.jetBbar_index = j2;
                sol.ntags = nb_tag[ib];
            }
        }

        /*mass scan*/

        if(vw_max>0){
            vect_sol.push_back(sol);
            //jeka
            //cout << "N tags:  " << sol.ntags << endl;
        }

    } ///end jets loop

    if(nSol>0){
        std::nth_element(begin(vect_sol), begin(vect_sol), end(vect_sol),
                         [](const struct_KinematicReconstruction& a, const struct_KinematicReconstruction& b){
                             return  b.ntags < a.ntags || (b.ntags == a.ntags && b.weight < a.weight);
                         });

        sol=vect_sol[0];
    }

}       // End of KinematicReconstruction constructor














