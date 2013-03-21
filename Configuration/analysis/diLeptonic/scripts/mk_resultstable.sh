#!/bin/zsh
echo "\\\begin{table}[h]"
echo "	\\\begin{center}"
echo "		\\\caption{\\\small"
echo "		 Normalised differential cross section as a function of the \\\pt-ordered lepton observables: the transverse momentum ($ p_T^{Lead.l}$, $ p_T^{NLead.l}$) and the pseudorapidity ($\\\eta^{Lead.l}$, $\\\eta^{NLead.l}$).}"
echo "		\\\label{tab:diffxsecorderedlepton}"
echo "		\\\begin{tabular}{c|c||c|c|c|c}" 
echo "			\\\hline "
echo "			\\\hline            bin-center [GeV]     & bin [GeV] & $ 1/\\\sigma d\\\sigma/dp_T^{Lead.l}$ & stat. [\\\%] & sys. [\\\%] & total [\\\%] \\\\\\"
echo "		\\\hline"
tail -n +4  combined/HypLeptonpTLeadLaTeX.txt
echo "			\\\hline "
echo "			\\\hline            bin-center [GeV]     & bin [GeV] & $ 1/\\\sigma d\\\sigma/dp_T^{NLead.l}$ & stat. [\\\%] & sys. [\\\%] & total [\\\%] \\\\\\"
echo "		\\\hline"
tail -n +4  combined/HypLeptonpTNLeadLaTeX.txt
echo "			\\\hline"
echo "			\\\hline            bin-center       & bin  & $ 1/\\\sigma d\\\sigma/d\\\eta^{Lead.l}$ & stat. [\\\%] & sys. [\\\%] & total [\\\%] \\\\\\"
echo "			\\\hline"
tail -n +4 combined/HypLeptonEtaLeadLaTeX.txt
echo "			\\\hline"
echo "			\\\hline            bin-center       & bin  & $ 1/\\\sigma d\\\sigma/d\\\eta^{NLead.l}$ & stat. [\\\%] & sys. [\\\%] & total [\\\%] \\\\\\"
echo "			\\\hline"
tail -n +4 combined/HypLeptonEtaNLeadLaTeX.txt
echo "			\\\hline"
echo "			\\\hline            bin-center [GeV]      & bin [GeV] & $ 1/\\\sigma d\\\sigma/dp_T^{\\\ell\\\ell}$ & stat. [\\\%] & sys. [\\\%] & total [\\\%] \\\\\\"
echo "			\\\hline "
tail -n +4 combined/HypLLBarpTLaTeX.txt
echo "			\\\hline"
echo "			\\\hline            bin-center [GeV]      & bin [GeV] & $ 1/\\\sigma d\\\sigma/dm^{\\\ell\\\ell}$ & stat. [\\\%] & sys. [\\\%] & total [\\\%] \\\\\\"
echo "			\\\hline"
tail -n +4 combined/HypLLBarMassLaTeX.txt
echo "		\\\hline"
echo "  	\\\hline"
echo "		\\\end{tabular}"
echo "	\\\end{center}"
echo "\\\end{table}"
echo " "
echo "\\\begin{table}[h]"
echo "	\\\begin{center}"
echo "		\\\caption{\\\small"
echo "		 Normalised differential cross section as a function of lepton observables: the transverse momentum of the lepton pair $ p_T^{\\\ell\\\ell}$, and the invariant mass of the lepton pair $ m^{\\\ell\\\ell}$.}"
echo "		\\\label{tab:diffxseclep}"
echo "		\\\begin{tabular}{c|c||c|c|c|c}" 
echo "			\\\hline"
echo "			\\\hline            bin-center [GeV]      & bin [GeV] & $ 1/\\\sigma d\\\sigma/dp_T^{\\\ell\\\ell}$ & stat. [\\\%] & sys. [\\\%] & total [\\\%] \\\\\\"
echo "			\\\hline "
tail -n +4 combined/HypLLBarpTLaTeX.txt
echo "			\\\hline"
echo "			\\\hline            bin-center [GeV]      & bin [GeV] & $ 1/\\\sigma d\\\sigma/dm^{\\\ell\\\ell}$ & stat. [\\\%] & sys. [\\\%] & total [\\\%] \\\\\\"
echo "			\\\hline"
tail -n +4 combined/HypLLBarMassLaTeX.txt
echo "		\\\hline"
echo "  	\\\hline"
echo "		\\\end{tabular}"
echo "	\\\end{center}"
echo "\\\end{table}"
echo " "
echo "\\\begin{table}[h]"
echo "	\\\begin{center}"
echo "		\\\caption{\\\small "
echo "		Normalised differential cross section as a function of the \\\pt-ordered top-quark observables: the transverse momentum ($ p_T^{Lead.t}$, $ p_T^{NLead.t}$) and the rapidity ($ y^{Lead.t}$, $ y^{NLead.t}$).}"
echo "		\\\label{tab:diffxsecorederedtop}"
echo "		\\\begin{tabular}{c|c||c|c|c|c} "
echo "			\\\hline "
echo "			\\\hline            bin-center [GeV]      & bin [GeV] & $ 1/\\\sigma d\\\sigma/p_T^{t~{Lead.t}}$ & stat. [\\\%] & sys. [\\\%] & total [\\\%] \\\\\\"
echo "		\\\hline"
tail -n +4 combined/HypToppTLeadLaTeX.txt
echo "			\\\hline"
echo "			\\\hline            bin-center       & bin & $ 1/\\\sigma d\\\sigma/p_T^{t~{NLead.t}}$ & stat. [\\\%] & sys. [\\\%] & total [\\\%] \\\\\\"
echo "			\\\hline"
tail -n +4 combined/HypToppTNLeadLaTeX.txt
echo "			\\\hline"
echo "			\\\hline            bin-center       & bin & $ 1/\\\sigma d\\\sigma/y^{t~{Lead.t}}$ & stat. [\\\%] & sys. [\\\%] & total [\\\%] \\\\\\"
echo "			\\\hline"
tail -n +4 combined/HypTopRapidityLeadLaTeX.txt
echo "			\\\hline"
echo "			\\\hline            bin-center       & bin & $ 1/\\\sigma d\\\sigma/y^{t~{NLead.t}}$ & stat. [\\\%] & sys. [\\\%] & total [\\\%] \\\\\\"
echo "			\\\hline"
tail -n +4 combined/HypTopRapidityNLeadLaTeX.txt
echo "			\\\hline"
echo "		\\\end{tabular}"
echo "	\\\end{center}"
echo "\\\end{table}"
echo " "
echo "\\\begin{table}[h]"
echo "	\\\begin{center}"
echo "		\\\caption{\\\small "
echo "		Normalised differential cross section as a function of top quark observables, the transverse momentum of the top quarks, $ p_T^{t}$, the rapidity of the top quarks , $ y^{t}$, the transverse momentum of the top quark pair, $ p_T^{\ttbar}$ and the invariant mass of the quark pair $ m^{\ttbar}$.}"
echo "		\\\label{tab:diffxsectop}"
echo "		\\\begin{tabular}{c|c||c|c|c|c} "
echo "			\\\hline "
echo "			\\\hline            bin-center [GeV]      & bin [GeV] & $ 1/\\\sigma d\\\sigma/d p_T^{\\\ttbar}$ & stat. [\\\%] & sys. [\\\%] & total [\\\%] \\\\\\"
echo "			\\\hline "
tail -n +4 combined/HypTTBarpTLaTeX.txt
echo "			\\\hline" 
echo "			\\\hline            bin-center       & bin & $ 1/\\\sigma d\\\sigma/y^{\\\ttbar}$ & stat. [\\\%] & sys. [\\\%] & total [\\\%] \\\\\\"
echo "			\\\hline"
tail -n +4 combined/HypTTBarRapidityLaTeX.txt
echo "			\\\hline" 
echo "			\\\hline            bin-center [GeV]      & bin [GeV] & $ 1/\\\sigma d\\\sigma/dm^{\\\ttbar}$ & stat. [\\\%] & sys. [\\\%] & total [\\\%] \\\\\\"
echo "			\\\hline"		
tail -n +4 combined/HypTTBarMassLaTeX.txt
echo "                  \\\hline"
echo "  		\\\hline"
echo "		\\\end{tabular}"
echo "	\\\end{center}"
echo "\\\end{table}"
echo " "
echo "\\\begin{table}[h]"
echo "	\\\begin{center}"
echo "		\\\caption{\\\small"
echo "                  Normalised differential cross section as a function of the \\\pt-ordered bjet observables: the transverse momentum ($ p_T^{Lead.b-jet}$, $ p_T^{NLead.b-jet}$) and the pseudorapidity ($\\\eta^{Lead.b-jet}$, $\\\eta^{NLead.b-jet}$).}"
echo "		\\\label{tab:diffxsecorderedbjet}"
echo "		\\\begin{tabular}{c|c||c|c|c|c}"
echo "			\\\hline" 
echo "			\\\hline            bin-center [GeV]      & bin [GeV] & $ 1/\\\sigma d\\\sigma/p_T^{b~{Lead.b-jet}}$ & stat. [\\\%] & sys. [\\\%] & total [\\\%] \\\\\\"
echo "		\\\hline"
tail -n +4 combined/HypBJetpTLeadLaTeX.txt
echo "			\\\hline" 
echo "			\\\hline            bin-center [GeV]      & bin [GeV] & $ 1/\\\sigma d\\\sigma/p_T^{b~{NLead.b-jet}}$ & stat. [\\\%] & sys. [\\\%] & total [\\\%] \\\\\\"
echo "		\\\hline"
tail -n +4 combined/HypBJetpTNLeadLaTeX.txt
echo "			\\\hline"
echo "			\\\hline            bin-center       & bin & $ 1/\\\sigma d\\\sigma/\\\eta^{Lead.b-jet}$ & stat. [\\\%] & sys. [\\\%] & total [\\\%] \\\\\\"
echo "			\\\hline" 
tail -n +4 combined/HypBJetEtaLeadLaTeX.txt
echo "			\\\hline"
echo "			\\\hline            bin-center       & bin & $ 1/\\\sigma d\\\sigma/\\\eta^{NLead.b-jet}$ & stat. [\\\%] & sys. [\\\%] & total [\\\%] \\\\\\"
echo "			\\\hline" 
tail -n +4 combined/HypBJetEtaNLeadLaTeX.txt
echo "  		\\\hline"
echo "		\\\end{tabular}"
echo "	\\\end{center}"
echo "\\\end{table}"
echo " "
echo "\\\begin{table}[h]"
echo "	\\\begin{center}"
echo "		\\\caption{\\\small"
echo "                  Normalised differential cross section as a function of the invariant mass of the lepton-b-jet system}"
echo "		\\\label{tab:diffxseclbmass}"
echo "		\\\begin{tabular}{c|c||c|c|c|c}"
echo "			\\\hline" 
echo "			\\\hline            bin-center       & bin & $ 1/\\\sigma d\\\sigma/dm^{\\\ell  b  } $ & stat. [\\\%] & sys. [\\\%] & total [\\\%] \\\\\\"
echo "			\\\hline" 
tail -n +4 combined/HypLeptonBjetMassLaTeX.txt
echo "  		\\\hline"
echo "		\\\end{tabular}"
echo "	\\\end{center}"
echo "\\\end{table}"