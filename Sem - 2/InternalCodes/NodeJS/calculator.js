module.exports = {
    add: (a, b) => a + b,
    subtract: (a, b) => a - b,
    multiply: (a, b) => a * b,
    divide: (a, b) => (b !== 0 ? a / b : 'Error: Division by zero'),
    modulus: (a, b) => a % b,
    power: (a, b) => Math.pow(a, b)
};
