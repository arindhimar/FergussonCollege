const fs = require('fs')
const readline= require('readline')

const rl = readline.createInterface
({
    input:process.stdin,
    output:process.stdout
})

const path = "sample.txt"

function writeFile(){
    rl.question("Enter content to write     ",(content)=>{
        fs.writeFile(path,content,(err)=>{
            if(err){
                console.log(err)
                return
            }

            console.log("written")
            menu();
        })
    })
}

function appendFile(){
    rl.question("Enter content to append     ",(content)=>{
        fs.appendFile(path,content,(err)=>{
            if(err){
                console.log(err)
                return
            }

            console.log("appended")
            menu();
        })
    })
}

function readFile(){
    fs.readFile(path,'utf-8',(err,content)=>{
        if (err){
            console.log(err)
            return
        }

        console.log(content)

        menu();
    })
}


function menu(){
    console.log("1-write")
    console.log("2-append")
    console.log("3-read")

    rl.question("select         ",(ch)=>{
        if (ch=="1"){
            writeFile();
        }
        else if(ch=="2"){
            appendFile()
        }
        else if(ch=="3"){
            readFile()
        }
        else{
            menu();
        }
    })
}

menu();