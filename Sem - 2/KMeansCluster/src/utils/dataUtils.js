export const generateRandomData = (count) => {
    const data = []
  
    for (let i = 0; i < count; i++) {
      const customerID = (i + 1).toString().padStart(4, "0")
      const gender = Math.random() > 0.5 ? "Male" : "Female"
      const age = Math.floor(Math.random() * 60) + 18
      const income = Math.floor(Math.random() * 150) + 20
      const spendingScore = Math.floor(Math.random() * 100) + 1
  
      data.push({
        CustomerID: customerID,
        Genre: gender,
        Age: age.toString(),
        "Annual Income (k$)": income.toString(),
        "Spending Score (1-100)": spendingScore.toString(),
      })
    }
  
    return data
  }
  
  