$(document).ready(function () {
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
            const heightPercentage = (value / maxValue) * 100;
            const box = $('<div></div>')
                .addClass('array-box')
                .css('height', `${heightPercentage}%`)
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
    async function visualizeInsertionKey(key) {
        $("#insertionSortKey").empty(); // Clear previous key
        const keyBox = $('<div></div>').addClass('array-box').text(key).css('background-color', '#f1c40f');

        $("#insertionSortKey").append(keyBox); // Show current key value
    }

    async function insertionSort() {
        let n = array.length;
        let insertionSortArray = [...array];

        for (let i = 1; i < n; i++) {
            let key = insertionSortArray[i];
            let j = i - 1;

            // Highlight the key element
            await visualizeInsertionKey(key);
            await visualizeInsertionArray(insertionSortArray, i, j, true);

            while (j >= 0 && insertionSortArray[j] > key) {
                insertionSortArray[j + 1] = insertionSortArray[j];
                j--;

                // Visualize the array after shifting the element
                await visualizeInsertionArray(insertionSortArray, i, j + 1, false);
            }
            insertionSortArray[j + 1] = key;

            // Visualize the array after placing the key in its correct position
            await visualizeInsertionArray(insertionSortArray, j + 1, -1, true);
        }

        // Final visualization when sorting is done
        await visualizeInsertionArray(insertionSortArray, -1, -1, true);
    }

    async function visualizeInsertionArray(arr, keyIndex, compareIndex, inserted = false) {
        $("#arrayDisplay2").empty(); // Clear the insertion sort display

        const maxValue = Math.max(...arr, 1); // Avoid division by zero
        arr.forEach((value, index) => {
            const heightPercentage = (value / maxValue) * 100;
            const box = $('<div></div>')
                .addClass('array-box')
                .css('height', `${heightPercentage}%`)
                .text(value);

            // Highlight the key element
            if (index === keyIndex) {
                box.css('background-color', '#f1c40f'); // Highlight the key element in yellow
            }

            // Highlight the comparison element
            if (index === compareIndex && !inserted) {
                box.css('background-color', '#ff6347'); // Highlight the comparison element in red
            }

            $("#arrayDisplay2").append(box);
        });

        await sleep(500); // Adjust the delay as needed
    }




    // Event listener for the 'Add' button and Enter key press
    $('#addButton').click(function () {
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

    $('#arrayInput').keypress(function (e) {
        if (e.which === 13) { // Enter key is pressed
            const inputValue = $(this).val().trim();

            if (inputValue !== '' && !isNaN(inputValue)) { // Ensure input is not empty and is a number
                const number = Number(inputValue);
                array.push(number);
                updateArrayDisplay();
                $(this).val('');
            } else {
                // Show error message in the designated area (if needed)
                $(this).val('');
            }
        }
    });

    // Event listener for the 'Start Both' button
    $("#startButton").click(async function () {
        $("#arrayDisplay1").empty();
        $("#arrayDisplay2").empty();
        $("#arrayDisplay").children().clone().appendTo("#arrayDisplay1");
        $("#arrayDisplay").children().clone().appendTo("#arrayDisplay2");

        // Run both sorting algorithms simultaneously
        await Promise.all([bubbleSort(), insertionSort()]);
    });

});