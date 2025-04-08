const readline = require('readline')
const calc = require('./calcmod')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

function menu() {
    console.log("1-add")
    console.log("2-sub")
    console.log("3-mul")
    console.log("4-div")

    rl.question("select", (ch) => {
        rl.question("enter n1", (n1) => {
            rl.question("enter n2", (n2) => {
                const a = parseFloat(n1)
                const b = parseFloat(n2)

                let result;

                if( ch=="1"){
                    console.log(calc.add(a,b))
                }
                else if( ch=="2"){
                    console.log(calc.min(a,b))
                }
                else if( ch=="3"){
                    console.log(calc.mul(a,b))
                }
                else if( ch=="4"){
                    console.log(calc.div(a,b))
                }
                menu()
            })
        })
    })
}

menu()