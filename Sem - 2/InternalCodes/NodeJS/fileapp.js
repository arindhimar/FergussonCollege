const fs = require('fs');
const readline = require('readline');
const filePath = 'Sample.txt';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function createFile() {
    rl.question('Enter content to write into the file: ', (content) => {
        fs.writeFile(filePath, content, (err) => {
            if (err) {
                console.error('Error creating file:', err);
                return;
            }
            console.log('File created and written successfully!');
            showMenu();
        });
    });
}

function readFile() {
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) {
            console.error('Error reading file:', err);
            return;
        }
        console.log('File content:\n', data);
        showMenu();
    });
}

function appendToFile() {
    rl.question('Enter content to append to the file: ', (content) => {
        fs.appendFile(filePath, `\n${content}`, (err) => {
            if (err) {
                console.error('Error appending to file:', err);
                return;
            }
            console.log('Content appended successfully!');
            showMenu();
        });
    });
}

function deleteFile() {
    fs.unlink(filePath, (err) => {
        if (err) {
            console.error('Error deleting file:', err);
            return;
        }
        console.log('File deleted successfully!');
        showMenu();
    });
}

function showMenu() {
    console.log('\nChoose an option:');
    console.log('1. Create and Write File');
    console.log('2. Read File');
    console.log('3. Append to File');
    console.log('4. Delete File');
    console.log('5. Exit');

    rl.question('Enter your choice: ', (choice) => {
        switch (choice) {
            case '1':
                createFile();
                break;
            case '2':
                readFile();
                break;
            case '3':
                appendToFile();
                break;
            case '4':
                deleteFile();
                break;
            case '5':
                console.log('Exiting...');
                rl.close();
                return;
            default:
                console.log('Invalid choice, please try again.');
                showMenu();
        }
    });
}

showMenu();