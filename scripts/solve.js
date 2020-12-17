
let number = 9788000005025;
let highestNumber =  9788999995025;
 
 
for( let i = number; i <= highestNumber ; i = i + 10000){
	
    if(i%1235 === 0){
		
        if(isbnChec(i)){
            console.log(i)
            break
        }
    }
}
 
 

function isbnChec(number){
    function numberToArray(number) {
        let array = number.toString().split("");
        return array.map(x => parseInt(x));
    }
 
    let modifiedArray = numberToArray(number)
 
   
    let finalArray = [];
    for(let i =0 ; i< modifiedArray.length ; i++){
        var temp;
        if(i%2 ==0){
             temp = modifiedArray[i] * 1
            
        }else{
             temp = modifiedArray[i] * 3
        }
 
        finalArray.push(temp)
    }

    let total =0;
    for(let j = 0 ; j < finalArray.length ; j++){
       total += finalArray[j];   
    }
 
    if(total % 10 === 0){
        return true
    }else{
        return false
    }
}
 
 
