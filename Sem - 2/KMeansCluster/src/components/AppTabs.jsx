"use client"

import { useState } from "react"
import { BookOpen, BarChart2, Info } from "lucide-react"

const AppTabs = ({ children }) => {
  const [activeTab, setActiveTab] = useState("visualization")

  return (
    <div className="w-full">
      {/* Tab Navigation */}
      <div className="flex border-b border-gray-200 dark:border-gray-700 mb-6">
        <button
          onClick={() => setActiveTab("visualization")}
          className={`flex items-center gap-2 py-3 px-4 font-medium text-sm transition-colors ${
            activeTab === "visualization"
              ? "text-sky-600 dark:text-sky-400 border-b-2 border-sky-500 dark:border-sky-400"
              : "text-gray-600 dark:text-gray-400 hover:text-gray-800 dark:hover:text-gray-200"
          }`}
        >
          <BarChart2 className="w-4 h-4" />
          Visualization
        </button>
        <button
          onClick={() => setActiveTab("explanation")}
          className={`flex items-center gap-2 py-3 px-4 font-medium text-sm transition-colors ${
            activeTab === "explanation"
              ? "text-sky-600 dark:text-sky-400 border-b-2 border-sky-500 dark:border-sky-400"
              : "text-gray-600 dark:text-gray-400 hover:text-gray-800 dark:hover:text-gray-200"
          }`}
        >
          <BookOpen className="w-4 h-4" />
          Algorithm Explanation
        </button>
        <button
          onClick={() => setActiveTab("about")}
          className={`flex items-center gap-2 py-3 px-4 font-medium text-sm transition-colors ${
            activeTab === "about"
              ? "text-sky-600 dark:text-sky-400 border-b-2 border-sky-500 dark:border-sky-400"
              : "text-gray-600 dark:text-gray-400 hover:text-gray-800 dark:hover:text-gray-200"
          }`}
        >
          <Info className="w-4 h-4" />
          About
        </button>
      </div>

      {/* Tab Content */}
      {children.map((child) => {
        // Only render the active tab
        if (child.props.tabId === activeTab) {
          return (
            <div key={child.props.tabId} className="animate-fadeIn">
              {child}
            </div>
          )
        }
        return null
      })}
    </div>
  )
}

const TabPanel = ({ children, tabId }) => {
  return <div>{children}</div>
}

AppTabs.TabPanel = TabPanel

export default AppTabs

