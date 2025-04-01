"use client"

import { useState } from "react"
import { ChevronDown, ChevronRight } from "lucide-react"

const ClusterStats = ({ data, xAxis, yAxis, clusterColors }) => {
  const [expandedClusters, setExpandedClusters] = useState({})

  // Group data by clusters
  const clusterGroups = {}
  data.forEach((point) => {
    const cluster = point.cluster !== undefined ? point.cluster : "unclustered"
    if (!clusterGroups[cluster]) {
      clusterGroups[cluster] = []
    }
    clusterGroups[cluster].push(point)
  })

  // Calculate statistics for each cluster
  const clusterStats = {}
  Object.entries(clusterGroups).forEach(([cluster, points]) => {
    // Skip unclustered points
    if (cluster === "unclustered") return

    // Calculate basic statistics
    const xValues = points.map((p) => Number(p[xAxis]))
    const yValues = points.map((p) => Number(p[yAxis]))

    const xMean = xValues.reduce((sum, val) => sum + val, 0) / points.length
    const yMean = yValues.reduce((sum, val) => sum + val, 0) / points.length

    const xStdDev = Math.sqrt(xValues.reduce((sum, val) => sum + Math.pow(val - xMean, 2), 0) / points.length)
    const yStdDev = Math.sqrt(yValues.reduce((sum, val) => sum + Math.pow(val - yMean, 2), 0) / points.length)

    // Calculate min, max values
    const xMin = Math.min(...xValues)
    const xMax = Math.max(...xValues)
    const yMin = Math.min(...yValues)
    const yMax = Math.max(...yValues)

    clusterStats[cluster] = {
      count: points.length,
      xMean: xMean.toFixed(2),
      yMean: yMean.toFixed(2),
      xStdDev: xStdDev.toFixed(2),
      yStdDev: yStdDev.toFixed(2),
      xMin: xMin.toFixed(2),
      xMax: xMax.toFixed(2),
      yMin: yMin.toFixed(2),
      yMax: yMax.toFixed(2),
    }
  })

  const toggleCluster = (cluster) => {
    setExpandedClusters((prev) => ({
      ...prev,
      [cluster]: !prev[cluster],
    }))
  }

  return (
    <div className="mt-3 bg-gray-50 dark:bg-gray-700 p-4 rounded-lg animate-fadeIn">
      <h3 className="text-sm font-medium text-gray-800 dark:text-gray-200 mb-3">Cluster Statistics</h3>

      <div className="space-y-3">
        {Object.keys(clusterStats)
          .sort((a, b) => Number(a) - Number(b))
          .map((cluster) => (
            <div key={cluster} className="border border-gray-200 dark:border-gray-600 rounded-lg overflow-hidden">
              <div
                className="flex items-center justify-between p-3 cursor-pointer hover:bg-gray-100 dark:hover:bg-gray-600"
                onClick={() => toggleCluster(cluster)}
                style={{
                  borderLeft: `4px solid ${clusterColors[Number(cluster) % clusterColors.length]}`,
                }}
              >
                <div className="flex items-center">
                  {expandedClusters[cluster] ? (
                    <ChevronDown className="w-4 h-4 mr-2 text-gray-500 dark:text-gray-400" />
                  ) : (
                    <ChevronRight className="w-4 h-4 mr-2 text-gray-500 dark:text-gray-400" />
                  )}
                  <span className="font-medium">Cluster {cluster}</span>
                  <span className="ml-2 text-sm text-gray-500 dark:text-gray-400">
                    ({clusterStats[cluster].count} points)
                  </span>
                </div>
                <div className="text-sm">
                  {xAxis}: {clusterStats[cluster].xMean} | {yAxis}: {clusterStats[cluster].yMean}
                </div>
              </div>

              {expandedClusters[cluster] && (
                <div className="p-3 bg-white dark:bg-gray-800 border-t border-gray-200 dark:border-gray-600">
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                      <h4 className="text-sm font-medium mb-2">{xAxis} Statistics</h4>
                      <table className="w-full text-sm">
                        <tbody>
                          <tr>
                            <td className="py-1 text-gray-600 dark:text-gray-400">Mean:</td>
                            <td className="py-1 font-medium text-right">{clusterStats[cluster].xMean}</td>
                          </tr>
                          <tr>
                            <td className="py-1 text-gray-600 dark:text-gray-400">Std Dev:</td>
                            <td className="py-1 font-medium text-right">{clusterStats[cluster].xStdDev}</td>
                          </tr>
                          <tr>
                            <td className="py-1 text-gray-600 dark:text-gray-400">Min:</td>
                            <td className="py-1 font-medium text-right">{clusterStats[cluster].xMin}</td>
                          </tr>
                          <tr>
                            <td className="py-1 text-gray-600 dark:text-gray-400">Max:</td>
                            <td className="py-1 font-medium text-right">{clusterStats[cluster].xMax}</td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                    <div>
                      <h4 className="text-sm font-medium mb-2">{yAxis} Statistics</h4>
                      <table className="w-full text-sm">
                        <tbody>
                          <tr>
                            <td className="py-1 text-gray-600 dark:text-gray-400">Mean:</td>
                            <td className="py-1 font-medium text-right">{clusterStats[cluster].yMean}</td>
                          </tr>
                          <tr>
                            <td className="py-1 text-gray-600 dark:text-gray-400">Std Dev:</td>
                            <td className="py-1 font-medium text-right">{clusterStats[cluster].yStdDev}</td>
                          </tr>
                          <tr>
                            <td className="py-1 text-gray-600 dark:text-gray-400">Min:</td>
                            <td className="py-1 font-medium text-right">{clusterStats[cluster].yMin}</td>
                          </tr>
                          <tr>
                            <td className="py-1 text-gray-600 dark:text-gray-400">Max:</td>
                            <td className="py-1 font-medium text-right">{clusterStats[cluster].yMax}</td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
              )}
            </div>
          ))}
      </div>
    </div>
  )
}

export default ClusterStats

