const fs = require('fs')
const readfile = require('readline')

const filePath = "sample.txt"

const rl = readfile.createInterface({
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

            console.log("written")

            showMenu();

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

            console.log("written")

            showMenu();

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

        showMenu();
    })
}

function showMenu( ) {
    console.log("1-write")
    console.log("2-read")
    console.log("3-append")
    rl.question("select options",(ch)=>{
        if (ch=="1"){
            writeFile();
        }
        else if (ch=="2"){
            readFile();
        }
        else if(ch=="3"){
            appendFile();
        }
        else{
            showMenu();
        }
    })
}


showMenu()