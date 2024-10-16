$(document).ready(function () {
    $('#bubbleSortLanguage').change(function () {
        const language = $(this).val();
        const codeDisplay = $('#bubbleSortCode');

        let code = '';
        switch (language) {
            case 'python':
                code = `def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr`;
                break;
            case 'javascript':
                code = `function bubbleSort(arr) {
    let n = arr.length;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
            }
        }
    }
    return arr;
}`;
                break;
            case 'cpp':
                code = `void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                std::swap(arr[j], arr[j+1]);
            }
        }
    }
}`;
                break;
        }

        codeDisplay.html(`<pre><code class="language-${language}">${code}</code></pre>`);
    });

    // Similar code for Insertion Sort
    $('#insertionSortLanguage').change(function () {
        const language = $(this).val();
        const codeDisplay = $('#insertionSortCode');

        let code = '';
        switch (language) {
            case 'python':
                code = `def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr`;
                break;
            case 'javascript':
                code = `function insertionSort(arr) {
    for (let i = 1; i < arr.length; i++) {
        let key = arr[i];
        let j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
    return arr;
}`;
                break;
            case 'cpp':
                code = `void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}`;
                break;
        }

        codeDisplay.html(`<pre><code class="language-${language}">${code}</code></pre>`);
    });

    $('.toggle-complexity').click(function () {
        $(this).next('.complexity-list').slideToggle(); // Toggle the visibility of the complexity list
        $(this).toggleClass('expanded'); // Rotate icon
    });


    var array = [];

    // Function to display the array in boxes
    // Function to update the array display
    function updateArrayDisplay() {
        $('#arrayDisplay').empty();

        array.forEach(value => {
            const box = $('<div></div>')
                .addClass('array-box')
                .text(value);
            $('#arrayDisplay').append(box);
        });
    }

    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    async function visualizeArray(arr, index1, index2, swapped = false) {
        $("#arrayDisplay1").empty(); // Clear the bubble sort display

        const maxValue = Math.max(...arr, 1); // Avoid division by zero
        arr.forEach((value, index) => {
            const widthPercentage = (value / maxValue) * 100; // Calculate width relative to the max value
            const box = $('<div></div>')
                .addClass('array-box')
                .css({
                    'height': `${widthPercentage}%`, // Set a fixed height for uniformity
                    'display': 'inline-block', // Display horizontally
                    'margin': '0 2px' // Add some space between the boxes
                })
                .text(value);

            // Highlight the elements being compared
            if (index === index1 || index === index2) {
                box.css('background-color', swapped ? '#ff6347' : '#f1c40f'); // Use different color for swap
            }

            $("#arrayDisplay1").append(box);
        });

        await sleep(500); // Adjust the delay as needed
    }


    async function visualizeBubbleImportantValues(val1, val2) {
        $("#bubbleSortImportant").empty(); // Clear previous values
        const value1Box = $('<div></div>').addClass('array-box').text(val1).css('background-color', '#ff6347');
        const value2Box = $('<div></div>').addClass('array-box').text(val2).css('background-color', '#ff6347');

        $("#bubbleSortImportant").append(value1Box).append(value2Box); // Show swapped values
    }


    async function bubbleSort() {
        let n = array.length;
        let bubbleSortArray = [...array];

        for (let i = 0; i < n - 1; i++) {
            for (let j = 0; j < n - i - 1; j++) {
                // Visualize the comparison
                await visualizeArray(bubbleSortArray, j, j + 1);

                if (bubbleSortArray[j] > bubbleSortArray[j + 1]) {
                    // Swap elements
                    let temp = bubbleSortArray[j];
                    bubbleSortArray[j] = bubbleSortArray[j + 1];
                    bubbleSortArray[j + 1] = temp;

                    // Update visualization after swap
                    await visualizeArray(bubbleSortArray, j, j + 1, true);
                    await visualizeBubbleImportantValues(bubbleSortArray[j], bubbleSortArray[j + 1]);
                }
            }
        }
        // Final visualization when sorting is done
        await visualizeArray(bubbleSortArray, -1, -1, true);
    }

    // Event listener for the 'Add' button and Enter key press
    $('#addBubbleSortValue').click(function () {
        const inputValue = $('#arrayInput').val().trim();

        // Split the input by commas, spaces, or both (using a regular expression)
        const values = inputValue.split(/[\s,]+/).map(val => val.trim());

        values.forEach(value => {
            // Ensure each value is a number and not empty
            if (value !== '' && !isNaN(value)) {
                const number = Number(value);
                array.push(number); // Push valid numbers to the array
            }
        });

        // Update the array display after all valid values are added
        updateArrayDisplay();

        // Clear the input field
        $('#arrayInput').val('');
    });

    // Event listener for the Test Case dropdown for Bubble Sort
    $('#bubbleTestCaseSelect').change(function () {
        const selectedCase = $(this).val();

        // Clear the current array and display
        array = [];
        $('#arrayInput').val(''); // Clear the input field

        // Generate the appropriate test case array
        let testArray = [];

        switch (selectedCase) {
            case 'best': // Best case: Already sorted array
                testArray = Array.from({ length: 10 }, (_, i) => i + 1); // 1, 2, 3, ..., 10
                break;

            case 'average': // Average case: Random array
                testArray = Array.from({ length: 10 }, () => Math.floor(Math.random() * 100)); // Random values between 0-99
                break;

            case 'worst': // Worst case: Reverse sorted array
                testArray = Array.from({ length: 10 }, (_, i) => 10 - i); // 10, 9, 8, ..., 1
                break;
        }

        // Populate the array with the generated test case values
        testArray.forEach(value => array.push(value));

        // Update the display with the test case array
        updateArrayDisplay();
    });



    $('#insertionSortLanguage').change(function () {
        const language = $(this).val();
        const codeDisplay = $('#insertionSortCode');

        let code = '';
        switch (language) {
            case 'python':
                code = `def insertion_sort(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr`;
                break;
            case 'javascript':
                code = `function insertionSort(arr) {
        for (let i = 1; i < arr.length; i++) {
            let key = arr[i];
            let j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = key;
        }
        return arr;
    }`;
                break;
            case 'cpp':
                code = `void insertionSort(int arr[], int n) {
        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
    }`;
                break;
        }

        codeDisplay.html(`<pre><code class="language-${language}">${code}</code></pre>`);
    });

    let insertionArray = [];



    // Function to update the insertion array display
    function updateInsertionArrayDisplay() {
        $('#arrayInsertionDisplay').empty();

        insertionArray.forEach(value => {
            const box = $('<div></div>')
                .addClass('array-box')
                .text(value);
            $('#arrayInsertionDisplay').append(box);
        });
    }

    async function visualizeInsertionArray(arr, index1, index2) {
        $("#insertionSortDisplay").empty(); // Clear the insertion sort display

        const maxValue = Math.max(...arr, 1); // Avoid division by zero
        arr.forEach((value, index) => {
            const widthPercentage = (value / maxValue) * 100; // Calculate width relative to the max value
            const box = $('<div></div>')
                .addClass('array-box')
                .css({
                    'height': `${widthPercentage}%`, // Set a fixed height for uniformity
                    'display': 'inline-block', // Display horizontally
                    'margin': '0 2px' // Add some space between the boxes
                });

            // Highlight the elements being compared
            if (index === index1 || index === index2) {
                box.css('background-color', '#f1c40f'); // Use a highlight color for comparison
            }

            $("#insertionSortDisplay").append(box);
        });

        await sleep(500); // Adjust the delay as needed
    }

    async function insertionSort() {
        let insertionSortArray = [...insertionArray];

        for (let i = 1; i < insertionSortArray.length; i++) {
            let key = insertionSortArray[i];
            let j = i - 1;

            // Visualize the current state
            await visualizeInsertionArray(insertionSortArray, i, j);

            while (j >= 0 && insertionSortArray[j] > key) {
                insertionSortArray[j + 1] = insertionSortArray[j];
                j--;

                // Visualize the current state after each shift
                await visualizeInsertionArray(insertionSortArray, i, j);
            }
            insertionSortArray[j + 1] = key;

            // Final state visualization after inserting key
            await visualizeInsertionArray(insertionSortArray, -1, -1);
        }
    }

    // Event listener for the Test Case dropdown
    $('#insertionTestCaseSelect').change(function () {
        const selectedCase = $(this).val();

        // Clear the current insertion array and display
        insertionArray = [];
        $('#insertionArrayInput').val(''); // Clear the input field

        // Generate the appropriate test case array
        let testArray = [];

        switch (selectedCase) {
            case 'best': // Best case: Already sorted array
                testArray = Array.from({ length: 10 }, (_, i) => i + 1); // 1, 2, 3, ..., 10
                break;

            case 'average': // Average case: Random array
                testArray = Array.from({ length: 10 }, () => Math.floor(Math.random() * 100)); // Random values between 0-99
                break;

            case 'worst': // Worst case: Reverse sorted array
                testArray = Array.from({ length: 10 }, (_, i) => 10 - i); // 10, 9, 8, ..., 1
                break;
        }

        // Populate the insertion array with the generated test case values
        testArray.forEach(value => insertionArray.push(value));

        // Update the display with the test case array
        updateInsertionArrayDisplay();
    });


    // Event listener for the 'Add' button for Insertion Sort
    $('#addInsertionSortValue').click(function () {
        const inputValue = $('#insertionArrayInput').val().trim();

        // Split the input by commas, spaces, or both (using a regular expression)
        const values = inputValue.split(/[\s,]+/).map(val => val.trim());

        values.forEach(value => {
            // Ensure each value is a number and not empty
            if (value !== '' && !isNaN(value)) {
                const number = Number(value);
                insertionArray.push(number); // Push valid numbers to the insertionArray
            }
        });

        // Update the insertion array display after all valid values are added
        updateInsertionArrayDisplay();

        // Clear the input field
        $('#insertionArrayInput').val('');
    });

    $("#startInsertionVisualization").click(async function () {
        $("#insertionSortDisplay").empty();
        $("#insertionArrayDisplay").children().clone().appendTo("#insertionSortDisplay");

        // Run the insertion sort visualization
        await insertionSort();
    });

    $("#startBubbleVisualization").click(async function () {
        $("#arrayDisplay1").empty();
        $("#arrayDisplay2").empty();
        $("#arrayDisplay").children().clone().appendTo("#arrayDisplay1");
        $("#arrayDisplay").children().clone().appendTo("#arrayDisplay2");

        // Run both sorting algorithms simultaneously
        await Promise.all([bubbleSort()]);
    });























    async function insertionSort() {
        let insertionSortArray = [...insertionArray];

        for (let i = 1; i < insertionSortArray.length; i++) {
            let key = insertionSortArray[i];
            let j = i - 1;

            // Visualize the current state
            await visualizeInsertionArray(insertionSortArray, i, j);

            while (j >= 0 && insertionSortArray[j] > key) {
                insertionSortArray[j + 1] = insertionSortArray[j];
                j--;

                // Visualize the current state after each shift
                await visualizeInsertionArray(insertionSortArray, i, j);
            }
            insertionSortArray[j + 1] = key;

            // Final state visualization after inserting key
            await visualizeInsertionArray(insertionSortArray, -1, -1);
        }
    }

    async function bubbleSort() {
        let n = array.length;
        let bubbleSortArray = [...array];

        for (let i = 0; i < n - 1; i++) {
            for (let j = 0; j < n - i - 1; j++) {
                // Visualize the comparison
                await visualizeArray(bubbleSortArray, j, j + 1);

                if (bubbleSortArray[j] > bubbleSortArray[j + 1]) {
                    // Swap elements
                    let temp = bubbleSortArray[j];
                    bubbleSortArray[j] = bubbleSortArray[j + 1];
                    bubbleSortArray[j + 1] = temp;

                    // Update visualization after swap
                    await visualizeArray(bubbleSortArray, j, j + 1, true);
                    await visualizeBubbleImportantValues(bubbleSortArray[j], bubbleSortArray[j + 1]);
                }
            }
        }
        // Final visualization when sorting is done
        await visualizeArray(bubbleSortArray, -1, -1, true);
    }










    var comparisonArray = [];

    function updateComparisonArrayDisplay() {
        $('#arrayComparisionDisplay').empty();
        const maxValue = Math.max(...comparisonArray, 1);
        comparisonArray.forEach(value => {
            const heightPercentage = (value / maxValue) * 100;
            const box = $('<div></div>')
                .addClass('array-box')
                .css('height', `${heightPercentage}%`)
                .text(value);
            $('#arrayComparisionDisplay').append(box);
        });
    }

    $('#comparisonTestCaseSelect').change(function () {
        const selectedCase = $(this).val();
    
        // Clear the current comparison array and display
        comparisonArray = [];
        $('#comparisionArrayInput').val(''); // Clear the input field
    
        // Generate the appropriate test case array
        let testArray = [];
    
        switch (selectedCase) {
            case 'best': // Best case: Already sorted array
                testArray = Array.from({ length: 10 }, (_, i) => i + 1); // 1, 2, 3, ..., 10
                break;
    
            case 'average': // Average case: Random array
                testArray = Array.from({ length: 10 }, () => Math.floor(Math.random() * 100)); // Random values between 0-99
                break;
    
            case 'worst': // Worst case: Reverse sorted array
                testArray = Array.from({ length: 10 }, (_, i) => 10 - i); // 10, 9, 8, ..., 1
                break;
        }
    
        // Populate the comparison array with the generated test case values
        testArray.forEach(value => comparisonArray.push(value));
    
        // Update the display with the test case array
        updateComparisonArrayDisplay();
    });

    $('#addComparisionSortValue').click(function () {
        const inputValue = $('#comparisionArrayInput').val().trim();

        // Split the input by commas, spaces, or both (using a regular expression)
        const values = inputValue.split(/[\s,]+/).map(val => val.trim());

        values.forEach(value => {
            // Ensure each value is a number and not empty
            if (value !== '' && !isNaN(value)) {
                const number = Number(value);
                comparisonArray.push(number); // Push valid numbers to the comparisonArray
            }
        });

        // Update the comparison array display after all valid values are added
        updateComparisonArrayDisplay();

        // Clear the input field
        $('#comparisionArrayInput').val('');
    });


    async function visualizeComparisonArray(arr, algorithm, index1, index2, key = null) {
        const displayId = algorithm === 'bubble' ? "comparisonBubbleSortDisplay" : "comparisonInsertionSortDisplay";
        $(`#${displayId}`).empty();

        const maxValue = Math.max(...arr, 1);
        arr.forEach((value, index) => {
            const heightPercentage = (value / maxValue) * 100;
            const box = $('<div></div>')
                .addClass('array-box')
                .css({
                    'height': `${heightPercentage}%`,
                    'display': 'inline-block',
                    'margin': '0 2px'
                })
                .text(value);

            if (index === index1 || index === index2) {
                box.css('background-color', '#f1c40f');
            }

            $(`#${displayId}`).append(box);
        });

        // Display intermediate values
        if (algorithm === 'bubble') {
            $('#comparisonBubbleIntermediateValues').text(`Comparing: ${arr[index1]} and ${arr[index2]}`);
        } else {
            $('#comparisonInsertionIntermediateValues').text(`Key: ${key}, Comparing with: ${arr[index2]}`);
        }

        await sleep(500);
    }

    async function comparisonBubbleSort(arr) {
        let n = arr.length;
        for (let i = 0; i < n - 1; i++) {
            for (let j = 0; j < n - i - 1; j++) {
                await visualizeComparisonArray(arr, 'bubble', j, j + 1);
                if (arr[j] > arr[j + 1]) {
                    [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
                    await visualizeComparisonArray(arr, 'bubble', j, j + 1);
                }
            }
        }
    }

    async function comparisonInsertionSort(arr) {
        for (let i = 1; i < arr.length; i++) {
            let key = arr[i];
            let j = i - 1;
            await visualizeComparisonArray(arr, 'insertion', i, j, key);
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
                await visualizeComparisonArray(arr, 'insertion', i, j, key);
            }
            arr[j + 1] = key;
            await visualizeComparisonArray(arr, 'insertion', i, j + 1, key);
        }
    }

    $("#startComparisionVisualization").click(async function () {
        const bubbleSortArray = [...comparisonArray];
        const insertionSortArray = [...comparisonArray];

        $("#comparisonBubbleSortDisplay").empty();
        $("#comparisonInsertionSortDisplay").empty();

        // Start both sorting algorithms simultaneously
        await Promise.all([
            comparisonBubbleSort(bubbleSortArray),
            comparisonInsertionSort(insertionSortArray)
        ]);
    });



});
