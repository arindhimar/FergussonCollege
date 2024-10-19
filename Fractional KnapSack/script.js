let items = [];
let itemIndex = 0;

function generatePredefinedInput() {
    const predefinedItems = [
        { profit: 60, weight: 10 },
        { profit: 100, weight: 20 },
        { profit: 120, weight: 30 }
    ];

    const predefinedCapacity = 50;

    $('#numItems').val(predefinedItems.length);
    $('#capacity').val(predefinedCapacity);
    
    const itemInputs = $('#itemInputs');
    itemInputs.empty();  

    predefinedItems.forEach((item, i) => {
        itemInputs.append(`
            <div>
                <label>Item ${i + 1} - Profit:</label>
                <input type="number" id="profit${i}" value="${item.profit}" required>
                <label>Weight:</label>
                <input type="number" id="weight${i}" value="${item.weight}" required><br><br>
            </div>
        `);
    });
}

function startKnapsackProcess() {
    const numItems = $('#numItems').val();
    const capacity = $('#capacity').val();

    items = [];

    for (let i = 0; i < numItems; i++) {
        const profit = parseFloat($(`#profit${i}`).val());
        const weight = parseFloat($(`#weight${i}`).val());
        const ratio = profit / weight;
        items.push({ item: i + 1, profit, weight, ratio });
    }

    items.sort((a, b) => b.ratio - a.ratio);

    itemIndex = 0;
    $('#itemsOutsideSack').empty();  
    items.forEach(item => {
        const circle = $('<div>').addClass('circle').text(`Item ${item.item}`).draggable({
            revert: 'invalid',
            containment: '#itemsOutsideSack'
        });
        $('#itemsOutsideSack').append(circle);
    });

    // Animate sack opening before starting to add items
    $('#knapsackSack').css('transform', 'scale(1.1)');
    setTimeout(() => {
        $('#knapsackSack').css('transform', 'scale(1)');
    }, 500); 
}

function processNextItem(remainingCapacity) {
    if (itemIndex >= items.length || remainingCapacity <= 0) {
        return;
    }

    const item = items[itemIndex];
    let weightTaken = Math.min(item.weight, remainingCapacity);
    let profitGained = weightTaken * item.ratio;
    remainingCapacity -= weightTaken;

    const circle = $('#itemsOutsideSack .circle').eq(itemIndex);

    // Animate item falling into sack with a bounce effect
    circle.css({
        transition: 'transform 0.5s ease-in-out',
        transform: 'translateY(100px) scale(1.2)' // Bounce effect
    });

    // After falling, animate into the sack
    setTimeout(() => {
        // Create a new item element for the sack
        const sackItem = $('<div>').addClass('sack-item').text(`Item ${item.item}`);
        
        // Append the new item to the itemsInSack div
        $('#itemsInSack').append(sackItem);

        // Animate the item scaling to give a visual effect
        sackItem.css({
            transform: 'scale(0)' // Start small
        });

        setTimeout(() => {
            sackItem.css({
                transform: 'scale(1)' // Scale to normal size
            });

            // Add sound effect (optional)
            const audio = new Audio('path/to/sound.mp3'); // Add a sound file path
            audio.play();

            setTimeout(() => {
                $('#resultTable tbody').append(`
                    <tr>
                        <td>${item.item}</td>
                        <td>${profitGained.toFixed(2)}</td>
                        <td>${remainingCapacity.toFixed(2)}</td>
                    </tr>
                `);

                // Remove the circle from the outside area
                circle.remove();

                itemIndex++;
                processNextItem(remainingCapacity);
            }, 500); // Delay for next item
        }, 300); // Delay for scale animation
    }, 500); // Delay for falling animation
}

$(document).ready(function() {
    generatePredefinedInput();

    // Make the sack droppable
    $('#knapsackSack').droppable({
        accept: '.circle', // Accept only items with the class "circle"
        drop: function(event, ui) {
            const itemText = ui.draggable.text(); // Get the text of the dragged item
            // Append item to sack
            const sackItem = $('<div>').addClass('sack-item').text(itemText);
            $('#itemsInSack').append(sackItem);

            // Remove item from outside
            ui.draggable.remove();

            // Add animation effect when adding to sack
            sackItem.css({ transform: 'scale(0)' }); // Start small
            setTimeout(() => {
                sackItem.css({ transform: 'scale(1)' }); // Scale to normal size
            }, 300);
        }
    });
});
