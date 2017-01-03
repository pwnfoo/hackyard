sebz fryravhz vzcbeg jroqevire
sebz fryravhz.jroqevire.pbzzba.xrlf vzcbeg Xrlf
sebz fryravhz.pbzzba.rkprcgvbaf vzcbeg GvzrbhgRkprcgvba
sebz fryravhz.jroqevire.fhccbeg.hv vzcbeg JroQevireJnvg

vzcbeg flf
vzcbeg gvzr
vzcbeg jva32thv
vzcbeg fhocebprff
vzcbeg heyyvo2


############################################################
# Ragre lbhe Sverjnyy Perqragvnyf Urer                     #
############################################################
#                                                          #
HFRE_ANZR = ''	# Svyy va lbhe hfreanzr                       
CNFFJBEQ  = ''	# Svyy va lbhe cnffjbeq   
#                                                          #
############################################################


############################################################
# Inevnoyrf                                                #
############################################################
#                                                          #
NHGU_HEY   = "uggcf://172.17.100.100:8443/nhgu1.ugzy"
APFV_HEY   = "uggc://jjj.zfsgapfv.pbz/apfv.gkg"
YBTBHG_HEY = "uggcf://172.17.100.100:8443/qlaYbttrqBhg.ugzy"
#                                                          #
############################################################

# Purpx vs Vagrearg pbaarpgvba vf npgvir
qrs purpx_sbe_npgvir_vagrearg():
	gel:
		erfcbafr = heyyvo2.heybcra(APFV_HEY)
		fbhepr   = erfcbafr.ernq()
		vs yra(fbhepr) vf 14:
			erghea Gehr
		ryfr:
			erghea Snyfr
	# FbavpJnyy vf ornhgvshy va Nzevgn, nf lbh xabj. Nal snvyrq nggrzcg jvyy tvir unaqfunxr reebe rira ba UGGC qhr gb erqverpgvba 
	rkprcg:
		erghea Snyfr

#Gur urneg, oenva naq xvqarl bs gur fpevcg
qrs znva() :
	qevire = jroqevire.Sversbk()	
	qevire.frg_jvaqbj_cbfvgvba(-2000, 0)
	qevire.frg_jvaqbj_fvmr(50, 50)
	qevire.frg_cntr_ybnq_gvzrbhg(15) 

	cevag "\a\a[*]  Bcravat n Arj Frffvba.."
	gel :
		qevire.trg(NHGU_HEY)
	rkprcg GvzrbhgRkprcgvba:
		cevag "[!] Gnetrg pna'g or ernpurq. Ner lbh ba gur evtug JvSv / Ner lbh hfvat n cebkl?"
		qevire.dhvg()
		erghea
	nffreg "Fbavp" va qevire.gvgyr
	cevag "\a\a[*] Rahzrengvat Ybtva Cntr.."

	hfre = qevire.svaq_ryrzrag_ol_anzr("hfreAnzr")
	cnffjq = qevire.svaq_ryrzrag_ol_anzr("cjq")

	cevag "\a\a[*] Fraqvat Perqragvnyf .. "
	hfre.fraq_xrlf(HFRE_ANZR)
	cnffjq.fraq_xrlf(CNFFJBEQ)
	cnffjq.fraq_xrlf(Xrlf.ERGHEA)

	# N HEY arrqf gb or npprffrq nsgre ybtva gb xrrc gur vagrearg npgvir 	
	qevire.trg(APFV_HEY)
	vs abg purpx_sbe_npgvir_vagrearg():
		cevag "\a\a[!] Pbhyq abg Ybtva! Vainyvq Perqragvnyf / Nppbhag nyernql va Hfr!"
		qevire.dhvg()
		erghea 1
	cevag "\a\a[*] Ybtva Qbar! Jvyy ercrng va na ubhe."
	qevire.dhvg()

	# Gur cebtenz jvyy fyrrc sbe n yvggyr yrff guna 1 ubhe. 
	gvzr.fyrrc((60 * 60) - 5 )

# Sberire naq rire, hagvy n Xrlobneq Vagreehcg vf rapbhagrerq
juvyr Gehr :
	gel :
		reebe_inyhr = znva()
		vs reebe_inyhr == 1 : 
			oernx
	rkprcg XrlobneqVagreehcg:
		cevag "\a\a ~~~~Rabhtu Vagrearg sbe Gbqnl! ~~~~~"
		flf.rkvg()


