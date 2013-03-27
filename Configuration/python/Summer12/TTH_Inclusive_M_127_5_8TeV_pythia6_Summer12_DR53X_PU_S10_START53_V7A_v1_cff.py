import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/006D0102-E601-E211-8E61-002590200930.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/027D36B7-DF01-E211-BB7A-0025902009A4.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/0420291B-DA01-E211-ACED-002590200B68.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/06D29A2D-CA01-E211-B481-0025902008B8.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/0802095A-FD01-E211-8511-001E6739751C.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/08429900-E601-E211-9CFF-002590200894.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/085760DA-C101-E211-A05F-0025902008C8.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/0AC23FC8-FA01-E211-AE5D-0025B3E06510.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/16EFB98B-FC01-E211-964A-001E67398791.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/1A8142F1-E601-E211-A420-002590200978.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/1C6EEF2D-E101-E211-A97E-001E67396E32.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/0AC65554-CD01-E211-9B44-001E67396A09.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/162145C3-DF01-E211-B55A-001E67398CE1.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/1643053F-1302-E211-A950-002590200A98.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/16934840-DE01-E211-9B06-001E67396BA3.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/1E0334CD-DE01-E211-8F5E-001E67396BAD.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/1E7CB947-FC01-E211-8DAB-002590200844.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/24FF61CC-FA01-E211-944D-003048673E8A.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/282400C9-FA01-E211-95EF-002590200A6C.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/1E87EC12-DA01-E211-AD0E-001E67397D73.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/1EC7DBA3-0F02-E211-8E8B-003048673F12.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/228344A3-FB01-E211-B32C-002590200A1C.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/2AD278C0-DA01-E211-B7B4-001E67396E0A.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/24358090-E201-E211-B8F9-001E67398791.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/30F1D894-F901-E211-86A2-001E67397620.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/284C22BC-0D02-E211-A637-001E67397D55.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/28FD61D5-C201-E211-8199-001E67397D73.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/382AF27E-DD01-E211-AE19-001E67396BA3.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/386CDC69-CB01-E211-B861-002590200974.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/2A5BAAE9-F101-E211-803D-001E67396E1E.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/2C39AE4F-E401-E211-8C83-001E67397D55.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/3422AFD0-E401-E211-8784-002590200828.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/407FB791-EE01-E211-AFD2-001E67396DCE.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/409C82D1-E401-E211-8A3C-003048670B64.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/466C265A-FB01-E211-8D71-0025B3E05D6E.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/365C3962-F601-E211-96F6-003048D462C4.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/3A298627-E101-E211-88F7-001E6739815B.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/48DCCFE9-E101-E211-9DF2-001E673967C5.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/3A7ACF3F-DE01-E211-A42E-001E67396E7D.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/546CB168-EA01-E211-AADA-0025902009E8.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/56C58198-D501-E211-8BCE-001E67396FE5.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/588846AA-0202-E211-A82E-001E67398DE5.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/5A7544CC-E901-E211-A6AF-002590200B78.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/62533BFD-DB01-E211-9471-001E67396C9D.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/625FD98A-F901-E211-BDD6-002590200B64.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/66C7725E-F801-E211-8DAD-002590200B44.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/3C6C8F9B-EC01-E211-9343-001E67397CC9.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/6E5715B2-FB01-E211-8BDB-002590200834.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/46F42161-F801-E211-BB41-002590200A28.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/72D36767-F601-E211-82CA-002481E1510C.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/48195F00-F001-E211-BE07-001E67397396.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/748B0DFA-E501-E211-8C32-002590200874.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/500A21C4-DF01-E211-9D70-001E673972AB.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/683AB952-FD01-E211-AE96-001E67396FCC.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/7AE599C5-FB01-E211-8B3C-001E67396568.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/7EB38A73-1702-E211-A0C9-001E673973D2.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/728933DD-D101-E211-AF99-001E67396E1E.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/82B9E192-D801-E211-99CE-001E6739830E.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/746884BF-DB01-E211-A752-001E67397215.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/78AA4CA2-F401-E211-9EFB-001E6739720B.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/86F03AC9-E501-E211-96BB-002590200AD8.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/78D5E796-F801-E211-8333-002590200B14.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/8A57BF65-C301-E211-8CBC-001E67397D73.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/82048DA1-0002-E211-98EA-001E67397D64.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/868FD5F2-E101-E211-AAB2-00304867407E.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/86CC1C7B-1B02-E211-ADC3-001E67396761.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/9016CA27-E101-E211-8476-001E67396D56.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/9027122F-F901-E211-8F73-0025B3E05BCC.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/88FE3441-0402-E211-9DFC-003048673F1E.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/966BDF87-E801-E211-983B-00259020081C.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/8C09397D-DD01-E211-A256-001E67397698.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/8C09E528-0802-E211-A386-001E67397E1D.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/8E311DB7-DB01-E211-A19A-001E67396FCC.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/92E1B2FE-DB01-E211-A50D-001E6739713E.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/96D2CCBA-1002-E211-96BC-00304866C360.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/9ECA26C0-DE01-E211-A97A-001E6739692D.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/98314B54-E301-E211-9439-001E67397053.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/A644C5C0-E001-E211-B5CB-001E67398CA0.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/A87B7F48-E301-E211-BBC1-001E67398791.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/AC1A7601-DC01-E211-83D5-001E67397C33.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/AEE3D646-FC01-E211-9644-001E67396D56.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/9AAE7066-EB01-E211-8662-002590200938.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/9AD25DAC-DA01-E211-B293-001E67398228.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/9C5B30B3-1102-E211-A470-001E67396E64.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/B8802C3A-C101-E211-815C-001E67396D42.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/A4B8DBB6-DF01-E211-A365-001E67396F9A.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/B6833C23-FE01-E211-AA6C-001E67398C05.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/B6A4DDBF-E001-E211-B41F-001E67397698.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/C485EE76-D901-E211-B500-001E67397D73.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/B6C87C51-0E02-E211-BEE9-003048D47A5E.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/C8F242AF-E001-E211-A30F-001E673969D2.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/CA7804DB-DE01-E211-B651-001E67398C5A.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/CC46F051-E301-E211-8EAE-001E673972E7.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/CCFF4E2E-F901-E211-ABDA-001E67396D6F.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/BA7DB939-FE01-E211-9593-001E67396905.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/D278A0DF-E501-E211-AD3F-0025902008C4.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/C09ED507-C001-E211-BD4B-001E67397CC9.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/D4AE224B-E301-E211-9451-001E67397AA3.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/D62BA2A7-E701-E211-9E70-002590200984.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/C0AF62F7-E101-E211-8CC7-001E673972E7.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/D6EF7263-FB01-E211-8C36-001E67398520.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/D80309C8-DB01-E211-98DD-001E67397B07.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/D80B0AAA-F001-E211-843A-001E67398DE5.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/C8D7893F-DE01-E211-B951-001E67396DCE.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/D0EC615A-FB01-E211-9943-002481E15000.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/EC1F6E90-C401-E211-835D-001E673975F8.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/D40E5AB1-1202-E211-A556-0025B3E06556.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/D69B6DDE-C501-E211-8E8E-002590200898.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/F06ED2C3-F701-E211-8F55-002590200AC0.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/F07452D3-EE01-E211-AD7F-001E67398C5A.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/DC4779FE-F101-E211-B72C-001E67396D79.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/E0F0B6CB-E401-E211-8D94-001E67398156.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/FA1F8779-FF01-E211-BA92-001E67396D4C.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/EE46D439-F501-E211-A8BC-001E6739720B.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/FCE28C94-E201-E211-87C8-001E67397AA3.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/EEF1A114-1502-E211-B3DA-00304867406E.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/F4CF312C-E401-E211-B9BD-001E67398791.root',
       '/store/mc/Summer12_DR53X/TTH_Inclusive_M-127_5_8TeV_pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/F4D26694-F801-E211-BF91-001E67396D6F.root' ] );


secFiles.extend( [
               ] )
