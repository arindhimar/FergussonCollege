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
} from "lucide-react"

const AnimationControls = ({
  currentStep,
  totalSteps,
  onStepChange,
  isPlaying,
  togglePlay,
  resetAnimation,
  skipToEnd,
  animationSpeed,
  setAnimationSpeed,
}) => {
  const [showSettings, setShowSettings] = useState(false)

  const handlePrevStep = () => {
    onStepChange(Math.max(0, currentStep - 1))
  }

  const handleNextStep = () => {
    onStepChange(Math.min(totalSteps - 1, currentStep + 1))
  }

  // Calculate progress percentage
  const progressPercentage = totalSteps > 1 ? (currentStep / (totalSteps - 1)) * 100 : 0

  return (
    <div className="bg-gray-50 dark:bg-gray-700 p-4 rounded-lg mb-4 animate-fadeIn">
      <div className="flex items-center justify-between mb-2">
        <div className="text-sm font-medium text-gray-700 dark:text-gray-300">Animation Controls</div>
        <div className="flex items-center gap-2">
          <button
            onClick={() => setShowSettings(!showSettings)}
            className="p-1 rounded-full hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors"
            title="Animation Settings"
          >
            <Settings className="w-4 h-4 text-gray-600 dark:text-gray-400" />
          </button>
          <div className="text-sm text-gray-600 dark:text-gray-400">
            Step {currentStep + 1} of {totalSteps}
          </div>
        </div>
      </div>

      {/* Progress Bar */}
      <div
        className="w-full bg-gray-200 dark:bg-gray-600 rounded-full h-2.5 mb-4 cursor-pointer"
        onClick={(e) => {
          const rect = e.currentTarget.getBoundingClientRect()
          const x = e.clientX - rect.left
          const clickedPosition = x / rect.width
          const newStep = Math.floor(clickedPosition * totalSteps)
          onStepChange(Math.min(Math.max(0, newStep), totalSteps - 1))
        }}
      >
        <div
          className="bg-sky-500 h-2.5 rounded-full transition-all duration-300 ease-in-out"
          style={{ width: `${progressPercentage}%` }}
        ></div>
      </div>

      {/* Animation Settings */}
      {showSettings && (
        <div className="mb-4 p-3 bg-white dark:bg-gray-800 rounded-md shadow-sm border border-gray-200 dark:border-gray-700 animate-fadeIn">
          <div className="flex flex-col gap-2">
            <label className="text-sm font-medium text-gray-700 dark:text-gray-300">Animation Speed</label>
            <div className="flex items-center gap-3">
              <span className="text-xs text-gray-500 dark:text-gray-400">Slow</span>
              <input
                type="range"
                min="200"
                max="2000"
                step="100"
                value={animationSpeed}
                onChange={(e) => setAnimationSpeed(Number(e.target.value))}
                className="flex-1 h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700"
              />
              <span className="text-xs text-gray-500 dark:text-gray-400">Fast</span>
              <span className="text-xs font-medium bg-gray-100 dark:bg-gray-600 px-2 py-1 rounded-md">
                {(animationSpeed / 1000).toFixed(1)}s
              </span>
            </div>
          </div>
        </div>
      )}

      {/* Control Buttons */}
      <div className="flex justify-center space-x-4">
        <button
          onClick={resetAnimation}
          className="p-2 rounded-full bg-gray-200 dark:bg-gray-600 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-500 transition-colors"
          title="Reset"
        >
          <RefreshCwIcon className="w-5 h-5" />
        </button>

        <button
          onClick={handlePrevStep}
          disabled={currentStep === 0}
          className="p-2 rounded-full bg-gray-200 dark:bg-gray-600 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-500 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
          title="Previous Step"
        >
          <SkipBackIcon className="w-5 h-5" />
        </button>

        <button
          onClick={togglePlay}
          className="p-2 rounded-full bg-sky-100 dark:bg-sky-900 text-sky-600 dark:text-sky-400 hover:bg-sky-200 dark:hover:bg-sky-800 transition-colors"
          title={isPlaying ? "Pause" : "Play"}
        >
          {isPlaying ? <PauseIcon className="w-5 h-5" /> : <PlayIcon className="w-5 h-5" />}
        </button>

        <button
          onClick={handleNextStep}
          disabled={currentStep === totalSteps - 1}
          className="p-2 rounded-full bg-gray-200 dark:bg-gray-600 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-500 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
          title="Next Step"
        >
          <SkipForwardIcon className="w-5 h-5" />
        </button>

        <button
          onClick={skipToEnd}
          disabled={currentStep === totalSteps - 1}
          className="p-2 rounded-full bg-amber-100 dark:bg-amber-900 text-amber-600 dark:text-amber-400 hover:bg-amber-200 dark:hover:bg-amber-800 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
          title="Skip to End"
        >
          <FastForwardIcon className="w-5 h-5" />
        </button>
      </div>
    </div>
  )
}

export default AnimationControls

