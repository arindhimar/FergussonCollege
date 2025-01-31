function getFirstElements(arr, n = 1) {
    return arr.slice(0, n);
}

function FirstElementsComponent() {
    const handleGetFirstElements = () => {
        const input = document.getElementById("arrayInput2").value;
        const arr = JSON.parse(input);
        const n = parseInt(document.getElementById("nInput").value, 10);
        const result = getFirstElements(arr, n);
        document.getElementById("result2").innerText = `First ${n} elements: ${result}`;
    };

    return (
        <div>
            <h1>Get First Elements of an Array</h1>
            <input type="text" id="arrayInput2" placeholder="Enter array" />
            <input type="number" id="nInput" placeholder="Number of elements" />
            <button onClick={handleGetFirstElements}>Get First Elements</button>
            <p id="result2"></p>
        </div>
    );
}

export default FirstElementsComponent;