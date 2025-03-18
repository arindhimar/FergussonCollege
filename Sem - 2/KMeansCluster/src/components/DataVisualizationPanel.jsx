"use client"

import { useState } from "react"
import { BarChartIcon, ScatterChartIcon as ScatterIcon, TableIcon, InfoIcon } from "lucide-react"
import ScatterPlot from "./visualizations/ScatterPlot"
import BarChart from "./visualizations/BarChart"
import DataTable from "./DataTable"
import AnimationControls from "./AnimationControls"
import StepExplanation from "./StepExplanation"

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
}) => {
  const [currentPage, setCurrentPage] = useState(1)
  const [showExplanation, setShowExplanation] = useState(true)
  const rowsPerPage = 10

  // Calculate pagination
  const totalPages = Math.ceil(data.length / rowsPerPage)
  const paginatedData = data.slice((currentPage - 1) * rowsPerPage, currentPage * rowsPerPage)

  // Generate cluster colors
  const clusterColors = [
    "rgb(56, 189, 248)", // sky-400
    "rgb(251, 146, 60)", // orange-400
    "rgb(168, 85, 247)", // purple-500
    "rgb(74, 222, 128)", // green-400
    "rgb(248, 113, 113)", // red-400
    "rgb(232, 121, 249)", // fuchsia-400
    "rgb(250, 204, 21)", // yellow-400
    "rgb(45, 212, 191)", // teal-400
    "rgb(129, 140, 248)", // indigo-400
    "rgb(244, 114, 182)", // pink-400
  ]

  // Highlight the row in the table that corresponds to the current point being processed
  const getHighlightedRowIndex = () => {
    if (currentDetailedStep && currentDetailedStep.type === "assign" && currentDetailedStep.highlightedPoint !== null) {
      return currentDetailedStep.highlightedPoint
    }
    return -1
  }

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
        </div>
      </div>

      {/* Animation Controls */}
      {(visualizationType === "scatter" || visualizationType === "bar") && totalSteps > 0 && (
        <AnimationControls
          currentStep={animationStep}
          totalSteps={totalSteps}
          onStepChange={onStepChange}
          isPlaying={isAnimationPlaying}
          togglePlay={toggleAnimation}
          resetAnimation={resetAnimation}
        />
      )}

      {/* Step Explanation */}
      {showExplanation && (visualizationType === "scatter" || visualizationType === "bar") && (
        <StepExplanation
          currentDetailedStep={currentDetailedStep}
          animationStep={animationStep}
          totalSteps={totalSteps}
        />
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

              <span className="text-sm text-gray-600 dark:text-gray-400">
                Page {currentPage} of {totalPages}
              </span>

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

      {/* Legend */}
      {(visualizationType === "scatter" || visualizationType === "bar") &&
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
    </div>
  )
}

export default DataVisualizationPanel

