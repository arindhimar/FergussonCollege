"use client"

import { useState, useEffect } from "react"
import {
  BarChartIcon,
  ScatterChartIcon as ScatterIcon,
  TableIcon,
  InfoIcon,
  DownloadIcon,
  PieChartIcon,
} from "lucide-react"
import ScatterPlot from "./visualizations/ScatterPlot"
import BarChart from "./visualizations/BarChart"
import PieChart from "./visualizations/PieChart"
import DataTable from "./DataTable"
import StepExplanation from "./StepExplanation"
import ClusterStats from "./ClusterStats"

const DataVisualizationPanel = ({
  data,
  clusters,
  xAxis,
  yAxis,
  visualizationType,
  setVisualizationType,
  animationStep,
  totalSteps,
  onStepChange,
  isAnimationPlaying,
  toggleAnimation,
  resetAnimation,
  iterations,
  currentDetailedStep,
  animationSpeed,
  setAnimationSpeed,
}) => {
  const [currentPage, setCurrentPage] = useState(1)
  const [showExplanation, setShowExplanation] = useState(true)
  const [showStats, setShowStats] = useState(false)
  const rowsPerPage = 10

  // Calculate pagination
  const totalPages = Math.ceil(data.length / rowsPerPage)
  const paginatedData = data.slice((currentPage - 1) * rowsPerPage, currentPage * rowsPerPage)

  // Generate cluster colors
  const clusterColors = [
    "rgb(0, 122, 255)", // Bright blue
    "rgb(255, 59, 48)", // Bright red
    "rgb(76, 217, 100)", // Bright green
    "rgb(255, 149, 0)", // Bright orange
    "rgb(175, 82, 222)", // Bright purple
    "rgb(255, 204, 0)", // Bright yellow
    "rgb(90, 200, 250)", // Light blue
    "rgb(255, 45, 85)", // Pink
    "rgb(0, 199, 190)", // Teal
    "rgb(88, 86, 214)", // Indigo
  ]

  // Skip to the end of the animation
  const skipToEnd = () => {
    if (totalSteps > 0) {
      onStepChange(totalSteps - 1)
    }
  }

  // Export data as CSV
  const exportData = () => {
    if (!data || data.length === 0) return

    // Convert data to CSV format
    const headers = Object.keys(data[0]).join(",")
    const rows = data.map((row) => Object.values(row).join(","))
    const csvContent = [headers, ...rows].join("\n")

    // Create a blob and download link
    const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" })
    const url = URL.createObjectURL(blob)
    const link = document.createElement("a")
    link.setAttribute("href", url)
    link.setAttribute("download", `kmeans_clusters_${new Date().toISOString().slice(0, 10)}.csv`)
    link.style.visibility = "hidden"
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)
  }

  // Highlight the row in the table that corresponds to the current point being processed
  const getHighlightedRowIndex = () => {
    if (currentDetailedStep && currentDetailedStep.type === "assign" && currentDetailedStep.highlightedPoint !== null) {
      return currentDetailedStep.highlightedPoint
    }
    return -1
  }

  // Keyboard shortcuts for animation control
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return

      switch (e.key) {
        case " ":
          toggleAnimation()
          e.preventDefault()
          break
        case "ArrowRight":
          if (animationStep < totalSteps - 1) onStepChange(animationStep + 1)
          e.preventDefault()
          break
        case "ArrowLeft":
          if (animationStep > 0) onStepChange(animationStep - 1)
          e.preventDefault()
          break
        case "Home":
          resetAnimation()
          e.preventDefault()
          break
        case "End":
          skipToEnd()
          e.preventDefault()
          break
        default:
          break
      }
    }

    window.addEventListener("keydown", handleKeyDown)
    return () => window.removeEventListener("keydown", handleKeyDown)
  }, [animationStep, totalSteps, toggleAnimation, onStepChange, resetAnimation])

  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 h-full">
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-6">
        <h2 className="text-xl font-semibold text-gray-800 dark:text-gray-200">Data Visualization</h2>

        <div className="flex flex-wrap gap-2">
          <button
            onClick={() => setVisualizationType("table")}
            className={`p-2 rounded-md transition-all duration-200 ${
              visualizationType === "table"
                ? "bg-primary-100 dark:bg-primary-900 text-primary-600 dark:text-primary-400 shadow-md transform scale-105"
                : "bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 hover:bg-gray-200 dark:hover:bg-gray-600"
            }`}
            title="Table View"
          >
            <TableIcon className="w-5 h-5" />
          </button>

          <button
            onClick={() => setVisualizationType("scatter")}
            className={`p-2 rounded-md transition-all duration-200 ${
              visualizationType === "scatter"
                ? "bg-primary-100 dark:bg-primary-900 text-primary-600 dark:text-primary-400 shadow-md transform scale-105"
                : "bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 hover:bg-gray-200 dark:hover:bg-gray-600"
            }`}
            title="Scatter Plot"
          >
            <ScatterIcon className="w-5 h-5" />
          </button>

          <button
            onClick={() => setVisualizationType("bar")}
            className={`p-2 rounded-md transition-all duration-200 ${
              visualizationType === "bar"
                ? "bg-primary-100 dark:bg-primary-900 text-primary-600 dark:text-primary-400 shadow-md transform scale-105"
                : "bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 hover:bg-gray-200 dark:hover:bg-gray-600"
            }`}
            title="Bar Chart"
          >
            <BarChartIcon className="w-5 h-5" />
          </button>

          <button
            onClick={() => setVisualizationType("pie")}
            className={`p-2 rounded-md transition-all duration-200 ${
              visualizationType === "pie"
                ? "bg-primary-100 dark:bg-primary-900 text-primary-600 dark:text-primary-400 shadow-md transform scale-105"
                : "bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 hover:bg-gray-200 dark:hover:bg-gray-600"
            }`}
            title="Pie Chart"
          >
            <PieChartIcon className="w-5 h-5" />
          </button>

          <button
            onClick={() => setShowExplanation(!showExplanation)}
            className={`p-2 rounded-md transition-all duration-200 ${
              showExplanation
                ? "bg-primary-100 dark:bg-primary-900 text-primary-600 dark:text-primary-400 shadow-md"
                : "bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 hover:bg-gray-200 dark:hover:bg-gray-600"
            }`}
            title="Toggle Explanation"
          >
            <InfoIcon className="w-5 h-5" />
          </button>

          <button
            onClick={exportData}
            disabled={!data || data.length === 0}
            className={`p-2 rounded-md transition-all duration-200 
              ${
                !data || data.length === 0
                  ? "bg-gray-100 dark:bg-gray-700 text-gray-400 dark:text-gray-600 cursor-not-allowed"
                  : "bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-400 hover:bg-gray-200 dark:hover:bg-gray-600"
              }`}
            title="Export Data as CSV"
          >
            <DownloadIcon className="w-5 h-5" />
          </button>
        </div>
      </div>

      {/* Step Explanation */}
      {showExplanation &&
        (visualizationType === "scatter" || visualizationType === "bar" || visualizationType === "pie") && (
          <StepExplanation
            currentDetailedStep={currentDetailedStep}
            animationStep={animationStep}
            totalSteps={totalSteps}
          />
        )}

      {/* Cluster Statistics Button */}
      {data && data.some((d) => d.cluster !== undefined) && (
        <div className="mb-4">
          <button
            onClick={() => setShowStats(!showStats)}
            className="text-sm flex items-center gap-2 text-sky-600 dark:text-sky-400 hover:underline"
          >
            {showStats ? "Hide" : "Show"} Cluster Statistics
            <span className="text-xs bg-sky-100 dark:bg-sky-900 text-sky-800 dark:text-sky-200 px-2 py-0.5 rounded-full">
              New
            </span>
          </button>

          {showStats && <ClusterStats data={data} xAxis={xAxis} yAxis={yAxis} clusterColors={clusterColors} />}
        </div>
      )}

      {/* Table View */}
      {visualizationType === "table" && (
        <div className="space-y-4 mt-4">
          <DataTable
            data={paginatedData}
            clusterColors={clusterColors}
            highlightedRowIndex={getHighlightedRowIndex()}
          />

          {/* Pagination */}
          {totalPages > 1 && (
            <div className="flex justify-between items-center mt-4">
              <button
                onClick={() => setCurrentPage((prev) => Math.max(prev - 1, 1))}
                disabled={currentPage === 1}
                className="px-3 py-1 border border-gray-300 dark:border-gray-600 rounded-md text-sm disabled:opacity-50 transition-colors hover:bg-gray-100 dark:hover:bg-gray-700"
              >
                Previous
              </button>

              <div className="flex items-center gap-1">
                {Array.from({ length: Math.min(5, totalPages) }, (_, i) => {
                  // Show pages around current page
                  let pageNum
                  if (totalPages <= 5) {
                    pageNum = i + 1
                  } else if (currentPage <= 3) {
                    pageNum = i + 1
                  } else if (currentPage >= totalPages - 2) {
                    pageNum = totalPages - 4 + i
                  } else {
                    pageNum = currentPage - 2 + i
                  }

                  return (
                    <button
                      key={i}
                      onClick={() => setCurrentPage(pageNum)}
                      className={`w-8 h-8 flex items-center justify-center rounded-md text-sm
                        ${
                          currentPage === pageNum
                            ? "bg-sky-100 dark:bg-sky-900 text-sky-700 dark:text-sky-300 font-medium"
                            : "text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700"
                        }`}
                    >
                      {pageNum}
                    </button>
                  )
                })}
              </div>

              <button
                onClick={() => setCurrentPage((prev) => Math.min(prev + 1, totalPages))}
                disabled={currentPage === totalPages}
                className="px-3 py-1 border border-gray-300 dark:border-gray-600 rounded-md text-sm disabled:opacity-50 transition-colors hover:bg-gray-100 dark:hover:bg-gray-700"
              >
                Next
              </button>
            </div>
          )}
        </div>
      )}

      {/* Scatter Plot View */}
      {visualizationType === "scatter" && (
        <div className="h-[500px] mt-4">
          <ScatterPlot
            data={data}
            clusters={clusters}
            xAxis={xAxis}
            yAxis={yAxis}
            clusterColors={clusterColors}
            currentDetailedStep={currentDetailedStep}
          />
        </div>
      )}

      {/* Bar Chart View */}
      {visualizationType === "bar" && (
        <div className="h-[500px] mt-4">
          <BarChart data={data} xAxis={xAxis} clusterColors={clusterColors} />
        </div>
      )}

      {/* Pie Chart View */}
      {visualizationType === "pie" && (
        <div className="h-[500px] mt-4">
          <PieChart data={data} clusterColors={clusterColors} />
        </div>
      )}

      {/* Legend */}
      {(visualizationType === "scatter" || visualizationType === "bar" || visualizationType === "pie") &&
        data.some((d) => d.cluster !== undefined) && (
          <div className="mt-4 flex flex-wrap gap-3 bg-gray-50 dark:bg-gray-700 p-3 rounded-lg">
            <div className="text-sm font-medium mr-2">Clusters:</div>
            {Array.from(new Set(data.map((d) => d.cluster)))
              .sort((a, b) => a - b)
              .map((cluster, index) => (
                <div key={cluster} className="flex items-center">
                  <div
                    className="w-4 h-4 rounded-full mr-1"
                    style={{ backgroundColor: clusterColors[cluster % clusterColors.length] }}
                  ></div>
                  <span className="text-sm text-gray-700 dark:text-gray-300">Cluster {cluster}</span>
                </div>
              ))}
          </div>
        )}

      {/* Keyboard Shortcuts Help */}
      <div className="mt-6 pt-4 border-t border-gray-200 dark:border-gray-700">
        <details className="text-sm text-gray-600 dark:text-gray-400">
          <summary className="cursor-pointer hover:text-gray-800 dark:hover:text-gray-200">Keyboard Shortcuts</summary>
          <div className="mt-2 grid grid-cols-2 gap-2 text-xs">
            <div className="flex items-center gap-2">
              <kbd className="px-2 py-1 bg-gray-100 dark:bg-gray-700 rounded">Space</kbd>
              <span>Play/Pause</span>
            </div>
            <div className="flex items-center gap-2">
              <kbd className="px-2 py-1 bg-gray-100 dark:bg-gray-700 rounded">←</kbd>
              <span>Previous Step</span>
            </div>
            <div className="flex items-center gap-2">
              <kbd className="px-2 py-1 bg-gray-100 dark:bg-gray-700 rounded">→</kbd>
              <span>Next Step</span>
            </div>
            <div className="flex items-center gap-2">
              <kbd className="px-2 py-1 bg-gray-100 dark:bg-gray-700 rounded">Home</kbd>
              <span>Reset</span>
            </div>
            <div className="flex items-center gap-2">
              <kbd className="px-2 py-1 bg-gray-100 dark:bg-gray-700 rounded">End</kbd>
              <span>Skip to End</span>
            </div>
          </div>
        </details>
      </div>
    </div>
  )
}

export default DataVisualizationPanel

