import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/006F21C0-E5E0-E111-9642-0030487D5EAF.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/025F9307-EAE0-E111-A3AE-0030487F1C4F.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/02A837AF-E6E0-E111-AA3B-0030487D8581.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/02C4B800-D5E0-E111-87BE-003048C6763A.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/04F5FF9D-F4E0-E111-951A-0030487E4ED5.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/06BD626E-CFE0-E111-A26D-0025901D47AA.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/085E8DBF-F1E0-E111-8AA0-0025901D4764.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/0AF86507-EFE0-E111-85B9-003048C6941C.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/10ED9E13-C8E0-E111-B890-00266CF9C1AC.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/12218213-FAE0-E111-8F6F-0030487D5EB3.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/12859506-EAE0-E111-A781-0025901D4090.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/12F5BBB3-F1E0-E111-A5C0-0025901D4C3E.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/14AB5E15-EAE0-E111-8CA3-0030487E55BB.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/1A2781CE-D2E0-E111-AD2E-0030487F132D.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/1AE09BB7-EDE0-E111-8AC3-0025901D481E.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/1C9E3214-EAE0-E111-B425-0030487F1BD3.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/1CB0045C-D7E0-E111-A2DA-002481E76052.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/1E365F78-0AE1-E111-9C6C-0030487E5179.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/20802FAF-02E1-E111-BD1B-0025901D490C.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/20AF6128-ECE0-E111-994D-0030487FA349.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/225F926D-D8E0-E111-96C6-003048C69406.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/22B6D9B9-EDE0-E111-A1D8-0025901D4A58.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/22C4EA96-F6E0-E111-8214-003048C6931E.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/2413B5F5-EFE0-E111-A313-00266CFFA654.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/28A565AB-C6E0-E111-9250-0025901D42BC.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/2C3F00DD-DEE0-E111-ADEF-0030487D858B.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/2CE012C3-D1E0-E111-AE02-003048F0E3BE.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/2E24CA02-EAE0-E111-ADEB-0030487F1309.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/32EAD9A8-F1E0-E111-B04B-0030487F1735.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/36BF93B8-03E1-E111-9F0E-0025901D481E.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/3AE2E36B-EDE0-E111-92C8-0025901D4932.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/3C2CBE11-EAE0-E111-8AED-0030487D7EB1.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/3CE04C7F-E9E0-E111-A81C-0030487EA3DD.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/4088C55B-E8E0-E111-88A5-0030487F1797.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/4282C323-D6E0-E111-9B9F-0030487F933F.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/42AFA5BC-14E1-E111-8227-0030487D86CB.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/44A87272-F6E0-E111-A546-0025901D4C3C.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/44D0BA4B-E9E0-E111-8A1B-0030487F1797.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/4673698F-E8E0-E111-BCEB-003048D4385C.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/46B51317-0BE1-E111-9812-0025904B12E0.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/46C5CBFE-D3E0-E111-BE24-0030487EB003.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/46FAED4B-E9E0-E111-804F-0025904B0FE6.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/48E4376C-EDE0-E111-87CD-0025901D47AA.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/4A31C8CE-F1E0-E111-B90C-00266CFFA654.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/4C6B9A5C-E2E0-E111-A0D7-0030487F1C55.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/4E19F841-DBE0-E111-A2CA-0030487F1A4F.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/4E215AF1-DAE0-E111-8FD6-0030487F1665.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/4E587455-E9E0-E111-9321-0025901D4090.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/502845A2-E0E0-E111-8078-0030487DE7BD.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/50CE39BA-F1E0-E111-9368-0025901D4124.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/529478C3-E1E0-E111-B459-0030487E54B7.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/52F1ED17-CFE0-E111-A33B-003048C692F2.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/545E4B6E-EDE0-E111-B623-0025901D492E.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/54D84BBC-EDE0-E111-AE87-0025901D4D6C.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/5699AEF4-E9E0-E111-AC95-002481E946EE.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/5A11DE13-E8E0-E111-928A-0030487D5DBF.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/5A145CF4-0DE1-E111-93E4-0030487E5179.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/5A6D2D6D-E8E0-E111-A038-003048C693EE.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/5AF2BDB9-E5E0-E111-B50A-0025901D47AA.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/5C69CB31-ECE0-E111-B6A1-003048D43982.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/5C9A047F-E9E0-E111-8A79-0030487EA3DD.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/624BC439-12E1-E111-B07E-0025904B1448.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/62E94ABA-F4E0-E111-AA3E-0025904B1446.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/64690420-EFE0-E111-ABA8-0030487D5D67.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/68217A95-F2E0-E111-BFB5-0025901D4764.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/68246F93-E8E0-E111-B2D9-00266CF32F18.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/68A77C76-CAE0-E111-8F06-003048D43642.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/68F5FF1D-E3E0-E111-8E30-0030487D605B.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/6A84C40D-C1E0-E111-A811-0030487F1BCF.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/6AA686CE-F3E0-E111-91E7-0030487E4ED5.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/6C39F609-04E1-E111-9622-00215AEDFC8E.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/6C641A11-EAE0-E111-B7ED-0030487EA3DD.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/6CC64BA9-E6E0-E111-B95D-0030487E0A29.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/6E7FBB9A-E8E0-E111-B39D-0025901D4090.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/70791309-E5E0-E111-9F18-0025901D40CA.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/70B0E0FF-EEE0-E111-AA59-0025901D4A58.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/729C64A9-05E1-E111-93FB-0030487D83B9.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/72C5092C-ECE0-E111-B5EF-0030487F1A55.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/74EE01B5-CCE0-E111-9525-003048F0E424.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/76720815-D1E0-E111-BCE6-003048F0E1EE.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/76EFF758-11E1-E111-A39F-002590494C94.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/78877E4A-EBE0-E111-914B-D8D385FF6C5E.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/7A7A55CC-0BE1-E111-BEF4-0030487FA4C5.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/7C9F6C38-F3E0-E111-9A3C-0030487D5D67.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/7EE89C21-D0E0-E111-9C5E-003048C692FA.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/8287F14F-E6E0-E111-B3AE-0025901D4D64.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/82B38FB4-EEE0-E111-AC21-0030487D5D8F.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/844C3C6F-DDE0-E111-AC84-003048C69424.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/8646B5FC-E9E0-E111-96EE-0030487F1651.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/86CF90B0-F4E0-E111-AC20-0030487F3EA7.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/86E99B21-E1E0-E111-A61C-0030487D7EB1.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/88613BB8-F4E0-E111-AC8A-0030487F1A49.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/88B685D3-F3E0-E111-A824-0025901D493E.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/8A049AC9-F3E0-E111-AE6B-003048D43944.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/8EAB4459-0EE1-E111-8A53-0025901D4A0E.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/90090620-EFE0-E111-B6D6-0030487D5D67.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/90EC715B-E2E0-E111-B00C-0030487F1A31.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/9423C932-ECE0-E111-A6C3-0030487EB003.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/94E4455A-E6E0-E111-ABF2-0025901D47AA.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/966D14AA-C9E0-E111-9988-0030487D5EA1.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/98386AAD-E4E0-E111-9BDD-003048C692FA.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/9851E56A-EDE0-E111-939C-0025901D484C.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/988EA13A-DEE0-E111-AD90-0030487D5E5F.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/98BA43F8-FCE0-E111-ABD8-00266CF327C0.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/98E175FD-EEE0-E111-ACB6-003048C692A4.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/9CE1106F-EDE0-E111-A37D-0025901D490C.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/9CEA5896-E3E0-E111-9A86-0030487F1A31.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/A07E7CCF-EEE0-E111-84FD-0025901D4D6E.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/A0B186E0-F0E0-E111-AEC2-0030487F1735.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/A0C57F77-EDE0-E111-9C92-0025901D4864.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/A0D9EA46-EFE0-E111-9260-003048C690A2.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/A28C029C-D2E0-E111-8ED9-0030487F932D.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/A4F41046-0FE1-E111-A143-0030487F91D7.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/A624EFA4-09E1-E111-8E98-002590494C74.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/A85C04E6-F6E0-E111-A01B-0025901D4C3C.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/A88E2EC0-EDE0-E111-8557-0025901D4D6C.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/AA4968B2-F5E0-E111-93F3-003048D43734.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/AC738C0E-F9E0-E111-BC8D-003048C693D0.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/AC846C02-F1E0-E111-B640-003048C69424.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/AC90587E-EBE0-E111-98CA-0030487F1A55.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/ACD19529-F9E0-E111-92AD-0030487D8633.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/ACF4690E-E1E0-E111-BD41-0030487F92B5.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/ACF61E3E-EBE0-E111-8DAB-0030487FA349.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/AE86C92B-11E1-E111-9AAB-003048D439A0.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/AEDAF242-EBE0-E111-B7D8-002481E0D398.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/B09265E8-DCE0-E111-B179-0030487D5DAF.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/B20205EB-CDE0-E111-AC82-003048D3CDE0.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/B270051F-EFE0-E111-8720-0030487D5D67.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/B4268CB4-EDE0-E111-B80B-0025901D4A58.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/B45F7795-06E1-E111-9B92-003048C693E8.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/B4905567-E9E0-E111-8D41-0030487E55BB.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/B674CDC8-E3E0-E111-A450-0030487D605B.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/B68B82DB-E6E0-E111-A7A6-0025901D4D64.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/B82AE0E7-D1E0-E111-A587-0030487F932D.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/B8317936-06E1-E111-8758-0025904B1370.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/B83AD46A-DCE0-E111-9F1F-0030487CF3F7.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/B8D11556-E6E0-E111-9785-00266CF330B8.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/BA6608FA-08E1-E111-A247-003048C692A2.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/BA9C7D3E-CEE0-E111-A7D1-00266CF32F90.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/BAE1EACF-EEE0-E111-8749-0025901D4864.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/BE2699FA-E5E0-E111-8598-0030487D8581.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/C059C814-EAE0-E111-A2F1-002590494CBC.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/C6F37DB5-E4E0-E111-9A56-0030487E52A3.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/C82EA118-EAE0-E111-876A-002481E94C7A.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/C8FCD8EF-E9E0-E111-904A-0030487F1BD7.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/CA05E1E9-F0E0-E111-A341-003048D3CD62.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/CA4C4588-E3E0-E111-A4E4-0030487E4EB9.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/CAA99B2B-ECE0-E111-9233-0030487FA623.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/D274A497-E0E0-E111-AD6A-0030487E52A1.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/D6052320-EAE0-E111-B923-0025904B0FE6.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/D66FA847-D3E0-E111-BACD-0030487EB003.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/D67DFCC9-EEE0-E111-8A09-0025904B1340.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/D6C8331E-F0E0-E111-ADF1-0030487F1735.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/D8CDC048-EBE0-E111-8812-0030487F1737.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/DA3313E7-F6E0-E111-8BA5-003048C693D2.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/DA633A76-EDE0-E111-8EE3-0025901D4864.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/DCAB1D0A-F0E0-E111-96D9-00266CFFA654.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/DE67B2AD-CCE0-E111-AEEC-002481E94C7A.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/DEB2B7C7-F3E0-E111-A5BF-0025901D493C.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/E075D982-F2E0-E111-887B-0030487D5EAF.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/E6804D0A-F0E0-E111-AA7E-00266CFFA654.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/E847CB97-0CE1-E111-8836-0025901D481E.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/E89E5271-EBE0-E111-A675-003048D43982.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/EA0DE567-F6E0-E111-8A36-0025901D4932.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/EA8CC94B-D7E0-E111-8132-0030487F933F.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/EAE8DCFB-F8E0-E111-AE40-0030487D5EB3.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/EAFE9013-E5E0-E111-8D0C-0025901D47AA.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/E69DC46E-EDE0-E111-BA36-0025901D4138.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/F0320729-E3E0-E111-A46E-0030487F1C55.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/F63056AB-F4E0-E111-B053-002590494CC2.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/F6FA59EB-F0E0-E111-A140-0030487F1A55.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/F87813CB-E6E0-E111-B8FE-0025901D42BC.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/FABDA633-08E1-E111-8CBB-003048C69310.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/FACF19D7-F3E0-E111-9EDD-0030487F3EA7.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/EAA9FB36-29E1-E111-AB38-00266CF327C4.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/FCA079BC-E5E0-E111-8EF8-0025901D40CA.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/FE0E3C07-F0E0-E111-93FC-0030487F938F.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/EC91EBFB-E9E0-E111-B770-0030487F1BD7.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/FE4EBC76-EDE0-E111-B532-0025901D4864.root',
       '/store/data/Run2012A/SingleElectron/AOD/recover-06Aug2012-v1/0000/EE3AD6E4-2EE1-E111-B3F2-00266CF32EB8.root' ] );


secFiles.extend( [
               ] )

