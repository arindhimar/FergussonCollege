function mergeAndRemoveDuplicates(arr1, arr2) {
    return [...new Set([...arr1, ...arr2])];
}

function MergeArraysComponent() {
    const handleMergeArrays = () => {
        const input1 = document.getElementById("arrayInput3").value;
        const input2 = document.getElementById("arrayInput4").value;
        const arr1 = JSON.parse(input1);
        const arr2 = JSON.parse(input2);
        const result = mergeAndRemoveDuplicates(arr1, arr2);
        document.getElementById("mergeResult").innerText = `Merged Array: ${result}`;
    };

    return (
        <div>
            <h1>Merge Two Arrays and Remove Duplicates</h1>
            <input type="text" id="arrayInput3" placeholder="Enter first array" />
            <input type="text" id="arrayInput4" placeholder="Enter second array" />
            <button onClick={handleMergeArrays}>Merge Arrays</button>
            <p id="mergeResult"></p>
        </div>
    );
}

export default MergeArraysComponent;