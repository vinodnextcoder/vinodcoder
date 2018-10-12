var pdfUtil = require('pdf-to-text');
var Regex = require("regex");
const utf8 = require('utf8');
var fs = require('fs');
var async = require("async");
var spawn = require("child_process").spawn;
var pdf_path = "./CRM_EDW_RFP.pdf";
var async = require('async');
var textfile_name =""
var option = {from: 0, to: 5};
async.auto({
    one: function (callback, arg1) {
	pdfUtil.pdfToText(pdf_path, option, function(err, data) {
	    textfile_name = pdf_path.replace(".pdf",".txt");
	    fs.writeFile(textfile_name, data, function(err) {
		if(err) {
		    return console.log(err);
		}
		console.log("The file was saved!");
	    });
	    callback(null,data)
	})
    },
    two: ['one', function (callback, arg1) {	
	  var process = spawn('python',["./process_text.py",textfile_name, "khetade"] );
	process.stdout.on('data', function(data) {	
	    arg1(null,data.toString());
	})
	}]
},
function (err, result) {
    console.log(result.two);
});

