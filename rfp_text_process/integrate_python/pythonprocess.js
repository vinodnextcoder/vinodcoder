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
		var process = spawn('python',["./process_text.py",pdf_path, "khetade"] );
		process.stdout.on('data', function(data) {
			// console.log(data.toString());
			callback(null,data.toString());
		})
    }
 
},
function (err, result) {
    console.log(result);
});

