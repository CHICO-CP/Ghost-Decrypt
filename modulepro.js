#!/usr/bin/env node
var _0x389457=_0x4360;function _0x4360(_0x2203c7,_0x619c14){var _0x28505f=_0x2850();return _0x4360=function(_0x4360f7,_0xd7609f){_0x4360f7=_0x4360f7-0x14b;var _0x362974=_0x28505f[_0x4360f7];return _0x362974;},_0x4360(_0x2203c7,_0x619c14);}(function(_0x210216,_0x46715f){var _0x3c077f=_0x4360,_0x32ad8e=_0x210216();while(!![]){try{var _0x15af08=-parseInt(_0x3c077f(0x14e))/0x1*(-parseInt(_0x3c077f(0x168))/0x2)+-parseInt(_0x3c077f(0x164))/0x3+-parseInt(_0x3c077f(0x171))/0x4+parseInt(_0x3c077f(0x176))/0x5+-parseInt(_0x3c077f(0x14b))/0x6*(parseInt(_0x3c077f(0x14f))/0x7)+-parseInt(_0x3c077f(0x177))/0x8*(-parseInt(_0x3c077f(0x174))/0x9)+parseInt(_0x3c077f(0x17c))/0xa;if(_0x15af08===_0x46715f)break;else _0x32ad8e['push'](_0x32ad8e['shift']());}catch(_0xb077d0){_0x32ad8e['push'](_0x32ad8e['shift']());}}}(_0x2850,0x3358a));const fs=require('fs'),path=require('path'),mainUtils=require(_0x389457(0x159));var configFile,languageFile,layoutFile,outputType=0x0,showHelp=![],libMethodsDirListArray=fs[_0x389457(0x17d)](__dirname+'/lib/methods'),libMethodsArray=[];for(let c=0x0;c<libMethodsDirListArray['length'];c++){path['parse'](libMethodsDirListArray[c])['ext']==_0x389457(0x16d)&&libMethodsArray[_0x389457(0x14d)](require(__dirname+_0x389457(0x163)+libMethodsDirListArray[c]));}try{configFile=JSON[_0x389457(0x15f)](fs[_0x389457(0x14c)](__dirname+_0x389457(0x156)));}catch(_0x479099){console['log']('[ERROR]\x20-\x20There\x20was\x20an\x20error\x20while\x20loading\x20config\x20file\x20at\x20module\x20'+path['parse'](__filename)[_0x389457(0x157)]),process[_0x389457(0x17b)]();}try{languageFile=JSON['parse'](fs[_0x389457(0x14c)](__dirname+_0x389457(0x16c)+configFile[_0x389457(0x178)]+_0x389457(0x15c)));}catch(_0x1e3dec){console[_0x389457(0x15a)]('[ERORR]\x20-\x20There\x20was\x20an\x20error\x20while\x20loading\x20language\x20file.'),process['exit']();}try{layoutFile=JSON[_0x389457(0x15f)](fs[_0x389457(0x14c)](__dirname+_0x389457(0x162)+configFile['layout']+_0x389457(0x158)));}catch(_0x449b52){console[_0x389457(0x15a)]('[ERORR]\x20-\x20There\x20was\x20an\x20error\x20while\x20loading\x20the\x20layout\x20file.'),process['exit']();}for(let c=0x0;c<process[_0x389457(0x154)][_0x389457(0x179)];c++){switch(process[_0x389457(0x154)][c]){case'--keyFile':case'-k':console[_0x389457(0x15a)]('[INFO]\x20-\x20Your\x20new\x20key\x20file\x20path\x20was\x20automatically\x20saved\x20into\x20the\x20main\x20configuration\x20file.'),configFile[_0x389457(0x155)]=process[_0x389457(0x154)][c+0x1];break;case _0x389457(0x160):case'-l':console[_0x389457(0x15a)](_0x389457(0x152)),configFile['language']=process[_0x389457(0x154)][c+0x1];break;case _0x389457(0x16f):case'-r':outputType=0x1;break;case _0x389457(0x151):case'-j':outputType=0x2;break;case'--help':case'-h':showHelp=!![];break;}}if(showHelp){var helpContent=['Usage:\x20node\x20script.js\x20[--args\x20-a...]','',_0x389457(0x17a),_0x389457(0x172),_0x389457(0x15e),_0x389457(0x170),_0x389457(0x169)];for(let c=0x0;c<helpContent[_0x389457(0x179)];c++){console[_0x389457(0x15a)](helpContent[c]);}process[_0x389457(0x17b)]();}function _0x2850(){var _0x2090bd=['./lib/mainUtils','log','invalidFile','.lang.json','stringify','--raw,\x20-r\x09\x09Display\x20only\x20RAW\x20output\x20(without\x20any\x20kind\x20of\x20parsing)','parse','--language','raw','/cfg/layout/','/lib/methods/','273147IbkRCw','metadata','existsSync','decryptFile','78LArdJd','--help,\x20-h\x09\x09Display\x20this\x20help\x20text','[ERROR]\x20-\x20','content','/cfg/lang/','.js','writeFileSync','--raw','--json,\x20-j\x09\x09Display\x20only\x20JSON\x20output','1125852EkbBrw','--language,\x20-l\x09\x09Set\x20a\x20custom\x20language\x20for\x20the\x20console\x20output/results','error','9BjEZCR','[ERROR]\x20-\x20An\x20error\x20occured\x20writing\x20the\x20configuration\x20file.','1574750iRlEJV','611792afaulu','language','length','--keyFile,\x20-k\x09\x09Specify\x20an\x20exact\x20path\x20for\x20a\x20custom\x20keyFile','exit','4824960stxUmk','readdirSync','24qdlarF','readFileSync','push','2954LGEqCN','711025dHOLjO','jsonResponseParsing','--json','[INFO]\x20-\x20Your\x20new\x20language\x20preference\x20was\x20automatically\x20saved\x20into\x20the\x20main\x20configuration\x20file.','decryptionFailed','argv','keyFile','/cfg/config.inc.json','base','.layout.json'];_0x2850=function(){return _0x2090bd;};return _0x2850();}function loopFunction(){var _0x1e8e0f=_0x389457;try{fs[_0x1e8e0f(0x16e)](__dirname+_0x1e8e0f(0x156),JSON[_0x1e8e0f(0x15d)](configFile,null,'\x09'));}catch(_0x2a3b84){console[_0x1e8e0f(0x15a)](_0x1e8e0f(0x175)),process[_0x1e8e0f(0x17b)]();}}loopFunction(),console['log']();!fs[_0x389457(0x166)](process[_0x389457(0x154)][process[_0x389457(0x154)]['length']-0x1])&&(console['log'](_0x389457(0x16a)+languageFile[_0x389457(0x15b)]),process[_0x389457(0x17b)]());var decryptionStage;for(let c=0x0;c<libMethodsArray['length'];c++){for(let d=0x0;d<libMethodsArray[c][_0x389457(0x165)]['schemeLength'];d++){decryptionStage=libMethodsArray[c][_0x389457(0x167)](fs[_0x389457(0x14c)](process[_0x389457(0x154)][process['argv'][_0x389457(0x179)]-0x1]),configFile,d);if(decryptionStage[_0x389457(0x173)]!=0x1)break;}if(decryptionStage[_0x389457(0x173)]!=0x1)break;}decryptionStage[_0x389457(0x173)]==0x1&&(console[_0x389457(0x15a)]('[ERROR]\x20-\x20'+languageFile[_0x389457(0x153)]),process[_0x389457(0x17b)]());switch(outputType){case 0x1:console[_0x389457(0x15a)](decryptionStage[_0x389457(0x161)]);break;case 0x2:console['log'](decryptionStage[_0x389457(0x16b)]);break;default:console[_0x389457(0x15a)](mainUtils[_0x389457(0x150)](decryptionStage['content'],languageFile,layoutFile));break;}process[_0x389457(0x17b)]();