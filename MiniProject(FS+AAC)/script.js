$(document).ready(function() {
    const array = []; 

    // Function to display the array in boxes
    function updateArrayDisplay() {
        $('#arrayDisplay').empty(); 
        array.forEach(value => {
            const box = $('<div></div>')
                .addClass('array-box') 
                .text(value); 
            $('#arrayDisplay').append(box);
        });
    }

    // Function to update the sorting visualizations
    function updateSortingDisplay(containerId, currentArray) {
        const container = $(containerId);
        container.empty();
        currentArray.forEach(value => {
            const bar = $('<div></div>').addClass('bar').css('height', value * 4 + 'px').text(value);
            container.append(bar);
        });
    }

    // Bubble Sort Function
    async function bubbleSort() {
        const n = array.length;
        const currentArray = [...array]; // Create a copy for visualization
        for (let i = 0; i < n - 1; i++) {
            for (let j = 0; j < n - i - 1; j++) {
                if (currentArray[j] > currentArray[j + 1]) {
                    // Swap
                    [currentArray[j], currentArray[j + 1]] = [currentArray[j + 1], currentArray[j]];
                    updateSortingDisplay('#bubbleSort', currentArray);
                    await new Promise(resolve => setTimeout(resolve, 500)); // Delay for visualization
                }
            }
        }
        updateSortingDisplay('#bubbleSort', currentArray); // Final display after sorting
    }

    // Insertion Sort Function
    async function insertionSort() {
        const n = array.length;
        const currentArray = [...array]; // Create a copy for visualization
        for (let i = 1; i < n; i++) {
            let key = currentArray[i];
            let j = i - 1;

            // Move elements of currentArray[0..i-1] that are greater than key to one position ahead
            while (j >= 0 && currentArray[j] > key) {
                currentArray[j + 1] = currentArray[j];
                updateSortingDisplay('#insertionSort', currentArray);
                await new Promise(resolve => setTimeout(resolve, 500)); // Delay for visualization
                j--;
            }
            currentArray[j + 1] = key;
            updateSortingDisplay('#insertionSort', currentArray);
        }
        updateSortingDisplay('#insertionSort', currentArray); // Final display after sorting
    }

    // Event listener for the 'Add' button
    $('#addButton').click(function() {
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

    // Event listener for the 'Start Both' button
    $('#startButton').click(async function() {
        if (array.length === 0) {
            // Handle empty array case
            return;
        }
        await bubbleSort();
        await insertionSort();
    });
});
