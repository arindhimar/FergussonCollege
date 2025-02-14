

document.addEventListener("DOMContentLoaded", () => {
  const editor = CodeMirror.fromTextArea(document.getElementById("sqlEditor"), {
    mode: "text/x-sql",
    theme: "monokai",
    lineNumbers: true,
    autoCloseBrackets: true,
    matchBrackets: true,
    indentUnit: 4,
    tabSize: 4,
    indentWithTabs: true,
    extraKeys: { "Ctrl-Space": "autocomplete" },
  })

  const checkSyntaxBtn = document.getElementById("checkSyntaxBtn")
  const clearEditorBtn = document.getElementById("clearEditorBtn")
  const saveQueryBtn = document.getElementById("saveQueryBtn")
  const loadQueryBtn = document.getElementById("loadQueryBtn")
  const newQueryBtn = document.getElementById("newQueryBtn")
  const formatQueryBtn = document.getElementById("formatQueryBtn")
  const clearHistoryBtn = document.getElementById("clearHistoryBtn")
  const settingsBtn = document.getElementById("settingsBtn")
  const saveSettingsBtn = document.getElementById("saveSettingsBtn")
  const closeSettingsBtn = document.getElementById("closeSettingsBtn")
  const resultDiv = document.getElementById("result")
  const historyList = document.getElementById("historyList")
  const settingsModal = document.getElementById("settingsModal")
  const themeSelect = document.getElementById("themeSelect")
  const fontSizeInput = document.getElementById("fontSizeInput")

  checkSyntaxBtn.addEventListener("click", async () => {
    const query = editor.getValue()
    if (!query.trim()) {
      showNotification("Query cannot be empty!", "error")
      return
    }

    try {
      const response = await fetch("http://127.0.0.1:5000/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ query: query }),
      })

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const result = await response.json()
      displayResult(result)
      addToHistory(query, result.message)
    } catch (error) {
      console.error("Error checking syntax:", error)
      showNotification("Failed to check syntax. Please try again.", "error")
    }
  })

  clearEditorBtn.addEventListener("click", () => {
    editor.setValue("")
  })

  saveQueryBtn.addEventListener("click", () => {
    const query = editor.getValue()
    if (query.trim() !== "") {
      localStorage.setItem("savedQuery", query)
      showNotification("Query saved successfully!", "success")
    } else {
      showNotification("Cannot save an empty query!", "error")
    }
  })

  loadQueryBtn.addEventListener("click", () => {
    const savedQuery = localStorage.getItem("savedQuery")
    if (savedQuery) {
      editor.setValue(savedQuery)
      showNotification("Query loaded successfully!", "success")
    } else {
      showNotification("No saved query found!", "error")
    }
  })

  newQueryBtn.addEventListener("click", () => {
    if (confirm("Are you sure you want to start a new query? This will clear the current editor.")) {
      editor.setValue("")
      showNotification("New query started!", "success")
    }
  })

  formatQueryBtn.addEventListener("click", () => {
    const query = editor.getValue()
    const formattedQuery = sqlFormatter.format(query)
    editor.setValue(formattedQuery)
    showNotification("Query formatted!", "success")
  })

  clearHistoryBtn.addEventListener("click", () => {
    if (confirm("Are you sure you want to clear the entire query history?")) {
      localStorage.removeItem("queryHistory")
      updateHistoryList()
      showNotification("Query history cleared!", "success")
    }
  })

  settingsBtn.addEventListener("click", () => {
    settingsModal.style.display = "block"
  })

  saveSettingsBtn.addEventListener("click", () => {
    const theme = themeSelect.value
    const fontSize = fontSizeInput.value
    editor.setOption("theme", theme)
    document.querySelector(".CodeMirror").style.fontSize = `${fontSize}px`
    localStorage.setItem("editorTheme", theme)
    localStorage.setItem("editorFontSize", fontSize)
    settingsModal.style.display = "none"
    showNotification("Settings saved!", "success")
  })

  closeSettingsBtn.addEventListener("click", () => {
    settingsModal.style.display = "none"
  })

  historyList.addEventListener("click", (e) => {
    if (e.target && e.target.nodeName === "LI") {
      const query = e.target.dataset.query
      editor.setValue(query)
      showNotification("Query loaded from history!", "success")
    }
  })

  function displayResult(result) {
    resultDiv.innerHTML = `
            <div class="${result.isValid ? "success" : "error"}">
                <i class="fas ${result.isValid ? "fa-check-circle" : "fa-exclamation-circle"}"></i>
                ${result.message}
            </div>
        `
  }

  function addToHistory(query, result) {
    const history = JSON.parse(localStorage.getItem("queryHistory")) || []
    history.unshift({ query, result })
    if (history.length > 10) history.pop()
    localStorage.setItem("queryHistory", JSON.stringify(history))
    updateHistoryList()
  }

  function updateHistoryList() {
    const history = JSON.parse(localStorage.getItem("queryHistory")) || []
    historyList.innerHTML = ""
    history.forEach((item) => {
      const li = document.createElement("li")
      li.textContent = item.query.substring(0, 50) + (item.query.length > 50 ? "..." : "")
      li.title = item.result
      li.dataset.query = item.query
      historyList.appendChild(li)
    })
  }

  function showNotification(message, type) {
    const notification = document.createElement("div")
    notification.textContent = message
    notification.className = `notification ${type}`
    document.body.appendChild(notification)
    setTimeout(() => {
      notification.classList.add("show")
      setTimeout(() => {
        notification.classList.remove("show")
        setTimeout(() => {
          document.body.removeChild(notification)
        }, 300)
      }, 2000)
    }, 100)
  }

  // Load saved settings
  const savedTheme = localStorage.getItem("editorTheme")
  const savedFontSize = localStorage.getItem("editorFontSize")
  if (savedTheme) {
    editor.setOption("theme", savedTheme)
    themeSelect.value = savedTheme
  }
  if (savedFontSize) {
    document.querySelector(".CodeMirror").style.fontSize = `${savedFontSize}px`
    fontSizeInput.value = savedFontSize
  }

  // Load saved query if exists
  const savedQuery = localStorage.getItem("savedQuery")
  if (savedQuery) {
    editor.setValue(savedQuery)
  }

  // Initial history update
  updateHistoryList()
})

