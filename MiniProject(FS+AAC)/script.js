$(document).ready(function () {
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

    // Bubble sort function
    function bubbleSort() {
        let n = array.length;
        let bubbleSortArray = [...array];
        for (let i = 0; i < n - 1; i++) {
            for (let j = 0; j < n - i - 1; j++) {
                if (bubbleSortArray[j] > bubbleSortArray[j + 1]) {
                
                    let temp = bubbleSortArray[j];
                    bubbleSortArray[j] = bubbleSortArray[j + 1];
                    bubbleSortArray[j + 1] = temp;
                }
                
                
            }
        }
    }

    // Insertion sort function
    function insertionSort() {
        let n = array.length;
        let insertionSortArray = [...array];
        for (let i = 1; i < n; i++) {
            let key = insertionSortArray[i];
            let j = i - 1;
            while (j >= 0 && insertionSortArray[j] > key) {
                insertionSortArray[j + 1] = insertionSortArray[j];
                j--;
            }
            insertionSortArray[j + 1] = key;
        }
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

    $("#startButton").click(function (e) { 
        e.preventDefault();
        $("#arrayDisplay1").empty();
        $("#arrayDisplay").children().clone().appendTo("#arrayDisplay1");
    });
});
