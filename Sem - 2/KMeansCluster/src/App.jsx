"use client"

import { useState, useEffect, useRef } from "react"
import DataEntryPanel from "./components/DataEntryPanel"
import DataVisualizationPanel from "./components/DataVisualizationPanel"
import KMeansExplanation from "./components/KMeansExplanation"
import FloatingControls from "./components/FloatingControls"
import AppTabs from "./components/AppTabs"
import AboutSection from "./components/AboutSection"
import { runKMeansClustering } from "./utils/kmeansAlgorithm"
import { generateRandomData } from "./utils/dataUtils"

function App() {
  const [data, setData] = useState([])
  const [clusters, setClusters] = useState([])
  const [clusterCount, setClusterCount] = useState(3)
  const [xAxis, setXAxis] = useState("Annual Income (k$)")
  const [yAxis, setYAxis] = useState("Spending Score (1-100)")
  const [isLoading, setIsLoading] = useState(false)
  const [visualizationType, setVisualizationType] = useState("scatter")
  const [animationStep, setAnimationStep] = useState(0)
  const [totalSteps, setTotalSteps] = useState(0)
  const [isAnimationPlaying, setIsAnimationPlaying] = useState(false)
  const [iterations, setIterations] = useState([])
  const [detailedSteps, setDetailedSteps] = useState([])
  const [currentDetailedStep, setCurrentDetailedStep] = useState(null)
  const [animationSpeed, setAnimationSpeed] = useState(800) // ms between steps
  const animationRef = useRef(null)

  const columns = data.length > 0 ? Object.keys(data[0]).filter((col) => col !== "cluster") : []

  const handleAddDataPoint = (newDataPoint) => {
    setData([...data, { ...newDataPoint, CustomerID: (data.length + 1).toString().padStart(4, "0") }])
  }

  const handleFileUpload = async (file) => {
    setIsLoading(true)
    try {
      const text = await file.text()
      const rows = text.split("\n")
      const headers = rows[0].split(",").map((h) => h.trim())

      const parsedData = rows
        .slice(1)
        .filter((row) => row.trim())
        .map((row, index) => {
          const values = row.split(",").map((v) => v.trim())
          const rowData = {}

          headers.forEach((header, i) => {
            rowData[header] = values[i] || ""
          })

          // Add CustomerID if not present
          if (!rowData.CustomerID) {
            rowData.CustomerID = (index + 1).toString().padStart(4, "0")
          }

          return rowData
        })

      setData(parsedData)
    } catch (error) {
      console.error("Error parsing CSV:", error)
      alert("Error parsing CSV file. Please check the format.")
    } finally {
      setIsLoading(false)
    }
  }

  const handleLoadSampleData = async () => {
    setIsLoading(true)
    try {
      const response = await fetch(
        "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/Mall_Customers%20%281%29-3FokRdcjcZrbB4oNKESih1cR3oNkbQ.csv",
      )
      const text = await response.text()
      const rows = text.split("\n")
      const headers = rows[0].split(",").map((h) => h.trim())

      const parsedData = rows
        .slice(1)
        .filter((row) => row.trim())
        .map((row) => {
          const values = row.split(",").map((v) => v.trim())
          const rowData = {}

          headers.forEach((header, i) => {
            rowData[header] = values[i] || ""
          })

          return rowData
        })

      setData(parsedData)
    } catch (error) {
      console.error("Error loading sample data:", error)
      alert("Error loading sample data. Please try again.")
    } finally {
      setIsLoading(false)
    }
  }

  const handleGenerateRandomData = () => {
    const randomData = generateRandomData(20) // Reduced to 20 for clearer visualization
    setData(randomData)
  }

  const runClustering = () => {
    if (data.length === 0) {
      alert("Please add data before running clustering")
      return
    }

    setIsLoading(true)
    setAnimationStep(0)
    setIsAnimationPlaying(false)

    // Clear any existing animation
    if (animationRef.current) {
      clearTimeout(animationRef.current)
    }

    try {
      const result = runKMeansClustering(data, clusterCount, xAxis, yAxis)

      // Set initial state
      setIterations(result.iterations)
      setDetailedSteps(result.detailedSteps)
      setTotalSteps(result.detailedSteps.length)

      if (result.detailedSteps.length > 0) {
        const initialStep = result.detailedSteps[0]
        setCurrentDetailedStep(initialStep)

        // Set initial data state
        const initialData = initialStep.points.map((p) => {
          const point = { ...p }
          point[xAxis] = p.x
          point[yAxis] = p.y
          return point
        })

        const initialCentroids = initialStep.centroids.map((c) => {
          const centroid = {}
          centroid[xAxis] = c.x
          centroid[yAxis] = c.y
          return centroid
        })

        setData(initialData)
        setClusters(initialCentroids)
      }

      // Auto-start animation if there are steps
      if (result.detailedSteps.length > 1) {
        setIsAnimationPlaying(true)
      }
    } catch (error) {
      console.error("Error running clustering:", error)
      alert("Error running clustering. Please check your data.")
    } finally {
      setIsLoading(false)
    }
  }

  const handleStepChange = (step) => {
    if (step >= 0 && step < totalSteps) {
      setAnimationStep(step)

      const currentStep = detailedSteps[step]
      setCurrentDetailedStep(currentStep)

      // Update data and clusters based on the current step
      if (currentStep.type === "recalculate") {
        // For recalculation steps, show both old and new centroids
        const updatedData = currentStep.points.map((p) => {
          const point = { ...p }
          point[xAxis] = p.x
          point[yAxis] = p.y
          return point
        })

        const updatedCentroids = currentStep.newCentroids.map((c) => {
          const centroid = {}
          centroid[xAxis] = c.x
          centroid[yAxis] = c.y
          return centroid
        })

        setData(updatedData)
        setClusters(updatedCentroids)
      } else {
        // For other steps, just show current state
        const updatedData = currentStep.points.map((p) => {
          const point = { ...p }
          point[xAxis] = p.x
          point[yAxis] = p.y
          return point
        })

        const updatedCentroids = currentStep.centroids.map((c) => {
          const centroid = {}
          centroid[xAxis] = c.x
          centroid[yAxis] = c.y
          return centroid
        })

        setData(updatedData)
        setClusters(updatedCentroids)
      }
    }
  }

  const toggleAnimation = () => {
    setIsAnimationPlaying(!isAnimationPlaying)
  }

  const resetAnimation = () => {
    setAnimationStep(0)
    handleStepChange(0)
    setIsAnimationPlaying(false)
  }

  const skipToEnd = () => {
    if (totalSteps > 0) {
      setAnimationStep(totalSteps - 1)
      handleStepChange(totalSteps - 1)
      setIsAnimationPlaying(false)
    }
  }

  // Handle animation playback
  useEffect(() => {
    if (isAnimationPlaying && animationStep < totalSteps - 1) {
      animationRef.current = setTimeout(() => {
        const nextStep = animationStep + 1
        setAnimationStep(nextStep)
        handleStepChange(nextStep)
      }, animationSpeed)
    } else if (animationStep >= totalSteps - 1) {
      setIsAnimationPlaying(false)
    }

    return () => {
      if (animationRef.current) {
        clearTimeout(animationRef.current)
      }
    }
  }, [isAnimationPlaying, animationStep, totalSteps, animationSpeed])

  // Show floating controls only when animation is available
  const showFloatingControls =
    totalSteps > 0 && (visualizationType === "scatter" || visualizationType === "bar" || visualizationType === "pie")

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800 text-gray-800 dark:text-gray-200">
      <header className="bg-white dark:bg-gray-800 shadow-md">
        <div className="max-w-7xl mx-auto py-4 px-4 sm:px-6 lg:px-8">
          <h1 className="text-3xl font-bold text-sky-600 dark:text-sky-400">
            Customer Segmentation with K-Means Clustering
          </h1>
        </div>
      </header>

      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <AppTabs>
          <AppTabs.TabPanel tabId="visualization">
            <div className="flex flex-col lg:flex-row gap-6">
              {/* Left Panel */}
              <div className="lg:w-1/3">
                <DataEntryPanel
                  onAddDataPoint={handleAddDataPoint}
                  onFileUpload={handleFileUpload}
                  onLoadSampleData={handleLoadSampleData}
                  onGenerateRandomData={handleGenerateRandomData}
                  columns={columns}
                  xAxis={xAxis}
                  yAxis={yAxis}
                  setXAxis={setXAxis}
                  setYAxis={setYAxis}
                  clusterCount={clusterCount}
                  setClusterCount={setClusterCount}
                  onRunClustering={runClustering}
                  isLoading={isLoading}
                />
              </div>

              {/* Right Panel */}
              <div className="lg:w-2/3">
                <DataVisualizationPanel
                  data={data}
                  clusters={clusters}
                  xAxis={xAxis}
                  yAxis={yAxis}
                  visualizationType={visualizationType}
                  setVisualizationType={setVisualizationType}
                  animationStep={animationStep}
                  totalSteps={totalSteps}
                  onStepChange={handleStepChange}
                  isAnimationPlaying={isAnimationPlaying}
                  toggleAnimation={toggleAnimation}
                  resetAnimation={resetAnimation}
                  iterations={iterations}
                  currentDetailedStep={currentDetailedStep}
                  animationSpeed={animationSpeed}
                  setAnimationSpeed={setAnimationSpeed}
                />
              </div>
            </div>
          </AppTabs.TabPanel>

          <AppTabs.TabPanel tabId="explanation">
            <KMeansExplanation />
          </AppTabs.TabPanel>

          <AppTabs.TabPanel tabId="about">
            <AboutSection />
          </AppTabs.TabPanel>
        </AppTabs>

        {/* Floating Animation Controls */}
        <FloatingControls
          currentStep={animationStep}
          totalSteps={totalSteps}
          onStepChange={handleStepChange}
          isPlaying={isAnimationPlaying}
          togglePlay={toggleAnimation}
          resetAnimation={resetAnimation}
          skipToEnd={skipToEnd}
          animationSpeed={animationSpeed}
          setAnimationSpeed={setAnimationSpeed}
          isVisible={showFloatingControls}
        />
      </main>
    </div>
  )
}

export default App

