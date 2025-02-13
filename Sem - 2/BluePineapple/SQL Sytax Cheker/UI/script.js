;(<script type="text/javascript" src="brython.js"></script>) < script
type = "text/javascript"
src="brython_stdlib.js">
</script>
;<script type="text/javascript" src="sql_parser.js"></script>

document.addEventListener("DOMContentLoaded", () => {
  brython()
})

function checkSyntax() {
  const sqlInput = document.getElementById("sqlInput").value
  const resultDiv = document.getElementById("result")
  const historyList = document.getElementById("historyList")

  // Call the Python function to check syntax
  const result = __BRYTHON__.builtins.getattr(__BRYTHON__.imported.sql_parser, "check_syntax")(sqlInput)

  // Display the result
  resultDiv.textContent = result

  // Add to history
  const historyItem = document.createElement("li")
  historyItem.textContent = `${sqlInput} - ${result}`
  historyList.prepend(historyItem)

  // Limit history to 10 items
  if (historyList.children.length > 10) {
    historyList.removeChild(historyList.lastChild)
  }
}

document.getElementById("checkButton").addEventListener("click", checkSyntax)

