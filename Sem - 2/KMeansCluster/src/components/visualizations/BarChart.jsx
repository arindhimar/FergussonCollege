"use client"

import { useEffect, useRef } from "react"

const BarChart = ({ data, xAxis, clusterColors }) => {
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

    // Set padding
    const padding = { top: 40, right: 40, bottom: 60, left: 60 }
    const plotWidth = rect.width - padding.left - padding.right
    const plotHeight = rect.height - padding.top - padding.bottom

    // Group data by clusters
    const clusterGroups = {}
    data.forEach((point) => {
      const cluster = point.cluster !== undefined ? point.cluster : "unclustered"
      if (!clusterGroups[cluster]) {
        clusterGroups[cluster] = []
      }
      clusterGroups[cluster].push(point)
    })

    // Calculate average value for each cluster
    const clusterAverages = {}
    Object.entries(clusterGroups).forEach(([cluster, points]) => {
      const sum = points.reduce((acc, point) => acc + Number.parseFloat(point[xAxis]), 0)
      clusterAverages[cluster] = sum / points.length
    })

    // Sort clusters by their average values
    const sortedClusters = Object.keys(clusterAverages).sort((a, b) => {
      if (a === "unclustered") return -1
      if (b === "unclustered") return 1
      return clusterAverages[a] - clusterAverages[b]
    })

    // Find max value for scaling
    const maxAverage = Math.max(...Object.values(clusterAverages))

    // Calculate bar width and spacing
    const barCount = sortedClusters.length
    const barWidth = plotWidth / (barCount * 2)
    const barSpacing = barWidth

    // Draw axes
    ctx.beginPath()
    ctx.strokeStyle = "#ccc"
    ctx.lineWidth = 1

    // X-axis
    ctx.moveTo(padding.left, rect.height - padding.bottom)
    ctx.lineTo(rect.width - padding.right, rect.height - padding.bottom)

    // Y-axis
    ctx.moveTo(padding.left, padding.top)
    ctx.lineTo(padding.left, rect.height - padding.bottom)
    ctx.stroke()

    // Draw axis labels
    ctx.fillStyle = "#666"
    ctx.font = "12px Arial"
    ctx.textAlign = "center"

    // X-axis label
    ctx.fillText("Clusters", rect.width / 2, rect.height - 10)

    // Y-axis label
    ctx.save()
    ctx.translate(15, rect.height / 2)
    ctx.rotate(-Math.PI / 2)
    ctx.fillText(`Average ${xAxis}`, 0, 0)
    ctx.restore()

    // Draw Y-axis ticks and values
    const yStep = maxAverage / 5
    ctx.textAlign = "right"
    for (let i = 0; i <= 5; i++) {
      const value = i * yStep
      const y = rect.height - padding.bottom - (plotHeight * value) / maxAverage
      ctx.beginPath()
      ctx.moveTo(padding.left, y)
      ctx.lineTo(padding.left - 5, y)
      ctx.stroke()
      ctx.fillText(value.toFixed(0), padding.left - 10, y + 4)
    }

    // Draw bars
    sortedClusters.forEach((cluster, i) => {
      const x = padding.left + i * (barWidth + barSpacing) + barSpacing
      const value = clusterAverages[cluster]
      const barHeight = (plotHeight * value) / maxAverage
      const y = rect.height - padding.bottom - barHeight

      // Draw bar
      ctx.beginPath()
      ctx.rect(x, y, barWidth, barHeight)

      if (cluster === "unclustered") {
        ctx.fillStyle = "#999"
      } else {
        ctx.fillStyle = clusterColors[Number.parseInt(cluster) % clusterColors.length]
      }

      ctx.fill()
      ctx.strokeStyle = "#fff"
      ctx.lineWidth = 1
      ctx.stroke()

      // Draw cluster label
      ctx.fillStyle = "#666"
      ctx.font = "12px Arial"
      ctx.textAlign = "center"
      ctx.fillText(
        cluster === "unclustered" ? "Unclustered" : `Cluster ${cluster}`,
        x + barWidth / 2,
        rect.height - padding.bottom + 20,
      )

      // Draw value on top of bar
      ctx.fillStyle = "#333"
      ctx.textAlign = "center"
      ctx.fillText(value.toFixed(1), x + barWidth / 2, y - 10)
    })
  }, [data, xAxis, clusterColors])

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

export default BarChart

