// Author: Kerstin Tackmann, Andreas Hoecker, Heiko Lacker

/**********************************************************************************
 *                                                                                *
 * Project: BaseSVDUnfold - data unfolding based on Singular Value Decomposition     *
 * Package: ROOT                                                                  *
 * Class  : BaseSVDUnfold                                                            *
 *                                                                                *
 * Description:                                                                   *
 *      Single class implementation of SVD data unfolding based on:               *
 *          A. Hoecker, V. Kartvelishvili,                                        *
 *          "SVD approach to data unfolding"                                      *
 *          NIM A372, 469 (1996) [hep-ph/9509307]                                 *
 *                                                                                *
 * Authors:                                                                       *
 *      Kerstin Tackmann <Kerstin.Tackmann@cern.ch>   - CERN, Switzerland         *
 *      Andreas Hoecker  <Andreas.Hoecker@cern.ch>    - CERN, Switzerland         *
 *      Heiko Lacker     <lacker@physik.hu-berlin.de> - Humboldt U, Germany       *
 *                                                                                *
 * Copyright (c) 2010:                                                            *
 *      CERN, Switzerland                                                         *
 *      Humboldt University, Germany                                              *
 *                                                                                *
 **********************************************************************************/

//////////////////////////////////////////////////////////////////////////
//                                                                      //
// BaseSVDUnfold                                                           //
//                                                                      //
// Data unfolding using Singular Value Decomposition (hep-ph/9509307)   //
// Authors: Kerstin Tackmann, Andreas Hoecker, Heiko Lacker             //
//                                                                      //
//////////////////////////////////////////////////////////////////////////

#ifndef BASESVDUNFOLD_H
#define BASESVDUNFOLD_H

#ifndef ROOT_TObject
#include "TObject.h"
#endif
#ifndef ROOT_TMatrixD
#include "TMatrixD.h"
#endif
#ifndef ROOT_TVectorD
#include "TVectorD.h"
#endif
#ifndef ROOT_TMatrixDSym
#include "TMatrixDSym.h"
#endif

class TH1D;
class TH2D;

class BaseSVDUnfold : public TObject {

public:

   // Constructor
   // Initialisation of unfolding
   // "bdat" - measured data distribution (number of events)
   // "Bcov" - covariance matrix for measured data distribution
   // "bini" - reconstructed MC distribution (number of events)
   // "xini" - truth MC distribution (number of events)
   // "Adet" - detector response matrix (number of events)
   BaseSVDUnfold();
   BaseSVDUnfold( const TH1D* bdat, const TH1D* bini, const TH1D* xini, const TH2D* Adet );
   BaseSVDUnfold( const TH1D* bdat, TH2D* Bcov, const TH1D* bini, const TH1D* xini, const TH2D* Adet );
   BaseSVDUnfold( const BaseSVDUnfold& other );

   // Destructor
   virtual ~BaseSVDUnfold(); 

   // Set option to normalize unfolded spectrum to unit area
   // "normalize" - switch 
   void     SetNormalize ( Bool_t normalize ) { fNormalize = normalize; }

   // Do the unfolding
   // "kreg"   - number of singular values used (regularisation)
   virtual TH1D*    Unfold       ( Int_t kreg );

   // Determine for given input error matrix covariance matrix of unfolded 
   // spectrum from toy simulation
   // "cov"    - covariance matrix on the measured spectrum, to be propagated
   // "ntoys"  - number of pseudo experiments used for the propagation
   // "seed"   - seed for pseudo experiments
   TH2D*    GetUnfoldCovMatrix( const TH2D* cov, Int_t ntoys, Int_t seed = 1 );

   // Determine covariance matrix of unfolded spectrum from finite statistics in 
   // response matrix
   // "ntoys"  - number of pseudo experiments used for the propagation
   // "seed"   - seed for pseudo experiments
   TH2D*    GetAdetCovMatrix( Int_t ntoys, Int_t seed=1 );

   // Regularisation parameter
   Int_t    GetKReg() const { return fKReg; }

   // Obtain the distribution of |d| (for determining the regularization)
   TH1D*    GetD() const;

   // Obtain the distribution of singular values
   TH1D*    GetSV() const;

   // Obtain the computed regularized covariance matrix
   TH2D*    GetXtau() const;

   // Obtain the computed inverse of the covariance matrix
   TH2D*    GetXinv() const;
   
   // Helper functions
   Double_t ComputeChiSquared( const TH1D& truspec, const TH1D& unfspec );

protected: 
   
   // Helper functions for vector and matrix operations
   void            FillCurvatureMatrix( TMatrixD& tCurv, TMatrixD& tC ) const;
   static Double_t GetCurvature       ( const TVectorD& vec, const TMatrixD& curv );

   void            InitHistos  ( );

   // Helper functions
   static void     H2V      ( const TH1D* histo, TVectorD& vec   );
   static void     H2Verr   ( const TH1D* histo, TVectorD& vec   );
   static void     V2H      ( const TVectorD& vec, TH1D& histo   );
   static void     H2M      ( const TH2D* histo, TMatrixD& mat   );
   static void     M2H      ( const TMatrixD& mat, TH2D& histo   );
   static TMatrixD MatDivVec( const TMatrixD& mat, const TVectorD& vec, Int_t zero=0 );
   static TVectorD CompProd ( const TVectorD& vec1, const TVectorD& vec2 );

   static TVectorD VecDiv                 ( const TVectorD& vec1, const TVectorD& vec2, Int_t zero = 0 );
   static void     RegularisedSymMatInvert( TMatrixDSym& mat, Double_t eps = 1e-3 );
   
   // Class members
   Int_t       fNdim;        //! Truth and reconstructed dimensions
   Int_t       fDdim;        //! Derivative for curvature matrix
   Bool_t      fNormalize;   //! Normalize unfolded spectrum to 1
   Int_t       fKReg;        //! Regularisation parameter
   TH1D*       fDHist;       //! Distribution of d (for checking regularization)
   TH1D*       fSVHist;      //! Distribution of singular values
   TH2D*       fXtau;        //! Computed regularized covariance matrix
   TH2D*       fXinv;        //! Computed inverse of covariance matrix

   // Input histos
   const TH1D* fBdat;        // measured distribution (data)
   TH2D* fBcov;        // covariance matrix of measured distribution (data)
   const TH1D* fBini;        // reconstructed distribution (MC)
   const TH1D* fXini;        // truth distribution (MC)
   const TH2D* fAdet;        // Detector response matrix

   // Evaluation of covariance matrices
   TH1D*       fToyhisto;    //! Toy MC histogram
   TH2D*       fToymat;      //! Toy MC detector response matrix
   Bool_t      fToyMode;     //! Internal switch for covariance matrix propagation
   Bool_t      fMatToyMode;  //! Internal switch for evaluation of statistical uncertainties from response matrix

   
   //ClassDef( BaseSVDUnfold, 0 ) // Data unfolding using Singular Value Decomposition (hep-ph/9509307)   
};

#endif
