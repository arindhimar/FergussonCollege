                if "BETWEEN" in condition:
                    between_match = re.match(
                        r"(\w+)\s+BETWEEN\s+(['\"]?\d+(\.\d*)?['\"]?)\s+AND\s+(['\"]?\d+(\.\d*)?['\"]?)", 
                        condition
                    )
                    
                    if between_match:
                        print("MKC idhr aana ")  # Debug print statement
                        column, val1, _, val2, _ = between_match.groups()  # Extract values
                        print(column, val1, val2)
                        
                        # Remove quotes and check if both are numeric
                        val1_clean = val1.replace("'", "").replace('"', "")
                        val2_clean = val2.replace("'", "").replace('"', "")
                        
                        if not (val1_clean.replace(".", "", 1).isdigit() and val2_clean.replace(".", "", 1).isdigit()):
                            return f"Syntax Error: Invalid BETWEEN values! `{val1}` and `{val2}` must be numbers."
                    else:
                        return "Syntax Error: Invalid BETWEEN syntax! Expected format: column BETWEEN value1 AND value2"
