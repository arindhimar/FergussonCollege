"use client"

import { useEffect, useRef } from "react"

const ScatterPlot = ({ data, clusters, xAxis, yAxis, clusterColors, currentDetailedStep }) => {
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
    const padding = 40
    const plotWidth = rect.width - padding * 2
    const plotHeight = rect.height - padding * 2

    // Find min and max values for axes
    const xValues = data.map((d) => Number.parseFloat(d[xAxis]))
    const yValues = data.map((d) => Number.parseFloat(d[yAxis]))

    const xMin = Math.min(...xValues)
    const xMax = Math.max(...xValues)
    const yMin = Math.min(...yValues)
    const yMax = Math.max(...yValues)

    // Add some margin to the ranges
    const xRange = (xMax - xMin) * 1.1
    const yRange = (yMax - yMin) * 1.1

    const xStart = xMin - xRange * 0.05
    const yStart = yMin - yRange * 0.05

    // Scale function to convert data values to canvas coordinates
    const scaleX = (value) => padding + (plotWidth * (Number.parseFloat(value) - xStart)) / xRange
    const scaleY = (value) => rect.height - padding - (plotHeight * (Number.parseFloat(value) - yStart)) / yRange

    // Draw grid
    ctx.beginPath()
    ctx.strokeStyle = "#eee"
    ctx.lineWidth = 0.5

    // Vertical grid lines
    for (let i = 0; i <= 5; i++) {
      const x = padding + (i / 5) * plotWidth
      ctx.moveTo(x, padding)
      ctx.lineTo(x, rect.height - padding)
    }

    // Horizontal grid lines
    for (let i = 0; i <= 5; i++) {
      const y = padding + (i / 5) * plotHeight
      ctx.moveTo(padding, y)
      ctx.lineTo(rect.width - padding, y)
    }

    ctx.stroke()

    // Draw axes
    ctx.beginPath()
    ctx.strokeStyle = "#ccc"
    ctx.lineWidth = 1

    // X-axis
    ctx.moveTo(padding, rect.height - padding)
    ctx.lineTo(rect.width - padding, rect.height - padding)

    // Y-axis
    ctx.moveTo(padding, padding)
    ctx.lineTo(padding, rect.height - padding)
    ctx.stroke()

    // Draw axis labels
    ctx.fillStyle = "#666"
    ctx.font = "12px Arial"
    ctx.textAlign = "center"

    // X-axis label
    ctx.fillText(xAxis, rect.width / 2, rect.height - 10)

    // Y-axis label
    ctx.save()
    ctx.translate(15, rect.height / 2)
    ctx.rotate(-Math.PI / 2)
    ctx.fillText(yAxis, 0, 0)
    ctx.restore()

    // Draw axis ticks and values
    ctx.textAlign = "center"

    // X-axis ticks
    const xStep = xRange / 5
    for (let i = 0; i <= 5; i++) {
      const value = xStart + i * xStep
      const x = scaleX(value)
      ctx.beginPath()
      ctx.moveTo(x, rect.height - padding)
      ctx.lineTo(x, rect.height - padding + 5)
      ctx.stroke()
      ctx.fillText(value.toFixed(0), x, rect.height - padding + 20)
    }

    // Y-axis ticks
    const yStep = yRange / 5
    ctx.textAlign = "right"
    for (let i = 0; i <= 5; i++) {
      const value = yStart + i * yStep
      const y = scaleY(value)
      ctx.beginPath()
      ctx.moveTo(padding, y)
      ctx.lineTo(padding - 5, y)
      ctx.stroke()
      ctx.fillText(value.toFixed(0), padding - 10, y + 4)
    }

    // Handle centroid movement visualization for recalculation steps
    if (currentDetailedStep && currentDetailedStep.type === "recalculate") {
      // Draw arrows from old to new centroids
      currentDetailedStep.oldCentroids.forEach((oldCentroid, i) => {
        const newCentroid = currentDetailedStep.newCentroids[i]

        const oldX = scaleX(oldCentroid.x)
        const oldY = scaleY(oldCentroid.y)
        const newX = scaleX(newCentroid.x)
        const newY = scaleY(newCentroid.y)

        // Draw line from old to new position
        ctx.beginPath()
        ctx.moveTo(oldX, oldY)
        ctx.lineTo(newX, newY)
        ctx.strokeStyle = clusterColors[i % clusterColors.length]
        ctx.lineWidth = 2
        ctx.setLineDash([3, 3]) // Dashed line
        ctx.stroke()
        ctx.setLineDash([]) // Reset to solid line

        // Draw arrow at the end
        const angle = Math.atan2(newY - oldY, newX - oldX)
        const arrowSize = 10

        ctx.beginPath()
        ctx.moveTo(newX, newY)
        ctx.lineTo(newX - arrowSize * Math.cos(angle - Math.PI / 6), newY - arrowSize * Math.sin(angle - Math.PI / 6))
        ctx.lineTo(newX - arrowSize * Math.cos(angle + Math.PI / 6), newY - arrowSize * Math.sin(angle + Math.PI / 6))
        ctx.closePath()
        ctx.fillStyle = clusterColors[i % clusterColors.length]
        ctx.fill()

        // Draw old centroid (faded)
        ctx.beginPath()
        ctx.arc(oldX, oldY, 8, 0, Math.PI * 2)
        ctx.fillStyle = clusterColors[i % clusterColors.length] + "40" // 25% opacity
        ctx.fill()
        ctx.strokeStyle = "#fff"
        ctx.lineWidth = 1
        ctx.stroke()

        // Label
        ctx.fillStyle = "#666"
        ctx.font = "10px Arial"
        ctx.textAlign = "center"
        ctx.fillText("Old C" + i, oldX, oldY - 12)
      })
    }

    // Draw data points
    data.forEach((point, index) => {
      const x = scaleX(point[xAxis])
      const y = scaleY(point[yAxis])

      // Determine if this point is being highlighted in the current step
      const isHighlighted =
        currentDetailedStep &&
        currentDetailedStep.highlightedPoint !== null &&
        currentDetailedStep.highlightedPoint === index

      // For assignment steps, draw lines to all centroids with distances
      if (isHighlighted && currentDetailedStep.type === "assign" && currentDetailedStep.distances) {
        currentDetailedStep.distances.forEach((distanceInfo, i) => {
          const centroidIndex = distanceInfo.centroidIndex
          const centroid = clusters[centroidIndex]
          const centroidX = scaleX(centroid[xAxis])
          const centroidY = scaleY(centroid[yAxis])

          // Draw line to centroid
          ctx.beginPath()
          ctx.moveTo(x, y)
          ctx.lineTo(centroidX, centroidY)

          // Style based on whether this is the closest centroid
          if (i === 0) {
            // Closest centroid - solid line
            ctx.strokeStyle = clusterColors[centroidIndex % clusterColors.length]
            ctx.lineWidth = 2
            ctx.setLineDash([])
          } else {
            // Other centroids - dashed, faded line
            ctx.strokeStyle = clusterColors[centroidIndex % clusterColors.length] + "40" // 25% opacity
            ctx.lineWidth = 1
            ctx.setLineDash([2, 2])
          }

          ctx.stroke()
          ctx.setLineDash([]) // Reset to solid line

          // Draw distance label
          const midX = (x + centroidX) / 2
          const midY = (y + centroidY) / 2

          ctx.fillStyle = i === 0 ? "#000" : "#666"
          ctx.font = i === 0 ? "bold 10px Arial" : "10px Arial"
          ctx.textAlign = "center"
          ctx.textBaseline = "middle"

          // Draw background for text
          const distanceText = distanceInfo.distance.toFixed(1)
          const textWidth = ctx.measureText(distanceText).width
          ctx.fillStyle = i === 0 ? "rgba(255, 255, 255, 0.8)" : "rgba(255, 255, 255, 0.6)"
          ctx.fillRect(midX - textWidth / 2 - 2, midY - 7, textWidth + 4, 14)

          // Draw text
          ctx.fillStyle = i === 0 ? "#000" : "#666"
          ctx.fillText(distanceText, midX, midY)
        })
      }
      // For normal points, just draw connection to their assigned cluster
      else if (point.cluster !== undefined && clusters && clusters.length > 0) {
        const centroidX = scaleX(clusters[point.cluster][xAxis])
        const centroidY = scaleY(clusters[point.cluster][yAxis])

        ctx.beginPath()
        ctx.moveTo(x, y)
        ctx.lineTo(centroidX, centroidY)
        ctx.strokeStyle = clusterColors[point.cluster % clusterColors.length] + "30" // 20% opacity
        ctx.lineWidth = 0.5
        ctx.stroke()
      }

      // Draw the point
      const pointRadius = isHighlighted ? 10 : 6
      ctx.beginPath()
      ctx.arc(x, y, pointRadius, 0, Math.PI * 2)

      if (point.cluster !== undefined) {
        ctx.fillStyle = clusterColors[point.cluster % clusterColors.length]
      } else {
        ctx.fillStyle = "#999"
      }

      // For highlighted points, add a glow effect
      if (isHighlighted) {
        ctx.shadowColor = "rgba(0, 0, 0, 0.5)"
        ctx.shadowBlur = 10
      }

      ctx.fill()
      ctx.shadowColor = "transparent"
      ctx.shadowBlur = 0
      ctx.strokeStyle = "#fff"
      ctx.lineWidth = 1.5
      ctx.stroke()

      // Add point ID for highlighted point
      if (isHighlighted) {
        ctx.fillStyle = "#fff"
        ctx.font = "bold 10px Arial"
        ctx.textAlign = "center"
        ctx.textBaseline = "middle"
        ctx.fillText((index + 1).toString(), x, y)

        // Add a pulsing circle around the highlighted point
        ctx.beginPath()
        const pulseSize = 15 + Math.sin(Date.now() / 200) * 3
        ctx.arc(x, y, pulseSize, 0, Math.PI * 2)
        ctx.strokeStyle = "rgba(255, 255, 0, 0.5)"
        ctx.lineWidth = 2
        ctx.stroke()
      }
    })

    // Draw cluster centroids
    if (clusters && clusters.length > 0) {
      clusters.forEach((centroid, i) => {
        const x = scaleX(centroid[xAxis])
        const y = scaleY(centroid[yAxis])

        // Draw centroid
        ctx.beginPath()
        ctx.arc(x, y, 10, 0, Math.PI * 2)
        ctx.fillStyle = clusterColors[i % clusterColors.length]
        ctx.fill()
        ctx.strokeStyle = "#fff"
        ctx.lineWidth = 2
        ctx.stroke()

        // Draw centroid label
        ctx.fillStyle = "#fff"
        ctx.font = "bold 12px Arial"
        ctx.textAlign = "center"
        ctx.fillText(`C${i}`, x, y + 4)

        // Draw pulsing effect for centroids
        const pulseSize = 16 + Math.sin(Date.now() / 300) * 3
        ctx.beginPath()
        ctx.arc(x, y, pulseSize, 0, Math.PI * 2)
        ctx.strokeStyle = clusterColors[i % clusterColors.length] + "40" // 25% opacity
        ctx.lineWidth = 2
        ctx.stroke()
      })
    }
  }, [data, clusters, xAxis, yAxis, clusterColors, currentDetailedStep])

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

      {/* Point info overlay for highlighted point */}
      {currentDetailedStep && currentDetailedStep.highlightedPoint !== null && (
        <div className="absolute top-2 left-2 bg-white dark:bg-gray-800 p-2 rounded-md shadow-md border border-gray-200 dark:border-gray-700 text-xs">
          <div className="font-medium">Point {currentDetailedStep.highlightedPoint + 1}</div>
          {currentDetailedStep.points && currentDetailedStep.highlightedPoint < currentDetailedStep.points.length && (
            <div>
              {xAxis}: {currentDetailedStep.points[currentDetailedStep.highlightedPoint].x.toFixed(1)},{yAxis}:{" "}
              {currentDetailedStep.points[currentDetailedStep.highlightedPoint].y.toFixed(1)}
            </div>
          )}
        </div>
      )}
    </div>
  )
}

export default ScatterPlot

