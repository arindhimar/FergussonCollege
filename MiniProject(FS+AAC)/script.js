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


    const array = [];

    // Function to display the array in boxes
    function updateArrayDisplay() {
        $('#arrayDisplay').empty();
        const maxValue = Math.max(...array, 1); // Avoid division by zero if array is empty
        array.forEach(value => {
            const heightPercentage = (value / maxValue) * 100; // Calculate height relative to the max value
            const box = $('<div></div>')
                .addClass('array-box')
                .css('height', `${heightPercentage}%`) // Set height dynamically
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

        if (inputValue !== '' && !isNaN(inputValue)) { // Ensure input is not empty and is a number
            const number = Number(inputValue);
            array.push(number);
            updateArrayDisplay();
            $('#arrayInput').val('');
        } else {
            // Show error message in the designated area (if needed)
            $('#arrayInput').val('');
        }
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

    const insertionArray = [];

    // Function to display the array in boxes for Insertion Sort
    function updateInsertionArrayDisplay() {
        $('#arrayInsertionDisplay').empty();
        const maxValue = Math.max(...insertionArray, 1); // Avoid division by zero if array is empty
        insertionArray.forEach(value => {
            const heightPercentage = (value / maxValue) * 100; // Calculate height relative to the max value
            const box = $('<div></div>')
                .addClass('array-box')
                .css('height', `${heightPercentage}%`) // Set height dynamically
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

    // Event listener for the 'Add' button for Insertion Sort
    $('#addInsertionSortValue').click(function () {
        const inputValue = $('#insertionArrayInput').val().trim();

        if (inputValue !== '' && !isNaN(inputValue)) { // Ensure input is not empty and is a number
            const number = Number(inputValue);
            insertionArray.push(number);
            updateInsertionArrayDisplay();
            $('#insertionArrayInput').val(''); // Clear the input field
        } else {
            // Optionally show error message in the designated area (if needed)
            $('#insertionArrayInput').val('');
        }
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


});
