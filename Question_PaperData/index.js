const fs = require('fs');
const difficulty = ["easy","medium","hard"];

const no_questions = 1000;

var res_arr = [];
try{
    for(var i=1;i<=no_questions;i++){
        var temp_obj = {};
        temp_obj.qNo = 'Q'+i.toString();
        temp_obj.diff = difficulty[Math.floor(Math.random() * 3)];
        temp_obj.marks = (Math.floor(Math.random() * 100)+1);
        res_arr.push(temp_obj);
    }
}
catch(e){
    console.log('E: '+e);
}

fs.writeFileSync('questions.txt',JSON.stringify(res_arr),(err)=>{
    if(!err){
        console.log('Wrote Successfully.');
    }
});
console.log(res_arr)