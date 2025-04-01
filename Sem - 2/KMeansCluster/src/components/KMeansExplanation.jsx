"use client"

import { useState } from "react"
import { ChevronDown, ChevronRight, Info, BookOpen, Lightbulb, BarChart3, GitCompare } from "lucide-react"

const KMeansExplanation = () => {
  const [expandedSections, setExpandedSections] = useState({
    algorithm: true,
    inputOutput: false,
    useCases: false,
    example: false,
    comparison: false,
    centroids: false,
  })

  const toggleSection = (section) => {
    setExpandedSections((prev) => ({
      ...prev,
      [section]: !prev[section],
    }))
  }

  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 mb-6">
      <h2 className="text-2xl font-bold text-sky-600 dark:text-sky-400 mb-6">Understanding K-Means Clustering</h2>

      {/* Algorithm Section */}
      <div className="mb-6">
        <button
          onClick={() => toggleSection("algorithm")}
          className="flex items-center w-full text-left font-semibold text-lg text-gray-800 dark:text-gray-200 mb-2"
        >
          {expandedSections.algorithm ? (
            <ChevronDown className="w-5 h-5 mr-2 text-sky-500" />
          ) : (
            <ChevronRight className="w-5 h-5 mr-2 text-sky-500" />
          )}
          How K-Means Clustering Works
        </button>

        {expandedSections.algorithm && (
          <div className="pl-7 animate-fadeIn">
            <p className="text-gray-700 dark:text-gray-300 mb-3">
              K-Means is an unsupervised machine learning algorithm used to identify and group similar data points in
              larger datasets without requiring labeled data.
            </p>

            <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg mb-4">
              <h4 className="font-medium text-gray-800 dark:text-gray-200 mb-2">The Algorithm Steps:</h4>
              <ol className="list-decimal list-inside space-y-2 text-gray-700 dark:text-gray-300">
                <li>
                  <span className="font-medium">Initialization:</span> Randomly place K centroids in the data space
                </li>
                <li>
                  <span className="font-medium">Assignment:</span> Assign each data point to the nearest centroid,
                  forming K clusters
                </li>
                <li>
                  <span className="font-medium">Update:</span> Recalculate each centroid as the mean of all points
                  assigned to that cluster
                </li>
                <li>
                  <span className="font-medium">Repeat:</span> Iterate steps 2-3 until centroids no longer move
                  significantly (convergence)
                </li>
              </ol>
            </div>

            <div className="flex items-start mb-3">
              <Info className="w-5 h-5 text-sky-500 mr-2 mt-0.5 flex-shrink-0" />
              <p className="text-gray-700 dark:text-gray-300">
                The "K" in K-Means refers to the number of clusters you want to identify in your data. This is a
                hyperparameter that must be specified before running the algorithm.
              </p>
            </div>

            <div className="flex items-start">
              <Lightbulb className="w-5 h-5 text-amber-500 mr-2 mt-0.5 flex-shrink-0" />
              <p className="text-gray-700 dark:text-gray-300">
                K-Means aims to minimize the sum of squared distances between data points and their assigned cluster
                centroids, also known as inertia or within-cluster sum of squares (WCSS).
              </p>
            </div>
          </div>
        )}
      </div>

      {/* Input/Output Section */}
      <div className="mb-6">
        <button
          onClick={() => toggleSection("inputOutput")}
          className="flex items-center w-full text-left font-semibold text-lg text-gray-800 dark:text-gray-200 mb-2"
        >
          {expandedSections.inputOutput ? (
            <ChevronDown className="w-5 h-5 mr-2 text-sky-500" />
          ) : (
            <ChevronRight className="w-5 h-5 mr-2 text-sky-500" />
          )}
          Inputs and Outputs
        </button>

        {expandedSections.inputOutput && (
          <div className="pl-7 animate-fadeIn">
            <div className="grid md:grid-cols-2 gap-4 mb-4">
              <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                <h4 className="font-medium text-gray-800 dark:text-gray-200 mb-2">Inputs:</h4>
                <ul className="list-disc list-inside space-y-2 text-gray-700 dark:text-gray-300">
                  <li>
                    <span className="font-medium">Dataset:</span> A collection of data points with numerical features
                  </li>
                  <li>
                    <span className="font-medium">K:</span> The number of clusters to form
                  </li>
                  <li>
                    <span className="font-medium">Features:</span> The attributes used for clustering (e.g., income and
                    spending score)
                  </li>
                  <li>
                    <span className="font-medium">Optional:</span> Maximum iterations, convergence threshold, etc.
                  </li>
                </ul>
              </div>

              <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                <h4 className="font-medium text-gray-800 dark:text-gray-200 mb-2">Outputs:</h4>
                <ul className="list-disc list-inside space-y-2 text-gray-700 dark:text-gray-300">
                  <li>
                    <span className="font-medium">Cluster Assignments:</span> Label for each data point indicating its
                    cluster
                  </li>
                  <li>
                    <span className="font-medium">Centroids:</span> The coordinates of each cluster center
                  </li>
                  <li>
                    <span className="font-medium">Inertia:</span> Sum of squared distances of samples to their closest
                    centroid
                  </li>
                  <li>
                    <span className="font-medium">Iterations:</span> Number of iterations needed to converge
                  </li>
                </ul>
              </div>
            </div>

            <div className="flex items-start">
              <Info className="w-5 h-5 text-sky-500 mr-2 mt-0.5 flex-shrink-0" />
              <p className="text-gray-700 dark:text-gray-300">
                K-Means works best with numerical data and requires features to be on similar scales for optimal
                results. Categorical data must be encoded numerically or using techniques like one-hot encoding before
                clustering.
              </p>
            </div>
          </div>
        )}
      </div>

      {/* Use Cases Section */}
      <div className="mb-6">
        <button
          onClick={() => toggleSection("useCases")}
          className="flex items-center w-full text-left font-semibold text-lg text-gray-800 dark:text-gray-200 mb-2"
        >
          {expandedSections.useCases ? (
            <ChevronDown className="w-5 h-5 mr-2 text-sky-500" />
          ) : (
            <ChevronRight className="w-5 h-5 mr-2 text-sky-500" />
          )}
          Common Use Cases
        </button>

        {expandedSections.useCases && (
          <div className="pl-7 animate-fadeIn">
            <div className="grid md:grid-cols-2 gap-4 mb-4">
              <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                <h4 className="font-medium text-gray-800 dark:text-gray-200 mb-2">Business Applications:</h4>
                <ul className="list-disc list-inside space-y-2 text-gray-700 dark:text-gray-300">
                  <li>
                    <span className="font-medium">Customer Segmentation:</span> Group customers by purchasing behavior
                  </li>
                  <li>
                    <span className="font-medium">Market Segmentation:</span> Identify distinct market segments
                  </li>
                  <li>
                    <span className="font-medium">Inventory Categorization:</span> Group products by sales patterns
                  </li>
                  <li>
                    <span className="font-medium">Anomaly Detection:</span> Identify unusual data points
                  </li>
                </ul>
              </div>

              <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg">
                <h4 className="font-medium text-gray-800 dark:text-gray-200 mb-2">Technical Applications:</h4>
                <ul className="list-disc list-inside space-y-2 text-gray-700 dark:text-gray-300">
                  <li>
                    <span className="font-medium">Image Compression:</span> Reduce color palette in images
                  </li>
                  <li>
                    <span className="font-medium">Document Clustering:</span> Group similar documents
                  </li>
                  <li>
                    <span className="font-medium">Feature Engineering:</span> Create new features for supervised
                    learning
                  </li>
                  <li>
                    <span className="font-medium">Recommendation Systems:</span> Group similar items or users
                  </li>
                </ul>
              </div>
            </div>

            <div className="flex items-start">
              <Lightbulb className="w-5 h-5 text-amber-500 mr-2 mt-0.5 flex-shrink-0" />
              <p className="text-gray-700 dark:text-gray-300">
                K-Means is particularly valuable when you need to discover hidden patterns in your data or reduce
                complex datasets into manageable groups for further analysis or targeted strategies.
              </p>
            </div>
          </div>
        )}
      </div>

      {/* Example Use Case Section */}
      <div className="mb-6">
        <button
          onClick={() => toggleSection("example")}
          className="flex items-center w-full text-left font-semibold text-lg text-gray-800 dark:text-gray-200 mb-2"
        >
          {expandedSections.example ? (
            <ChevronDown className="w-5 h-5 mr-2 text-sky-500" />
          ) : (
            <ChevronRight className="w-5 h-5 mr-2 text-sky-500" />
          )}
          Example: Customer Segmentation
        </button>

        {expandedSections.example && (
          <div className="pl-7 animate-fadeIn">
            <p className="text-gray-700 dark:text-gray-300 mb-4">
              This application demonstrates customer segmentation using K-Means clustering. By analyzing customers based
              on their annual income and spending score, we can identify distinct customer groups with similar
              behaviors.
            </p>

            <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg mb-4">
              <h4 className="font-medium text-gray-800 dark:text-gray-200 mb-2">Step-by-Step Process:</h4>
              <ol className="list-decimal list-inside space-y-2 text-gray-700 dark:text-gray-300">
                <li>
                  <span className="font-medium">Data Collection:</span> Gather customer data (income, spending score,
                  etc.)
                </li>
                <li>
                  <span className="font-medium">Feature Selection:</span> Choose relevant attributes for clustering
                </li>
                <li>
                  <span className="font-medium">Determine K:</span> Select the optimal number of customer segments
                </li>
                <li>
                  <span className="font-medium">Run K-Means:</span> Apply the algorithm to identify customer clusters
                </li>
                <li>
                  <span className="font-medium">Analyze Results:</span> Interpret each cluster's characteristics
                </li>
                <li>
                  <span className="font-medium">Strategic Application:</span> Develop targeted marketing strategies for
                  each segment
                </li>
              </ol>
            </div>

            <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg mb-4">
              <h4 className="font-medium text-gray-800 dark:text-gray-200 mb-2">Potential Customer Segments:</h4>
              <div className="grid md:grid-cols-2 gap-3">
                <div className="bg-white dark:bg-gray-600 p-3 rounded-md">
                  <h5 className="font-medium text-sky-600 dark:text-sky-400">High Income, High Spending</h5>
                  <p className="text-sm text-gray-700 dark:text-gray-300">
                    Premium customers who are ideal for luxury products and premium services
                  </p>
                </div>
                <div className="bg-white dark:bg-gray-600 p-3 rounded-md">
                  <h5 className="font-medium text-orange-600 dark:text-orange-400">High Income, Low Spending</h5>
                  <p className="text-sm text-gray-700 dark:text-gray-300">
                    Potential targets for special promotions to increase their spending
                  </p>
                </div>
                <div className="bg-white dark:bg-gray-600 p-3 rounded-md">
                  <h5 className="font-medium text-purple-600 dark:text-purple-400">Low Income, High Spending</h5>
                  <p className="text-sm text-gray-700 dark:text-gray-300">
                    Value-conscious customers who prioritize certain purchases
                  </p>
                </div>
                <div className="bg-white dark:bg-gray-600 p-3 rounded-md">
                  <h5 className="font-medium text-green-600 dark:text-green-400">Low Income, Low Spending</h5>
                  <p className="text-sm text-gray-700 dark:text-gray-300">
                    Budget-conscious customers who may respond to value offerings
                  </p>
                </div>
              </div>
            </div>

            <div className="flex items-start">
              <BookOpen className="w-5 h-5 text-sky-500 mr-2 mt-0.5 flex-shrink-0" />
              <p className="text-gray-700 dark:text-gray-300">
                By identifying these segments, businesses can tailor their marketing strategies, product offerings, and
                customer experiences to better meet the needs of each group, ultimately improving customer satisfaction
                and increasing revenue.
              </p>
            </div>
          </div>
        )}
      </div>

      {/* Algorithm Comparison Section */}
      <div className="mb-6">
        <button
          onClick={() => toggleSection("comparison")}
          className="flex items-center w-full text-left font-semibold text-lg text-gray-800 dark:text-gray-200 mb-2"
        >
          {expandedSections.comparison ? (
            <ChevronDown className="w-5 h-5 mr-2 text-sky-500" />
          ) : (
            <ChevronRight className="w-5 h-5 mr-2 text-sky-500" />
          )}
          Comparison with Other Clustering Algorithms
        </button>

        {expandedSections.comparison && (
          <div className="pl-7 animate-fadeIn">
            <p className="text-gray-700 dark:text-gray-300 mb-4">
              While K-Means is one of the most popular clustering algorithms, it's important to understand how it
              compares to other methods to choose the right approach for your specific needs.
            </p>

            <div className="overflow-x-auto mb-4">
              <table className="min-w-full bg-white dark:bg-gray-700 rounded-lg overflow-hidden">
                <thead className="bg-gray-100 dark:bg-gray-600">
                  <tr>
                    <th className="py-3 px-4 text-left text-sm font-medium text-gray-700 dark:text-gray-200">
                      Algorithm
                    </th>
                    <th className="py-3 px-4 text-left text-sm font-medium text-gray-700 dark:text-gray-200">
                      Strengths
                    </th>
                    <th className="py-3 px-4 text-left text-sm font-medium text-gray-700 dark:text-gray-200">
                      Limitations
                    </th>
                    <th className="py-3 px-4 text-left text-sm font-medium text-gray-700 dark:text-gray-200">
                      Best For
                    </th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-200 dark:divide-gray-600">
                  <tr>
                    <td className="py-3 px-4 text-sm font-medium text-sky-600 dark:text-sky-400">K-Means</td>
                    <td className="py-3 px-4 text-sm text-gray-700 dark:text-gray-300">
                      <ul className="list-disc list-inside">
                        <li>Simple and fast</li>
                        <li>Scales well to large datasets</li>
                        <li>Easy to implement and interpret</li>
                      </ul>
                    </td>
                    <td className="py-3 px-4 text-sm text-gray-700 dark:text-gray-300">
                      <ul className="list-disc list-inside">
                        <li>Requires specifying K in advance</li>
                        <li>Only finds spherical clusters</li>
                        <li>Sensitive to outliers</li>
                        <li>Random initialization can lead to different results</li>
                      </ul>
                    </td>
                    <td className="py-3 px-4 text-sm text-gray-700 dark:text-gray-300">
                      Large datasets with well-separated, spherical clusters
                    </td>
                  </tr>
                  <tr>
                    <td className="py-3 px-4 text-sm font-medium text-purple-600 dark:text-purple-400">
                      Hierarchical Clustering
                    </td>
                    <td className="py-3 px-4 text-sm text-gray-700 dark:text-gray-300">
                      <ul className="list-disc list-inside">
                        <li>No need to specify number of clusters</li>
                        <li>Produces a dendrogram for visualization</li>
                        <li>Can find clusters of different shapes</li>
                      </ul>
                    </td>
                    <td className="py-3 px-4 text-sm text-gray-700 dark:text-gray-300">
                      <ul className="list-disc list-inside">
                        <li>Computationally expensive (O(n³))</li>
                        <li>Not suitable for large datasets</li>
                        <li>Can't undo previous steps</li>
                      </ul>
                    </td>
                    <td className="py-3 px-4 text-sm text-gray-700 dark:text-gray-300">
                      Smaller datasets where hierarchy visualization is valuable
                    </td>
                  </tr>
                  <tr>
                    <td className="py-3 px-4 text-sm font-medium text-orange-600 dark:text-orange-400">DBSCAN</td>
                    <td className="py-3 px-4 text-sm text-gray-700 dark:text-gray-300">
                      <ul className="list-disc list-inside">
                        <li>No need to specify number of clusters</li>
                        <li>Can find arbitrarily shaped clusters</li>
                        <li>Robust to outliers</li>
                      </ul>
                    </td>
                    <td className="py-3 px-4 text-sm text-gray-700 dark:text-gray-300">
                      <ul className="list-disc list-inside">
                        <li>Sensitive to parameter settings</li>
                        <li>Struggles with varying density clusters</li>
                        <li>Less efficient for high-dimensional data</li>
                      </ul>
                    </td>
                    <td className="py-3 px-4 text-sm text-gray-700 dark:text-gray-300">
                      Datasets with noise and non-spherical clusters
                    </td>
                  </tr>
                  <tr>
                    <td className="py-3 px-4 text-sm font-medium text-green-600 dark:text-green-400">
                      Gaussian Mixture Models
                    </td>
                    <td className="py-3 px-4 text-sm text-gray-700 dark:text-gray-300">
                      <ul className="list-disc list-inside">
                        <li>Soft clustering (probability of membership)</li>
                        <li>Can find elliptical clusters</li>
                        <li>More flexible than K-Means</li>
                      </ul>
                    </td>
                    <td className="py-3 px-4 text-sm text-gray-700 dark:text-gray-300">
                      <ul className="list-disc list-inside">
                        <li>More complex to implement</li>
                        <li>Slower than K-Means</li>
                        <li>Can overfit with insufficient data</li>
                      </ul>
                    </td>
                    <td className="py-3 px-4 text-sm text-gray-700 dark:text-gray-300">
                      Overlapping clusters with varying sizes and densities
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div className="flex items-start">
              <GitCompare className="w-5 h-5 text-sky-500 mr-2 mt-0.5 flex-shrink-0" />
              <p className="text-gray-700 dark:text-gray-300">
                K-Means is often the first algorithm to try due to its simplicity and efficiency. However, if your data
                has complex structures, varying densities, or you don't know the number of clusters in advance, consider
                exploring alternative clustering methods.
              </p>
            </div>
          </div>
        )}
      </div>

      {/* Centroids Section */}
      <div className="mb-6">
        <button
          onClick={() => toggleSection("centroids")}
          className="flex items-center w-full text-left font-semibold text-lg text-gray-800 dark:text-gray-200 mb-2"
        >
          {expandedSections.centroids ? (
            <ChevronDown className="w-5 h-5 mr-2 text-sky-500" />
          ) : (
            <ChevronRight className="w-5 h-5 mr-2 text-sky-500" />
          )}
          Understanding Centroids
        </button>

        {expandedSections.centroids && (
          <div className="pl-7 animate-fadeIn">
            <p className="text-gray-700 dark:text-gray-300 mb-4">
              Centroids are the heart of the K-Means algorithm. They represent the center points of each cluster and
              drive the entire clustering process.
            </p>

            <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg mb-4">
              <h4 className="font-medium text-gray-800 dark:text-gray-200 mb-2">What are Centroids?</h4>
              <p className="text-gray-700 dark:text-gray-300 mb-3">
                A centroid is the arithmetic mean position of all points in a cluster. For a 2D dataset (like in our
                customer segmentation example), a centroid has an x-coordinate and a y-coordinate that represent the
                average values of those features for all points in the cluster.
              </p>
              <div className="flex items-start">
                <BarChart3 className="w-5 h-5 text-sky-500 mr-2 mt-0.5 flex-shrink-0" />
                <p className="text-gray-700 dark:text-gray-300">
                  <span className="font-medium">Mathematical Definition:</span> For a cluster C with n points, the
                  centroid coordinates are calculated as:
                  <br />
                  <span className="font-mono bg-gray-100 dark:bg-gray-600 px-2 py-1 rounded mt-2 inline-block">
                    centroid_x = (x₁ + x₂ + ... + xₙ) / n
                    <br />
                    centroid_y = (y₁ + y₂ + ... + yₙ) / n
                  </span>
                </p>
              </div>
            </div>

            <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg mb-4">
              <h4 className="font-medium text-gray-800 dark:text-gray-200 mb-2">Centroid Generation Process:</h4>
              <ol className="list-decimal list-inside space-y-2 text-gray-700 dark:text-gray-300">
                <li>
                  <span className="font-medium">Initial Placement:</span> Centroids are initially placed randomly within
                  the data space (or using more advanced initialization methods like K-Means++)
                </li>
                <li>
                  <span className="font-medium">Point Assignment:</span> Each data point is assigned to its nearest
                  centroid based on Euclidean distance
                </li>
                <li>
                  <span className="font-medium">Recalculation:</span> After all points are assigned, each centroid is
                  moved to the average position of all points in its cluster
                </li>
                <li>
                  <span className="font-medium">Iteration:</span> Steps 2-3 are repeated until centroids stabilize
                  (convergence)
                </li>
              </ol>
            </div>

            <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg mb-4">
              <h4 className="font-medium text-gray-800 dark:text-gray-200 mb-2">Why Centroids Matter:</h4>
              <ul className="list-disc list-inside space-y-2 text-gray-700 dark:text-gray-300">
                <li>
                  <span className="font-medium">Cluster Representation:</span> Centroids provide a simple way to
                  represent the "typical" member of each cluster
                </li>
                <li>
                  <span className="font-medium">Classification:</span> New data points can be classified by finding the
                  closest centroid
                </li>
                <li>
                  <span className="font-medium">Dimensionality Reduction:</span> Complex data can be simplified by
                  representing points by their cluster centroids
                </li>
                <li>
                  <span className="font-medium">Optimization Target:</span> K-Means aims to find centroids that minimize
                  the total squared distance between points and their assigned centroids
                </li>
              </ul>
            </div>

            <div className="flex items-start">
              <Info className="w-5 h-5 text-sky-500 mr-2 mt-0.5 flex-shrink-0" />
              <p className="text-gray-700 dark:text-gray-300">
                The quality of the final clustering heavily depends on the initial placement of centroids. This is why
                K-Means is often run multiple times with different initializations, selecting the result with the lowest
                total intra-cluster variance.
              </p>
            </div>
          </div>
        )}
      </div>

      <div className="text-center pt-2 border-t border-gray-200 dark:border-gray-700">
        <p className="text-sm text-gray-600 dark:text-gray-400">
          K-Means is a powerful algorithm for discovering patterns in your data. Experiment with different values of K
          and features to find the most meaningful clusters for your specific use case.
        </p>
      </div>
    </div>
  )
}

export default KMeansExplanation

