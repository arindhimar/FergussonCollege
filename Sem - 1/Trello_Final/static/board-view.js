// Drag and Drop Functionality for Tasks
let draggedTask = null

document.addEventListener("DOMContentLoaded", () => {
  // Initialize drag and drop for all task cards
  initDragAndDrop()

  function initDragAndDrop() {
    document.querySelectorAll(".task-card").forEach((task) => {
      task.setAttribute("draggable", true)

      task.addEventListener("dragstart", (e) => {
        draggedTask = task
        e.dataTransfer.setData("text/plain", task.dataset.taskId)
        setTimeout(() => {
          task.classList.add("dragging")
        }, 0)
      })

      task.addEventListener("dragend", () => {
        task.classList.remove("dragging")
      })
    })

    document.querySelectorAll(".task-column").forEach((column) => {
      column.addEventListener("dragover", (e) => {
        e.preventDefault()
        column.classList.add("bg-gray-200")
      })

      column.addEventListener("dragleave", () => {
        column.classList.remove("bg-gray-200")
      })

      column.addEventListener("drop", async (e) => {
        e.preventDefault()
        column.classList.remove("bg-gray-200")

        const taskId = e.dataTransfer.getData("text/plain")
        if (!taskId) return

        const draggedElement = document.querySelector(`.task-card[data-task-id="${taskId}"]`)
        if (!draggedElement) return

        const newStatus = column.dataset.status
        const placeholder = column.querySelector(".add-task-placeholder")

        try {
          const response = await fetch(`/api/tasks/${taskId}/status`, {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ status: newStatus }),
          })

          if (response.ok) {
            // Move the task to the new column
            if (placeholder && placeholder.parentNode === column) {
              column.insertBefore(draggedElement, placeholder)
            } else {
              column.appendChild(draggedElement)
            }

            // Show a success message
            showFlashMessage("Task status updated successfully!", "success")
          } else {
            throw new Error("Failed to update task status")
          }
        } catch (error) {
          console.error("Error:", error)
          showFlashMessage("Failed to update task status. Please try again.", "error")
        }
      })
    })
  }

  function showFlashMessage(message, type) {
    const flash = document.createElement("div")
    flash.className = `flash ${type}`
    flash.textContent = message
    document.body.appendChild(flash)

    setTimeout(() => {
      flash.style.opacity = "0"
      setTimeout(() => {
        if (flash.parentNode) {
          document.body.removeChild(flash)
        }
      }, 500)
    }, 2000)
  }
})

