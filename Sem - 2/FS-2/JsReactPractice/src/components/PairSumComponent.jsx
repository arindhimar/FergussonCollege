function findPairWithSum(arr, target) {
    const map = new Map();
    for (let i = 0; i < arr.length; i++) {
        const complement = target - arr[i];
        if (map.has(complement)) {
            return [map.get(complement), i];
        }
        map.set(arr[i], i);
    }
    return null;
}

function PairSumComponent() {
    const handleFindPair = () => {
        const input = document.getElementById("pairInput").value;
        const arr = JSON.parse(input);
        const target = parseInt(document.getElementById("targetInput").value, 10);
        const result = findPairWithSum(arr, target);
        document.getElementById("pairResult").innerText = result ? `Indices: ${result}` : "No pair found";
    };

    return (
        <div>
            <h1>Find Pair with Specific Sum</h1>
            <input type="text" id="pairInput" placeholder="Enter array" />
            <input type="number" id="targetInput" placeholder="Target sum" />
            <button onClick={handleFindPair}>Find Pair</button>
            <p id="pairResult"></p>
        </div>
    );
}

export default PairSumComponent;