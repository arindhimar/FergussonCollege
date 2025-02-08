function isArray(input) {
    try {
        const parsedInput = JSON.parse(input);
        return Array.isArray(parsedInput);
    } catch {
        return false;
    }
}

function ArrayCheckComponent() {
    const handleCheck = () => {
        const input = document.getElementById("arrayInput").value;
        const result = isArray(input) ? "Array" : "Not an Array";
        document.getElementById("handleCheckResult").innerText = result;
    };

    return (
        <div>
            <h1>Check if Input is an Array</h1>
            <input type="text" id="arrayInput" />
            <button onClick={handleCheck}>Check</button>
            <p id="handleCheckResult"></p>
        </div>
    );
}

export default ArrayCheckComponent;