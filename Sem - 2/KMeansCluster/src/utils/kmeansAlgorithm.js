// K-means clustering implementation with detailed step tracking
export const runKMeansClustering = (data, k, xAxis, yAxis) => {
    // Make a deep copy of the data to avoid modifying the original
    const dataPoints = JSON.parse(JSON.stringify(data))
  
    // Extract the features we want to cluster on
    const points = dataPoints.map((point, index) => ({
      x: Number.parseFloat(point[xAxis]),
      y: Number.parseFloat(point[yAxis]),
      original: point,
      id: index, // Add an ID to track points
    }))
  
    // Initialize centroids randomly
    let centroids = initializeCentroids(points, k)
  
    // Store iterations for animation
    const iterations = []
    const detailedSteps = []
  
    // Add initial state with random centroids
    detailedSteps.push({
      type: "initial",
      message: "Initial random centroids placed",
      centroids: centroids.map((centroid, i) => ({
        x: centroid.x,
        y: centroid.y,
        cluster: i,
      })),
      points: points.map((point) => ({
        ...point.original,
        x: point.x,
        y: point.y,
        id: point.id,
      })),
      highlightedPoint: null,
      distances: null,
    })
  
    // Maximum iterations to prevent infinite loops
    const maxIterations = 20
    let iteration = 0
    let shouldContinue = true
  
    while (shouldContinue && iteration < maxIterations) {
      // Store current centroids for this iteration
      const currentCentroids = JSON.parse(JSON.stringify(centroids))
  
      // For each point, calculate distance to each centroid and assign to closest
      for (let pointIndex = 0; pointIndex < points.length; pointIndex++) {
        const point = points[pointIndex]
  
        // Calculate distances to each centroid
        const distances = centroids.map((centroid, centroidIndex) => ({
          centroidIndex,
          distance: euclideanDistance(point, centroid),
        }))
  
        // Sort distances to find closest
        distances.sort((a, b) => a.distance - b.distance)
  
        // Assign point to closest centroid
        const closestCentroid = distances[0].centroidIndex
        point.cluster = closestCentroid
  
        // Add detailed step for this point assignment
        detailedSteps.push({
          type: "assign",
          iteration,
          pointIndex,
          message: `Assigning point ${pointIndex + 1} to nearest cluster`,
          centroids: currentCentroids.map((centroid, i) => ({
            x: centroid.x,
            y: centroid.y,
            cluster: i,
          })),
          points: points.map((p) => ({
            ...p.original,
            x: p.x,
            y: p.y,
            id: p.id,
            cluster: p.cluster,
          })),
          highlightedPoint: pointIndex,
          distances: distances.map((d) => ({
            centroidIndex: d.centroidIndex,
            distance: d.distance,
          })),
        })
      }
  
      // Store iteration state after all points are assigned
      iterations.push({
        centroids: currentCentroids.map((centroid, i) => {
          const c = {}
          c[xAxis] = centroid.x
          c[yAxis] = centroid.y
          return c
        }),
        data: points.map((point) => ({
          ...point.original,
          cluster: point.cluster,
        })),
      })
  
      // Add detailed step for completed assignment phase
      detailedSteps.push({
        type: "assigned_all",
        iteration,
        message: `All points assigned to clusters for iteration ${iteration + 1}`,
        centroids: currentCentroids.map((centroid, i) => ({
          x: centroid.x,
          y: centroid.y,
          cluster: i,
        })),
        points: points.map((p) => ({
          ...p.original,
          x: p.x,
          y: p.y,
          id: p.id,
          cluster: p.cluster,
        })),
        highlightedPoint: null,
        distances: null,
      })
  
      // Calculate new centroids
      const newCentroids = calculateNewCentroids(points, k, centroids)
  
      // Add detailed step for centroid recalculation
      detailedSteps.push({
        type: "recalculate",
        iteration,
        message: `Recalculating centroids for iteration ${iteration + 1}`,
        oldCentroids: currentCentroids.map((centroid, i) => ({
          x: centroid.x,
          y: centroid.y,
          cluster: i,
        })),
        newCentroids: newCentroids.map((centroid, i) => ({
          x: centroid.x,
          y: centroid.y,
          cluster: i,
        })),
        points: points.map((p) => ({
          ...p.original,
          x: p.x,
          y: p.y,
          id: p.id,
          cluster: p.cluster,
        })),
        highlightedPoint: null,
        distances: null,
      })
  
      // Check if centroids have converged
      shouldContinue = !centroidsConverged(centroids, newCentroids)
  
      // Update centroids
      centroids = newCentroids
      iteration++
    }
  
    // Final assignment
    assignPointsToClusters(points, centroids)
  
    // Add final state to iterations if not already added
    if (iteration === maxIterations) {
      iterations.push({
        centroids: centroids.map((centroid, i) => {
          const c = {}
          c[xAxis] = centroid.x
          c[yAxis] = centroid.y
          return c
        }),
        data: points.map((point) => ({
          ...point.original,
          cluster: point.cluster,
        })),
      })
  
      // Add final detailed step
      detailedSteps.push({
        type: "final",
        message: "Algorithm complete - final clusters assigned",
        centroids: centroids.map((centroid, i) => ({
          x: centroid.x,
          y: centroid.y,
          cluster: i,
        })),
        points: points.map((p) => ({
          ...p.original,
          x: p.x,
          y: p.y,
          id: p.id,
          cluster: p.cluster,
        })),
        highlightedPoint: null,
        distances: null,
      })
    }
  
    // Return clustered data, centroids, iterations, and detailed steps
    return {
      clusteredData: points.map((point) => ({
        ...point.original,
        cluster: point.cluster,
      })),
      clusters: centroids.map((centroid, i) => {
        const c = {}
        c[xAxis] = centroid.x
        c[yAxis] = centroid.y
        return c
      }),
      iterations,
      detailedSteps,
      xAxis,
      yAxis,
    }
  }
  
  // Initialize centroids randomly
  const initializeCentroids = (points, k) => {
    // Find min and max values for each dimension
    const minX = Math.min(...points.map((p) => p.x))
    const maxX = Math.max(...points.map((p) => p.x))
    const minY = Math.min(...points.map((p) => p.y))
    const maxY = Math.max(...points.map((p) => p.y))
  
    // Generate k random centroids within the data range
    const centroids = []
    for (let i = 0; i < k; i++) {
      centroids.push({
        x: minX + Math.random() * (maxX - minX),
        y: minY + Math.random() * (maxY - minY),
      })
    }
  
    return centroids
  }
  
  // Assign points to the nearest centroid
  const assignPointsToClusters = (points, centroids) => {
    points.forEach((point) => {
      let minDistance = Number.POSITIVE_INFINITY
      let clusterIndex = 0
  
      centroids.forEach((centroid, i) => {
        const distance = euclideanDistance(point, centroid)
        if (distance < minDistance) {
          minDistance = distance
          clusterIndex = i
        }
      })
  
      point.cluster = clusterIndex
    })
  
    return points
  }
  
  // Calculate new centroids based on the mean of points in each cluster
  const calculateNewCentroids = (points, k, centroids) => {
    const newCentroids = []
  
    for (let i = 0; i < k; i++) {
      const clusterPoints = points.filter((point) => point.cluster === i)
  
      if (clusterPoints.length === 0) {
        // If no points in cluster, keep the old centroid
        newCentroids.push(centroids[i])
        continue
      }
  
      const sumX = clusterPoints.reduce((sum, point) => sum + point.x, 0)
      const sumY = clusterPoints.reduce((sum, point) => sum + point.y, 0)
  
      newCentroids.push({
        x: sumX / clusterPoints.length,
        y: sumY / clusterPoints.length,
      })
    }
  
    return newCentroids
  }
  
  // Check if centroids have converged
  const centroidsConverged = (oldCentroids, newCentroids) => {
    const threshold = 0.001
  
    for (let i = 0; i < oldCentroids.length; i++) {
      const distance = euclideanDistance(oldCentroids[i], newCentroids[i])
      if (distance > threshold) {
        return false
      }
    }
  
    return true
  }
  
  // Calculate Euclidean distance between two points
  const euclideanDistance = (point1, point2) => {
    return Math.sqrt(Math.pow(point1.x - point2.x, 2) + Math.pow(point1.y - point2.y, 2))
  }
  
  