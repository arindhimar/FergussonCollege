function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    section.scrollIntoView({ behavior: 'smooth' });
}



// Main entry point: Initialize event handlers and UI behavior
$(document).ready(function () {


    // Highlight the active section link in the navigation menu while scrolling
    $(window).scroll(function () {
        var scrollPos = $(document).scrollTop();

        $('nav ul li a').each(function () {
            var currLink = $(this);
            var sectionId = currLink.attr("href");

            var section = $(sectionId);

            if (section.position().top <= scrollPos && section.position().top + section.height() > scrollPos) {
                $('nav ul li a').removeClass("active");
                currLink.addClass("active");
            } else {
                currLink.removeClass("active");
            }
        });
    });


    // Event handler: Update Bubble Sort code display based on selected programming language
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

    // Toggle complexity details for sorting algorithms
    $('.toggle-complexity').click(function () {
        $(this).next('.complexity-list').slideToggle();
        $(this).toggleClass('expanded');
    });


    var array = [];

    // Update and display the current array state for sorting visualizations
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

    // Visualize the array for bubble sort, highlighting elements being compared/swapped
    async function visualizeArray(arr, index1, index2, swapped = false) {
        $("#arrayDisplay1").empty(); // Clear the bubble sort display

        const containerHeight = $("#arrayDisplay1").height(); // Get container height
        const containerWidth = $("#arrayDisplay1").width(); // Get container width
        const totalElements = arr.length;

        const gap = 2; // Adjust gap size (in pixels)

        const boxWidth = Math.floor((containerWidth - gap * (totalElements - 1)) / totalElements);
        const boxHeight = containerHeight; // Use full container height for each box

        if (boxWidth <= 0) {
            console.error("Container too small for the elements with gaps.");
            return; // Exit function early
        }

        arr.forEach((value, index) => {
            const box = $('<div></div>')
                .addClass('array-box')
                .css({
                    'height': `${boxHeight}px`, // Set height dynamically
                    'width': `${boxWidth}px`, // Set width dynamically
                    'display': 'inline-block', // Arrange boxes horizontally
                    'margin-right': `${gap}px`, // Add right margin for gaps
                    'text-align': 'center', // Center text horizontally
                    'line-height': `${boxHeight}px`, // Center text vertically
                    'box-sizing': 'border-box', // Include padding and border in dimensions
                    'color': '#333', // Text color
                    'font-weight': 'bold', // Emphasize the values
                })
                .text(value);

            if (index === index1 || index === index2) {
                box.css('background-color', swapped ? '#ff6347' : '#f1c40f'); // Highlight comparison or swap
            }

            $("#arrayDisplay1").append(box);
        });

        $("#arrayDisplay1 .array-box:last-child").css('margin-right', '0');

        await sleep(500); // Adjust the delay as needed
    }






    async function visualizeBubbleImportantValues(val1, val2) {
        $("#bubbleSortImportant").empty(); // Clear previous values
        const value1Box = $('<div></div>').addClass('array-box').text(val1).css('background-color', '#ff6347');
        const value2Box = $('<div></div>').addClass('array-box').text(val2).css('background-color', '#ff6347');

        $("#bubbleSortImportant").append(value1Box).append(value2Box); // Show swapped values
    }


    // Perform Bubble Sort and visualize the process step by step
    async function bubbleSort() {
        let n = array.length;
        let bubbleSortArray = [...array];

        for (let i = 0; i < n - 1; i++) {
            for (let j = 0; j < n - i - 1; j++) {
                await visualizeArray(bubbleSortArray, j, j + 1);

                if (bubbleSortArray[j] > bubbleSortArray[j + 1]) {
                    let temp = bubbleSortArray[j];
                    bubbleSortArray[j] = bubbleSortArray[j + 1];
                    bubbleSortArray[j + 1] = temp;

                    await visualizeArray(bubbleSortArray, j, j + 1, true);
                    await visualizeBubbleImportantValues(bubbleSortArray[j], bubbleSortArray[j + 1]);
                }
            }
        }
        await visualizeArray(bubbleSortArray, -1, -1, true);
    }

    // Event handler: Add values to the Bubble Sort array based on user input
    $('#addBubbleSortValue').click(function () {
        const inputValue = $('#arrayInput').val().trim();

        const values = inputValue.split(/[\s,]+/).map(val => val.trim());

        values.forEach(value => {
            if (value !== '' && !isNaN(value)) {
                const number = Number(value);
                array.push(number); // Push valid numbers to the array
            }
        });

        updateArrayDisplay();

        $('#arrayInput').val('');
    });

    // Generate predefined test cases for Bubble Sort and update the visualization
    $('#bubbleTestCaseSelect').change(function () {
        const selectedCase = $(this).val();

        array = [];
        $('#arrayInput').val(''); // Clear the input field

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

        testArray.forEach(value => array.push(value));

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

        const containerHeight = $("#insertionSortDisplay").height(); // Get container height
        const containerWidth = $("#insertionSortDisplay").width(); // Get container width
        const totalElements = arr.length;

        const gap = 2; // Define gap size
        const boxWidth = Math.floor((containerWidth - gap * (totalElements - 1)) / totalElements);
        const boxHeight = containerHeight; // Use full container height for each box

        if (boxWidth <= 0) {
            console.error("Container too small for the elements with gaps.");
            return; // Exit if the container is too small
        }

        arr.forEach((value, index) => {
            const box = $('<div></div>')
                .addClass('array-box')
                .css({
                    'height': `${boxHeight}px`,
                    'width': `${boxWidth}px`,
                    'display': 'inline-block',
                    'margin-right': `${gap}px`, // Add gap
                    'text-align': 'center',
                    'line-height': `${boxHeight}px`, // Center text vertically
                    'box-sizing': 'border-box',
                    'color': '#333',
                    'font-weight': 'bold',
                })
                .text(value);

            if (index === index1 || index === index2) {
                box.css('background-color', '#f1c40f'); // Highlight comparison
            }

            $("#insertionSortDisplay").append(box);
        });

        $("#insertionSortDisplay .array-box:last-child").css('margin-right', '0');

        await sleep(500); // Adjust delay as needed
    }

    // Perform Insertion Sort and visualize the process step by step
    async function insertionSort() {
        let insertionSortArray = [...insertionArray];

        for (let i = 1; i < insertionSortArray.length; i++) {
            let key = insertionSortArray[i];
            let j = i - 1;

            await visualizeInsertionArray(insertionSortArray, i, j);

            while (j >= 0 && insertionSortArray[j] > key) {
                insertionSortArray[j + 1] = insertionSortArray[j];
                j--;

                await visualizeInsertionArray(insertionSortArray, i, j);
            }
            insertionSortArray[j + 1] = key;

            await visualizeInsertionArray(insertionSortArray, -1, -1);
        }
    }

    $('#insertionTestCaseSelect').change(function () {
        const selectedCase = $(this).val();

        insertionArray = [];
        $('#insertionArrayInput').val(''); // Clear the input field

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

        testArray.forEach(value => insertionArray.push(value));

        updateInsertionArrayDisplay();
    });


    // Event handler: Add values to the Insertion Sort array based on user input
    $('#addInsertionSortValue').click(function () {
        const inputValue = $('#insertionArrayInput').val().trim();

        const values = inputValue.split(/[\s,]+/).map(val => val.trim());

        values.forEach(value => {
            if (value !== '' && !isNaN(value)) {
                const number = Number(value);
                insertionArray.push(number); // Push valid numbers to the insertionArray
            }
        });

        updateInsertionArrayDisplay();

        $('#insertionArrayInput').val('');
    });

    $("#startInsertionVisualization").click(async function () {
        $("#insertionSortDisplay").empty();
        $("#insertionArrayDisplay").children().clone().appendTo("#insertionSortDisplay");

        await insertionSort();
    });

    $("#startBubbleVisualization").click(async function () {
        $("#arrayDisplay1").empty();
        $("#arrayDisplay2").empty();
        $("#arrayDisplay").children().clone().appendTo("#arrayDisplay1");
        $("#arrayDisplay").children().clone().appendTo("#arrayDisplay2");

        await Promise.all([bubbleSort()]);
    });























    // Perform Insertion Sort and visualize the process step by step
    async function insertionSort() {
        let insertionSortArray = [...insertionArray];

        for (let i = 1; i < insertionSortArray.length; i++) {
            let key = insertionSortArray[i];
            let j = i - 1;

            await visualizeInsertionArray(insertionSortArray, i, j);

            while (j >= 0 && insertionSortArray[j] > key) {
                insertionSortArray[j + 1] = insertionSortArray[j];
                j--;

                await visualizeInsertionArray(insertionSortArray, i, j);
            }
            insertionSortArray[j + 1] = key;

            await visualizeInsertionArray(insertionSortArray, -1, -1);
        }
    }

    // Perform Bubble Sort and visualize the process step by step
    async function bubbleSort() {
        let n = array.length;
        let bubbleSortArray = [...array];

        for (let i = 0; i < n - 1; i++) {
            for (let j = 0; j < n - i - 1; j++) {
                await visualizeArray(bubbleSortArray, j, j + 1);

                if (bubbleSortArray[j] > bubbleSortArray[j + 1]) {
                    let temp = bubbleSortArray[j];
                    bubbleSortArray[j] = bubbleSortArray[j + 1];
                    bubbleSortArray[j + 1] = temp;

                    await visualizeArray(bubbleSortArray, j, j + 1, true);
                    await visualizeBubbleImportantValues(bubbleSortArray[j], bubbleSortArray[j + 1]);
                }
            }
        }
        await visualizeArray(bubbleSortArray, -1, -1, true);
    }










    var comparisonArray = [];

    function updateComparisonArrayDisplay() {
        $('#arrayComparisionDisplay').empty(); // Clear the container

        const containerHeight = $('#arrayComparisionDisplay').height(); // Get container height
        const containerWidth = $('#arrayComparisionDisplay').width(); // Get container width
        const totalElements = comparisonArray.length;

        const gap = 2; // Define gap size
        const boxWidth = Math.floor((containerWidth - gap * (totalElements - 1)) / totalElements);
        const boxHeight = containerHeight;

        if (boxWidth <= 0) {
            console.error("Container too small for the elements with gaps.");
            return; // Exit if the container is too small
        }

        comparisonArray.forEach(value => {
            const box = $('<div></div>')
                .addClass('array-box')
                .css({
                    'height': `${boxHeight}px`,
                    'width': `${boxWidth}px`,
                    'display': 'inline-block',
                    'margin-right': `${gap}px`,
                    'text-align': 'center',
                    'line-height': `${boxHeight}px`,
                    'box-sizing': 'border-box',
                    'color': '#333',
                    'font-weight': 'bold',
                })
                .text(value);

            $('#arrayComparisionDisplay').append(box);
        });

        $('#arrayComparisionDisplay .array-box:last-child').css('margin-right', '0'); // Remove extra margin
    }



    $('#comparisonTestCaseSelect').change(function () {
        const selectedCase = $(this).val();

        comparisonArray = [];
        $('#comparisionArrayInput').val(''); // Clear the input field

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

        testArray.forEach(value => comparisonArray.push(value));

        updateComparisonArrayDisplay();
    });

    $('#addComparisionSortValue').click(function () {
        const inputValue = $('#comparisionArrayInput').val().trim();

        const values = inputValue.split(/[\s,]+/).map(val => val.trim());

        values.forEach(value => {
            if (value !== '' && !isNaN(value)) {
                const number = Number(value);
                comparisonArray.push(number); // Push valid numbers to the comparisonArray
            }
        });

        updateComparisonArrayDisplay();

        $('#comparisionArrayInput').val('');
    });


    async function visualizeComparisonArray(arr, algorithm, index1, index2, key = null) {
        const displayId = algorithm === 'bubble' ? "comparisonBubbleSortDisplay" : "comparisonInsertionSortDisplay";
        $(`#${displayId}`).empty(); // Clear the display container
    
        const containerHeight = $(`#${displayId}`).height(); // Get container height
        const containerWidth = $(`#${displayId}`).width(); // Get container width
        const totalElements = arr.length;
    
        const gap = 2; // Define gap size
        const boxWidth = Math.floor((containerWidth - gap * (totalElements - 1)) / totalElements);
        const boxHeight = containerHeight;
    
        if (boxWidth <= 0) {
            console.error("Container too small for the elements with gaps.");
            return; // Exit if the container is too small
        }
    
        arr.forEach((value, index) => {
            const box = $('<div></div>')
                .addClass('array-box')
                .css({
                    'height': `${boxHeight}px`,
                    'width': `${boxWidth}px`,
                    'display': 'inline-block',
                    'margin-right': `${gap}px`,
                    'text-align': 'center',
                    'line-height': `${boxHeight}px`,
                    'box-sizing': 'border-box',
                    'color': '#333',
                    'font-weight': 'bold',
                })
                .text(value);
    
            if (index === index1 || index === index2) {
                box.css('background-color', '#f1c40f'); // Highlight comparison
            }
    
            $(`#${displayId}`).append(box);
        });
    
        $(`#${displayId} .array-box:last-child`).css('margin-right', '0'); // Remove extra margin
    
        if (algorithm === 'bubble') {
            $('#comparisonBubbleIntermediateValues').text(`Comparing: ${arr[index1]} and ${arr[index2]}`);
        } else {
            $('#comparisonInsertionIntermediateValues').text(`Key: ${key}, Comparing with: ${arr[index2]}`);
        }
    
        await sleep(500); // Adjust delay as needed
    }
    
    async function comparisonBubbleSort(arr) {
        let n = arr.length;
        let swapCount = 0; // Variable to track swaps
        const startTime = performance.now(); // Start the timer
    
        for (let i = 0; i < n - 1; i++) {
            for (let j = 0; j < n - i - 1; j++) {
                await visualizeComparisonArray(arr, 'bubble', j, j + 1);
                if (arr[j] > arr[j + 1]) {
                    // Swap elements
                    [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
                    swapCount++; // Increment swap count
                    await visualizeComparisonArray(arr, 'bubble', j, j + 1);
                }
                // Update the time and swap count continuously
                updateBubbleSortStats(swapCount, performance.now() - startTime);
            }
        }
    }
    
    async function comparisonInsertionSort(arr) {
        let swapCount = 0; // Variable to track swaps
        const startTime = performance.now(); // Start the timer
    
        for (let i = 1; i < arr.length; i++) {
            let key = arr[i];
            let j = i - 1;
    
            // Ensure j is within bounds when calling visualizeComparisonArray
            await visualizeComparisonArray(arr, 'insertion', i, j >= 0 ? j : 0, key);
    
            // Perform comparisons and shifts
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j]; // Shift the element
                j--;
                swapCount++; // Increment swap count for each shift
                // Ensure j is within bounds when calling visualizeComparisonArray
                await visualizeComparisonArray(arr, 'insertion', i, j >= 0 ? j : 0, key);
            }
    
            // Insert the key into its correct position
            arr[j + 1] = key;
            // Ensure j + 1 is within bounds
            await visualizeComparisonArray(arr, 'insertion', i, j + 1, key);
    
            // Update the stats continuously
            updateInsertionSortStats(swapCount, performance.now() - startTime);
        }
    }
    
    
    // Function to update Bubble Sort stats
    function updateBubbleSortStats(swapCount, timeElapsed) {
        $('#comparisonBubbleSortTime').text(`Time Taken: ${(timeElapsed / 1000).toFixed(2)}s`);
        $('#comparisonBubbleSortSwaps').text(`Total Swaps: ${swapCount}`);
    }
    
    // Function to update Insertion Sort stats
    function updateInsertionSortStats(swapCount, timeElapsed) {
        $('#comparisonInsertionSortTime').text(`Time Taken: ${(timeElapsed / 1000).toFixed(2)}s`);
        $('#comparisonInsertionSortSwaps').text(`Total Swaps: ${swapCount}`);
    }
    
    $("#startComparisionVisualization").click(async function () {
        const bubbleSortArray = [...comparisonArray];
        const insertionSortArray = [...comparisonArray];
    
        $("#comparisonBubbleSortDisplay").empty();
        $("#comparisonInsertionSortDisplay").empty();
    
      
        console.clear(); 
    
        // Initialize the display of initial stats
        $('#comparisonBubbleSortTime').text("Time Taken: 0s");
        $('#comparisonBubbleSortSwaps').text("Total Swaps: 0");
        $('#comparisonInsertionSortTime').text("Time Taken: 0s");
        $('#comparisonInsertionSortSwaps').text("Total Swaps: 0");
    
        await Promise.all([
            comparisonBubbleSort(bubbleSortArray),
            comparisonInsertionSort(insertionSortArray)
        ]);
    });
    


});
