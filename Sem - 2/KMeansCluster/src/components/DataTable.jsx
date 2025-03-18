const DataTable = ({ data, clusterColors, highlightedRowIndex }) => {
    if (!data || data.length === 0) {
      return (
        <div className="text-center py-8 text-gray-500 dark:text-gray-400">
          No data available. Please add data points or load a dataset.
        </div>
      )
    }
  
    const columns = Object.keys(data[0]).filter((col) => col !== "cluster")
  
    return (
      <div className="overflow-x-auto">
        <table className="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
          <thead className="bg-gray-50 dark:bg-gray-700">
            <tr>
              {columns.map((column) => (
                <th
                  key={column}
                  scope="col"
                  className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider"
                >
                  {column}
                </th>
              ))}
              {data.some((row) => row.cluster !== undefined) && (
                <th
                  scope="col"
                  className="px-6 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider"
                >
                  Cluster
                </th>
              )}
            </tr>
          </thead>
          <tbody className="bg-white dark:bg-gray-800 divide-y divide-gray-200 dark:divide-gray-700">
            {data.map((row, rowIndex) => {
              const isHighlighted = rowIndex === highlightedRowIndex
  
              return (
                <tr
                  key={rowIndex}
                  className={`
                    ${rowIndex % 2 === 0 ? "bg-white dark:bg-gray-800" : "bg-gray-50 dark:bg-gray-700"}
                    ${isHighlighted ? "bg-yellow-100 dark:bg-yellow-900 animate-pulse-slow" : ""}
                    transition-colors duration-300
                  `}
                >
                  {columns.map((column) => (
                    <td
                      key={`${rowIndex}-${column}`}
                      className={`px-6 py-4 whitespace-nowrap text-sm ${
                        isHighlighted
                          ? "font-medium text-gray-900 dark:text-gray-100"
                          : "text-gray-700 dark:text-gray-300"
                      }`}
                    >
                      {row[column]}
                    </td>
                  ))}
                  {row.cluster !== undefined && (
                    <td className="px-6 py-4 whitespace-nowrap text-sm">
                      <span
                        className="px-2 py-1 rounded-full text-xs font-medium text-white"
                        style={{ backgroundColor: clusterColors[row.cluster % clusterColors.length] }}
                      >
                        Cluster {row.cluster}
                      </span>
                    </td>
                  )}
                </tr>
              )
            })}
          </tbody>
        </table>
      </div>
    )
  }
  
  export default DataTable
  
  