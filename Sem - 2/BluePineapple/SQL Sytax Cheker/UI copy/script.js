<!DOCTYPE
html>
<html>
<head>
<title>SQL Editor</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/6.65.7/codemirror.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/6.65.7/theme/dracula.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/6.65.7/codemirror.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/6.65.7/mode/sql/sql.min.js"></script>


<style>
body {
    font-family: sans-serif;
}
#sqlEditor {
    width: 800px;
    height: 400px;
    border: 1px solid #ccc;
}
#result {
    margin-top: 10px;
    font-weight: bold;
}
#historyList {
    margin-top: 10px;
    list-style-type: none;
    padding: 0;
}
#historyList li {
    cursor: pointer;
}
</style>
</head>
<body>

<h1>SQL Editor</h1>

<textarea id="sqlEditor">
-- Enter your SQL query here
</textarea>

<button id="checkSyntaxBtn">Check Syntax</button>
<button id="clearEditorBtn">Clear Editor</button>
<button id="saveQueryBtn">Save Query</button>
<button id="clearHistoryBtn">Clear History</button>

<div id="result"></div>

<h2>Query History</h2>
<ul id="historyList"></ul>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const editor = CodeMirror.fromTextArea(document.getElementById("sqlEditor"), {
        mode: "text/x-sql",
        theme: "dracula",
        lineNumbers: true,
        autoCloseBrackets: true,
        matchBrackets: true,
        indentUnit: 4,
        tabSize: 4,
        indentWithTabs: true,
        extraKeys: {"Ctrl-Space": "autocomplete"}
    });

    const checkSyntaxBtn = document.getElementById('checkSyntaxBtn');
    const clearEditorBtn = document.getElementById('clearEditorBtn');
    const saveQueryBtn = document.getElementById('saveQueryBtn');
    const clearHistoryBtn = document.getElementById('clearHistoryBtn');
    const resultDiv = document.getElementById('result');
    const historyList = document.getElementById('historyList');

    checkSyntaxBtn.addEventListener('click', function() {
        const query = editor.getValue();
        const result = checkSyntax(query);
        displayResult(result);
        addToHistory(query, result);
    });

    clearEditorBtn.addEventListener('click', function() {
        editor.setValue('');
    });

    saveQueryBtn.addEventListener('click', function() {
        const query = editor.getValue();
        if (query.trim() !== '') {
            localStorage.setItem('savedQuery', query);
            alert('Query saved successfully!');
        } else {
            alert('Cannot save an empty query!');
        }
    });

    clearHistoryBtn.addEventListener('click', function() {
        localStorage.removeItem('queryHistory');
        updateHistoryList();
    });

    historyList.addEventListener('click', function(e) {
        if (e.target && e.target.nodeName === "LI") {
            const query = e.target.dataset.query;
            editor.setValue(query);
        }
    });

    function checkSyntax(query) {
        // This is a simplified syntax check. In a real-world scenario,
        // you'd want to implement a more robust SQL parser here.
        const keywords = ['SELECT', 'FROM', 'WHERE', 'INSERT', 'UPDATE', 'DELETE', 'CREATE', 'ALTER', 'DROP'];
        const uppercaseQuery = query.toUpperCase();
        
        let isValid = true;
        let errorMessage = '';

        // Check for basic structure
        if (!uppercaseQuery.includes('SELECT') && !uppercaseQuery.includes('INSERT') && 
            !uppercaseQuery.includes('UPDATE') && !uppercaseQuery.includes('DELETE') &&
            !uppercaseQuery.includes('CREATE') && !uppercaseQuery.includes('ALTER') &&
            !uppercaseQuery.includes('DROP')) {
            isValid = false;
            errorMessage = 'Query must include a valid SQL command (SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, DROP)';
        }

        // Check for semicolon at the end
        if (!query.trim().endsWith(';')) {
            isValid = false;
            errorMessage += ' Query must end with a semicolon.';
        }

        // Check for balanced parentheses
        const openParenCount = (query.match(/\(/g) || []).length;
        const closeParenCount = (query.match(/\)/g) || []).length;
        if (openParenCount !== closeParenCount) {
            isValid = false;
            errorMessage += ' Unbalanced parentheses.';
        }

        return {
            isValid: isValid,
            message: isValid ? 'Syntax appears to be valid.' : 'Syntax error: ' + errorMessage.trim()
        };
    }

    function displayResult(result) {
        resultDiv.textContent = result.message;
        resultDiv.style.color = result.isValid ? 'green' : 'red';
    }

    function addToHistory(query, result) {
        let history = JSON.parse(localStorage.getItem('queryHistory')) || [];
        history.unshift({ query, result: result.message });
        if (history.length > 10) history.pop();
        localStorage.setItem('queryHistory', JSON.stringify(history));
        updateHistoryList();
    }

    function updateHistoryList() {
        const history = JSON.parse(localStorage.getItem('queryHistory')) || [];
        historyList.innerHTML = '';
        history.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item.query;
            li.title = item.result;
            li.dataset.query = item.query;
            historyList.appendChild(li);
        });
    }

    // Load saved query if exists
    const savedQuery = localStorage.getItem('savedQuery');
    if (savedQuery) {
        editor.setValue(savedQuery);
    }

    // Initial history update
    updateHistoryList();
});
</script>

</body>
</html>

