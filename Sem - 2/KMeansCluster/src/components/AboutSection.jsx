"use client"

import { Github, Globe, Mail } from "lucide-react"

const AboutSection = () => {
  return (
    <div className="max-w-3xl mx-auto">
      <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-6 mb-6">
        <h2 className="text-2xl font-bold text-sky-600 dark:text-sky-400 mb-4">About This Project</h2>

        <p className="text-gray-700 dark:text-gray-300 mb-6">
          This interactive K-Means Clustering visualization tool was created to help users understand how the K-Means
          algorithm works through visual demonstration. It allows you to explore the step-by-step process of clustering
          data points and see how the algorithm converges to find optimal clusters.
        </p>

        <h3 className="text-xl font-semibold text-gray-800 dark:text-gray-200 mb-3">Features</h3>

        <ul className="list-disc list-inside space-y-2 text-gray-700 dark:text-gray-300 mb-6">
          <li>Interactive visualization of the K-Means clustering algorithm</li>
          <li>Step-by-step animation with adjustable speed</li>
          <li>Multiple visualization types (scatter plot, bar chart, pie chart)</li>
          <li>Detailed statistics for each cluster</li>
          <li>Sample data loading and random data generation</li>
          <li>CSV data import and export</li>
          <li>Comprehensive algorithm explanation</li>
        </ul>

        <h3 className="text-xl font-semibold text-gray-800 dark:text-gray-200 mb-3">How to Use</h3>

        <ol className="list-decimal list-inside space-y-2 text-gray-700 dark:text-gray-300 mb-6">
          <li>Load sample data, generate random data, or upload your own CSV file</li>
          <li>Select the number of clusters (K) you want to identify</li>
          <li>Choose which features to use for the X and Y axes</li>
          <li>Click "Run Clustering" to start the algorithm</li>
          <li>Use the animation controls to step through the algorithm or watch it automatically</li>
          <li>Switch between different visualization types to explore the results</li>
          <li>View detailed statistics about each cluster</li>
        </ol>

        <h3 className="text-xl font-semibold text-gray-800 dark:text-gray-200 mb-3">Technologies Used</h3>

        <div className="grid grid-cols-2 md:grid-cols-3 gap-3 mb-6">
          <div className="bg-gray-50 dark:bg-gray-700 p-3 rounded-lg text-center">
            <div className="font-medium text-gray-800 dark:text-gray-200 mb-1">React</div>
            <div className="text-sm text-gray-600 dark:text-gray-400">UI Framework</div>
          </div>
          <div className="bg-gray-50 dark:bg-gray-700 p-3 rounded-lg text-center">
            <div className="font-medium text-gray-800 dark:text-gray-200 mb-1">Tailwind CSS</div>
            <div className="text-sm text-gray-600 dark:text-gray-400">Styling</div>
          </div>
          <div className="bg-gray-50 dark:bg-gray-700 p-3 rounded-lg text-center">
            <div className="font-medium text-gray-800 dark:text-gray-200 mb-1">JavaScript</div>
            <div className="text-sm text-gray-600 dark:text-gray-400">Programming Language</div>
          </div>
          <div className="bg-gray-50 dark:bg-gray-700 p-3 rounded-lg text-center">
            <div className="font-medium text-gray-800 dark:text-gray-200 mb-1">HTML5 Canvas</div>
            <div className="text-sm text-gray-600 dark:text-gray-400">Visualization</div>
          </div>
          <div className="bg-gray-50 dark:bg-gray-700 p-3 rounded-lg text-center">
            <div className="font-medium text-gray-800 dark:text-gray-200 mb-1">CSV</div>
            <div className="text-sm text-gray-600 dark:text-gray-400">Data Format</div>
          </div>
        </div>

        <div className="flex flex-col md:flex-row justify-center items-center gap-4 pt-4 border-t border-gray-200 dark:border-gray-700">
          <a
            href="https://github.com/arindhimar/FergussonCollege/tree/FullStack-1/Sem%20-%202/KMeansCluster"
            className="flex items-center gap-2 text-gray-700 dark:text-gray-300 hover:text-sky-600 dark:hover:text-sky-400"
          >
            <Github className="w-5 h-5" />
            <span>GitHub Repository</span>
          </a>

          <a
            href="mailto:arindhimar.fc@gmail.com"
            className="flex items-center gap-2 text-gray-700 dark:text-gray-300 hover:text-sky-600 dark:hover:text-sky-400"
          >
            <Mail className="w-5 h-5" />
            <span>Contact</span>
          </a>
        </div>
      </div>
    </div>
  )
}

export default AboutSection

