"use client"

import { useState } from "react"
import { ChevronDownIcon, PlusIcon, UploadIcon, DatabaseIcon, PlayIcon, RefreshCwIcon } from "lucide-react"

const DataEntryPanel = ({
  onAddDataPoint,
  onFileUpload,
  onLoadSampleData,
  onGenerateRandomData,
  columns,
  xAxis,
  yAxis,
  setXAxis,
  setYAxis,
  clusterCount,
  setClusterCount,
  onRunClustering,
  isLoading,
}) => {
  const [newDataPoint, setNewDataPoint] = useState({
    Genre: "Male",
    Age: "",
    "Annual Income (k$)": "",
    "Spending Score (1-100)": "",
  })

  const handleInputChange = (e) => {
    const { name, value } = e.target
    setNewDataPoint((prev) => ({ ...prev, [name]: value }))
  }

  const handleAddDataPoint = (e) => {
    e.preventDefault()
    onAddDataPoint(newDataPoint)
    setNewDataPoint({
      Genre: "Male",
      Age: "",
      "Annual Income (k$)": "",
      "Spending Score (1-100)": "",
    })
  }

  const handleFileChange = (e) => {
    const file = e.target.files[0]
    if (file) {
      onFileUpload(file)
    }
  }

  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 h-full">
      <h2 className="text-xl font-semibold mb-6 text-gray-800 dark:text-gray-200">Data Entry & Controls</h2>

      {/* Data Entry Form */}
      <form onSubmit={handleAddDataPoint} className="mb-6">
        <div className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Gender</label>
            <select
              name="Genre"
              value={newDataPoint.Genre}
              onChange={handleInputChange}
              className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:outline-none focus:ring-sky-500 focus:border-sky-500 dark:bg-gray-700 transition-colors"
              required
            >
              <option value="Male">Male</option>
              <option value="Female">Female</option>
            </select>
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Age</label>
            <input
              type="number"
              name="Age"
              value={newDataPoint.Age}
              onChange={handleInputChange}
              placeholder="Enter age"
              className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:outline-none focus:ring-sky-500 focus:border-sky-500 dark:bg-gray-700 transition-colors"
              required
              min="1"
              max="100"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
              Annual Income (k$)
            </label>
            <input
              type="number"
              name="Annual Income (k$)"
              value={newDataPoint["Annual Income (k$)"]}
              onChange={handleInputChange}
              placeholder="Enter annual income"
              className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:outline-none focus:ring-sky-500 focus:border-sky-500 dark:bg-gray-700 transition-colors"
              required
              min="1"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
              Spending Score (1-100)
            </label>
            <input
              type="number"
              name="Spending Score (1-100)"
              value={newDataPoint["Spending Score (1-100)"]}
              onChange={handleInputChange}
              placeholder="Enter spending score"
              className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:outline-none focus:ring-sky-500 focus:border-sky-500 dark:bg-gray-700 transition-colors"
              required
              min="1"
              max="100"
            />
          </div>

          <button
            type="submit"
            className="w-full flex justify-center items-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-sky-600 hover:bg-sky-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-sky-500 transition-all duration-200 transform hover:scale-105"
          >
            <PlusIcon className="w-4 h-4 mr-2" />
            Add Data Point
          </button>
        </div>
      </form>

      {/* Data Loading Options */}
      <div className="space-y-4 mb-6">
        <div className="flex flex-col space-y-2">
          <label className="block text-sm font-medium text-gray-700 dark:text-gray-300">Load Data</label>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            <div className="relative group">
              <input
                type="file"
                accept=".csv"
                onChange={handleFileChange}
                className="absolute inset-0 w-full h-full opacity-0 cursor-pointer z-10"
              />
              <button
                type="button"
                className="w-full flex justify-center items-center px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm text-sm font-medium text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-700 group-hover:bg-gray-50 dark:group-hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-sky-500 transition-all duration-200"
              >
                <UploadIcon className="w-4 h-4 mr-2" />
                Upload CSV
              </button>
            </div>

            <button
              type="button"
              onClick={onLoadSampleData}
              className="flex justify-center items-center px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm text-sm font-medium text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-sky-500 transition-all duration-200"
            >
              <DatabaseIcon className="w-4 h-4 mr-2" />
              Load Sample Data
            </button>
          </div>

          <button
            type="button"
            onClick={onGenerateRandomData}
            className="flex justify-center items-center px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm text-sm font-medium text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-sky-500 transition-all duration-200"
          >
            <RefreshCwIcon className="w-4 h-4 mr-2" />
            Generate Random Data
          </button>
        </div>
      </div>

      {/* Clustering Controls */}
      <div className="space-y-4 mb-6 bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
        <h3 className="text-sm font-medium text-gray-800 dark:text-gray-200 mb-3">Clustering Settings</h3>

        <div>
          <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">X-Axis Feature</label>
          <div className="relative">
            <select
              value={xAxis}
              onChange={(e) => setXAxis(e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:outline-none focus:ring-sky-500 focus:border-sky-500 appearance-none dark:bg-gray-700 transition-colors"
            >
              {columns
                .filter((col) => col !== "CustomerID" && col !== "Genre")
                .map((col) => (
                  <option key={col} value={col}>
                    {col}
                  </option>
                ))}
            </select>
            <ChevronDownIcon className="absolute right-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400 pointer-events-none" />
          </div>
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">Y-Axis Feature</label>
          <div className="relative">
            <select
              value={yAxis}
              onChange={(e) => setYAxis(e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:outline-none focus:ring-sky-500 focus:border-sky-500 appearance-none dark:bg-gray-700 transition-colors"
            >
              {columns
                .filter((col) => col !== "CustomerID" && col !== "Genre")
                .map((col) => (
                  <option key={col} value={col}>
                    {col}
                  </option>
                ))}
            </select>
            <ChevronDownIcon className="absolute right-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400 pointer-events-none" />
          </div>
        </div>

        <div>
          <div className="flex justify-between items-center">
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300">Number of Clusters (K)</label>
            <span className="text-sm font-medium text-sky-600 dark:text-sky-400">{clusterCount}</span>
          </div>
          <input
            type="range"
            min="2"
            max="10"
            value={clusterCount}
            onChange={(e) => setClusterCount(Number.parseInt(e.target.value))}
            className="w-full h-2 bg-gray-200 dark:bg-gray-600 rounded-lg appearance-none cursor-pointer mt-2"
          />
          <div className="flex justify-between text-xs text-gray-500 dark:text-gray-400 mt-1">
            <span>2</span>
            <span>10</span>
          </div>
        </div>
      </div>

      {/* Run Clustering Button */}
      <button
        type="button"
        onClick={onRunClustering}
        disabled={isLoading}
        className="w-full flex justify-center items-center px-4 py-3 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-gradient-to-r from-sky-500 to-sky-600 hover:from-sky-600 hover:to-sky-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-sky-500 transition-all duration-300 transform hover:scale-105 disabled:opacity-70 disabled:cursor-not-allowed disabled:transform-none"
      >
        {isLoading ? (
          <>
            <svg
              className="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
              <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
              <path
                className="opacity-75"
                fill="currentColor"
                d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
              ></path>
            </svg>
            Processing...
          </>
        ) : (
          <>
            <PlayIcon className="w-5 h-5 mr-2" />
            Run K-Means Clustering
          </>
        )}
      </button>
    </div>
  )
}

export default DataEntryPanel

