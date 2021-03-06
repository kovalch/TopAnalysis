import FWCore.ParameterSet.Config as cms

################################################################################
# Dataset: /WZ_TuneZ2_7TeV_pythia6_tauola/Summer11-PU_S4_START42_V11-v1/AODSIM # 
# Events : 4265243                                                             #
# xSec   : 18.2 (NLO MCFM)                                                     #
# eff    : 1.0                                                                 #
################################################################################


maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource", fileNames = cms.untracked.vstring( *(
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/FE05A6E5-6DA2-E011-8066-003048679076.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/FCFF8852-62A2-E011-AD1B-00261894386A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/FAD35200-64A2-E011-B1DD-002618943985.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/FAACFC06-62A2-E011-A8D8-002354EF3BD0.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/FA416492-66A2-E011-8389-00261894389E.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/F8890307-62A2-E011-9094-00261894396D.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/F8500764-67A2-E011-9FD4-0026189438FC.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/F84F638A-5EA2-E011-ADD1-002618943943.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/F6580E09-60A2-E011-A9B9-003048679182.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/F638C4FE-65A2-E011-A80A-002618943939.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/F63065DF-78A2-E011-9B52-00304867BECC.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/F245AC5E-74A2-E011-AD3D-003048678FE0.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/F0A18775-6EA2-E011-ACD8-003048678FE4.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/EEB55E52-62A2-E011-8B55-0018F3D0967E.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/EEA663A5-69A2-E011-9DFD-00304867BFF2.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/EE4A2263-67A2-E011-B542-0026189438B3.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/ECB79E58-20A3-E011-8007-0026189438F2.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/EC3F5DAD-67A2-E011-858A-003048678FC4.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/EA45A158-88A2-E011-A83F-001A92971B88.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/EA210644-66A2-E011-8880-002618943927.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/E8BF96DA-5CA2-E011-9DED-002618943933.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/E8B7A3E5-60A2-E011-BD11-00261894396E.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/E86D13AF-67A2-E011-BBB5-002354EF3BDF.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/E6D964B2-5DA2-E011-B501-0026189438FC.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/E67E4371-70A2-E011-9204-00304867915A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/E60E1E4E-6FA2-E011-924A-0030486790B8.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/E0958D9A-64A2-E011-826F-0026189438BF.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/DEC68C6B-65A2-E011-8904-00261894396A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/DCFC3475-61A2-E011-AA0D-00304867C0F6.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/DCBA79AD-67A2-E011-81DC-0026189438D2.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/DC4B7DD7-71A2-E011-8179-002354EF3BE0.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/DAFA8601-64A2-E011-8D04-002618943860.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/D8174F88-68A2-E011-84E3-003048678B86.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/D80C9E41-66A2-E011-B180-00261894387B.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/D6D8CD5B-6BA2-E011-8482-0018F3D0967E.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/D6BD64D1-6AA2-E011-8A4A-00304867915A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/D4CF2999-78A2-E011-AFA8-003048D3FC94.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/D2EC9B85-68A2-E011-9B17-002618943829.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/D2A56A1D-67A2-E011-85D6-002618943821.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/D2733B65-67A2-E011-8884-002354EF3BD0.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/D0EAC985-75A2-E011-B8BD-003048679076.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/D03DDFA0-88A2-E011-B295-001A92971B8E.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/D000826F-72A2-E011-AC0F-003048679296.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/CEBFB066-67A2-E011-93F8-00304867915A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/CCF83402-66A2-E011-BCEA-002618943821.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/CC837DE3-6FA2-E011-94C9-0018F3D0967E.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/CA2FB00E-6DA2-E011-AC6E-002618FDA28E.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/CA1F5AF9-65A2-E011-98A3-0026189438A7.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/C61098A4-58A2-E011-8DF7-0026189438FC.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/C4F431DF-6FA2-E011-888D-003048679296.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/C45DE376-72A2-E011-99A0-003048679296.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/C2CC2A20-65A2-E011-A9FE-002618943969.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/C29C594E-6FA2-E011-863C-003048679076.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/C22F1DE5-6DA2-E011-807D-002618943948.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/BAE58401-64A2-E011-86F4-002618943811.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/BA023962-5FA2-E011-9DB0-002354EF3BDB.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/B8F49275-61A2-E011-9A2A-0026189437EB.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/B8B16F0C-6DA2-E011-8FBB-002618943877.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/B44EC2AD-67A2-E011-A035-0026189438A7.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/B2EE0870-70A2-E011-B029-002618943800.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/B2D63124-92A2-E011-9E9B-002618943980.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/B28DDF6F-82A2-E011-B1FC-0018F3D0967E.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/B270050E-6DA2-E011-B40E-002354EF3BDA.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/B03BA18A-68A2-E011-A4B6-00304867BFF2.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/B02F58B4-93A2-E011-8FC5-002618943896.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/AAE47269-65A2-E011-BAD7-00261894393F.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/A6F31205-6FA2-E011-9E5D-003048678F9C.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/A6EB584E-60A2-E011-84B4-002354EF3BDF.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/A6CA0DC2-6CA2-E011-8D77-003048678B0A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/A485C64D-60A2-E011-ACC6-002618943969.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/A2B7C9FF-70A2-E011-91FC-00261894393C.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/A2AED506-62A2-E011-90A2-0026189437FA.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/A25767E3-6DA2-E011-8303-0030486790B8.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/A0AE9BA2-6BA2-E011-84AB-002618943964.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/9EC599ED-8FA2-E011-BAAB-001A92971BD8.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/9EBB195A-20A3-E011-8456-0026189438F7.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/9CA5AA28-70A2-E011-8A8C-003048D3FC94.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/9C1E4448-66A2-E011-A0CF-00304867915A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/9A5A309B-60A2-E011-BB56-00261894393B.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/982EC51B-74A2-E011-8F43-002618943919.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/96AF8B47-71A2-E011-A61B-003048679076.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/94E9EB98-64A2-E011-8FD8-00261894393F.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/9437204D-6FA2-E011-AD6C-00261894389C.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/924D3031-6CA2-E011-AB45-002618943971.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/923CAF76-72A2-E011-AD21-003048679296.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/8E5492E9-20A3-E011-8792-00304867926C.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/8E43D493-64A2-E011-871B-00261894396A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/8E295786-68A2-E011-93D4-003048678FD6.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/8E055FA6-69A2-E011-AF26-00261894388F.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/8C3C568C-66A2-E011-9C02-0026189438FC.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/8A96244E-6FA2-E011-9963-003048679048.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/8A2F1F0D-6DA2-E011-9C2C-002354EF3BE3.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/88FD8D3F-73A2-E011-A7EA-00261894389C.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/8687B93A-6AA2-E011-8A66-002354EF3BD0.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/842271CD-77A2-E011-9030-003048679076.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/8269B806-62A2-E011-9D4A-0026189438AE.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/8231DBB8-79A2-E011-8769-00304867915A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/80A25D5A-91A2-E011-8F4F-001A92971B72.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/80064783-8EA2-E011-81B9-00261894385A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/7C7DCAF5-7FA2-E011-A88A-001A9281172C.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/7C525420-65A2-E011-8029-002618943972.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/7AFAF036-75A2-E011-86E8-003048D3FC94.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/78FD8F59-20A3-E011-A598-002618943970.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/78E356E8-76A2-E011-9810-003048679296.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/78B63154-62A2-E011-B85E-002354EF3BDF.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/7449C9A1-6BA2-E011-8DEB-002618943963.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/72F59A2B-70A2-E011-BB43-003048679076.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/72B85269-7BA2-E011-841E-003048679076.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/72549E02-64A2-E011-B017-003048678FB8.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/70EA51CD-6AA2-E011-BED4-002618943964.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/703B74A6-69A2-E011-AB86-003048678B86.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/702D0F2A-63A2-E011-867C-002618943811.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/6E1156A5-69A2-E011-AD0D-0030486792A8.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/6CA19F26-70A2-E011-8237-002618943916.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/6AA9E547-6CA2-E011-8133-003048678FE4.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/68BDF52C-5BA2-E011-AC95-002618943800.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/6822825D-6BA2-E011-BADA-00304867BEDE.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/66D25EA7-69A2-E011-9795-003048D3FC94.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/6647FD00-5CA2-E011-B946-002618943880.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/6623077F-61A2-E011-AEDC-00261894392D.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/64F418FE-8DA2-E011-B819-003048D25B68.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/64A03C20-65A2-E011-8650-0026189437F0.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/645611CF-6CA2-E011-9954-002618943821.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/62A8841D-74A2-E011-AD50-0026189438CF.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/622ED1A5-69A2-E011-8B7B-002618943829.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/60FC0802-64A2-E011-8D68-00261894390A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/60FB58A1-6BA2-E011-B929-0030486790B8.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/604C7A90-73A2-E011-B61D-003048679076.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/60237CCF-6AA2-E011-B5FF-0030486792AC.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/5C6BA7F5-84A2-E011-948D-001A92810AEE.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/586C81E8-60A2-E011-B9AF-002618943800.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/585CDF6F-63A2-E011-9092-002618943978.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/56A88AAD-67A2-E011-BBB4-003048679182.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/56413805-6FA2-E011-AE29-003048679164.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/52D1DDE9-20A3-E011-8A84-002618943831.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/52465349-64A2-E011-A54B-002618943969.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/50EA719D-6DA2-E011-B13E-003048678BEA.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/4EFE3568-72A2-E011-9BC3-003048B835A2.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/4EED645B-6BA2-E011-A183-001A92971B32.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/4CFD8FC6-6CA2-E011-A70F-002618943821.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/4CF68185-68A2-E011-A0AD-00261894380A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/4CCC2EA7-69A2-E011-A532-0026189437FC.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/4CBB2172-67A2-E011-AC06-002618943821.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/4C2D10B2-67A2-E011-811B-00261894393B.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/4C24D68C-66A2-E011-9998-002618943821.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/4AF12906-60A2-E011-A1B5-0026189438D8.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/4ADCB7FA-65A2-E011-B8EC-0026189438AE.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/48E20052-62A2-E011-953D-002618943856.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/489F7D46-66A2-E011-8A5E-002354EF3BDF.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/482FB675-6EA2-E011-A9AA-003048679076.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/482C9FAC-74A2-E011-9E19-003048679076.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/46F7B81D-67A2-E011-A283-002618943896.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/46D3F58C-66A2-E011-A656-00248C0BE018.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/46BC3B01-64A2-E011-B7B3-0026189438BF.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/46A56321-65A2-E011-B90A-003048678FD6.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/44F9AEAE-67A2-E011-93B3-00261894385A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/44CEEBD9-5CA2-E011-9484-00261894397D.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/442B77A1-6BA2-E011-9307-0026189438BC.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/42E37E87-68A2-E011-8FC1-00304867BED8.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/42C0E134-6CA2-E011-B078-00304867918A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/40EEE5C2-6CA2-E011-9E9B-002618943981.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/40039986-68A2-E011-9183-002618943821.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/3EEFC606-62A2-E011-9619-002618943894.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/3ECD5838-75A2-E011-944B-00304867915A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/3EB6D728-63A2-E011-89ED-002354EF3BDD.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/3A8191C5-77A2-E011-A928-002354EF3BE3.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/38BA400D-6DA2-E011-8613-00304867915A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/38140107-81A2-E011-A27D-0018F3D0967A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/366346B1-67A2-E011-BEFB-00304867BFAE.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/361033AE-67A2-E011-BF7A-00304867920C.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/34CB1AAE-67A2-E011-A1FE-002618943829.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/322AFCD0-6AA2-E011-B86A-00304867918A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/307E7E76-6EA2-E011-88A9-003048679296.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/302C882B-70A2-E011-AB79-003048678FE0.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/301DAED6-71A2-E011-9941-003048678B30.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/2CE73A48-71A2-E011-843F-003048D3FC94.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/2C24AE43-66A2-E011-A69F-002618943896.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/2A41B8A7-69A2-E011-A2FF-003048678D9A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/2892F669-65A2-E011-BF3E-0026189438E3.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/26751439-6AA2-E011-8D7D-002618943856.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/246480A2-6BA2-E011-9581-003048678FEA.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/24166CF3-D1A2-E011-8205-003048679294.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/1E294013-6DA2-E011-80DD-003048678FEA.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/1CFF2D07-62A2-E011-B965-0026189438FD.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/1CCC57F0-86A2-E011-9508-0018F3D096F6.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/1AED0117-74A2-E011-AB80-002354EF3BDA.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/18A9639B-60A2-E011-BFD0-00261894396F.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/16C42E5B-8FA2-E011-AA71-00261894385A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/1654FC63-8DA2-E011-B128-00261894385A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/14DB8D03-64A2-E011-8480-003048678FD6.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/1253958B-5EA2-E011-AD5E-0026189438D4.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/1098FA74-EEA3-E011-82CB-002618943898.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/0C6662B2-5DA2-E011-9F25-00261894382D.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/0C022211-76A2-E011-98A6-0030486790A6.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/08733BDA-71A2-E011-AFED-003048679076.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/08729A5C-69A2-E011-BBDA-002618943884.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/06FE39A6-69A2-E011-8E3A-003048679084.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/06606268-72A2-E011-BCD0-00261894393C.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/0652B8CD-6AA2-E011-8E90-00304867BEDE.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/04BB3B00-71A2-E011-B1F7-0030486792BA.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/0481FF2B-84A2-E011-9B16-0018F3D0967A.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/02575940-6AA2-E011-9015-002618943877.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/00F6D186-68A2-E011-92F5-003048D3FC94.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/00AAC263-5FA2-E011-94AF-002618943856.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/0085DC8F-7AA2-E011-964A-00304867920C.root',
'/store/mc/Summer11/WZ_TuneZ2_7TeV_pythia6_tauola/AODSIM/PU_S4_START42_V11-v1/0000/0069E7CD-8EA2-E011-92DC-001A92971B0C.root'
    ) )
)
