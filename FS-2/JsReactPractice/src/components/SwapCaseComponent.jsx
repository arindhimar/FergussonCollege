function swapCase(str) {
    return str.split('').map(char => {
        return char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase();
    }).join('');
}

function SwapCaseComponent() {
    const handleSwapCase = () => {
        const input = document.getElementById("caseInput").value;
        const result = swapCase(input);
        document.getElementById("caseResult").innerText = result;
    };

    return (
        <div>
            <h1>Swap Case of Each Character</h1>
            <input type="text" id="caseInput" />
            <button onClick={handleSwapCase}>Swap Case</button>
            <p id="caseResult"></p>
        </div>
    );
}

export default SwapCaseComponent;