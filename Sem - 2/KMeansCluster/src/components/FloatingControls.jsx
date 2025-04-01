"use client"

import { useState } from "react"
import {
  PlayIcon,
  PauseIcon,
  SkipBackIcon,
  SkipForwardIcon,
  RefreshCwIcon,
  FastForwardIcon,
  Settings,
  ChevronUp,
  ChevronDown,
} from "lucide-react"

const FloatingControls = ({
  currentStep,
  totalSteps,
  onStepChange,
  isPlaying,
  togglePlay,
  resetAnimation,
  skipToEnd,
  animationSpeed,
  setAnimationSpeed,
  isVisible,
}) => {
  const [expanded, setExpanded] = useState(true)
  const [showSettings, setShowSettings] = useState(false)

  const handlePrevStep = () => {
    onStepChange(Math.max(0, currentStep - 1))
  }

  const handleNextStep = () => {
    onStepChange(Math.min(totalSteps - 1, currentStep + 1))
  }

  // Calculate progress percentage
  const progressPercentage = totalSteps > 1 ? (currentStep / (totalSteps - 1)) * 100 : 0

  if (!isVisible) return null

  return (
    <div className="fixed bottom-4 right-4 z-50 animate-fadeIn">
      <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg border border-gray-200 dark:border-gray-700 overflow-hidden">
        {/* Header */}
        <div className="flex items-center justify-between p-2 bg-gray-50 dark:bg-gray-700 border-b border-gray-200 dark:border-gray-700">
          <button
            onClick={() => setExpanded(!expanded)}
            className="flex items-center gap-1 text-sm font-medium text-gray-700 dark:text-gray-300"
          >
            {expanded ? <ChevronDown className="w-4 h-4" /> : <ChevronUp className="w-4 h-4" />}
            Animation Controls
          </button>
          <div className="flex items-center gap-2">
            <div className="text-xs text-gray-600 dark:text-gray-400">
              Step {currentStep + 1}/{totalSteps}
            </div>
          </div>
        </div>

        {/* Body */}
        {expanded && (
          <div className="p-3">
            {/* Progress Bar */}
            <div
              className="w-full bg-gray-200 dark:bg-gray-600 rounded-full h-2 mb-3 cursor-pointer"
              onClick={(e) => {
                const rect = e.currentTarget.getBoundingClientRect()
                const x = e.clientX - rect.left
                const clickedPosition = x / rect.width
                const newStep = Math.floor(clickedPosition * totalSteps)
                onStepChange(Math.min(Math.max(0, newStep), totalSteps - 1))
              }}
            >
              <div
                className="bg-sky-500 h-2 rounded-full transition-all duration-300 ease-in-out"
                style={{ width: `${progressPercentage}%` }}
              ></div>
            </div>

            {/* Settings Toggle */}
            <div className="flex justify-end mb-2">
              <button
                onClick={() => setShowSettings(!showSettings)}
                className="text-xs flex items-center gap-1 text-gray-600 dark:text-gray-400 hover:text-gray-800 dark:hover:text-gray-200"
              >
                <Settings className="w-3 h-3" />
                {showSettings ? "Hide Settings" : "Show Settings"}
              </button>
            </div>

            {/* Animation Settings */}
            {showSettings && (
              <div className="mb-3 p-2 bg-gray-50 dark:bg-gray-700 rounded-md animate-fadeIn">
                <div className="flex flex-col gap-1">
                  <label className="text-xs font-medium text-gray-700 dark:text-gray-300">Animation Speed</label>
                  <div className="flex items-center gap-2">
                    <span className="text-xs text-gray-500 dark:text-gray-400">Fast</span>
                    <input
                      type="range"
                      min="200"
                      max="2000"
                      step="100"
                      value={animationSpeed}
                      onChange={(e) => setAnimationSpeed(Number(e.target.value))}
                      className="flex-1 h-1.5 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700"
                    />
                    <span className="text-xs text-gray-500 dark:text-gray-400">Slow</span>
                    <span className="text-xs font-medium bg-gray-100 dark:bg-gray-600 px-1.5 py-0.5 rounded">
                      {(animationSpeed / 1000).toFixed(1)}s
                    </span>
                  </div>
                </div>
              </div>
            )}

            {/* Control Buttons */}
            <div className="flex justify-center space-x-3">
              <button
                onClick={resetAnimation}
                className="p-1.5 rounded-full bg-gray-200 dark:bg-gray-600 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-500 transition-colors"
                title="Reset"
              >
                <RefreshCwIcon className="w-4 h-4" />
              </button>

              <button
                onClick={handlePrevStep}
                disabled={currentStep === 0}
                className="p-1.5 rounded-full bg-gray-200 dark:bg-gray-600 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-500 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
                title="Previous Step"
              >
                <SkipBackIcon className="w-4 h-4" />
              </button>

              <button
                onClick={togglePlay}
                className="p-1.5 rounded-full bg-sky-100 dark:bg-sky-900 text-sky-600 dark:text-sky-400 hover:bg-sky-200 dark:hover:bg-sky-800 transition-colors"
                title={isPlaying ? "Pause" : "Play"}
              >
                {isPlaying ? <PauseIcon className="w-4 h-4" /> : <PlayIcon className="w-4 h-4" />}
              </button>

              <button
                onClick={handleNextStep}
                disabled={currentStep === totalSteps - 1}
                className="p-1.5 rounded-full bg-gray-200 dark:bg-gray-600 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-500 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
                title="Next Step"
              >
                <SkipForwardIcon className="w-4 h-4" />
              </button>

              <button
                onClick={skipToEnd}
                disabled={currentStep === totalSteps - 1}
                className="p-1.5 rounded-full bg-amber-100 dark:bg-amber-900 text-amber-600 dark:text-amber-400 hover:bg-amber-200 dark:hover:bg-amber-800 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
                title="Skip to End"
              >
                <FastForwardIcon className="w-4 h-4" />
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default FloatingControls

