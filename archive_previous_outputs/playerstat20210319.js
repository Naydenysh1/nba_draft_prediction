// var teams;
var tableHTML;
var data;
var tdata = [];
// if (compyear == '2020') {compyear = '2019'}
var docomp = 0
var addevan = 0
var limitstring
var multiyearnote = " "
var multidone = ""
var himid = ['Connecticut','Wichita St.','Cincinnati','Gonzaga',"Memphis","Houston"]
var noo = []
var showalltransfers = -1
var showeveryone = - 1
var d2tranlist = [];

if (year < 2026) {showalltransfers = 1}
// var year = source.substring(0,4);
// var teams = []
if (sIndex > 56) {
	dopoints = 1
} else {
	dopoints = 0
}
yeartext = ''
percentageArray = [15, 18, 21]
function sortTableData(sortIndex) {

	if (sortIndex == 45) {

		alltdata.sort(function (a,b) {
			if (a[45] == null) {
				a[45] = 80}
			if (b[45] == null) {b[45] = 80}
			
			if (sortToggle == 1) { 
				if (a[sortIndex] < b[sortIndex]) {
					return -1;
				} else if (a[sortIndex] > b[sortIndex]) {
					return 1;
				} else return 0;
			} else {
				if (b[sortIndex] < a[sortIndex]) {
					return -1;
				} else if (b[sortIndex] > a[sortIndex]) {
					return 1;
				} else return 0;
			};
		})	
	} else if (sortIndex == 'tprate') {
		alltdata.sort(function (a,b) {
				ab = (a[20]+a[17] > 0) ? a[20]/(a[20]+a[17]) : 0
				ba = (b[20]+b[17] > 0) ? b[20]/(b[20]+b[17]) : 0
			if (sortToggle == 1) { 
				if (ab < ba) {
					return -1;
				} else if (ab > ba) {
					return 1;
				} else return 0;
			} else {
				if (ba < ab) {
					return -1;
				} else if (ba > ab ) {
					return 1;
				} else return 0;
			};
		})
		
	} else {

		alltdata.sort(function (a,b) {
				var actualSortIndex = sortIndex;
				var ab = a[actualSortIndex] !== undefined ? a[actualSortIndex] : -99;
				var ba = b[actualSortIndex] !== undefined ? b[actualSortIndex] : -99;

			if (sortToggle == 1) { 
				if (ab < ba) {
					return -1;
				} else if (ab > ba) {
					return 1;
				} else return 0;
			} else {
				if (ba < ab) {
					return -1;
				} else if (ba > ab ) {
					return 1;
				} else return 0;
			};
		})
	
	}
	makeTable();
};

function teamChoices(id) {
	var el = document.getElementById(id);
		
	el.options.length = 2;
	var opt = document.createElement('option');
	opt.innerHTML = 'All';
	el.appendChild(opt);

	teams.forEach(function(team) {
		var opt = document.createElement('option');
		opt.innerHTML = team;
		el.appendChild(opt);
	});
};	

function getcomptrid() {
	tdata = alltdata
	len = tdata.length
	if (xvalue == 'trans') {
		$.getJSON("gettridstats.php?year="+compyear+"&trid="+comptrid, function(jsonData) {
			comp = jsonData[0];
		}).done(function() {
			comp[35] = comp[1]
			if (alltdata[0] != comp) {
				alltdata.unshift(comp)
			}
			compareSort()
			return
		})
	} else {
		for (var i = 0, brk = 0; i < len && brk == 0; i++) {
			trid = tdata[i][32]
			ayear = tdata[i][31]
			if (year == 'career') {
				if (trid == comptrid) {
					comp = tdata[i]
					brk = 1
				}			
			} else {
				if (trid == comptrid && ayear == compyear) {
					comp = tdata[i]
					brk = 1
				}
			}
		}
	}
}

function doTheSort(sortcol,id) {

	if (sIndex == sortcol) {
		if (sortToggle == 0) {
			sortToggle = 1;
		} else sortToggle = 0;
	} else sortToggle = 0;
	sIndex = sortcol;
	$('td.filter').css('background-color','#ffffff');
	$(id).css("background-color", "#cccccc");

	if (sIndex == 99) {
		if (comptrid != '') {
			getcomptrid()
		compareSort()
		}
	} else {
		$('span#findertype').text('Finder')
		comptrid = '';
		compyear = '';
		sortTableData(sortcol);
	}
	
};	

function makeinches(ht) {
	if (typeof(ht) == "number") {
		return 0
	}
	var s = ht.split('-');
	return Number(s[0]) * 12 + Number(s[1]);
}

function doTheHeightSort(sortcol,id) {
	if (sIndex == sortcol) {
		if (sortToggle == 0) {
			sortToggle = 1;
		} else sortToggle = 0;
	} else sortToggle = 0;
	sIndex = sortcol;
	$('td').css('background-color','#ffffff');
	$(id).css("background-color", "#cccccc");
	alltdata.sort(function (a,b) {
		if (sortcol > a.length - 1 || a[26] == 0 || a[26] == null) {
			aht = 0;
		} else {
			aht = makeinches(a[26]);
		}
		if (sortcol > b.length - 1 || b[26] == 0 || b[26] == null) {
			bht = 0;
		} else {			
			bht = makeinches(b[26]);
		}
		if (sortToggle == 1) { 
			if (aht < bht) {
				return -1;
			} else if (aht > bht) {
				return 1;
			} else return 0;
		} else {
			if (bht < aht) {
				return -1;
			} else if (bht > aht) {
				return 1;
			} else return 0;
		};
	});
	makeTable();
};	

function reverseSelect() {
		if (nofilter == 1) {
			return;
		}
		minmin = Number($('input#minmin').val())* minSelect		
		minppg =Number($('input#minppg').val())* ppgSelect		
		minORtg = Number($('input#ortg').val())* ortgSelect	

		minusage = Number($('input#usage').val())* usageSelect	
		mineFG =Number( $('input#efg').val())* efgSelect		
		minTS = Number($('input#ts').val())* tsSelect		
		minOR = Number($('input#oreb').val())* orebSelect	
		minDR = Number($('input#dreb').val())* drebSelect	
		minAst =Number( $('input#ast').val())* astSelect		
		minTO = Number($('input#tov').val())* tovSelect		
		minATO =Number($('input#ato').val())* atoSelect		
		minBlk =Number( $('input#blk').val())* blkSelect		
		minStl =Number( $('input#stl').val())* stlSelect		
		minftr =Number( $('input#ftr').val())* ftrSelect		
		minpfr =Number( $('input#pfr').val())* pfrSelect		
		minrimmade = Number($('input#rimmade').val())* rimmadeSelect	
		minrimatt = Number($('input#rimatt').val())* rimattSelect	
		minrimper = Number($('input#rimper').val())* rimperSelect	
		minmidmade = Number($('input#midmade').val())* midmadeSelect	
		minmidatt = Number($('input#midatt').val())* midattSelect	
		minmidper = Number($('input#midper').val())* midperSelect	
		mindunkmade = Number($('input#dunkmade').val())* dunkmadeSelect	
		mindunkatt = Number($('input#dunkatt').val())* dunkattSelect	
		mindunkper = Number($('input#dunkper').val())* dunkperSelect	
		minftm = Number($('input#ftm').val())* ftmSelect		
		minfta =Number( $('input#fta').val())	* ftaSelect		
		minFT = Number($('input#ftper').val())* ftperSelect	
		mintwopm = Number($('input#twopm').val())* twopmSelect	
		mintwopa =Number( $('input#twopa').val())* twopaSelect	
		min2P = Number($('input#twoper').val())* twoperSelect	
		minthreepm = Number($('input#threepm').val())* threepmSelect	
		minthreepa = Number($('input#threepa').val())* threepaSelect	
		min3P = Number($('input#threeper').val())* threeperSelect
		mintp100 = Number($('input#tp100').val())* tp100Select
		minpick = Number($('input#minpick').val())* pickSelect
		mindpag = Number($('input#mindpag').val())* dpagSelect
		minadrtg = Number($('input#minadrtg').val())* adrtgSelect
// 		minbpm = 	Number($('input#bpm').val())* bpmSelect
		mingbpm = 	Number($('input#gbpm').val())* gbpmSelect
// 		minobpm = 	Number($('input#obpm').val())*obpmSelect
// 		mindbpm = 	Number($('input#dbpm').val())*dbpmSelect
		minmpg = 	Number($('input#minmpg').val())*mpgSelect
		minogbpm = 	Number($('input#ogbpm').val())*ogbpmSelect
		mindgbpm = 	Number($('input#dgbpm').val())*dgbpmSelect
}
$(document).ready(function() {
	reverseSelect()
	if (sIndex == 99){
		$('span#findertype').text('Comps')
		$('span#mobilecomps').html("May not work on mobile.</br>")
	}
	
	rawstartyear = parseInt(start.slice(0,4))
	rawendyear = parseInt(end.slice(0,4))
	rawstartdate = parseInt(start.slice(4,8))
	rawenddate = parseInt(end.slice(4,8))
	
	if (rawenddate > 501) {
		endyear = rawendyear+1
	} else {
		endyear = rawendyear
	}
	if (rawstartdate > 501) {
		startyear = rawstartyear+1
	} else {
		startyear = rawstartyear
	}
	
	numyears = endyear - startyear + 1
	
	if (numyears > 1) {
		multiyear = 1
		year = startyear
		multidone = "(LOADING)"
	} else {
		multiyear = 0
	}
	
	if (String(topx).search('mpg') > -1) {
		mpglimit = 1
	} else {
		mpglimit = 0
	}
	if (year == 'career') {
		if (conyes == 1) {
			source = 'conf_careerstats.json'
		} else {
			source = "careerstats.json?hi=1"
		}
	} else if (year == 'ncaa10') {
		source = 'ncaastatsdecade.json'
	} else if (specialSource == 1 || topx == 'ncaa' || topx == 'H' || topx == 'A' || topx == 'AN' || topx == 'NC' || mpglimit == 1) {
		source = "pslice.php?year="+year+'&top='+topx+'&start='+start+'&end='+end
	} else if (year == 'trans') {
		source = "2027_transfer_stats.json"
	} else if (year == 'trans2026') {
		source = "2026_transfer_stats.json"
		year = 'trans'
	} else if (year == 'all' && (cvalue == 'grads' || xvalue == 'grads')) {
		source = "gradtransfers.json";	
	} else if (year == 'all' && (cvalue == 'trans' || xvalue == 'trans')) {
		source = "reftransfers.json";	
	} else if (year == 'all' && (cvalue == 'd2trans' || xvalue == 'd2trans')) {
		source = "d2transfers.json";	
	} else if (year == 'all' && conyes == 0) {
		source = "all_advstats.json?hi=2"
	} else if (year == 'all' && conyes == 1) {
		source = "all_conf_advstats.json?hi=2"
	} else if (division != 1) {
		source = year + "_d"+ division +"_advanced_player_stats.json?h=7"
	} else if (topx == "alan") {
		source = "alanstats.json"
	} else {
		source = 'getadvstats.php?year='+year+'&specialSource='+specialSource+'&conyes='+conyes+'&start='+start+'&end='+end+'&top='+topx+'&xvalue='+xvalue+'&page='+page+'&team='+fteam;
	}
	$.getJSON(source, function(jsonData) {
		alltdata = jsonData;
		if (multiyear == 1) {
			multiyearnote = "Years: "+year
			makeFullLink()
			while (year < endyear) {
				year ++
				multiyearnote = multiyearnote + ", "+year
				if (division == 1) {
					source = "pslice.php?year="+year+'&top='+topx+'&start='+start+'&end='+end
				} else {
					source = year + "_d"+ division +"_advanced_player_stats.json?h=15"
				}
				$.getJSON(source, function(jsonData) {
					newtdata = jsonData;
					alltdata = alltdata.concat(newtdata)			
				}).success(function() {
					sortTableData(sIndex)
					multidone = ""
					makeFullLink()
					year = endyear


				})	
			}
		}
		if (year == 'career') {
			careerteams = alltdata[1];
			alltdata = alltdata[0];
		}
	}) .done(function() {
	$.getJSON('tsdict_static.json', function (jData) {
		tsdict = jData;
	})	
	$.getJSON('nbatrids.json?hi=1', function (jData2) {
		nbatrids = jData2;
	})	
	.done(function () {
// 	special transfer stuff
	noo = []; // this creates array to check if guy has stats for most recent year, allowing prev year to show in trans portal
	if (year == 2025) {
		alltdata.forEach(function(i) {
			yyy = i[31]
			pname = i[0]
			ttt = i[1]
			if (yyy == 2025) {
				noo[pname+ttt] = 1
			}
		})
	}
	$.getJSON('all_ncaa.json', function(jsonData) {
		allncaa = jsonData;
	})
	$.getJSON('tridyeartransfers.json',function(jsonData2) {
		trantridyear = jsonData2[0];
		tranoutyear = jsonData2[1];
	})
	.done(function() {
// 	$.ajax({
// 	  url: source,
// 	  dataType: 'json',
// 	  async: false,
// 	  success: function(data) {
// 		//stuff
// 		//...
// 	  }
// 	});
	if( sortToggle == 1 ) {sortToggle =0 } else {sortToggle = 1};
	if (division != 1) {
		teams = []
		alltdata.forEach(function(a) {
			ttt = a[1]
			if (!(teams.includes(ttt))) {
				teams.push(ttt)
			}
		})
		teams.sort()
		teamChoices('team')
		if (year == 2023) {
			transource = '2024_d2_transonly.json'
		} else {
			transource = 'all_d2_transfers.json'
		}
		$.getJSON(transource, function (tranData) {
			tranData.forEach(function(a) {
				tranyear = a[0]
				pname = a[1]
				if (tranyear == 2025) {d2tranlist.push(pname)}
			})	
		}).done(function() {
			makeTable()
		})
	}			
	
	if (sIndex == 26) {
		doTheHeightSort(26, 'td#26');
		} else {;
			doTheSort(sIndex,'td#ppgg');
// 			if (year!= 'all' && (cvalue == 'grads' || cvalue == 'trans' || xvalue == 'grads' || xvalue== 'trans')) {
// 				doTheSort(sIndex,'td#ppgg');
// 				doTheSort(sIndex,'td#ppgg');
// 			}
// 
	};
	})
	
	
	
	
// 	makeTable();

	$('td#0').click(function() {doTheSort(0,this)});	
	$('th#teamx').click(function() {
		doTheSort(1,this)
	});	
	$('td#1').click(function() {doTheSort(3,this)});
	$('td#2').click(function() {doTheSort(4,this)});
	$('td#3').click(function() {doTheSort(5,this)});
	$('td#4').click(function() {doTheSort(6,this)});
	$('td#5').click(function() {doTheSort(7,this)});
	$('td#6').click(function() {doTheSort(8,this)});
	$('td#7').click(function() {doTheSort(9,this)});
	$('td#8').click(function() {doTheSort(10,this)});
	$('td#9').click(function() {doTheSort(11,this)});
	$('td#10').click(function() {doTheSort(12,this)});
	$('td#11').click(function() {doTheSort(22,this)});
	$('td#12').click(function() {doTheSort(23,this)});
	$('td#14').click(function() {doTheSort(24,this)});
	$('td#15').click(function() {doTheSort(21,this)});
	$('td#17').click(function() {doTheSort(2,this)});
	$('td#16').click(function() {doTheSort(15,this)});
	$('td#18').click(function() {doTheSort(24,this)});
	$('td#19').click(function() {doTheSort(16,this)});
	$('td#20').click(function() {doTheSort(17,this)});
	$('td#21').click(function() {doTheSort(19,this)});
	$('td#22').click(function() {doTheSort(20,this)});
	$('td#23').click(function() {doTheSort(13,this)});
	$('td#24').click(function() {doTheSort(14,this)});
	$('td#25').click(function() {doTheSort(1,this)});
	$('td#34').click(function() {doTheSort(34,this)});
	$('td#35').click(function() {doTheSort(35,this)});
	$('td#36').click(function() {doTheSort(36,this)});
	$('td#37').click(function() {doTheSort(37,this)});
	$('td#38').click(function() {doTheSort(38,this)});
	$('td#39').click(function() {doTheSort(39,this)});
	$('td#40').click(function() {doTheSort(40,this)});
	$('td#41').click(function() {doTheSort(41,this)});
	$('td#42').click(function() {doTheSort(42,this)});
	$('td#43').click(function() {doTheSort(43,this)});
	$('td#44').click(function() {doTheSort(44,this)});
	$('td#65').click(function() {doTheSort(65,this)});
	$('td#pick').click(function() {doTheSort(45,this)});
	$('td#dpag').click(function() {doTheSort(48,this)});
	$('td#adrtg').click(function() {doTheSort(47,this)});
	$('td#role').click(function() {doTheSort(64,this)});

	$('td#bpm').click(function() {doTheSort(50,this)});
	$('td#obpm').click(function() {doTheSort(51,this)});
	$('td#dbpm').click(function() {doTheSort(52,this)});
	$('td#gbpm').click(function() {doTheSort(53,this)});
	$('td#ogbpm').click(function() {doTheSort(55,this)});
	$('td#dgbpm').click(function() {doTheSort(56,this)});
	$('td#mpg').click(function() {doTheSort(54,this)});
	$('td#tp100').click(function() {doTheSort(65,this)});

	$('td#maxrec').click(function() {doTheSort(34,this)});
	$('td#ppgg').click(function() {doTheSort(28,this)});
	$('td#26').click(function() {doTheHeightSort(26,this)});
	$('td#27').click(function() {doTheHeightSort(26,this)});
	$('td#pts').click(function() {doTheSort(63,this)});
	$('td#reb').click(function() {doTheSort(59,this)});
	$('td#ast').click(function() {doTheSort(60,this)});

		
	$('input').change(function() {
		minGP = Number($('input#gp').val())
		minht =Number($('input#ht').val())
		maxht =Number($('input#maxht').val())
		minrec =Number($('input#min_rec').val())
		maxrec =Number($('input#max_rec').val())
		minpick =Number($('input#minpick').val())
		mindpag =Number($('input#mindpag').val())
		minadrtg =Number($('input#minadrtg').val())

// 		minbpm =Number($('input#bpm').val())
// 		minobpm =Number($('input#obpm').val())
// 		mindbpm =Number($('input#dbpm').val())
		mingbpm =Number($('input#gbpm').val())
		minogbpm =Number($('input#ogbpm').val())
		mindgbpm =Number($('input#dgbpm').val())
		minmpg =Number($('input#mpg').val())

		kw =$('input#kw').val();
		reverseSelect()
		
		
		sortTableData(sIndex);

	});			
	$('select#division').change(function() {
		division = $('select#division').val();
		fullLink = makeFullLink();
		window.location.href = fullink;		
	})	
	$('select').change(function() {
		if (nofilter == 1) {
			return
		}
		yvalue = $('select#yr').val()
		if (xvalue == "trans" || xvalue == 'grads' || year == 'trans') {
			oldteam = $("select#oldteam").val();
		} else {
			oldteam = "All"
		}
		if (oldteam == undefined) {oldteam = "All"}
		tvalue = $("select#team").val();
		cvalue = $('select#conference').val();	
		ocvalue = $('select#oldconference').val();
		slimit = $('select#state').val()	
		minrole = $('select#role').val();			
		if (year == 'all' || year == 'career') {
			xvalue = $('select#xvalueall').val();
		} else {
			xvalue = $('select#xvalue').val();
		}
		if (xvalue == undefined) {xvalue = 'All'};
		if (slimit == undefined || slimit == 'undefined') {slimit = 'All'};
		if (year == 'career' || year == 'all') {
			yearvalue = $('select#yearvalue').val();
		} else {
			yearvalue = 'All';
		}
		minage = $('select#ageSelect').val();
		minSelect		= $('select#minSelect').val()
		ppgSelect		= $('select#ppgSelect').val()
		ortgSelect		= $('select#ortgSelect').val()
		usageSelect		= $('select#usageSelect').val()
		efgSelect		= $('select#efgSelect').val()
		tsSelect		= $('select#tsSelect').val()
		orebSelect		= $('select#orebSelect').val()
		drebSelect		= $('select#drebSelect').val()
		astSelect		= $('select#astSelect').val()
		tovSelect		= $('select#tovSelect').val()
		atoSelect		= $('select#atoSelect').val()
		blkSelect		= $('select#blkSelect').val()
		stlSelect		= $('select#stlSelect').val()
		ftrSelect		= $('select#ftrSelect').val()
		pfrSelect		= $('select#pfrSelect').val()
		rimmadeSelect	= $('select#rimmadeSelect').val()
		rimattSelect	= $('select#rimattSelect').val()
		rimperSelect	= $('select#rimperSelect').val()
		midmadeSelect	= $('select#midmadeSelect').val()
		midattSelect	= $('select#midattSelect').val()
		midperSelect	= $('select#midperSelect').val()
		pickSelect		= $('select#pickSelect').val()
		dpagSelect		= $('select#dpagSelect').val()
		adrtgSelect		= $('select#adrtgSelect').val()

// 		bpmSelect		= $('select#bpmSelect').val()
// 		obpmSelect		= $('select#obpmSelect').val()
// 		dbpmSelect		= $('select#dbpmSelect').val()
		gbpmSelect		= $('select#gbpmSelect').val()
		ogbpmSelect		= $('select#ogbpmSelect').val()
		dgbpmSelect		= $('select#dgbpmSelect').val()
		mpgSelect		= $('select#mpgSelect').val()

		dunkmadeSelect	= $('select#dunkmadeSelect').val()
		dunkattSelect	= $('select#dunkattSelect').val()
		dunkperSelect	= $('select#dunkperSelect').val()


		ftmSelect		= $('select#ftmSelect').val()
		ftaSelect		= $('select#ftaSelect').val()
		ftperSelect	= $('select#ftperSelect').val()
		twopmSelect	= $('select#twopmSelect').val()
		twopaSelect	= $('select#twopaSelect').val()
		twoperSelect	= $('select#twoperSelect').val()
		threepmSelect	= $('select#threepmSelect').val()
		threepaSelect	= $('select#threepaSelect').val()
		threeperSelect	= $('select#threeperSelect').val()
		tp100Select	= $('select#tp100Select').val()
				
		reverseSelect()

		sortTableData(sIndex);

	});	
	
	});
	});

	if (page == 'team') {
		invisible(0);
		invisible('teamx');
		invisible('confx');
		if (window.innerWidth > 600) {
			showstat[15] = 1
			showstat[40] = 1
			showstat[41] = 1
			showstat[42] = 1
			showstat[44] = 1
			hideselect();
		}
	}

		


});	



function dirChoice(s, val, name) {
	if (s == 1) {
		return '<span style="white-space:nowrap">'+name + '≥ ' + s*val + ";</span> "
	} else {
		return '<span style="white-space:nowrap">'+name + '≤ ' + s*val + ";</span> "
	}
}

function makeFullLink() {
	limitstring = ""
	fullink = '?link=y';
	if (comptrid != '') {fullink += '&trid='+comptrid};
	if (compyear != '') {fullink += '&compyear='+compyear};
	if (sIndex != 28) {fullink += '&sIndex='+sIndex};
	if (oldteam != 'All') {fullink += '&oldteam='+encodeURIComponent(oldteam)};
	if (minusage != 5) {
		fullink += '&minusage='+minusage*usageSelect
		limitstring += dirChoice(usageSelect, minusage, "Usage ")
	};
	if (minGP != 0) {fullink += '&minGP='+minGP
		limitstring += dirChoice(1, minGP, "Games Played ")
	};
	if (minORtg != 0) {fullink += '&minORtg='+minORtg*ortgSelect
			limitstring += dirChoice(ortgSelect, minORtg, "O-Rating ")
	};
	if (mineFG != 0) {fullink += '&mineFG='+mineFG*efgSelect
			limitstring += dirChoice(efgSelect, mineFG, "eFG% ")
	};
	if (minTS != 0) {fullink += '&minTS='+minTS*tsSelect		
		limitstring += dirChoice(tsSelect, minTS, "TS% ")
	};
	if (minOR != 0) {fullink += '&minOR='+minOR*orebSelect
			limitstring += dirChoice(orebSelect, minOR, "Off Reb % ")
	};
	if (minDR != 0) {fullink += '&minDR='+minDR*drebSelect
			limitstring += dirChoice(drebSelect, minDR, "Def Reb % ")
	};
	if (minAst != 0) {fullink += '&minAst='+minAst*astSelect
			limitstring += dirChoice(astSelect, minAst, "Assist % ")
	};
	if (minATO != 0) {fullink += '&minATO='+minATO*atoSelect
			limitstring += dirChoice(atoSelect, minATO, "Ast/TO Ratio ")
	};
	if (minTO != 0) {fullink += '&minTO='+minTO*tovSelect
			limitstring += dirChoice(tovSelect, minTO, "Turnover % ")
	};
	if (minBlk != 0) {fullink += '&minBlk='+minBlk*blkSelect
			limitstring += dirChoice(blkSelect, minBlk, "Block % ")
	};
	if (minStl != 0) {fullink += '&minStl='+minStl*stlSelect
			limitstring += dirChoice(stlSelect, minStl, "Steal % ")
	};
	if (min2P != 0) {fullink += '&min2P='+min2P*twoperSelect
			limitstring += dirChoice(twoperSelect, min2P, "2P FG % ")
	};
	if (min3P != 0) {fullink += '&min3P='+min3P*threeperSelect
			limitstring += dirChoice(threeperSelect, min3P, "3P FG % ")
	};
	if (mintp100 != 0) {fullink += '&mintp100='+mintp100*tp100Select
			limitstring += dirChoice(tp100Select, mintp100, "3PA/100 Poss ")
	};
	if (minFT != 0) {fullink += '&minFT='+minFT*ftperSelect
			limitstring += dirChoice(ftperSelect, minFT, "Free Throw % ")
	};
	if (minftr != 0) {fullink += '&minftr='+minftr*ftrSelect
			limitstring += dirChoice(ftrSelect, minftr, "Free Throw Rate ")
	};
	if (minpfr != 0) {fullink += '&minpfr='+minpfr*pfrSelect
			limitstring += dirChoice(pfrSelect, minpfr, "Fouls/40 ")
	};
	if (minht != 0) {fullink += '&minht='+minht
			limitstring += dirChoice(1, minht, "Height ")
	};
	if (maxht != 100 && maxht != 0) {fullink += '&maxht='+maxht
			limitstring += dirChoice(-1, maxht*-1, "Height ")
	};
	if (minrec != 0) {fullink += '&minrec='+minrec
			limitstring += dirChoice(1, minrec, "Rec. Rank ")
	};
	if (maxrec != 100) {fullink += '&maxrec='+maxrec
			limitstring += dirChoice(-1, maxrec, "Rec. Rank ")
	};
	if (minftm != 0) {fullink += '&minftm='+minftm*ftmSelect
			limitstring += dirChoice(ftmSelect, minftm, "FT made ")
	};
	if (minfta != 0) {fullink += '&minfta='+minfta*ftaSelect
			limitstring += dirChoice(ftaSelect, minfta, "FT att. ")
	};
	if (minthreepm != 0) {fullink += '&minthreepm='+minthreepm*threepmSelect
			limitstring += dirChoice(threepmSelect, minthreepm, "3P made ")
	};
	if (minthreepa != 0) {fullink += '&minthreepa='+minthreepa*threepaSelect
			limitstring += dirChoice(threepaSelect, minthreepa, "3P att. ")
	};
	if (mintwopm != 0) {fullink += '&mintwopm='+mintwopm*twopmSelect
			limitstring += dirChoice(twopmSelect, mintwopm, "2P made ")
	};
	if (mintwopa != 0) {fullink += '&mintwopa='+mintwopa*twopaSelect
			limitstring += dirChoice(twopaSelect, mintwopa, "2P att. ")
	};
	if (sortToggle != 0) {fullink += '&sortToggle='+sortToggle};
	if (minrimmade != 0) {fullink += '&minrimmade='+minrimmade*rimmadeSelect
			limitstring += dirChoice(rimmadeSelect, minrimmade, "Makes at rim ")
	};
	if (minrimatt != 0) {fullink += '&minrimatt='+minrimatt*rimattSelect
			limitstring += dirChoice(rimattSelect, minrimatt, "Attempts at rim ")
	};
	if (minrimper != 0) {fullink += '&minrimper='+minrimper*rimperSelect
			limitstring += dirChoice(rimperSelect, minrimper, "FG% at rim ")
	};
	if (minmidmade != 0) {fullink += '&minmidmade='+minmidmade*midmadeSelect
			limitstring += dirChoice(midmadeSelect, minmidmade, "Far 2s made ")
	};
	if (minmidatt != 0) {fullink += '&minmidatt='+minmidatt*midattSelect
			limitstring += dirChoice(midattSelect, minmidatt, "Far 2s attempted ")
	};
	if (minmidper != 0) {fullink += '&minmidper='+minmidper*midperSelect
			limitstring += dirChoice(midperSelect, minmidper, "Far 2 FG% ")
	};
	if (minpick != 0) {fullink += '&minpick='+minpick*pickSelect
			limitstring += dirChoice(pickSelect, minpick, "Draft pick ")
	};
	if (mindpag*dpagSelect != -10) {fullink += '&mindpag='+mindpag*dpagSelect
			limitstring += dirChoice(dpagSelect, mindpag, "Def. PRPG! ")
	};
	if (minadrtg != 0) {fullink += '&minadrtg='+minadrtg*adrtgSelect
			limitstring += dirChoice(adrtgSelect, minadrtg, "Def. Rating ")
	};
	if (showfull != 0) {fullink += '&showfull=1'};

// 	if (minbpm*bpmSelect != -20) {fullink += '&minbpm='+minbpm*bpmSelect};
// 	if (minobpm*obpmSelect != -20) {fullink += '&minobpm='+minobpm*obpmSelect};
// 	if (mindbpm*dbpmSelect != -20) {fullink += '&mindbpm='+mindbpm*dbpmSelect};
	if (mingbpm*gbpmSelect != -20) {fullink += '&mingbpm='+mingbpm*gbpmSelect
			limitstring += dirChoice(gbpmSelect, mingbpm, "Box +/- ")
	};
	if (minogbpm*ogbpmSelect != -20) {fullink += '&minogbpm='+minogbpm*ogbpmSelect
			limitstring += dirChoice(ogbpmSelect, minogbpm, "Off. BPM ")
	};
	if (mindgbpm*dgbpmSelect != -20) {fullink += '&mindgbpm='+mindgbpm*dgbpmSelect
			limitstring += dirChoice(dgbpmSelect, mindgbpm, "Def. BPM ")
	};
	if (minmpg*mpgSelect != 0) {fullink += '&minmpg='+minmpg*mpgSelect
			limitstring += dirChoice(mpgSelect, minmpg, "Minutes ")
	};

	if (mindunkmade != 0) {fullink += '&mindunkmade='+mindunkmade*dunkmadeSelect
			limitstring += dirChoice(dunkmadeSelect, mindunkmade, "Dunks made ")
	};
	if (mindunkatt != 0) {fullink += '&mindunkatt='+mindunkatt*dunkattSelect
			limitstring += dirChoice(dunkattSelect, mindunkatt, "Dunks attempted ")
	};
	if (mindunkper != 0) {fullink += '&mindunkper='+mindunkper*dunkperSelect
			limitstring += dirChoice(dunkperSelect, mindunkper, "Dunk FG% ")
	};

	if (yvalue != 'All') {fullink += '&yvalue='+yvalue
		limitstring += "Class = " + yvalue + "; "
	};
	if (cvalue != 'All') {
		fullink += '&cvalue='+cvalue
		limitstring += "Conf = " + cvalue + "; "
	};
	if (ocvalue != 'All' && ocvalue !== undefined) {
		fullink += '&ocvalue='+ocvalue
		limitstring += "Old Conf = " + ocvalue + "; "
	};
	if (minage != 'All') {
		fullink += '&age='+minage
		limitstring += "Age = " + minage + "; "
	};
	if (minrole != 'All') {
		fullink += '&role='+minrole
		limitstring += "Role = " + minrole + "; "
	};	
	if (xvalue != 'All') {fullink += '&xvalue='+xvalue};
	if (slimit != 'All') {fullink += '&slimit='+slimit};
	if (tvalue != 'All') {fullink += "&tvalue="+encodeURIComponent(tvalue)};
	fullink += '&year='+year;	
	if (minmin != 40) {fullink += '&minmin='+minmin*minSelect
			limitstring += dirChoice(minSelect, minmin, "Min% ")
	};
	if (conyes != 0) {fullink += '&c='+conyes};	
	if (topx != numteams ) {fullink += '&top='+topx};	
	if (kw != '') {fullink += '&kw='+kw};	
	fullink += '&start='+start;	
	fullink += '&end='+end;		
	if (minppg*ppgSelect != -10) {fullink += '&minppg='+minppg*ppgSelect
			limitstring += dirChoice(ppgSelect, minppg, "PORPAGATU! ")
	};
	if(minSelect	!= 1) {fullink += '&minSelect=-1'
			if (minmin == 40) {limitstring += dirChoice(minSelect, minmin, "Min% ")}
	}
	if(division		!= 1) {
		fullink += '&division='+division
	}
	
	if(ppgSelect	!= 1) {fullink += '&ppgSelect=-1'}
	if(ortgSelect	!= 1) {fullink += '&ortgSelect=-1'}
	if(usageSelect	!= 1) {fullink += '&usageSelect=-1'}
	if(efgSelect	!= 1) {fullink += '&efgSelect=-1'}
	if(tsSelect		!= 1) {fullink += '&tsSelect=-1'}
	if(orebSelect	!= 1) {fullink += '&orebSelect=-1'}
	if(drebSelect	!= 1) {fullink += '&drebSelect=-1'}
	if(astSelect	!= 1) {fullink += '&astSelect=-1'}
	if(tovSelect	!= 1) {fullink += '&tovSelect=-1'}
	if(atoSelect	!= 1) {fullink += '&atoSelect=-1'}
	if(blkSelect	!= 1) {fullink += '&blkSelect=-1'}
	if(stlSelect	!= 1) {fullink += '&stlSelect=-1'}
	if(ftrSelect	!= 1) {fullink += '&ftrSelect=-1'}
	if(pfrSelect	!= 1) {fullink += '&pfrSelect=-1'}
	if(rimmadeSelect!= 1) {fullink += '&rimmadeSelect=-1'}
	if(rimattSelect	!= 1) {fullink += '&rimattSelect=-1'}
	if(rimperSelect	!= 1) {fullink += '&rimperSelect=-1'}
	if(midmadeSelect!= 1) {fullink += '&midmadeSelect=-1'}
	if(midattSelect	!= 1) {fullink += '&midattSelect=-1'}
	if(midperSelect	!= 1) {fullink += '&midperSelect=-1'}
	if(dunkmadeSelect!= 1) {fullink += '&dunkmadeSelect=-1'}
	if(dunkattSelect	!= 1) {fullink += '&dunkattSelect=-1'}
	if(dunkperSelect	!= 1) {fullink += '&dunkperSelect=-1'}
	if(ftmSelect	!= 1) {fullink += '&ftmSelect=-1'}
	if(ftaSelect	!= 1) {fullink += '&ftaSelect=-1'}
	if(ftperSelect	!= 1) {fullink += '&ftperSelect=-1'}
	if(twopmSelect	!= 1) {fullink += '&twopmSelect=-1'}
	if(twopaSelect	!= 1) {fullink += '&twopaSelect=-1'}
	if(twoperSelect	!= 1) {fullink += '&twoperSelect=-1'}
	if(threepmSelect!= 1) {fullink += '&threepmSelect=-1'}
	if(threepaSelect!= 1) {fullink += '&threepaSelect=-1'}
	if(threeperSelect!= 1) {fullink += '&threeperSelect=-1'}
	if(tp100Select!= 1) {fullink += '&tp100Select=-1'}
	if(pickSelect!= 1) {fullink += '&pickSelect=-1'}
	if(dpagSelect!= 1) {fullink += '&dpagSelect=-1'}
	if(adrtgSelect!= 1) {fullink += '&adrtgSelect=-1'}
	
// 	if(bpmSelect!= 1) {fullink += '&bpmSelect=-1'}
// 	if(obpmSelect!= 1) {fullink += '&obpmSelect=-1'}
// 	if(dbpmSelect!= 1) {fullink += '&dbpmSelect=-1'}
	if(gbpmSelect!= 1) {fullink += '&gbpmSelect=-1'}
	if(ogbpmSelect!= 1) {fullink += '&ogbpmSelect=-1'}
	if(dgbpmSelect!= 1) {fullink += '&dgbpmSelect=-1'}
	if(mpgSelect!= 1) {fullink += '&mpgSelect=-1'}

	limitstring += multiyearnote
	limitstring += multidone
	
	$('span#limitstring').html(limitstring+'<br/>')
	return fullink
}

function changeYears() {
	if (page != 'playerstat' && page != 'playerstattest') {return;}
	years.forEach(function(y) {
		lnk = location.href.replace('&start='+start,'')
		lnk = lnk.replace('&end='+end,'')
		lnk = lnk.replace(year,y)
		lnk = lnk.replace('&top='+topx,'')
		$('option#'+y).val(lnk)
	})

}

function makePartLink() {
	partlink = "&top="+topx	
	partlink += '&begin='+start;	
	partlink += '&end='+end;
	
	return partlink;
}

var sum_dict = {}

function getsum(src) {
		summ = 0
		tdata = []
		i = 1
		ttdata = src
		playername = ttdata[0];
		team = ttdata[1];
		conf = ttdata[2];
		if (conf == 'P10') {conf = 'P12'};		
		gp = ttdata[3];
		mins = ttdata[4];
		ortg = ttdata[5];	
		usage = ttdata[6];
		efg = ttdata[7];
		ts = ttdata[8];
		oreb = ttdata[9];
		dreb = ttdata[10];
		ast = ttdata[11];
		tov = ttdata[12];
		blk = ttdata[22];
		stl = ttdata[23];
		ftr = ttdata[24];
		pfr = ttdata[30];
		
		ftm = ttdata[i][13];	
		fta = ttdata[i][14];
		ftper = fta == 0 ? 0 : ftm/fta
		fgm = ttdata[i][16];
		fga = ttdata[i][17];
		tpm = ttdata[i][19];
		tpa = ttdata[i][20];
		twoper = fga == 0 ? 0 : fgm / fga;
		threeper = tpa == 0? 0 : tpm / tpa;

		cl = ttdata[25];
		htText = ttdata[26];
		if (htText == null || htText == 0) {htText = 0}
		_inches = makeinches(htText)
		if (isNaN(_inches)) {_inches = 0}
		ppg = ttdata[28];
		_p = ttdata
		if (year == 'career' || year == "ncaa10") {
			allyears = ttdata[31]
			activeyear = allyears[allyears.length-1]
		} else {
			var activeyear = ttdata[31]
		}		
		rec_rk = ttdata[34];
		_rec_rkp = (rec_rk - 50) / 15 
		_threeRate = ttdata[20]/(ttdata[20]+ttdata[17])
		if (isNaN(_threeRate)) {_threeRate = 0}
		_threeratep = (_threeRate - .35) / .1
		adrtg = ttdata[47]
		gbpm = ttdata[53] !== undefined ? Number(ttdata[53]) : NaN;
		_gbpmp = !isNaN(gbpm) ? (gbpm - _stat_dict[53][0]) / _stat_dict[53][1] : 0;
		_adrtgp = (adrtg - _stat_dict[47][0]) / _stat_dict[47][1];
		_oratingp = (_p[5] - _stat_dict[5][0]) / _stat_dict[5][1];
		_usagep = (_p[6] - _stat_dict[6][0]) / _stat_dict[6][1];
		_tsp =  (_p[8] - _stat_dict[8][0]) / _stat_dict[8][1];
		_orbp = (_p[9] - _stat_dict[9][0]) / _stat_dict[9][1];
		_drbp = (_p[10] - _stat_dict[10][0]) / _stat_dict[10][1];
		_astp = (_p[11] - _stat_dict[11][0]) / _stat_dict[11][1];
		_tovp = (_p[12] - _stat_dict[12][0]) / _stat_dict[12][1];
		_blkp = (_p[22] - _stat_dict[22][0]) / _stat_dict[22][1];
		_stlp = (_p[23] - _stat_dict[23][0]) / _stat_dict[23][1];
		_ftrp = (_p[24] - _stat_dict[24][0]) / _stat_dict[24][1];
		_teamperf = (tsdict[activeyear][team][1] - .5) / .15
		_twoperp =(_p[18] - _stat_dict[18][0]) / _stat_dict[18][1];
		if (cl == 'Fr') {
			_cl = 0
		} else if (cl == 'So') {
			_cl = 2
		} else if (cl == 'Jr') {
			_cl = 3
		} else {
			_cl = 4
		}
			

		summ = Math.abs(oratingp-_oratingp) * 2
		+ Math.abs(usagep-_usagep) * 2
		+ Math.abs(tsp-_tsp) 
		+ Math.abs(orbp-_orbp) 
		+ Math.abs(drbp-_drbp) 
		+ Math.abs(astp-_astp) 
		+ Math.abs(tovp-_tovp) 
		+ Math.abs(blkp-_blkp)
		+ Math.abs(stlp-_stlp) * 2
		+ Math.abs(ftrp-_ftrp) 
		+ Math.abs(adrtgp-_adrtgp) 
		+ Math.abs(gbpmp-_gbpmp) 
		+ Math.abs(teamperf-_teamperf) * 2
		+ Math.abs(rec_rkp-_rec_rkp) 
		+ Math.abs(threeratep - _threeratep)
		+ Math.abs(twoperp - _twoperp)
		+ Math.abs(_cl - __cl)
		+ Math.abs(_inches - __inches) / 4
		

		sum_dict[String(ttdata[32])+String(activeyear)] = summ.toFixed(2)
		return summ
}

function compareSort() {
		$('span#findertype').text('Comps')
		i = 'hello'
		if (typeof(comp) == 'undefined') {
			getcomptrid()
		}
		ttdata = comp
		playername = ttdata[0];
		team = ttdata[1];
		conf = ttdata[2];
		if (conf == 'P10') {conf = 'P12'};		
		gp = ttdata[3];
		mins = ttdata[4];
		ortg = ttdata[5];	
		usage = ttdata[6];
		efg = ttdata[7];
		ts = ttdata[8];
		oreb = ttdata[9];
		dreb = ttdata[10];
		ast = ttdata[11];
		tov = ttdata[12];
		blk = ttdata[22];
		stl = ttdata[23];
		ftr = ttdata[24];
		pfr = ttdata[30];
		twoper = ttdata[18];
		threeper = ttdata[21];
		ftper = ttdata[15];
		ftm = ttdata[13];	
		fta = ttdata[14];
		fgm = ttdata[16];
		fga = ttdata[17];
		tpm = ttdata[19];
		tpa = ttdata[20];
		cl = ttdata[25];
		htText = ttdata[26];
		if (htText == null || htText == 0) {htText = 0}
		__inches = makeinches(htText)
		ppg = ttdata[28];
		_p = ttdata
		if (year == 'career' || year == "ncaa10") {
			allyears = ttdata[31]
			activeyear = allyears[allyears.length-1]
		} else {
			var activeyear = ttdata[31]
		}		
		rec_rk = ttdata[34];
		rec_rkp = (rec_rk - 50) / 15
		threeRate = ttdata[20]/(ttdata[20]+ttdata[17])
		if (isNaN(threeRate)) {threeRate = 0}
		threeratep = (threeRate - .35) / .1 
		adrtg = ttdata[47]
		gbpm = ttdata[53] !== undefined ? Number(ttdata[53]) : NaN;
		gbpmp = !isNaN(gbpm) ? (gbpm - _stat_dict[53][0]) / _stat_dict[53][1] : 0;
		adrtgp = (adrtg - _stat_dict[47][0]) / _stat_dict[47][1];
		oratingp = (_p[5] - _stat_dict[5][0]) / _stat_dict[5][1];
		usagep = (_p[6] - _stat_dict[6][0]) / _stat_dict[6][1];
		tsp =  (_p[8] - _stat_dict[8][0]) / _stat_dict[8][1];
		orbp = (_p[9] - _stat_dict[9][0]) / _stat_dict[9][1];
		drbp = (_p[10] - _stat_dict[10][0]) / _stat_dict[10][1];
		astp = (_p[11] - _stat_dict[11][0]) / _stat_dict[11][1];
		tovp = (_p[12] - _stat_dict[12][0]) / _stat_dict[12][1];
		blkp = (_p[22] - _stat_dict[22][0]) / _stat_dict[22][1];
		stlp = (_p[23] - _stat_dict[23][0]) / _stat_dict[23][1];
		ftrp = (_p[24] - _stat_dict[24][0]) / _stat_dict[24][1];// 		pfrp = Math.round(cdf((_p[30] - _stat_dict[30][0]) / _stat_dict[30][1])*100);
		teamperf = (tsdict[activeyear][team][1] - .5) / .15
		twoperp = (_p[18] - _stat_dict[18][0]) / _stat_dict[18][1];
		if (cl == 'Fr') {
			__cl = 0
		} else if (cl == 'So') {
			__cl = 2
		} else if (cl == 'Jr') {
			__cl = 3
		} else {
			__cl = 4
		}
	alltdata.sort(function (a,b) {
		asum = getsum(a)
		bsum = getsum(b)


		if (bsum > asum) {
			return -1;
		} else if (bsum < asum) {
			return 1;
		} else return 0;
	})
	makeTable();
}

function getAge(dateString, seasonYear) {
    if (!dateString) return null;
    var today = new Date(seasonYear, 5, 30); // June 30th of the season year
    var birthDate = new Date(dateString);
    if (isNaN(birthDate)) return null;

    var yearDiff = today.getFullYear() - birthDate.getFullYear();
    var monthDiff = today.getMonth() - birthDate.getMonth();

    if (today.getDate() < birthDate.getDate()) {
        monthDiff--;
    }

    return yearDiff + (monthDiff / 12);

}

per100 = 0
function makeTable() {
	if (Math.abs(min3P) > 1) {min3P = min3P / 100;}
	if (Math.abs(min2P) > 1) {min2P = min2P / 100;}
	if (Math.abs(minFT) > 1) {minFT = minFT / 100;}	
	if (Math.abs(minrimper) > 1) {minrimper = minrimper / 100;}		
	if (Math.abs(minmidper) > 1) {minmidper = minmidper / 100;}		
	if (Math.abs(mindunkper) > 1) {mindunkper = mindunkper / 100;}		
	if (start == end) {
		dopoints = 1;
		basicround = 0;
	} else {
		basicround = 1;
	}
	if (per100 == 1) {
		totalround = 1;
	} else {
		totalround = 0;
	}
	if (dopoints == 1) {
		pointshead = ''
		pointshead += "<th class='ast' id='ast'>Ast</th>";
		pointshead += "<th class='reb' id='reb'>Reb</th>";
		pointshead += "<th class='pts' id='pts'>Pts</th>";
	} else {
		pointshead = "";
	}
	if (year == 'all' || multiyear == 1) {
		yearhead = "<th class='31 mobileout' id='year'>Year</th>";
	} else {
		yearhead = "";
	}	
	if (mindunkmade != 0 || mindunkatt !=0 || mindunkmade != 0 || minrimmade != 0 || minrimatt !=0 || minmidmade != 0 || minmidatt != 0 || minrimper !=0 || minmidper !=0 || (sIndex >= 36 && sIndex <= 44)) {pbp = 1}
	else {pbp = 0}
    $('.ui-tooltip').remove()
	var spindex = sIndex;
	if (spindex == 16 || spindex == 17) {spindex = 1617};
	if (spindex == 13 || spindex == 14) {spindex = 1314};
	if (spindex == 19 || spindex == 20) {spindex = 1920};	
	if (spindex == 36 || spindex == 37) {spindex = 3637};	
	if (spindex == 38 || spindex == 39) {spindex = 3839};	
	var styleChange = '<style>._' + spindex + ' {font-weight:bold} </style>'
// 	xvalue = $('select#xvalue').val();				

	fullLink = makeFullLink();
	partlink = makePartLink();
	if (page == 'playerstat') {
		window.history.replaceState("", "Title", fullLink);
	}
	changeYears();
	if (year == 'trans' || (year == 'all' && (xvalue =='grads' || xvalue=='trans'))) {
		yearlink = 2025;
		conheader = 'Old Team';
	} else {
		yearlink = year;
		conheader = 'Conf';
	}
	tableHTML = styleChange + 
	'<table style="white-space:nowrap;margin:auto;table-layout:fixed"><thead><tr><th class="0 rk mobileout">Rk</th>\
	<th class="mobileout 45" id="pick">Pick</th><th class="mobileonly" id="player">Player</th>\
	<th class="mobileout" colspan="3" id="player">Player</th><th class="mobileout 34" id="rec">\
	</th><th style="text-align:left" class="teamx mobileout" id="teamx">Team</th>\
	<th style="text-align:left" class="mobileout confx" id="conference">'+conheader+'</th>\
	<th class="mobileout 3" id="gp">G</th><th class="mobileout 64" id="role">Role</th>\
	<th class=4 id="mins">Min%</th><th class=28 title="Adjusted PORPAGATU!" id="p">PRPG!</th>\
	<th class="mobileout 48" id="dpag">D-PRPG</th>\
	<!--<th class="mobileout 50" id="bpm">BPM</th><th class="mobileout 51" id="obpm">OBPM</th><th class="mobileout 52" id="dbpm">DBPM</th>--!>\
	<th class="mobileout 53" id="gbpm">BPM</th><th class="mobileout 55" id="ogbpm">OBPM</th>\
	<th class="mobileout 56" id="dgbpm">DBPM</th><th class=5 id="orating">ORtg</th>\
	<th class="mobileout 47" id="adrtg">D-Rtg</th><th class=6 id="usg">Usg</th>\
	<th class=7 id="efg">eFG</th><th class="mobileout 8" id="ts">TS</th><th class="mobileout 9" id="oreb">OR</th>\
	<th class="mobileout 10" id="orebd">DR</th><th class="mobileout 11" id="astper">Ast</th>\
	<th class="mobileout 12" id="tor">TO</th><th class="mobileout 35" id="ato">A/TO</th>\
	<th class="mobileout 22" id="blk">Blk</th><th class="mobileout 23" id="stl">Stl</th>\
	<th class="mobileout 24" id="ftr">FTR</th><th class="mobileout 30" id="pfr">FC/40</th>\
	<th  class="mobileout 42" id="dunk" colspan=2>Dunks</th><th class="mobileout 40" id="rim" colspan=2>Close 2</th>\
	<th  class="mobileout 41" id="mid" colspan=2>Far 2</th><th  class="mobileout 15" id="ftper" colspan=2>FT</th>\
	<th  class="mobileout 18" id="twoper" colspan=2>2P</th><th class="mobileout tprate" id="tprate" title="Three Point Attempt Rate">3PR</th>\
	<th class="mobileout 65" id="tp100" title="Threes per 100 possessions">3P/100</th>\
	<th  class="mobileout 21" id="threeper" colspan=2>3P</th>'+pointshead+yearhead+'</tr></thead><tbody>';
	var tdata = alltdata;
	var icount = 0
	tot_dunkm = 0
	tot_dunka = 0
	tot_rimm = 0
	tot_rima = 0
	tot_midm = 0
	tot_mida = 0
	tot_twom = 0
	tot_twoa = 0
	tot_threem = 0
	tot_threea = 0
	tot_ftm = 0
	tot_fta = 0
	
	if (kw == '-*') {endrk = 1000};
	for (var i = startrk-1; icount < endrk-startrk+1 && i < tdata.length; i++) {

		if (tdata[i] == 0) { continue;}
		playername = tdata[i][0];
		team = tdata[i][1];
		conf = tdata[i][2];
		if (conf == 'P10') {conf = 'P12'};		
		tp100 = tdata[i][65];
		tpa = tdata[i][20]
		possessions = tpa*100 / tp100
		per100q = per100 == 0 ? 1 : 100 / possessions
		gp = tdata[i][3];
		per100g = per100 == 0 ? 1 : 100 / possessions * gp
		mins = tdata[i][4];
		if (mins == 0) {continue;}
		ortg = tdata[i][5];	
		usage = tdata[i][6];
		efg = tdata[i][7];
		ts = tdata[i][8];
		oreb = tdata[i][9] ;
		dreb = tdata[i][10];
		ast = tdata[i][11];
		tov = tdata[i][12];
		blk = tdata[i][22];
		stl = tdata[i][23];
		ftr = tdata[i][24];
		pfr = tdata[i][30];
		ftm = tdata[i][13]*per100q;	
		fta = tdata[i][14]*per100q;
// 		ftper = fta == 0 ? 0 : ftm/fta
		ftper = tdata[i][15]
		fgm = tdata[i][16]*per100q;
		fga = tdata[i][17]*per100q;
		tpm = tdata[i][19]*per100q;
		tpa = tdata[i][20]*per100q;
// 		twoper = fga == 0? 0 : fgm / fga;
// 		threeper = tpa == 0? 0 : tpm / tpa;
		twoper = tdata[i][18]
		threeper = tdata[i][21]
		trid = tdata[i][32];
		pts = (ftm + fgm * 2 + tpm * 3);
		tprate = (tpa+fga > 0) ? tpa/(tpa+fga) : 0
		if (tp100 == undefined) {
			tp100 = 0;
		}
		if (year != 'career' && year != "ncaa10") {
			var activeyear = tdata[i][31]
			if (year == 'all') {
				if (activeyear < yearvalue) {
					continue;
				}
			}
		} else {
			var allyears = tdata[i][31]
			var activeyear = allyears[allyears.length-1]
			if (yearvalue != 'All' && !allyears.includes(parseInt(yearvalue))) {
				continue;
			}
			if (playername == 'Cooper Flagg') {console.log(
				allyears,
				activeyear,
				yearvalue,
				yearvalue != 'All' && !allyears.includes(parseInt(yearvalue))
				)
			}

		}

		comp_id = String(trid)+String(activeyear)
		compstat = sum_dict[comp_id]
		cl = tdata[i][25];
		htText = tdata[i][26];
		ppg = tdata[i][28];
		_p = tdata[i]
		if (activeyear < 2010 && pbp == 1) {continue;}
		nameteam = playername+team
		tranguy = ''
		shortyear = '';
// 		special transfer stuff
		if (activeyear != year && multiyear == 0 && xvalue != 'trans' && year != 'trans' && xvalue != 'grads' && year != 'trans' && year != 'all' && year != 'career' && year != "ncaa10" && division == 1) {continue;}

		rec_rk = tdata[i][34];
		ato = tdata[i][35] == null ? 0 : 		 tdata[i][35]
		rimmade = tdata[i][36] == null ? 0 : 	 tdata[i][36]*per100q
		rimatt = tdata[i][37] == null ? 0 : 	 tdata[i][37]*per100q
		rimper = (rimmade / rimatt);
		midmade = tdata[i][38] == null ? 0 : 	 tdata[i][38]*per100q
		midatt = tdata[i][39] == null ? 0 : 	 tdata[i][39]*per100q
		midper = (midmade / midatt);
		dunkmade = tdata[i][42] == null ? 0 :	 tdata[i][42]*per100q
		dunkatt = tdata[i][43] == null ? 0 : 	 tdata[i][43]*per100q
// 		dunkmade = tdata[i][42] == null ? 0 :	year != 'all' 	? tdata[i][42] : dunkmade   = '';
// 		dunkatt = tdata[i][43] == null ? 0 : 	year != 'all' 	? tdata[i][43] : dunkatt   = '';
		dunkper = (dunkmade / dunkatt);

		pick = Number(tdata[i][45])
		dpag = Number(tdata[i][48])
		adrtg = Number(tdata[i][47])
		if (division == '2' || tdata[i][2] == 'd2') {
			bpm = NaN;
			obpm = NaN;
			dbpm = NaN;
			gbpm = tdata[i][53] !== undefined ? Number(tdata[i][53]) : NaN;
			ogbpm = tdata[i][55] !== undefined ? Number(tdata[i][55]) : NaN;
			dgbpm = tdata[i][56] !== undefined ? Number(tdata[i][56]) : NaN;
		} else {
			bpm = Number(tdata[i][50]);
			obpm = Number(tdata[i][51]);
			dbpm = Number(tdata[i][52]);
			gbpm = Number(tdata[i][53]);
			ogbpm = Number(tdata[i][55]);
			dgbpm = Number(tdata[i][56]);
		}
		var raw_mpg = tdata[i][54] !== undefined ? Number(tdata[i][54]) : (Number(tdata[i][4]) / 100.0 * 40.0);
		mpg = !isNaN(raw_mpg) ? (raw_mpg * gp).toFixed(0) : 0;
		role = tdata[i][64]
		titletown = ""
		
		midper = isNaN(midper) ?    0 : midper
		rimper = isNaN(rimper) ?  	0: rimper
		dunkper = isNaN(dunkper) ?  0: dunkper
		if (pick == null || pick == 0 || isNaN(pick) || pick == 80) {
			picktext = '-';
			pick = 80;
		} else {
			picktext = pick;
		}

		if (year == 'all' || multiyear == 1 || activeyear != year && (xvalue == 'trans' || xvalue == 'grads')) {
			if (division == '2') {tdata[i][31] = tdata[i][29]}
			var playerlink = '?year='+activeyear+'&p='+encodeURIComponent(playername)+'&t='+encodeURIComponent(team);
			var shortyear = '('+tdata[i][31].toString().substr(-2,2)+')';
			if (year == 'all' || multiyear == 1) {
			yeartext = "<td class='mobileout _31' style='border-left:1px solid black;'>"+String(tdata[i][31])+"</td>";
			}
		} else {
			var playerlink = '?year='+yearlink+'&p='+encodeURIComponent(playername)+'&t='+encodeURIComponent(team);
			var shortyear = '';
			yeartext = '';
		} // else {
// 			var playerlink = '?year=all&p='+encodeURIComponent(playername);
// 		}	
		numtext = "</div>"

		if ((page != 'team' && trid != comptrid && page != 'team-history') || tdata[i][66] == 'd2'  ) {
			mins				*= minSelect		
			ppg				*= ppgSelect		
			ortg				*= ortgSelect		
			usage			*= usageSelect	
			efg				*= efgSelect		
			ts				*= tsSelect		
			oreb				*= orebSelect		
			dreb			*= drebSelect		
			ast				*= astSelect		
			tov				*= tovSelect		
			ato				*= atoSelect		
			blk				*= blkSelect		
			stl				*= stlSelect		
			ftr				*= ftrSelect		
			pfr				*= pfrSelect		
			rimmade			*= rimmadeSelect	
			rimatt			*= rimattSelect	
			rimper			*= rimperSelect	
			midmade			*= midmadeSelect	
			midatt			*= midattSelect	
			midper			*= midperSelect	
			dunkmade		*= dunkmadeSelect	
			dunkatt			*= dunkattSelect	
			dunkper			*= dunkperSelect	
			ftm				*= ftmSelect		
			fta		*= ftaSelect		
			ftper		*= ftperSelect	
			fgm	*= twopmSelect	
			fga	*= twopaSelect	
			twoper	*= twoperSelect	
			tpm	*= threepmSelect	
			tpa	*= threepaSelect	
			threeper	*= threeperSelect
			tp100	*= tp100Select
			pick 			*= pickSelect	
			dpag 			*= dpagSelect	
			adrtg 			*= adrtgSelect	
			bpm 			*= bpmSelect	
			obpm 			*= obpmSelect	
			dbpm 			*= dbpmSelect	
			gbpm 			*= gbpmSelect	
			mpg 			*= mpgSelect	
			ogbpm 			*= ogbpmSelect	
			dgbpm 			*= dgbpmSelect	


			if (xvalue == 'nba') {
				if (trid in nbatrids == false) {continue}
			} else if (xvalue == 'notnba') {
				if (trid in nbatrids) {continue}
			}
			if (year == 'trans') {
				team = tdata[i][34];
				rec_rk = ''
			}
			rec_rk = rec_rk == null ? 0 : rec_rk;
		
			if (tdata[i].length < 27 || tdata[i][26] == 0 ||tdata[i][26] == null) {
				var ht = 0;
			} else {
				var ht = makeinches(tdata[i][26]);
			}
		
			if (sIndex == 26 && ht == 0) {continue;}
		
			if (htText == undefined) {htText = 'n/a';}
		
			if (team == 'Arkansas Little Rock') {team = 'Little Rock';}
			if (team == 'IPFW') {team = 'Fort Wayne';}

			if ((ht == 'n/a' || ht == 0 || isNaN(ht)) && (minht > 0 || maxht < 100) && maxht != 1) {continue;}

			if (ato < minATO || rec_rk < minrec || rec_rk > maxrec || ppg < minppg || ht < minht || pfr < minpfr || ftr < minftr || mins < minmin || usage < minusage || gp < minGP || ortg < minORtg || efg < mineFG || ts < minTS || oreb < minOR || dreb < minDR || ast < minAst || blk < minBlk || stl < minStl || twoper < min2P || threeper < min3P || tp100 < mintp100 || ftper < minFT || ftm < minftm || fta < minfta || tpm < minthreepm || tpa < minthreepa || fgm < mintwopm || fga < mintwopa) {
				continue;
			}
		
			if (minTO != '' && minTO > tov) {continue};
			if (maxht != '' && ht > maxht) {continue};
		
			if(dunkmade < mindunkmade || dunkatt < mindunkatt || dunkper < mindunkper || rimmade < minrimmade || rimatt < minrimatt || rimper < minrimper || midmade < minmidmade || midatt < minmidatt || midper < minmidper) {continue;}
			if (bpm < minbpm || obpm < minobpm || dbpm < mindbpm ||ogbpm < minogbpm || dgbpm < mindgbpm || gbpm < mingbpm || mpg < minmpg || pick < minpick || dpag < mindpag || adrtg < minadrtg) {
				continue;
			} 

		
			mins			*= minSelect		
			ppg				*= ppgSelect		
			ortg			*= ortgSelect		
			usage			*= usageSelect	
			efg				*= efgSelect		
			ts				*= tsSelect		
			oreb			*= orebSelect		
			dreb			*= drebSelect		
			ast				*= astSelect		
			tov				*= tovSelect		
			ato				*= atoSelect		
			blk				*= blkSelect		
			stl				*= stlSelect		
			ftr				*= ftrSelect		
			pfr				*= pfrSelect		
			rimmade			*= rimmadeSelect	
			rimatt			*= rimattSelect	
			rimper			*= rimperSelect	
			midmade			*= midmadeSelect	
			midatt			*= midattSelect	
			midper			*= midperSelect	
			dunkmade		*= dunkmadeSelect	
			dunkatt			*= dunkattSelect	
			dunkper			*= dunkperSelect			
			ftm				*= ftmSelect		
			fta				*= ftaSelect		
			ftper			*= ftperSelect	
			fgm			*= twopmSelect	
			fga			*= twopaSelect	
			twoper			*= twoperSelect	
			tpm			*= threepmSelect	
			tpa			*= threepaSelect	
			threeper		*= threeperSelect
			tp100	*= tp100Select
			pick 		*= pickSelect	
			dpag 		*= dpagSelect	
			adrtg 		*= adrtgSelect	
			bpm 		*= bpmSelect	
			obpm 		*= obpmSelect	
			dbpm 		*= dbpmSelect	
			gbpm 		*= gbpmSelect	
			mpg 		*= mpgSelect	
			ogbpm 		*= ogbpmSelect	
			dgbpm 		*= dgbpmSelect	
		
			region = regions[team];
			if (slimit != undefined && slimit != 'undefined' && slimit != 'All') {
				if (tdata[i][33] == null) {continue;}
				pstate = tdata[i][33].split(", ").at(-1)
				if (slimit == "Intl") {
					if (states.indexOf(pstate) > -1) {continue;}
				} else {
					if (pstate != slimit) {continue;}
				}
			} 
			
			if (year == 'trans') {
				null
			} else if (cvalue != 'truhi' && cvalue != 'trumid' && cvalue != 'All' && cvalue != "Mid" && cvalue != 'High Major' && cvalue != 'NCAA' &&cvalue != conf && cvalue != 'Alive' && ncaaregions.indexOf(cvalue) <0 && cvalue != 'trans' && cvalue != 'grads' && cvalue !="pros" && cvalue != 'early' && cvalue != 'ret') {
				continue;
			} else if (cvalue == 'High Major' && himajor.indexOf(conf) < 0) {
				continue;
			} else if (cvalue == 'Mid' && himajor.indexOf(conf) >= 0) {
				continue;
			} else if (cvalue == 'trumid' && (himid.indexOf(team) >= 0 || himajor.indexOf(conf) >= 0)) {
				continue;
			} else if (cvalue == 'truhi' && himajor.indexOf(conf) < 0) {
				if (himid.indexOf(team) < 0) {
					continue;
				}
			} else if (cvalue == "NCAA") {
					if (activeyear in allncaa) {
						if (Object.keys(allncaa[activeyear]).includes(team) == false) {
							continue;
						} 
					} else {
						continue
					}
			} else if (cvalue == "Alive" && elims.indexOf(team) >= 0) {
				continue;
			} else if (cvalue == "Alive" && (Object.keys(allncaa[activeyear]).includes(team) == false)) {
				continue;		
			} else if (ncaaregions.indexOf(cvalue) >= 0) {
				if (region != cvalue) {
					continue;
				}
			} else if ((cvalue == 'grads' && year != 'all') || (cvalue == 'trans' && year != 'all')) {
				nameteam = playername+team
				if (!(nameteam in trandict)) {continue;}
				if (trandict[nameteam][2] != null && trandict[nameteam][2] != "" && showalltransfers == -1) {
					continue;
				} else if (trandict[nameteam][2] != null && trandict[nameteam][2] != "")  {
					tranguy = '<span title="transfering to '+ trandict[nameteam][2] +'"> *</span>'
				}
				if (cvalue == 'grads' && (trandict[nameteam][3] != 'Yes' || trandict[nameteam][3] != '') ) {continue;}
				if (cvalue == 'grads' && trandict[nameteam][2] == null && prevyeardict[trid] > 4 && showeveryone == -1) {continue;}
			} else if (cvalue == 'pros') {
				nameteam = playername+team
				if (!(nameteam in prodict)) {continue;}
			} else if (cvalue == 'early') {
				nameteam = playername+team
				if (!(nameteam in prodict) || cl == 'Sr') {continue;}
			} else if (cvalue == 'ret') {
				nameteam = playername+team
				if ((nameteam in prodict)) {continue;}
			} 
		
			if (yvalue == 'FrSo' && cl != 'Fr' && cl != 'So') {
					continue
			} else if (yvalue == 'NoSr' && cl == 'Sr') {
				continue;
			} else if (yvalue != 'All' && yvalue != cl && yvalue != 'FrSo' && yvalue != 'NoSr') {
				continue;
			}
			
            if (minage != 'All') {
                // Assuming birthdate is at index 66
                var birthDateString = tdata[i][66]; 
                var age = getAge(birthDateString, activeyear);
                if (age === null) {
                    continue;
                }
				
				if (minage == 'u19' && age >= 19) {
					continue;
				} else if (minage == 'u20' && (age >= 20)) {
					continue;
				} else if (minage == 'u21' && (age >= 21)) {
					continue;
				} else if (minage == 'u22' && (age >= 22)) {
					continue;
				} else if (minage == '22+' && age < 22) {
					continue;
					
				} else if (minage == '19' && (age < 19 || age >= 20)) {
					continue;
				} else if (minage == '20' && (age < 20 || age >= 21)) {
					continue;
				} else if (minage == '21' && (age < 21 || age >= 22)) {
					continue;
				} 
 
            }
            
			if (slimit != undefined && slimit != 'All') {
				town = tdata[i][33]
				titletown = 'title="'+town+'"'
			}				
			if ((xvalue == 'grads' && year != 'all') || (xvalue == 'trans' && year != 'all')) {
				town = tdata[i][33]
				titletown = 'title="'+town+'"'
				if (division == 2) {
					if (d2tranlist !== undefined) {

						if (d2tranlist.includes(playername) == false) {continue;}
					}
				} else {
					if (!(nameteam in trandict)) {continue;}
					if (trandict[nameteam][2] != "" && trandict[nameteam][2] != null && showalltransfers == -1) {
						continue;
					} else if (trandict[nameteam][2] != null && trandict[nameteam][2] != "") {
						tranguy = '<span title="transfering to '+ trandict[nameteam][2] +'"> *</span>'
					}
					if (xvalue == 'grads' && trandict[nameteam][3] != 1 && trandict[nameteam][3] != "") {continue;}
					if (trandict[nameteam][2] == null && prevyeardict[trid] > 4 && showeveryone == -1) {continue;}
				}
			} else if (xvalue == 'pros') {
				if (!(nameteam in prodict)) {continue;}
			} else if (xvalue == 'early') {
				if (!(nameteam in prodict) || cl == 'Sr') {continue;}
			} else if (xvalue == 'ret') {
				if ((nameteam in prodict && !(nameteam in trandict))) {continue;}
				if (nameteam in trandict) {
					newteam = trandict[nameteam][2]
					tranguy = '<span title="transfering to '+ newteam+'"> *</span>'
				}	
			}
			if (tvalue != 'All' && (tvalue != team || xvalue == 'transout') ) {
				if (year == 'career') {
					tridteams = careerteams[trid];
					if (tridteams.includes(tvalue) == false) {
						continue;
					} 
					if (xvalue == 'transout') {
						if (tridteams[tridteams.length - 1] == tvalue && trid+team in tranoutyear == false) {
							continue;
						}
					}
				} else if (year == 'all') {
					if (tvalue != team) {continue;}
				} else {
					continue;
				}
			}	
			if (year == 'trans' && playername+conf in trandict) {
					tranguy = '<span title="grad transfer"> *</span>'
				}
			
			if (minrole != 'All' && minrole != role) {	continue;}

			if (kw.charAt(0) == '-') {
				notext = kw.substr(1)
				if ((playername+shortyear+tranguy).toUpperCase().indexOf(notext.toUpperCase()) >= 0) {
					continue;
				}
			} else if (kw != '' & (playername+shortyear+tranguy).toUpperCase().indexOf(kw.toUpperCase()) == -1) {
				continue;
			} 

		} else {
			if ((tvalue != 'All' && tvalue != team) || mins < minmin || (comptrid != "" && comptrid != trid)) {
				continue;
			}
			if (page == 'team') {numtext = tdata[i][27] ==  null ? "</div>" : ("#"+tdata[i][27]).padEnd(4)+"</div>&nbsp;"}

		}


		if (activeyear == 2025 && year == 2026 && (noo[playername+team] == 1 || noo[playername+trandict[nameteam][2]] == 1) && division != 2) {continue;}


		var pchars = p.length;
		var ppure = playername.substring(0,pchars);
// 		if (p.substring(p.length-3) == "Jr.") {p = p.substring(0,p.length-3);}
		if (p != 0 && p.toUpperCase().replace(",",'').replace("Jr.",'').replace(" ",'') != ppure.toUpperCase().replace(",",'').replace("Jr.",'').replace(" ",'')) {continue;} 
		
		rk = icount+startrk;		

		_gtr[352] = _gtr[351];
		_gtr[0] = _gtr[1];

		_ppgp = Math.round(cdf((ppg - _stat_dict[25][0]) / _stat_dict[25][1])*100,1);
		_ppgc = _gtr[Math.round(352 - (_ppgp/100 * 351),0)]; 

		_dppgp = Math.round(cdf((dpag - _stat_dict[48][0]) / _stat_dict[48][1])*100,1);
		_dppgc = _gtr[Math.round(352 - (_dppgp/100 * 351),0)]; 

		if (isNaN(bpm)) { _bpmp = NaN; _bpmc = "#ffffff"; }
		else { _bpmp = Math.round(cdf((bpm - _stat_dict[50][0]) / _stat_dict[50][1])*100,1); _bpmc = _gtr[Math.round(352 - (_bpmp/100 * 351),0)]; }

		if (isNaN(obpm)) { _obpmp = NaN; _obpmc = "#ffffff"; }
		else { _obpmp = Math.round(cdf((obpm - _stat_dict[51][0]) / _stat_dict[51][1])*100,1); _obpmc = _gtr[Math.round(352 - (_obpmp/100 * 351),0)]; }

		if (isNaN(dbpm)) { _dbpmp = NaN; _dbpmc = "#ffffff"; }
		else { _dbpmp = Math.round(cdf((dbpm - _stat_dict[52][0]) / _stat_dict[52][1])*100,1); _dbpmc = _gtr[Math.round(352 - (_dbpmp/100 * 351),0)]; }

		if (isNaN(gbpm)) { _gbpmp = NaN; _gbpmc = "#ffffff"; }
		else { _gbpmp = Math.round(cdf((gbpm - _stat_dict[53][0]) / _stat_dict[53][1])*100,1); _gbpmc = _gtr[Math.round(352 - (_gbpmp/100 * 351),0)]; }

		if (isNaN(ogbpm)) { _ogbpmp = NaN; _ogbpmc = "#ffffff"; }
		else { _ogbpmp = Math.round(cdf((ogbpm - _stat_dict[51][0]) / _stat_dict[51][1])*100,1); _ogbpmc = _gtr[Math.round(352 - (_ogbpmp/100 * 351),0)]; }

		if (isNaN(dgbpm)) { _dgbpmp = NaN; _dgbpmc = "#ffffff"; }
		else { _dgbpmp = Math.round(cdf((dgbpm - _stat_dict[52][0]) / _stat_dict[52][1])*100,1); _dgbpmc = _gtr[Math.round(352 - (_dgbpmp/100 * 351),0)]; } 


		_adrtgp = Math.round(cdf((adrtg - _stat_dict[47][0]) / _stat_dict[47][1])*100,1);
		_adrtgc = _gtr[Math.round(_adrtgp/100 * 351,0)]; 

		_oratingp = Math.round(cdf((_p[5] - _stat_dict[5][0]) / _stat_dict[5][1])*100);
		_oratingc = _gtr[Math.round(352 - (_oratingp/100 * 351))];

		_usagep = Math.round(cdf((_p[6] - _stat_dict[6][0]) / _stat_dict[6][1])*100);
		_usagec = _gtr[Math.round(352 - (_usagep/100 * 351))]; 
		
		_efgp = Math.round(cdf((_p[7] - _stat_dict[7][0]) / _stat_dict[7][1])*100);
		_efgc = _gtr[Math.round(352 - (_efgp/100 * 351))]; 
		
		_tsp = Math.round(cdf((_p[8] - _stat_dict[8][0]) / _stat_dict[8][1])*100);
		_tsc = _gtr[Math.round(352 - (_tsp/100 * 351))]; 
		
		_orbp = Math.round(cdf((_p[9] - _stat_dict[9][0]) / _stat_dict[9][1])*100);
		_orbc = _gtr[Math.round(352 - (_orbp/100 * 351))]; 
		
		_drbp = Math.round(cdf((_p[10] - _stat_dict[10][0]) / _stat_dict[10][1])*100);
		_drbc = _gtr[Math.round(352 - (_drbp/100 * 351))]; 
		
		_astp = Math.round(cdf((_p[11] - _stat_dict[11][0]) / _stat_dict[11][1])*100);
		_astc = _gtr[Math.round(352 - (_astp/100 * 351))]; 
		
		_tovp = Math.round(cdf((_p[12] - _stat_dict[12][0]) / _stat_dict[12][1])*100);
		_tovc = _gtr[Math.round((_tovp/100 * 351))]; 

		_atop = Math.round(cdf((_p[35] - _stat_dict[35][0]) / _stat_dict[35][1])*100);
		_atoc = _gtr[Math.round(352 - (_atop/100 * 351))]; 

		
		_blkp = Math.round(cdf((_p[22] - _stat_dict[22][0]) / _stat_dict[22][1])*100);
		_blkc = _gtr[Math.round(352-(_blkp/100 * 351))]; 
		
		_stlp = Math.round(cdf((_p[23] - _stat_dict[23][0]) / _stat_dict[23][1])*100);
		_stlc = _gtr[Math.round(352-(_stlp/100 * 351))]; 
		
		_ftrp = Math.round(cdf((_p[24] - _stat_dict[24][0]) / _stat_dict[24][1])*100);
		_ftrc = _gtr[Math.round(352-(_ftrp/100 * 351))]; 

		_pfrp = Math.round(cdf((_p[30] - _stat_dict[30][0]) / _stat_dict[30][1])*100);
		_pfrc = _gtr[Math.round((_pfrp/100 * 351))]; 

		
		_ftperp = Math.round(cdf((_p[15] - _stat_dict[15][0]) / _stat_dict[15][1])*100);
		_ftperc = _gtr[Math.round(352-(_ftperp/100 * 351))]; 
		
		_twoperp = Math.round(cdf((_p[18] - _stat_dict[18][0]) / _stat_dict[18][1])*100);
		_twoperc = _gtr[Math.round(352-(_twoperp/100 * 351))]; 
		
		_threeperp = Math.round(cdf((_p[21] - _stat_dict[21][0]) / _stat_dict[21][1])*100);
		_threeperc = _gtr[Math.round(352-(_threeperp/100 * 351))];

		_rimperp = Math.round(cdf((rimper - _stat_dict[40][0]) / _stat_dict[40][1])*100);
		_rimperc = _gtr[Math.round(352-(_rimperp/100 * 351))];

		_midperp = Math.round(cdf((midper - _stat_dict[41][0]) / _stat_dict[41][1])*100);
		_midperc = _gtr[Math.round(352-(_midperp/100 * 351))];

		_dunkperp = Math.round(cdf((dunkper - _stat_dict[44][0]) / _stat_dict[44][1])*100);
		_dunkperc = _gtr[Math.round(352-(_dunkperp/100 * 351))];
	
		_tpratep = Math.round(cdf((tprate - .375) / .12)*100);
		_tpratec = _gtr[Math.round(352-(_tpratep/100 * 351))];
		
		_tp100p = Math.round(cdf((tp100 - 5.81) / 4.18)*100);
		_tp100c = _gtr[Math.round(352-(_tp100p/100 * 351))];
		
		gamelink = "results.php?team="+encodeURIComponent(team) + '&year='+yearlink+ partlink

		if (xvalue == 'evertrans') {
			if (trid in trantridyear == false) {continue;}
			if (activeyear < trantridyear[trid]) {continue;}	
		}
		
		if (xvalue == 'transout') {
			if (year == 'career') {
				skipthis = 1
				tridteams = careerteams[trid]
				tridteams.forEach(function(b) {
    				tridteam = trid+b
    				if (tridteam in tranoutyear) {
    					skipthis = 0
    				}
    			})
				if (skipthis == 1) {continue}				
			} else {
				tridteam = trid+team
				if (tridteam in tranoutyear == false) {continue;}
				tranyear = tranoutyear[trid]
				if (activeyear >= tranyear) {continue;}
			}
		}
		if (year == 'trans' ) {
			conf = tdata[i][1];				
		}
		if ((year == 'all' && (xvalue =='grads' || xvalue=='trans')) || year == 'trans') {
			if (year == 'trans') {
				conf = tdata[i][1]
				oldconf = tdata[i][2]
				newconf = tdata[i][66];
			} else {
				conf = tdata[i][35]
				oldconf = tdata[i][66]
				newconf = tdata[i][2];

			}
			if (oldteam != "All") {
				if (oldteam != conf) {
					continue;
				}
			}

			if (ocvalue != 'All') {
				if (ocvalue == 'd1') {
					if (oldconf == 'd2') {
						continue;
					}
				} else if (oldconf != ocvalue && ocvalue != 'High Major' && ocvalue != 'Mid' && ocvalue != 'trumid' && ocvalue != 'truhi') {
					continue;
				} else if (ocvalue == 'High Major' && himajor.indexOf(oldconf) < 0) {
					continue;
				} else if (ocvalue == 'Mid' && himajor.indexOf(oldconf) >= 0) {
					continue;
				} else if (ocvalue == 'trumid' && (himid.indexOf(oldteam) >= 0 || himajor.indexOf(oldconf) >= 0)) {
					continue;
				} else if (ocvalue == 'truhi' && himajor.indexOf(oldconf) < 0) {
					if (himid.indexOf(oldteam) < 0) {
						continue;
					}
				}
			}

			if (cvalue != 'All') {
				if (newconf != cvalue && cvalue != 'High Major' && cvalue != 'Mid' && cvalue != 'trumid' && cvalue != 'truhi' && cvalue != "NCAA" && cvalue != "Alive") {
					continue;
				} else if (cvalue == 'High Major' && himajor.indexOf(newconf) < 0) {
					continue;
				} else if (cvalue == 'Mid' && himajor.indexOf(newconf) >= 0) {
					continue;
				} else if (cvalue == 'trumid' && (himid.indexOf(newconf) >= 0 || himajor.indexOf(newconf) >= 0)) {
					continue;
				} else if (cvalue == 'truhi' && himajor.indexOf(newconf) < 0) {
					if (himid.indexOf(conf) < 0) {
						continue;
					}
				}
			}

		}
		if (isNaN(ato)) {
			ato = NaN
		}
		compstyle = '';
		if (comptrid == trid) {
			compstyle = "background-color:yellow";
		}	
		if (sIndex == 99) {
			rk = compstat
		}
		if (minage != 'All') {
			rk = age.toFixed(1)
		}		
		tableHTML += "<tr><td title='Click to see comps for this player' class='_0 mobileout' id="+i+">" + rk + "</td>";
		tableHTML += "<td class='_45 mobileout'>" + picktext + "</td>";			
		tableHTML += "<td class='mobileout' style='white-space:nowrap !important'><span style='white-space: nowrap'><div style='float: left; text-align: left;'>" + numtext + "<div " + titletown + " style='float: right; text-align: right'>"+ cl + "</div></span></td>";		
		tableHTML += "<td class='mobileout _26'>" + htText + "</td>";
		var d2_badge = '';
		var cell_bg = compstyle;
		if (year == 'trans' && oldconf == 'd2') {
			if (compstyle == '') {
				cell_bg = "background-color: #f8fafc;";
			}
			d2_badge = ' <span style="font-size: 8px; padding: 1px 4px; background-color: #cbd5e1; color: #334155; border-radius: 3px; font-weight: bold; margin-left: 4px; vertical-align: middle; display: inline-block;">D2</span>';
		}
		if (cvalue == 'd2trans' || xvalue == 'd2trans' || division == '2') {						
			tableHTML += '<td style="text-align:left;'+cell_bg+'"><a href="playerstat.php?division=2&kw=' + playername + '&start=20141101&end=20240501">' + playername + tranguy + '</a>' + d2_badge + ' '+shortyear+'</td>';	
		} else {
			tableHTML += '<td style="text-align:left;'+cell_bg+'"><a href="playerstat.php' + playerlink + '">' + playername + tranguy + '</a>' + d2_badge + ' '+shortyear+'</td>';	
		}
		tableHTML += '<td class="_34" class="mobileout"><span title = "RecruiT-Rank" style="font-size:8px">'+rec_rk+'</span></td>';		
		tableHTML += '<td class="mobileout _teamx" style="text-align:left"><a href="team.php?team=' + encodeURIComponent(team) + '&year='+activeyear+'">' + team.slice(0,20) + '</a></td>';
		tableHTML += "<td class='mobileout _confx' style='text-align:left'><a href='conf.php?conf=" + conf + "&year="+yearlink+"'>" + conf + "</a></td>";
		tableHTML += "<td class='mobileout _3' style='text-align:center'><a href="+'"'+ gamelink + '">' + gp + "</a></td>";			
		tableHTML += "<td class='mobileout _64' style='text-align:center'>" + role + "</td>";			
		tableHTML += "<td class='_4' style='text-align:center'>" + mins.toFixed(1) + "</td>";			
		tableHTML += "<td class='_28' style='background-color:"+_ppgc+"'>" + ppg.toFixed(1) + "</td>";			
		tableHTML += "<td class='_48' style='background-color:"+_dppgc+"'>" + dpag.toFixed(1) + "</td>";					
		var gbpm_text = !isNaN(gbpm) ? gbpm.toFixed(1) : "";
		var ogbpm_text = !isNaN(ogbpm) ? ogbpm.toFixed(1) : "";
		var dgbpm_text = !isNaN(dgbpm) ? dgbpm.toFixed(1) : "";
		tableHTML += "<td class='_53' style='background-color:"+_gbpmc+"'>" + gbpm_text + "</td>";			
		tableHTML += "<td class='_55' style='background-color:"+_ogbpmc+"'>" + ogbpm_text + "</td>";			
		tableHTML += "<td class='_56' style='background-color:"+_dgbpmc+"'>" + dgbpm_text + "</td>";			
		tableHTML += "<td class='_5' style='background-color:"+_oratingc+"'>" + ortg.toFixed(1) + "</td>";			
		tableHTML += "<td class='_47' style='background-color:"+_adrtgc+"'>" + adrtg.toFixed(1) + "</td>";			
		tableHTML += "<td class='_6' style='text-align:center; background-color:"+_usagec+"'>" + usage.toFixed(1) + "</td>";			
		tableHTML += "<td class='_7' style='text-align:center; background-color:"+_efgc+"'>" + efg.toFixed(1) + "</td>";			
		tableHTML += "<td class='mobileout _8' style='text-align:center; background-color:"+_tsc+"'>" + ts.toFixed(1) + "</td>";			
		tableHTML += "<td class='mobileout _9' style='text-align:center; background-color:"+_orbc+"'>" + oreb.toFixed(1) + "</td>";			
		tableHTML += "<td class='mobileout _10' style='text-align:center; background-color:"+_drbc+"'>" + dreb.toFixed(1) + "</td>";			
		tableHTML += "<td class='mobileout _11' style='text-align:center; background-color:"+_astc+"'>" + ast.toFixed(1) + "</td>";			
		tableHTML += "<td class='mobileout _12' style='text-align:center; background-color:"+_tovc+"'>" + tov.toFixed(1) + "</td>";			
		tableHTML += "<td class='mobileout _35' style='text-align:center; background-color:"+_atoc+"'>" + ato.toFixed(1) + "</td>";			
		tableHTML += "<td class='mobileout _22' style='text-align:center; background-color:"+_blkc+"'>" + blk.toFixed(1) + "</td>";			
		tableHTML += "<td class='mobileout _23' style='text-align:center; background-color:"+_stlc+"'>" + stl.toFixed(1) + "</td>";			
		tableHTML += "<td class='mobileout _24' style='text-align:center;border-right:1px solid black; background-color:"+_ftrc+"'>" + ftr.toFixed(1) + "</td>";	
		tableHTML += "<td class='mobileout _30' style='text-align:center;border-right:1px solid black; background-color:"+_pfrc+"'>" + pfr.toFixed(1) + "</td>";	
		tableHTML += "<td class='mobileout _4243' style='text-align:center'>" + dunkmade + '-' + dunkatt + "</td>";											
		tableHTML += "<td class='mobileout _44' style='text-align:center;border-right:1px solid black;background-color:"+_dunkperc+"'>" + dunkper.toFixed(3).replace("0.",".") + "</td>";					
		tableHTML += "<td class='mobileout _3637' style='text-align:center'>" + rimmade + '-' + rimatt + "</td>";											
		tableHTML += "<td class='mobileout _40' style='text-align:center;border-right:1px solid black;background-color:"+_rimperc+"'>" + rimper.toFixed(3).replace("0.",".") + "</td>";					
		tableHTML += "<td class='mobileout _3839' style='text-align:center'>" + midmade + '-' + midatt + "</td>";											
		tableHTML += "<td class='mobileout _41' style='text-align:center;border-right:1px solid black;background-color:"+_midperc+"'>" + midper.toFixed(3).replace("0.",".") + "</td>";					 
		tableHTML += "<td class='mobileout _1314' style='text-align:center'>" + ftm + '-' + fta + "</td>";											
		tableHTML += "<td class='mobileout _15' style='text-align:center;border-right:1px solid black; background-color:"+_ftperc+"'>" + ftper.toFixed(3).replace("0.",".") + "</td>";					
		tableHTML += "<td class='mobileout _1617' style='text-align:center'>" + fgm + '-' + fga + "</td>";							
		tableHTML += "<td class='mobileout _18' style='text-align:center;border-right:1px solid black; background-color:"+_twoperc+"'>" + twoper.toFixed(3).replace("0.",".") + "</td>";	
		tableHTML += "<td class='mobileout _tprate' style='text-align:center;border-right:1px solid black;background-color:"+_tpratec+"'>" + (tprate*100).toFixed(1) + "</td>";
		tableHTML += "<td class='mobileout _65' style='text-align:center;border-right:1px solid black;background-color:"+_tp100c+"'>" + tp100.toFixed(1) + "</td>";
		tableHTML += "<td class='mobileout _1920' style='text-align:center'>" + tpm + '-' + tpa + "</td>";
		tableHTML += "<td class='mobileout _21' style='text-align:center;background-color:"+_threeperc+"'>" + threeper.toFixed(3).replace("0.",".") + "</td>";	

		tot_dunkm += dunkmade
		tot_dunka += dunkatt
		tot_midm += midmade
		tot_mida += midatt
		tot_rimm += rimmade
		tot_rima += rimatt
		tot_ftm += ftm
		tot_fta += fta
		tot_twom += fgm
		tot_twoa += fga
		tot_threem += tpm
		tot_threea += tpa
		
		if (dopoints == 1) {
			rebounds = tdata[i][59] == null ? 0 :tdata[i][59]*per100g
			assists = tdata[i][60]== null ? 0 :tdata[i][60]*per100g
			pts = tdata[i][63]== null ? 0 :tdata[i][63]*per100g
// 			if (year == 'career') {
// 				rebounds /= gp
// 				assists /= gp
// 				pts /= gp
// 			}
	// 		r.extend([ORB, DRB, TRB, AST, STL, BLK, PTS])
			tableHTML += "<td style='border-left: 1px black solid'>" + assists.toFixed(basicround) + "</td>";	
			tableHTML += "<td >" + rebounds.toFixed(basicround) + "</td>";	
			tableHTML += "<td >" + pts.toFixed(basicround) + "</td>";	
		}	
		tableHTML += yeartext;	
		tableHTML += "</tr>";
		icount+=1;		
	};
	if (page != 'team') {
		tableHTML += '<tr><th id="expand" colspan =100><a>Show 100 more</a></th></tr>';
	} else {
		tot_dunkp = tot_dunka == 0 ? 0 : tot_dunkm/tot_dunka
		tot_rimp = tot_rima == 0 ? 0 : tot_rimm/tot_rima
		tot_midp = tot_mida == 0 ? 0 : tot_midm/tot_mida
		tot_ftp = tot_fta == 0 ? 0 : tot_ftm/tot_fta
		tot_twop = tot_twoa == 0 ? 0 : tot_twom/tot_twoa
		tot_threep = tot_threea == 0 ? 0 : tot_threem/tot_threea
		
		_ftperp = Math.round(cdf((tot_ftp - .6967) / .03894)*100);
		_ftperc = _gtr[Math.round(352-(_ftperp/100 * 351))]; 
		
		_twoperp = Math.round(cdf((tot_twop - .48456) / .03382)*100);
		_twoperc = _gtr[Math.round(352-(_twoperp/100 * 351))]; 
		
		_threeperp = Math.round(cdf((tot_threep - .34249) / .0288)*100);
		_threeperc = _gtr[Math.round(352-(_threeperp/100 * 351))];

		_rimperp = Math.round(cdf((tot_rimp - .60087) / .0402)*100);
		_rimperc = _gtr[Math.round(352-(_rimperp/100 * 351))];

		_midperp = Math.round(cdf((tot_midp - .35982) / .03516)*100);
		_midperc = _gtr[Math.round(352-(_midperp/100 * 351))];

		_dunkperp = Math.round(cdf((tot_dunkp - .8731) / .06244)*100);
		_dunkperc = _gtr[Math.round(352-(_dunkperp/100 * 351))];

		tableHTML += "<tr style='background-color:#ddd;border-top:2px solid black'><td class='_45 mobileout'></td>";			
		tableHTML += "<td class='mobileout'></td>";		
		tableHTML += "<td class='mobileout _26'></td>";						
		tableHTML += '<td style="text-align:left;"></td>';	
		tableHTML += '<td class="_34" class="mobileout"><span title = "RecruiT-Rank" style="font-size:8px"></span></td>';		
		tableHTML += '<td class="mobileout _teamx" style="text-align:left"></td>';
		tableHTML += "<td class='mobileout _confx' style='text-align:left'></td>";
		tableHTML += "<td class='mobileout _3' style='text-align:center'></td>";			
		tableHTML += "<td class='mobileout _64' ></td>";			
		tableHTML += "<td class='_4' ></td>";			
		tableHTML += "<td class='_28' ></td>";			
		tableHTML += "<td class='_48' ></td>";					
		tableHTML += "<td class='_53' ></td>";			
		tableHTML += "<td class='_55' ></td>";			
		tableHTML += "<td class='_56' ></td>";			
		tableHTML += "<td class='_5'  ></td>";			
		tableHTML += "<td class='_47' ></td>";			
		tableHTML += "<td class='_6' ></td>";			
		tableHTML += "<td class='_7' ></td>";			
		tableHTML += "<td class='mobileout _8' ></td>";			
		tableHTML += "<td class='mobileout _9' ></td>";			
		tableHTML += "<td class='mobileout _10'></td>";			
		tableHTML += "<td class='mobileout _11'></td>";			
		tableHTML += "<td class='mobileout _12'></td>";			
		tableHTML += "<td class='mobileout _35'></td>";			
		tableHTML += "<td class='mobileout _22'></td>";			
		tableHTML += "<td class='mobileout _23'></td>";			
		tableHTML += "<td class='mobileout _24'></td>";	
		tableHTML += "<td class='mobileout _30'></td>";	
		tableHTML += "<td class='mobileout _4243' style='text-align:center'>" + tot_dunkm.toFixed(totalround) + '-' + tot_dunka.toFixed(totalround) + "</td>";											
		tableHTML += "<td class='mobileout _44' style='text-align:center;border-right:1px solid black;background-color:"+_dunkperc+"'>" + (tot_dunkm/tot_dunka).toFixed(3).replace("0.",".") + "</td>";					
		tableHTML += "<td class='mobileout _3637' style='text-align:center'>" + tot_rimm.toFixed(totalround) + '-' + tot_rima.toFixed(totalround) + "</td>";											
		tableHTML += "<td class='mobileout _40' style='text-align:center;border-right:1px solid black;background-color:"+_rimperc+"'>" + (tot_rimm/tot_rima).toFixed(3).replace("0.",".") + "</td>";					
		tableHTML += "<td class='mobileout _3839' style='text-align:center'>" + tot_midm.toFixed(totalround) + '-' + tot_mida.toFixed(totalround) + "</td>";											
		tableHTML += "<td class='mobileout _41' style='text-align:center;border-right:1px solid black;background-color:"+_midperc+"'>" + (tot_midm/tot_mida).toFixed(3).replace("0.",".") + "</td>";					 
		tableHTML += "<td class='mobileout _1314' style='text-align:center'>" + tot_ftm.toFixed(totalround) + '-' + tot_fta.toFixed(totalround) + "</td>";											
		tableHTML += "<td class='mobileout _15' style='text-align:center;border-right:1px solid black; background-color:"+_ftperc+"'>" + (tot_ftm/tot_fta).toFixed(3).replace("0.",".") + "</td>";					
		tableHTML += "<td class='mobileout _1617' style='text-align:center'>" + tot_twom.toFixed(totalround) + '-' + tot_twoa.toFixed(totalround) + "</td>";							
		tableHTML += "<td class='mobileout _18' style='text-align:center;border-right:1px solid black; background-color:"+_twoperc+"'>" + (tot_twop).toFixed(3).replace("0.",".") + "</td>";	
		tableHTML += "<td class='mobileout _tprate' style='border-right:1px solid black'></td><td class='mobileout _65' style='border-right:1px solid black'></td>";
		tableHTML += "<td class='mobileout _1920' style='text-align:center'>" + tot_threem.toFixed(totalround) + '-' + tot_threea.toFixed(totalround) + "</td>";
		tableHTML += "<td class='mobileout _21' style='text-align:center;background-color:"+_threeperc+"'>" + (tot_threem/tot_threea).toFixed(3).replace("0.",".") + "</td>";	
	
	}
	tableHTML += '</tr><tr><th colspan =100><a href="playermaps.php'+ fullLink + '">Show Chart</a></th></tr></table>';

	document.getElementById("tble").innerHTML = tableHTML;		

	$('th#player').click(function() {doTheSort(0,$('td#0'))});	
	$('th#teamx').click(function() {doTheSort(1,$('td#25'))});	
	$('th#conference').click(function() {doTheSort(2,$('td#17'))});	
	$('th#gp').click(function() {doTheSort(3,$('td#1'))});
	$('th#p').click(function() {doTheSort(28,$('td#28'))});
	$('th#mins').click(function() {doTheSort(4,$('td#2'))});
	$('th#orating').click(function() {doTheSort(5,$('td#3'))});
	$('th#usg').click(function() {doTheSort(6,$('td#4'))});
	$('th#efg').click(function() {doTheSort(7,$('td#5'))});
	$('th#ts').click(function() {doTheSort(8,$('td#6'))});
	$('th#oreb').click(function() {doTheSort(9,$('td#7'))});
	$('th#orebd').click(function() {doTheSort(10,$('td#8'))});
	$('th#astper').click(function() {doTheSort(11,$('td#9'))});
	$('th#tor').click(function() {doTheSort(12,$('td#10'))});
	$('th#ato').click(function() {doTheSort(35,$('td#35'))});
	$('th#blk').click(function() {doTheSort(22,$('td#11'))});
	$('th#stl').click(function() {doTheSort(23,$('td#12'))});
	$('th#ftr').click(function() {doTheSort(24,$('td#14'))});
	$('th#pfr').click(function() {doTheSort(30,$('td#30'))});
	$('th#rim').click(function() {doTheSort(40,$('td#_rimper'))});
	$('th#mid').click(function() {doTheSort(41,$('td#_midper'))});
	$('th#dunk').click(function() {doTheSort(42,$('td#_dunk'))});
	$('th#twoper').click(function() {doTheSort(18,$('td#18'))});
	$('th#threeper').click(function() {doTheSort(21,$('td#21'))});
	$('th#ftper').click(function() {doTheSort(15,$('td#16'))});
	$('th#ht').click(function() {doTheHeightSort(26,$('td#26'))});
	$('th#pick').click(function() {doTheSort(45,$('td#45'))});
	$('th#dpag').click(function() {doTheSort(48,$('td#48'))});
	$('th#adrtg').click(function() {doTheSort(47,$('td#47'))});
	$('th#bpm').click(function() {doTheSort(50,$('td#bpm'))});
	$('th#obpm').click(function() {doTheSort(51,$('td#obpm'))});
	$('th#dbpm').click(function() {doTheSort(52,$('td#dbpm'))});
	$('th#gbpm').click(function() {doTheSort(53,$('td#gbpm'))});
	$('th#mpg').click(function() {doTheSort(54,$('td#mpg'))});
	$('th#ogbpm').click(function() {doTheSort(55,$('td#ogbpm'))});
	$('th#dgbpm').click(function() {doTheSort(56,$('td#dgbpm'))});
	$('th#pts').click(function() {doTheSort(63,$('td#pts'))});
	$('th#reb').click(function() {doTheSort(59,$('td#reb'))});
	$('th#ast').click(function() {doTheSort(60,$('td#ast'))});
	$('th#role').click(function() {doTheSort(64,$('td#role'))});
	$('th#year').click(function() {doTheSort(31,$('td#year'))});
	$('th#tprate').click(function() {doTheSort('tprate',$('td#tprate'))});
	$('th#tp100').click(function() {doTheSort(65,$('td#tp100'))});
	$('td._0').click(function() {
		x = $(this).attr('id')
		$('input#kw').val('')
		kw = ''
		comp = alltdata[x]
		docomp = 1
		sIndex = 99
		comptrid = comp[32]
		compyear = comp[31]
		if (xvalue == 'trans' || year == 'trans') {
			source = 'reftransfers.json';
			year = 'all'
			comp[35] = comp[1]
			$.getJSON(source, function(jsonData) {
				alltdata = jsonData;
			}).done(function() {	
				alltdata.unshift(comp)
				compareSort()
			})
		} else {
			compareSort()
		}
	})
	$('th#expand').click(function() {
		endrk += 100;
		makeTable();
	});
	$('td._0').hover(function() {
		text = $(this).text()
		$(this).text('Comps')
	},
					 function(){
		$(this).text(text)
	})
	$(document).ready(function() {
		if (showhidden == 1) {
			showHide();
		};

		showstat[sIndex] = 1
		if (sIndex == 36 || sIndex == 37) {
			showstat[40] = 1
			showstat[3637] = 1
		}
		if (sIndex == 38 || sIndex == 39) {
			showstat[41] = 1
			showstat[3839] = 1
		}
		if (sIndex == 42 || sIndex == 43) {
			showstat[44] = 1
			showstat[4243] = 1
		}

		if (sIndex == 13 || sIndex == 14) {
			showstat[15] = 1
			showstat[1314]=1
		}
		if (sIndex == 16 || sIndex == 17) {
			showstat[18] = 1
			showstat[1617] = 1
		}
		if (sIndex == 19 || sIndex == 20) {
			showstat[21] = 1
			showstat[1920] = 1
		}
		
		if (sIndex == 18) {
			showstat[1617] = 1
		}
		if (sIndex == 21) {
			showstat[1920] = 1
		}
		if (sIndex == 15) {
			showstat[1314] = 1
		}
		if (sIndex == 41) {
			showstat[3839] = 1
		}
		if (sIndex == 40) {
			showstat[3637] = 1
		}
		if (sIndex == 44) {
			showstat[4243] = 1
		}
		
		
		if (sIndex == 45) {
			showstat[45] = 1
		}		
		

		$('th.rk').click(function(){
			invisible(0);
		})
			
		hideselect();
	});

	if (page == 'team') {
		invisible(0);
		invisible('teamx');
		invisible('confx');
		invisible(65)
	}
	
	if (start == end) {
		invisible(8)
		invisible(9)
		invisible(10)
		invisible(11)
	}

};

// 		tableHTML += "<td class='_50' style='background-color:"+_bpmc+"'>" + bpm.toFixed(1) + "</td>";			
// 		tableHTML += "<td class='_51' style='background-color:"+_obpmc+"'>" + obpm.toFixed(1) + "</td>";			
// 		tableHTML += "<td class='_52' style='background-color:"+_dbpmc+"'>" + dbpm.toFixed(1) + "</td>";	
