const readline = require('readline');
const calc = require('./calculator');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function showMenu() {
    console.log('\nCalculator Menu:');
    console.log('1. Addition');
    console.log('2. Subtraction');
    console.log('3. Multiplication');
    console.log('4. Division');
    console.log('5. Modulus');
    console.log('6. Power');
    console.log('7. Exit');

    rl.question('Enter your choice: ', (choice) => {
        if (choice === '7') {
            console.log('Exiting...');
            rl.close();
            return;
        }

        rl.question('Enter first number: ', (num1) => {
            rl.question('Enter second number: ', (num2) => {
                const a = parseFloat(num1);
                const b = parseFloat(num2);
                let result;

                switch (choice) {
                    case '1':
                        result = calc.add(a, b);
                        break;
                    case '2':
                        result = calc.subtract(a, b);
                        break;
                    case '3':
                        result = calc.multiply(a, b);
                        break;
                    case '4':
                        result = calc.divide(a, b);
                        break;
                    case '5':
                        result = calc.modulus(a, b);
                        break;
                    case '6':
                        result = calc.power(a, b);
                        break;
                    default:
                        console.log('Invalid choice, please try again.');
                        showMenu();
                        return;
                }

                console.log(`Result: ${result}`);
                showMenu();
            });
        });
    });
}

showMenu();
