const StepExplanation = ({ currentDetailedStep, animationStep, totalSteps }) => {
    if (!currentDetailedStep) {
      return (
        <div className="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 p-4 rounded-lg mb-4 shadow-sm animate-fadeIn">
          <h3 className="text-sm font-semibold text-gray-800 dark:text-gray-200 mb-2">K-Means Algorithm Explanation</h3>
          <p className="text-sm text-gray-600 dark:text-gray-400">Run clustering to see the algorithm in action.</p>
        </div>
      )
    }
  
    // Generate explanation based on the current step type
    const getStepExplanation = () => {
      const { type, message, highlightedPoint, distances } = currentDetailedStep
  
      switch (type) {
        case "initial":
          return (
            <div>
              <p className="text-sm text-gray-600 dark:text-gray-400 mb-2">{message}</p>
              <p className="text-sm text-gray-600 dark:text-gray-400">
                The algorithm starts by randomly placing K centroids in the data space. These will serve as the initial
                centers for our clusters.
              </p>
            </div>
          )
  
        case "assign":
          return (
            <div>
              <p className="text-sm text-gray-600 dark:text-gray-400 mb-2">{message}</p>
              {distances && (
                <div className="mt-2 text-xs">
                  <p className="font-medium text-gray-700 dark:text-gray-300">Distance calculations:</p>
                  <div className="grid grid-cols-2 gap-2 mt-1">
                    {distances.map((d, i) => (
                      <div
                        key={i}
                        className={`p-1 rounded ${
                          i === 0
                            ? "bg-sky-100 dark:bg-sky-900 text-sky-800 dark:text-sky-200 font-medium"
                            : "bg-gray-100 dark:bg-gray-700"
                        }`}
                      >
                        Cluster {d.centroidIndex}: {d.distance.toFixed(2)} units
                        {i === 0 && <span className="ml-1">✓</span>}
                      </div>
                    ))}
                  </div>
                  <p className="mt-2 text-gray-600 dark:text-gray-400">
                    The point is assigned to Cluster {distances[0].centroidIndex} because it has the shortest distance.
                  </p>
                </div>
              )}
            </div>
          )
  
        case "assigned_all":
          return (
            <div>
              <p className="text-sm text-gray-600 dark:text-gray-400 mb-2">{message}</p>
              <p className="text-sm text-gray-600 dark:text-gray-400">
                All points have been assigned to their nearest centroid. Next, we'll recalculate the position of each
                centroid based on the mean position of all points in its cluster.
              </p>
            </div>
          )
  
        case "recalculate":
          return (
            <div>
              <p className="text-sm text-gray-600 dark:text-gray-400 mb-2">{message}</p>
              <p className="text-sm text-gray-600 dark:text-gray-400">
                Each centroid is moved to the average (mean) position of all points assigned to its cluster. This helps
                the centroids converge toward the natural centers of the data clusters.
              </p>
              {currentDetailedStep.oldCentroids && currentDetailedStep.newCentroids && (
                <div className="mt-2 text-xs">
                  <p className="font-medium text-gray-700 dark:text-gray-300">Centroid movements:</p>
                  <div className="grid grid-cols-1 gap-2 mt-1">
                    {currentDetailedStep.newCentroids.map((newC, i) => {
                      const oldC = currentDetailedStep.oldCentroids[i]
                      const distance = Math.sqrt(Math.pow(newC.x - oldC.x, 2) + Math.pow(newC.y - oldC.y, 2))
                      return (
                        <div key={i} className="bg-gray-100 dark:bg-gray-700 p-1 rounded">
                          Cluster {i}: Moved {distance.toFixed(2)} units
                        </div>
                      )
                    })}
                  </div>
                </div>
              )}
            </div>
          )
  
        case "final":
          return (
            <div>
              <p className="text-sm text-gray-600 dark:text-gray-400 mb-2">{message}</p>
              <p className="text-sm text-gray-600 dark:text-gray-400">
                The algorithm has converged! The centroids no longer move significantly between iterations, indicating
                we've found stable cluster centers.
              </p>
            </div>
          )
  
        default:
          return (
            <p className="text-sm text-gray-600 dark:text-gray-400">
              {message || "Exploring the K-means clustering algorithm..."}
            </p>
          )
      }
    }
  
    // Get cluster statistics
    const getClusterStats = () => {
      if (!currentDetailedStep.points) return null
  
      // Count points in each cluster
      const clusterCounts = {}
      currentDetailedStep.points.forEach((point) => {
        if (point.cluster !== undefined) {
          clusterCounts[point.cluster] = (clusterCounts[point.cluster] || 0) + 1
        }
      })
  
      if (Object.keys(clusterCounts).length === 0) return null
  
      return (
        <div className="mt-3 text-sm">
          <p className="font-medium text-gray-700 dark:text-gray-300">Cluster Sizes:</p>
          <div className="grid grid-cols-2 sm:grid-cols-3 gap-2 mt-1">
            {Object.entries(clusterCounts).map(([cluster, count]) => (
              <div key={cluster} className="bg-gray-100 dark:bg-gray-600 px-2 py-1 rounded">
                Cluster {cluster}: {count} points
              </div>
            ))}
          </div>
        </div>
      )
    }
  
    return (
      <div className="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 p-4 rounded-lg mb-4 shadow-sm animate-fadeIn">
        <div className="flex justify-between items-start mb-2">
          <h3 className="text-sm font-semibold text-gray-800 dark:text-gray-200">
            K-Means Algorithm Step {animationStep + 1} of {totalSteps}
          </h3>
  
          {currentDetailedStep.type === "assign" && (
            <span className="bg-sky-100 dark:bg-sky-900 text-sky-800 dark:text-sky-200 text-xs px-2 py-1 rounded-full">
              Point Assignment
            </span>
          )}
  
          {currentDetailedStep.type === "recalculate" && (
            <span className="bg-orange-100 dark:bg-orange-900 text-orange-800 dark:text-orange-200 text-xs px-2 py-1 rounded-full">
              Centroid Recalculation
            </span>
          )}
  
          {currentDetailedStep.type === "initial" && (
            <span className="bg-purple-100 dark:bg-purple-900 text-purple-800 dark:text-purple-200 text-xs px-2 py-1 rounded-full">
              Initialization
            </span>
          )}
  
          {currentDetailedStep.type === "final" && (
            <span className="bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200 text-xs px-2 py-1 rounded-full">
              Complete
            </span>
          )}
        </div>
  
        {getStepExplanation()}
  
        {getClusterStats()}
  
        {currentDetailedStep.type !== "initial" && currentDetailedStep.type !== "final" && (
          <div className="mt-3 text-xs text-gray-500 dark:text-gray-500 border-t border-gray-200 dark:border-gray-700 pt-2">
            <p>
              <span className="font-medium">How K-means works:</span> The algorithm alternates between (1) assigning
              points to the nearest centroid and (2) recalculating centroids as the average position of all points in the
              cluster, until convergence is reached.
            </p>
          </div>
        )}
      </div>
    )
  }
  
  export default StepExplanation
  
  