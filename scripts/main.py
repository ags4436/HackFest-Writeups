number = 9788000005025
highestNumber =  9788999995025
def checkisbn(number):
	list_of_number = list(str(number))
	final  = []
	for j in range(len(list_of_number)):
		if(j%2==0):
			sum =int(list_of_number[j])*1
			final.append(sum)
		else:
			sum =int(list_of_number[j])*3
			final.append(sum)
	total =0
	for i in range(len(final)):
		total +=final[i]
	if(total%10==0):
		print(number)
		
	else:
		pass
 
for i in range( 9788000005025,9788999995025,10000):
	# print(i)
	if(i%1235==0):
		checkisbn(i)
			
	# i+=10000





# for( let i = number; i <= highestNumber ; i = i + 10000){
	
#     if(i%1235 === 0){
		
#         if(numberChecker(i)){
#             console.log(i)
#             break
#         }
#     }
# }
 
 
# //////////////////////////////////////////////////////////////////////
# function numberChecker(number){
#     function numberToArray(number) {
#         let array = number.toString().split("");
#         return array.map(x => parseInt(x));
#     }
 
#     let modifiedArray = numberToArray(number)
 
#     // Now Start The Check
#     // console.log(modifiedArray)
#     let finalArray = [];
#     for(let i =0 ; i< modifiedArray.length ; i++){
#         var temp;
#         if(i%2 ==0){
#              temp = modifiedArray[i] * 1
            
#         }else{
#              temp = modifiedArray[i] * 3
#         }
 
#         finalArray.push(temp)
#     }
 
#     // Final Array
 
#     // console.log(finalArray)
 
#     // Finally Number Check
#     let total =0;
#     for(let j = 0 ; j < finalArray.length ; j++){
#        total += finalArray[j];   
#     }
 
#     if(total % 10 === 0){
#         return true
#     }else{
#         return false
#     }
# }
 
 
# /////////////////////////////////////////////////////////////////////////////