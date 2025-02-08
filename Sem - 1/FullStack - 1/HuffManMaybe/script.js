class Node {
    constructor(character, frequency) {
        this.character = character;
        this.frequency = frequency;
        this.left = null;
        this.right = null;
        this.id = character || `${frequency}`;
    }
}

const charFreqList = {};
const charFreqListElement = document.getElementById("char-freq-list");
const treeContainer = document.getElementById("tree-container");
const NODE_WIDTH = 50;  // Width of each node
const LEVEL_HEIGHT = 100;  // Distance between levels of the tree

// Helper function to add characters and frequencies to the list
function addCharacterFrequency() {
    const charInput = document.getElementById("char-input").value;
    const freqInput = parseInt(document.getElementById("freq-input").value);

    if (charInput && freqInput > 0) {
        charFreqList[charInput] = freqInput;
        const listItem = document.createElement("li");
        listItem.textContent = `${charInput}: ${freqInput}`;
        charFreqListElement.appendChild(listItem);

        // Clear input fields
        document.getElementById("char-input").value = '';
        document.getElementById("freq-input").value = '';
    }
}

// Helper function to create node elements
function createNodeElement(node, x, y) {
    const nodeElement = document.createElement("div");
    nodeElement.className = "node";
    nodeElement.textContent = node.character ? `${node.character} (${node.frequency})` : `${node.frequency}`;
    nodeElement.style.left = `${x - NODE_WIDTH / 2}px`;
    nodeElement.style.top = `${y - NODE_WIDTH / 2}px`;
    nodeElement.setAttribute("data-id", node.id);
    treeContainer.appendChild(nodeElement);
    return nodeElement;
}

// Helper function to create a line between parent and child
function createLineElement(parentElement, childElement) {
    const lineElement = document.createElement("div");
    lineElement.className = "line";

    const parentRect = parentElement.getBoundingClientRect();
    const childRect = childElement.getBoundingClientRect();

    const x1 = parentRect.left + parentRect.width / 2;
    const y1 = parentRect.top + parentRect.height / 2;
    const x2 = childRect.left + childRect.width / 2;
    const y2 = childRect.top + childRect.height / 2;

    const length = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
    const angle = Math.atan2(y2 - y1, x2 - x1) * 180 / Math.PI;

    lineElement.style.width = `${length}px`;
    lineElement.style.transform = `rotate(${angle}deg)`;
    lineElement.style.transformOrigin = '0 0';
    lineElement.style.left = `${x1}px`;
    lineElement.style.top = `${y1}px`;

    treeContainer.appendChild(lineElement);
}

// Recursive function to assign positions to the nodes
function assignPositions(node, depth, x, siblingCount) {
    if (!node) return;

    // Position the node at its correct coordinates
    const nodeElement = createNodeElement(node, x, depth * LEVEL_HEIGHT);

    if (node.left) {
        const leftX = x - siblingCount * (NODE_WIDTH * 2);
        const leftNodeElement = assignPositions(node.left, depth + 1, leftX, siblingCount / 2);
        createLineElement(nodeElement, leftNodeElement);
    }

    if (node.right) {
        const rightX = x + siblingCount * (NODE_WIDTH * 2);
        const rightNodeElement = assignPositions(node.right, depth + 1, rightX, siblingCount / 2);
        createLineElement(nodeElement, rightNodeElement);
    }

    return nodeElement;
}

// Create Huffman Tree with step-by-step animations
function buildHuffmanTreeWithAnimations(frequencyMap) {
    const priorityQueue = Object.entries(frequencyMap)
        .map(([char, freq]) => new Node(char, freq))
        .sort((a, b) => a.frequency - b.frequency);

    const nodeElements = {};

    priorityQueue.forEach(node => {
        const nodeElement = createNodeElement(node, window.innerWidth / 2, 50);
        nodeElements[node.id] = nodeElement;
    });

    const intervalId = setInterval(() => {
        if (priorityQueue.length > 1) {
            const left = priorityQueue.shift();
            const right = priorityQueue.shift();

            const parentNode = new Node(null, left.frequency + right.frequency);
            parentNode.left = left;
            parentNode.right = right;

            const parentElement = createNodeElement(parentNode, window.innerWidth / 2, 50);
            nodeElements[parentNode.id] = parentElement;

            // Merging nodes and assigning positions
            setTimeout(() => {
                assignPositions(parentNode, 0, window.innerWidth / 2, priorityQueue.length);
            }, 500);

            priorityQueue.push(parentNode);
            priorityQueue.sort((a, b) => a.frequency - b.frequency);
        } else {
            clearInterval(intervalId);  // Stop when tree is complete
        }
    }, 1500);  // Delay for each step to animate
}

// Add Event Listeners for input and button
document.getElementById("add-pair-button").addEventListener("click", addCharacterFrequency);

document.getElementById("build-tree-button").addEventListener("click", () => {
    document.getElementById("tree-container").innerHTML = "";  // Clear the tree display
    buildHuffmanTreeWithAnimations(charFreqList);
});
