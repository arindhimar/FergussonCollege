"use client"

import { PlayIcon, PauseIcon, SkipBackIcon, SkipForwardIcon, RefreshCwIcon } from "lucide-react"

const AnimationControls = ({ currentStep, totalSteps, onStepChange, isPlaying, togglePlay, resetAnimation }) => {
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
        <div className="text-sm text-gray-600 dark:text-gray-400">
          Step {currentStep + 1} of {totalSteps}
        </div>
      </div>

      {/* Progress Bar */}
      <div className="w-full bg-gray-200 dark:bg-gray-600 rounded-full h-2.5 mb-4">
        <div
          className="bg-sky-500 h-2.5 rounded-full transition-all duration-300 ease-in-out"
          style={{ width: `${progressPercentage}%` }}
        ></div>
      </div>

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
      </div>
    </div>
  )
}

export default AnimationControls

