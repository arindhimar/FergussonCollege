"use client"

import { useEffect, useRef } from "react"

const PieChart = ({ data, clusterColors }) => {
  const canvasRef = useRef(null)

  useEffect(() => {
    if (!data || data.length === 0) return

    const canvas = canvasRef.current
    const ctx = canvas.getContext("2d")
    const dpr = window.devicePixelRatio || 1

    // Set canvas dimensions accounting for device pixel ratio
    const rect = canvas.getBoundingClientRect()
    canvas.width = rect.width * dpr
    canvas.height = rect.height * dpr
    ctx.scale(dpr, dpr)

    // Clear canvas
    ctx.clearRect(0, 0, rect.width, rect.height)

    // Group data by clusters
    const clusterGroups = {}
    data.forEach((point) => {
      const cluster = point.cluster !== undefined ? point.cluster : "unclustered"
      if (!clusterGroups[cluster]) {
        clusterGroups[cluster] = []
      }
      clusterGroups[cluster].push(point)
    })

    // Calculate cluster sizes
    const clusterSizes = {}
    Object.entries(clusterGroups).forEach(([cluster, points]) => {
      clusterSizes[cluster] = points.length
    })

    // Sort clusters by size (descending)
    const sortedClusters = Object.keys(clusterSizes).sort((a, b) => {
      if (a === "unclustered") return 1
      if (b === "unclustered") return -1
      return clusterSizes[b] - clusterSizes[a]
    })

    // Calculate total points
    const totalPoints = data.length

    // Draw pie chart
    const centerX = rect.width / 2
    const centerY = rect.height / 2
    const radius = Math.min(centerX, centerY) * 0.8

    let startAngle = 0
    sortedClusters.forEach((cluster) => {
      const percentage = clusterSizes[cluster] / totalPoints
      const endAngle = startAngle + percentage * 2 * Math.PI

      // Draw pie slice
      ctx.beginPath()
      ctx.moveTo(centerX, centerY)
      ctx.arc(centerX, centerY, radius, startAngle, endAngle)
      ctx.closePath()

      if (cluster === "unclustered") {
        ctx.fillStyle = "#999"
      } else {
        ctx.fillStyle = clusterColors[Number.parseInt(cluster) % clusterColors.length]
      }

      ctx.fill()
      ctx.strokeStyle = "#fff"
      ctx.lineWidth = 2
      ctx.stroke()

      // Draw label
      const labelRadius = radius * 0.7
      const labelAngle = startAngle + (endAngle - startAngle) / 2
      const labelX = centerX + Math.cos(labelAngle) * labelRadius
      const labelY = centerY + Math.sin(labelAngle) * labelRadius

      ctx.fillStyle = "#fff"
      ctx.font = "bold 14px Arial"
      ctx.textAlign = "center"
      ctx.textBaseline = "middle"

      if (percentage > 0.05) {
        // Only draw label if slice is big enough
        ctx.fillText(cluster === "unclustered" ? "?" : cluster, labelX, labelY)
      }

      // Draw percentage
      const percentageRadius = radius * 1.1
      const percentageX = centerX + Math.cos(labelAngle) * percentageRadius
      const percentageY = centerY + Math.sin(labelAngle) * percentageRadius

      ctx.fillStyle = "#666"
      ctx.font = "12px Arial"

      if (percentage > 0.03) {
        // Only draw percentage if slice is big enough
        ctx.fillText(`${(percentage * 100).toFixed(1)}%`, percentageX, percentageY)
      }

      startAngle = endAngle
    })

    // Draw center circle (donut style)
    ctx.beginPath()
    ctx.arc(centerX, centerY, radius * 0.4, 0, 2 * Math.PI)
    ctx.fillStyle = "#fff"
    ctx.fill()
    ctx.strokeStyle = "#eee"
    ctx.lineWidth = 1
    ctx.stroke()

    // Draw title in center
    ctx.fillStyle = "#333"
    ctx.font = "bold 16px Arial"
    ctx.textAlign = "center"
    ctx.textBaseline = "middle"
    ctx.fillText("Cluster Distribution", centerX, centerY - 10)

    // Draw total count
    ctx.fillStyle = "#666"
    ctx.font = "14px Arial"
    ctx.fillText(`${totalPoints} data points`, centerX, centerY + 15)
  }, [data, clusterColors])

  return (
    <div className="w-full h-full relative">
      {(!data || data.length === 0) && (
        <div className="absolute inset-0 flex items-center justify-center text-gray-500 dark:text-gray-400">
          No data available. Please add data points or load a dataset.
        </div>
      )}
      <canvas
        ref={canvasRef}
        className="w-full h-full"
        style={{ display: !data || data.length === 0 ? "none" : "block" }}
      />
    </div>
  )
}

export default PieChart

