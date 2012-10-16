import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/FEBAC03B-D8DE-E111-A175-00304867902E.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/FE838901-AFDD-E111-80C3-00304867C1BA.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/FE700D12-D8DD-E111-8749-001A92971BD6.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/FCD68A04-AFDD-E111-BC61-003048D15DDA.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/FAD9CCA8-C7DD-E111-8B8C-001A928116B4.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/F8E7C06C-9FDD-E111-AE6F-002354EF3BD0.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/F807C688-DADE-E111-B0C8-003048FFD71A.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/F412C611-B5DD-E111-8B07-0026189437FA.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/F26235E7-9FDD-E111-AA16-002618943868.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/F210B808-94DD-E111-8EC4-002618943956.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/F0C12624-D7DE-E111-8A20-00304867902E.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/F00CFDFE-DBDD-E111-A950-003048FFD756.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/EE84F888-DADE-E111-A2E1-003048FFD71A.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/EE2AC612-D4DD-E111-B5A9-0018F3D0967A.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/EC8C5A58-C2DD-E111-B65A-003048FFCB8C.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/EAF4AA11-B2DD-E111-893D-003048679228.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/EA579BCA-91DD-E111-A56F-0026189438A2.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/E8937D71-27DF-E111-9358-00261894395B.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/E629273C-B7DD-E111-B925-002618943821.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/E6094AA5-AFDD-E111-A93A-003048678B86.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/E4E91448-AADD-E111-AB31-002618943975.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/E4B38BD3-D7DE-E111-8289-00304867906C.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/E2D778F6-92DD-E111-ACC5-00261894396B.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/E06FCDBC-B4DD-E111-91B3-0026189438D6.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/DC08B2D4-B4DD-E111-B5E1-0026189438DA.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/DA7360DF-E7DD-E111-8687-003048D3FC94.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/DA56518F-CDDD-E111-9BE0-0018F3D096F8.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/D886109D-D6DE-E111-B3EE-001A928116EC.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/D8108BD9-B4DD-E111-8E0F-001A928116D2.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/D693B169-D6DE-E111-BD36-001A92810AAE.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/D6067FA6-AFDD-E111-9E3C-003048D15E2C.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/D43AEADF-A6DD-E111-A720-003048678BE8.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/D412BCAA-D2DD-E111-BC85-003048678F78.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/D2A17D9A-B2DD-E111-AB6D-001A92810AA2.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/D2893CCD-B0DD-E111-8E72-0030486792F0.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/D00329A3-D5DD-E111-BC18-001A928116B4.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/CCEE21BF-B6DD-E111-8F69-001731EF61B4.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/CCB15A8A-A4DD-E111-8DE3-003048678BEA.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/CC9E0251-94DD-E111-8FDC-0025905822B6.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/CC07461D-B2DD-E111-9A55-002618943896.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/CAD56015-B0DD-E111-897D-0018F3D09612.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/CA8C13F6-E7DD-E111-98C5-001A92971B8A.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/CA194BE4-BCDD-E111-AB6F-0026189438DC.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/C8AF3D05-CFDD-E111-9C2D-001A92971B5E.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/C6FF4751-B7DD-E111-A758-0018F3D09630.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/C6FD8214-2DDF-E111-8647-00261894391C.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/C6F1AF5C-CADD-E111-A540-001A928116DA.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/C67B1088-26DF-E111-8A14-002618943869.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/C6649FCD-CEDD-E111-86C3-001A9281172A.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/C428DAFF-B8DD-E111-848A-0026189438AE.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/C2AF3DC8-BCDD-E111-A5C8-0026189438E3.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/C257E284-B8DD-E111-B9E8-0025905822B6.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/BC07C688-DADE-E111-9E98-003048FFD71A.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/B8BA08C3-A5DD-E111-8B6F-0030486792AC.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/B89FD0F4-A3DD-E111-97D4-003048B835A2.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/B60D2199-A7DD-E111-9527-003048678FA6.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/B2E9ABE1-27DF-E111-A34C-0026189438F3.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/B0FD97F9-EADD-E111-B1B5-0026189437F8.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/AC44C564-CEDD-E111-B9A1-003048FF9AA6.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/AA0DF3F8-DADE-E111-B5BE-003048FFD760.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/A4DA1CF9-DADE-E111-B4BD-003048FFD760.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/A49C773D-B2DD-E111-95A0-002618943937.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/A4945539-D6DD-E111-ACAD-003048678C9A.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/A0B93F57-A3DD-E111-9E86-003048D3C010.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/9EE1748C-DADE-E111-92F8-003048FFD71A.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/9C6CC2B0-CCDD-E111-B43F-0018F3D0962E.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/9AD3E733-BADD-E111-AE09-00261894389D.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/98D462A0-B5DD-E111-897D-002618943916.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/986405B8-ACDD-E111-8A58-00304867916E.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/9274AF01-AFDD-E111-B197-003048678FDE.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/90991802-D7DD-E111-9F15-001A92810AE4.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/90061B03-A3DD-E111-B267-00261894397E.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/8EB59D03-2BDF-E111-B71C-0026189438F4.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/8CCC51F9-DADE-E111-A9AF-003048FFD760.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/8CB4AB02-AFDD-E111-B029-003048678AE4.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/8A4E1EB1-AFDD-E111-B03F-003048679228.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/88F2E66C-E8DD-E111-88EA-0026189437F8.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/88D927C7-E8DD-E111-AF3D-003048679168.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/88A319E4-ABDD-E111-B1B4-001A9281173C.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/88863916-9ADD-E111-BA6B-002618943863.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/86CDEC00-A8DD-E111-945F-0030486792B6.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/8447516D-A0DD-E111-8B72-00261894395B.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/80F3419E-D6DD-E111-8740-003048678BB2.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/8076F7A3-D9DD-E111-AC84-001A92971B68.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/8049035C-2DDF-E111-91C0-002618943966.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/8017B6E2-D1DD-E111-A021-0018F3D096EE.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/7E45847C-D9DD-E111-A177-001A92971B38.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/7E356F26-F0DD-E111-8328-0026189438E1.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/7E31C15A-AFDD-E111-A1E1-002618943882.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/7CE7434D-A9DD-E111-A984-003048678FC6.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/7C5DC772-DADD-E111-BDFF-003048679228.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/7A87F506-AFDD-E111-8A19-003048678B76.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/78BC32E8-B7DD-E111-A654-002618943935.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/78A9BBC0-B9DD-E111-8D61-002618943910.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/789737C4-D8DD-E111-9311-003048678B86.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/766943F9-DADE-E111-9E3C-003048FFD760.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/762916B8-A3DD-E111-941B-002618943845.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/74921FD0-D8DE-E111-A3D6-00304867906C.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/74322713-C2DD-E111-A35C-00304867D838.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/74213365-A7DD-E111-A7D8-00304867C16A.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/7268D999-DBDE-E111-B561-0018F3D0961E.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/72628A5E-C2DD-E111-8176-00261894380D.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/722D1BF7-DBDE-E111-A395-001A928116EC.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/709E5520-DDDD-E111-BEA3-00261894395C.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/70477F0B-F7DD-E111-B4D0-002618943834.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/703FC9A2-D7DD-E111-851F-003048678B86.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/6E50913D-B6DD-E111-AED8-00261894396D.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/6CBB8DA6-D8DD-E111-83A7-001731EF61B4.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/6C6EF088-DADE-E111-8960-003048FFD71A.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/6C3B62E3-D3DD-E111-BFB3-003048678C9A.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/66DB7524-B3DD-E111-86D6-0018F3D09686.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/667300E6-DCDE-E111-BA97-00304867D836.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/64FDBBC1-D7DD-E111-BBCC-0018F3D09660.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/645C9704-C4DD-E111-9F76-0026189437ED.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/624A858A-2BDF-E111-A6A4-00261894390A.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/622B216D-26DF-E111-A7A7-00261894391B.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/5E68723E-9ADD-E111-A831-003048678B30.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/5C383124-A5DD-E111-9292-003048678F62.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/5A18C788-DADE-E111-B1EF-003048FFD71A.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/587145D9-A6DD-E111-84DA-00304867918A.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/580CF732-E7DD-E111-BC8B-001731EF61B4.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/580CC688-DADE-E111-97A2-003048FFD71A.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/54CB205C-EDDD-E111-828D-002618943985.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/540976B5-C9DD-E111-A62C-0026189438EF.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/4E3F3398-E0DD-E111-B064-00261894393F.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/4CADA67F-D3DD-E111-9028-003048FFCB74.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/4C06A208-D7DE-E111-A160-001A92971B8A.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/4AC59765-C8DD-E111-B133-003048678B76.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/4AAFBCFD-D0DD-E111-B634-0026189437ED.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/3E07BC68-A7DD-E111-985B-003048678B30.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/3CBE6676-99DD-E111-8B0E-0026189438BD.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/3ACBDE8F-ACDD-E111-BC33-001BFCDBD166.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/3AB52FCB-DADE-E111-A7B1-0018F3D096A4.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/38F4E727-DFDD-E111-8D1E-0018F3D0969C.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/3265AF4C-CEDD-E111-8D24-0018F34D0D62.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/2CCF2A8C-AFDD-E111-B63A-003048FFCBA8.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/2C1DBA87-CCDD-E111-A9A5-0018F3D096C6.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/24545ED2-95DD-E111-9C8A-002354EF3BDD.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/22B56B6F-D6DE-E111-B5BF-003048FF86CA.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/22496CB2-AFDD-E111-957A-003048D15DB6.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/2023DFCB-A0DD-E111-A5FA-0018F3D0968C.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/1E6D2348-28DF-E111-8382-002618943925.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/1CEB11B6-E7DD-E111-AF3C-001A92971B38.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/1C95143E-B3DD-E111-AA6F-002618943935.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/1C2307B9-D5DD-E111-8AA7-001A92811706.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/1A197C1E-A8DD-E111-A59F-0018F3D09630.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/185FC9F0-D0DD-E111-A7AF-001A92971AD8.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/14808DF2-C0DD-E111-9583-00261894389E.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/12FDFF0D-34DF-E111-8EAB-002618943810.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/1254BCD5-B4DD-E111-A448-002618943951.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/102814B1-AFDD-E111-A0D3-003048679228.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/0CA7B882-B4DD-E111-8349-0026189438B4.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/08CCBCA5-EEDD-E111-8D49-002618943985.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/08ACC271-DCDE-E111-B017-001A92810AAE.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/0896E40D-34DF-E111-8B7A-002618943810.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/0411461D-B2DD-E111-9DCB-002618943896.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/02939D83-ECDD-E111-AB4B-002618943918.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/00C55B6F-BDDD-E111-AEEC-00248C55CC4D.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/00BC2DAF-C3DD-E111-8DD4-0026189438E4.root',
       '/store/mc/Summer12_DR53X/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/003DAD57-C5DD-E111-AE4C-001A92971BDC.root' ] );


secFiles.extend( [
               ] )

