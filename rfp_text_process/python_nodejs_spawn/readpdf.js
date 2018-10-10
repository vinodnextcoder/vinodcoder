var pdfUtil = require('pdf-to-text');
var Regex = require("regex");
const utf8 = require('utf8');
var fs = require('fs');
var pdf_path = "./FINAL RFP.pdf";
 
//option to extract text from page 0 to 10
var option = {from: 0, to: 5};
 
pdfUtil.pdfToText(pdf_path, option, function(err, data) {
    if (err) throw(err);
    fs.writeFile("./test.txt", data, function(err) {
	if(err) {
            return console.log(err);
	}
    console.log("The file was saved!");
    }); 
   //console.log(data); //print text
    // var pdfdata=data;
    // pdfdata = pdfdata.replace(/|/g,"");
    // pdfdata = pdfdata.replace(//g,"");
    // pdfdata = pdfdata.split("\n");
    // console.log(pdfdata);
    //var pattern
    var regex1 = RegExp('foo*','g');
    var str1 = 'table football, foosball';
    
    // var array1;
    // var match;
    //while (match = regex1.exec(str1)) {
    //	console.log(match[1])
   // }
    // var temperatures = [];
    // for(var temp in pdfdata){
    // 	temperatures.push(+data[temp].match(/\d+/g));
    // }
    // console.log(temperatures)
    
    //#data=str1.split(" ") 
    // pdfdata.forEach(function(i) {
    // 	//var paragraph = 'The quick brown fox jumped over the lazy dog. It barked.';
    // 	var regex = //gi;
    // 	var found = i.match(regex);
    // 	if (found)
    // 	{
    // 	    console.log(found);
    // 	}
    // 	//console.log(i)
    // 	// if (regex1.test(i))
    // 	// {   
    // 	//     console.log(i);
    // 	// }
	
    // });
    
    // var paragraph = 'The quick brown fox jumped over the lazy dog. It barked.';
// var regex = /the/gi;
// var found = paragraph.match(regex);

//     console.log(found);
    
    //while ((array1 = regex1.exec(str1)) !== null) {
//	console.log(`Found ${array1[0]}. Next starts at ${regex1.lastIndex}.`);
  // expected output: "Found foo. Next starts at 9."
  // expected output: "Found foo. Next starts at 19."
//}
    // var arr=[]
    // for(i = 0; i < pdfdata.length - 1; i++) {
    // 	if (pdfdata[i].match(/a/g))
    // 	{
    // 	    console.log("mathc");
    // 	}
// 	//var myarray = pdfdata[i].match(pattern);
// 	arr=pdfdata[i].match(pattern);
// //	console.log(pdfdata[i])
            // }
//     console.log(arr)
    
    //pdfdata=pdfdata.replace(/[^\x20-\x7E]+/g, "");
    //console.log(pdfdata);
    
});
 
//Omit option to extract all text from the pdf file
// pdfUtil.pdfToText(pdf_path, function(err, data) {
//   if (err) throw(err);
//   console.log(data); //print all text    
// });
