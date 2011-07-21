import FWCore.ParameterSet.Config as cms

##########################################################################################
# Dataset: /QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/Summer11-PU_S3_START42_V11-v2/AODSIM #
# Events : 2081560                                                                       #
# eff    : 0.00059                                                                       #
# genXSec: 236.100.000 (LO PYTHIA)                                                       #
##########################################################################################

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource", fileNames = cms.untracked.vstring( *( 
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/F8CD8B2F-DA80-E011-9E37-00E08178C0C1.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/F87FA829-3A80-E011-9B58-00E08178C165.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/F409C81A-DA80-E011-9E92-001A6478AA34.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/F09420C8-1B80-E011-B414-003048D45FE0.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/E6CB0B91-0880-E011-B716-003048D46084.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/E68CCD77-E480-E011-B8D4-00E08178C18B.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/E491FB16-0B80-E011-BC3A-00E0817918BF.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/E2A61787-D980-E011-A2F6-001A64789D50.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/E0D9A5CE-0A80-E011-957E-00E08178C107.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/D6DB7054-2B80-E011-B8AA-00304863EFBC.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/D64B36EC-2B80-E011-8EED-003048D479D8.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/D4BC76F4-D780-E011-8B41-00E0817917FB.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/D2178F65-2D80-E011-AC6E-00E0817917A7.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/D0223B7C-D980-E011-854A-003048D46068.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/CEB9CD89-1880-E011-BBA3-003048674048.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/CE7F64DB-1E80-E011-A0A8-00E08178C165.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/CE37BFC7-3880-E011-A52B-002590200A28.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/C8F2A96F-E680-E011-B1C2-003048D4772E.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/C6EC59B2-E280-E011-B716-00E08178C133.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/C6C39DFE-1280-E011-BC3B-002481E1511E.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/C68C8B02-E980-E011-B4DA-00E08178C101.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/C4FE9F86-3680-E011-8F33-003048635E08.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/C2BEE207-4180-E011-889C-F04DA23BCE4C.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/BAA00946-4281-E011-A2BD-00304863EFBC.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/BA4B85D7-2680-E011-A686-00E081791769.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/B8736542-1A80-E011-BC1D-00E081791773.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/B2238B5D-3E80-E011-AC7E-00E081B08D11.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/AC91C97C-E680-E011-9BFD-003048D479CC.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/AAD08C8B-E180-E011-81A4-002590200A1C.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/A8EFCB1F-2980-E011-AFB3-002590200A68.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/A66E2204-E980-E011-AFF0-00E08178C147.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/A663DEC3-3C80-E011-BFDF-F04DA23BCE4C.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/A468E675-2580-E011-B08F-0025902008CC.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/A02563F2-FE80-E011-930B-0025B3E0651E.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/9A97ACAF-1D81-E011-8B22-001A64789500.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/98F6857C-D980-E011-85A9-00E08179187F.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/968E1D2B-DA80-E011-A78D-00E08178C161.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/948120A4-2280-E011-A316-00E08178C135.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/94193E3E-2880-E011-8056-00E08179178F.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/90A2ADD2-4480-E011-92B4-002590200A40.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/84BD5594-FD80-E011-B34E-003048635E34.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/82F2B009-DC80-E011-B9C9-002590200A58.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/82E37F78-E480-E011-8327-003048D47712.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/801D568F-1580-E011-A73B-001A647894E8.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/7A890ADA-E680-E011-A9BA-0025902008C8.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/7A5F3B30-1C80-E011-B97B-00E081791769.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/7A5D0EE2-1680-E011-BE01-003048D4601E.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/7475A2C7-DA80-E011-B532-002481E150F8.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/740C0F2E-DA80-E011-8448-001A64789D10.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/6EC10A8D-EE80-E011-85DA-00E0817918D9.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/6E084BD6-1980-E011-B434-003048635B86.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/6E01C052-3980-E011-977E-003048635E32.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/66C3277E-2380-E011-986B-00E08178C06F.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/660F0AEE-7481-E011-AC2D-002590200844.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/64F99892-D780-E011-ADB6-003048635B58.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/5EF8877F-E480-E011-BC6C-003048D462D2.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/5EEA6E8E-D980-E011-88D5-00E0817918A7.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/5E7D4E05-D780-E011-9AAF-003048D479CC.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/5E44AFAE-E280-E011-96C6-0025B3E05D46.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/5C7D12CE-EC80-E011-B9BF-002590200AB8.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/5A50B54B-DD80-E011-81B4-00259020097C.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/5A003C99-1D80-E011-B494-00E08178C109.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/58B40ED1-DD80-E011-9AEA-00E081791841.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/5893F29B-3280-E011-969B-00E08178C18B.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/58733900-3480-E011-AEED-00E08178C021.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/56DBBC67-2480-E011-8DB1-001A6478ABB4.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/54A3F605-1D80-E011-B3EC-001A64789E60.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/547E0ABC-2780-E011-BE8B-0025B3E063A2.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/5449499D-E180-E011-8070-002590200834.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/4E97F0E8-FB80-E011-BA46-003048D45FE2.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/48765656-0F80-E011-9CF9-001A6478A9DC.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/483E7C3F-D880-E011-B856-001A64789D78.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/465FA1DA-DF80-E011-BE15-002590200AC0.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/46544C66-E680-E011-9831-003048D46024.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/44D99A14-2B80-E011-AE0C-00E081791779.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/40B0C589-EE80-E011-9FC7-00E08178C147.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/3E4C95CF-DF80-E011-8F4E-003048D45FBA.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/3CA38D54-EF80-E011-8EAD-002590200B4C.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/3ADC7548-4081-E011-B850-0015170AE418.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/383A506C-E680-E011-853B-00304863EFBC.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/36990098-2581-E011-A6E6-00E08178C16D.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/32ADD87E-D980-E011-AC50-00E08178C119.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/3298C122-1780-E011-8A43-003048D46300.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/3223FB4D-F480-E011-BC5E-003048635E46.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/320BF943-0A80-E011-904C-00E0817918D9.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/30F1C63C-1980-E011-B946-0025B31E3C04.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/30A356F2-E980-E011-8FFA-003048D479F6.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/3086C339-3080-E011-A44E-00304863EFBC.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/307C1EFC-E980-E011-BBD2-00259020097C.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/304E96CE-2880-E011-AE6C-00304863EFBC.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/302DAEA0-E180-E011-8104-003048673E94.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/2C9D5924-2E80-E011-AE1F-00E08178C021.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/24785D19-0C81-E011-9E26-D8D385FF17DC.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/20801A80-E480-E011-BAAA-003048D45FDA.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/1ED5638A-2A80-E011-94CE-003048D45FE0.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/1CEEDFC2-0980-E011-8D30-00E08178C107.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/16FB1171-3B80-E011-AB15-00E081B08D11.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/1653D182-E480-E011-899D-00E0817917DF.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/1491DF1E-0980-E011-A614-003048D46138.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/12842624-DA80-E011-956A-003048D4604A.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/12798C46-F380-E011-89FD-003048635E46.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/12446D94-2C80-E011-ABC4-0025B3E06450.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/1087F5D3-E680-E011-A6C1-003048D479D6.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/0E5BD905-D780-E011-A1AC-0025B3E05CE4.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/0AB7D545-2F80-E011-A411-00304863EFBC.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/0A21F282-D980-E011-839B-002590200A40.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/0876044F-2680-E011-B200-003048D47742.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/04828F84-E480-E011-9902-0025902008B8.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/042C24F8-D780-E011-A8FA-00E08178C031.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/02F0FDD1-0281-E011-B0D4-0025B3E0653C.root',
'/store/mc/Summer11/QCD_Pt-20to30_BCtoE_TuneZ2_7TeV-pythia6/AODSIM/PU_S3_START42_V11-v2/0000/00615854-0D80-E011-8881-00304866C47A.root'
    ) )
)