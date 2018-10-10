// Use child_process.spawn method from  
    // child_process module and assign it 
    // to variable spawn 
var spawn = require("child_process").spawn; 
      
    // Parameters passed in spawn - 
    // 1. type_of_script 
    // 2. list containing Path of the script 
    //    and arguments for the script  
      
    // E.g : http://localhost:3000/name?firstname=Mike&lastname=Will 
    // so, first name = Mike and last name = Will 
var process = spawn('python',["./hello.py","./IDBIBankDataWarehouseRFQ.txt", "kheyade"] ); 
  
 process.stdout.on('data', function(data) { 
        console.log(data.toString()); 
    } ) 

// var spawn = require('child_process').spawn,
//     py    = spawn('python', ['compute_input.py']),
//     data = [1,2,3,4,5,6,7,8,9],
//     dataString = '';

// py.stdout.on('data', function(data){
//     console.log(data.toString())
//   dataString += data.toString();
// });
// py.stdout.on('end', function(){
//   console.log('Sum of numbers=',dataString);
// });
// py.stdin.write(JSON.stringify(data));
// py.stdin.end();
