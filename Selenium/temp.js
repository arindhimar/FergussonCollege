$.ajax({
    type: "method",
    url: "url",
    data: "data",
    dataType: "dataType",
    success: function (response) {
        
    },
    error: function (xhr, status, error) {
        console.error("Error occurred: " + error);
    }
});