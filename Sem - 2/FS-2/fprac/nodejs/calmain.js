const readline = require('readline')
const cal = require('./calcmod')


const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})


function menu(){
    console.log("1-add")
    console.log("2-sub")
    console.log("3-mul")
    console.log("4-div")

    rl.question("Select     ",(ch)=>{
        rl.question("enter n1",(n1)=>{
            rl.question("enter n2",(n2)=>{
                a = parseFloat(n1)
                b = parseFloat(n2)

                if (ch=="1"){
                    console.log(cal.add(a,b))
                }
                else if(ch=="2"){
                    console.log(cal.sub(a,b))
                }
                else if(ch=="3"){
                    console.log(cal.mul(a,b))
                }
                else if(ch=="4"){
                    console.log(cal.div(a,b))
                }
                menu()

            })
        })
    })
    
}


menu();