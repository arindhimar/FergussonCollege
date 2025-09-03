
var RenderDropDown = function (control, data, id, value) {
    control.empty();
    $.each(data, function () {
        control.append($("<option />").val(this[id]).text(this[value]));
    }); control.prepend($("<option selected='selected' />").val(0).text("Please Select"));
};

var GetLogOutUrl = function () {
    return "/StudentLogin/Index/";
}

var GetStorageContainerName = function () {
    //return "desdevelopmentcontainer"; // development
      return "desproductioncontainer"; // live
}

var GetAPIURL = function () {
    // DEVelopment
    //return "http://desapitest.mastersofterp.in/";
    //return "http://localhost:44675/";

    // UAT
    // return "https://uatdescollegeapi.mastersofterp.in/";
    
    //Live
      return "https://liveapi.deccansociety.org/";
}

var GetFeePyrURL = function () {
    // DEVelopment
    //return "http://localhost:52597/";

    // Testing
    //return "http://dessplit.mastersofterp.in/";

    //Live
      return "https://feepayr.deccansociety.org/";
}