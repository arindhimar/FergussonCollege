const fs = require('fs')
const readline = require('readline')

const filePath = "sample.txt"

const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})

function writeFile(){
    rl.question("enter text",(content)=>{
        fs.writeFile(filePath,content,(err)=>{
            if(err){
                console.log(err)
                return
            }

            console.log("writtn")
            menu();
        })
    })
}

function appendFile(){
    rl.question("enter text",(content)=>{
        fs.appendFile(filePath,content,(err)=>{
            if(err){
                console.log(err)
                return
            }

            console.log("append")
            menu();
        })
    })
}

function readFile(){
    fs.readFile(filePath,'utf-8',(err,content)=>{
        if(err){
            console.log(err)
            return
        }

        console.log(content)
        menu();
    })
}

function menu() {
    console.log("1-write")
    console.log("2-append")
    console.log("3-read")

    rl.question("select ",(ch)=>{
        if(ch=="1"){
            writeFile()
        }
        else if(ch=="2"){
            appendFile()
        }
        else if(ch=="3"){
            readFile()
        }
        else{
            menu()
        }
    })
}

menu()
