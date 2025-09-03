var EventRegistration = function () {
    var init = function () {
        $(".myAlert-fullscreen").hide();
        BindEvent();
        BindEventData();
    }
    var BindEvent = function () {
        $("#btnSubmit").click(function () {
            var FBList = new Array();
            var ansId;
            var qustionid;
            var flag = true;
            var leng;
            var ansdes;
            var qno = 1;
            var chk;
            if ($("#txtFirstName").val().trim() == "") {
                alert("Please Enter Name!")
                $("#txtFirstName").val("");
                $("#txtFirstName").focus();
                return false;
            }

            if ($("#txtLastName").val().trim() == "") {
                alert("Please Enter Last Name !")
                $("#txtLastName").val("");
                $("#txtLastName").focus();
                return false;
            }

            if ($("#txtMobile").val().trim() == "") {
                alert("Please Enter Mobile Number !")
                $("#txtMobile").val("")
                $("#txtMobile").focus();
                return false;
            }
            if ($("#txtMobile").val().trim() != "") {
                if ($("#txtMobile").val().trim().length != 10) {
                    alert("Please Enter 10 digit mobile no. !")
                    $("#txtMobile").focus();
                    return false;
                }
            }
            if ($("#txtEmail").val().trim() == "") {
                alert("Please Enter Email !")
                $("#txtEmail").val("");
                $("#txtEmail").focus();
                return false;
            }
         
            if ($("#txtEmail").val().trim() != "") {
                var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
                if (!regex.test($("#txtEmail").val())) {
                    alert("Enter Valid Email");
                    $("#txtEmail").val("");
                    $("#txtEmail").focus();
                    return false;
                };
            }
            var photoUpload = $("#image1").get(0);
            var photo = photoUpload.files;
            debugger;
            // Create FormData object  
            var fileData = new FormData();
            //fileData.append('image1', files);
            // Looping over all files and add it to FormData object  
            for (var i = 0; i < photo.length; i++) {
                fileData.append('file', photo[i]);
            }
            if (fileData.get("file") == null || fileData.get("file") == "") {
                alert("Please Upload Image!");
                return false;
            }
            //var formData = {
               
            //    EventMasterId: $("#hdnEventMasterId").val(),
            //    FirstName: $("#txtFirstName").val().trim(),
            //    MiddleName: $("#txtMiddleName").val().trim(),
            //    LastName: $("#txtLastName").val().trim(),
            //    EmailId: $("#txtEmail").val().trim(),
            //    MobileNo: $("#txtMobile").val().trim(),
            //    file:photo[0],
            //    FileName:$('#file-name').text(),
            //    FileSize: $('#hdnFileSize').val()
            //}
            fileData.append('FileName', $('#file-name').text());
            fileData.append('FileSize', $('#hdnFileSize').val());
            fileData.append('EventMasterId', $("#hdnEventMasterId").val());
            fileData.append('FirstName', $("#txtFirstName").val().trim());
            fileData.append('MiddleName', $("#txtMiddleName").val().trim());
            fileData.append('LastName', $("#txtLastName").val().trim());
            fileData.append('EmailId', $("#txtEmail").val());
            fileData.append('MobileNo', $("#txtMobile").val());
         
            //fileData.append('CollegeId', 0);
            $('input:hidden.QuesClass').each(function () {
                var quesId = 'hdnQ_Id' + $(this).val();
                qustionid = $('#' + quesId).val();

                var count = 1;

                $('input:radio[name="' + qustionid + '"]').each(function () {
                    debugger;
                    ansId = 'rdbQ' + count + qustionid;
                    var chked = $('input:radio[name="' + qustionid + '"]:checked').val();

                    if (chked) {
                        // alert("Your are a - " + ab);
                    }
                    else {
                        alert("Please enter answer of Q." + qno + "");
                        flag = false;
                        $('input:radio[name="' + qustionid + '"]:checked').focus();
                        return false;
                       
                    }

                    if (this.checked) {
                        var list = {
                            QuestionId: qustionid,
                            AnswerId: $('#' + ansId).val()
                        }
                        FBList.push(list);
                    }
                    count += 1;
                });

                count = 1;
                var an;
                $('textarea[name="' + qustionid + '"]').each(function () {
                    debugger;
                    ansdes = 'txt' + qustionid;
                    an = $('#' + ansdes).val().length;
                    if (an == 0) {
                        flag = false;
                        alert("Please enter answer.")
                        return false;
                    } else {
                        flag = true;
                        var list = {
                            QuestionId: qustionid,
                            AnsDescription: $('#' + ansdes).val(),
                        }
                        FBList.push(list);
                    }
                });

               

                $('input:checkbox[name="' + qustionid + '"]').each(function () {
                    leng = $('input:checkbox.RCClass' + qustionid + ':checked').length;
                    ansId = 'chkQ' + count + qustionid;
                    if (this.checked) {
                        var list = {
                            QuestionId: qustionid,
                            AnswerId: $('#' + ansId).val()
                        }
                        FBList.push(list);
                    }
                    count += 1;
                });

                if (leng == 0) {
                    alert("Please select atleast one answer of Q." + qno + "");
                    flag = false;
                    return false;
                }
                qno += 1;
            });

            //SaveData(formData, FBList);
            if (flag != false) {
                $.ajax({
                    url: '/Event/EventRegistration/InsertUpdateEventRegistration?Data=' + JSON.stringify(FBList),
                    type: 'Post',
                    data: fileData,
                    dataType: 'json',
                    contentType: false,
                    processData: false,
                    //contentType: "application/json;charset=utf-8",
                    success: function (data) {
                        if (data > 0) {
                            data = 1;
                        }
                        ToggleData(data);

                    },
                    error: function (errResponse) {
                        console.log(errResponse);
                    }
                })
            }
        })

        $("#btnCancel").click(function () {
            Clear();
        })
        $('#image1').change(function () {


            var input = this; // avoid using 'this' directly
            if (input.files && input.files[0]) {
                var type = input.files[0].type; // image/jpg, image/png, image/jpeg...
                var type_reg = /^image\/(jpg|png|jpeg|gif)$/;
                var regex = new RegExp("(.*?)\.(pdf)$");
                // alert(regex.test(type))
                if (type_reg.test(type)) {
                    if (typeof (FileReader) != "undefined") {
                        //if (input.files[0].size > 80000) {
                        if (input.files[0].size > 200000) {
                            $("#file-name").text('');
                            $("#FileUpload_Preview img").attr("src", "/Images/Common/nophoto.jpg");
                            //alert("Max size 80kb!");
                            alert("Max size 200kb!");
                            return false;
                        }
                        else {
                            $("#file-name").text(this.files[0].name);
                            var reader = new FileReader();
                            reader.onload = function (e) {
                                //-----------------------------------
                                // Preview image
                                //-----------------------------------
                                $("#FileUpload_Preview img").attr("src", e.target.result);
                                $("#imgLink").attr('href', e.target.result);
                            }
                            reader.readAsDataURL($(this)[0].files[0]);

                        }
                    }
                    //$("#FileUpload_Preview img").attr("src", this.files[0]);
                } else if (regex.test(type)) {
                    // if (input.files[0].size > 80000) {
                    if (input.files[0].size > 200000) {
                        $("#file-name").text('');
                        $("#FileUpload_Preview img").attr("src", "/Images/Common/nophoto.jpg");
                        //alert("Max size 80kb!");
                        alert("Max size 200kb!");
                        return false;
                    }
                    else {
                        $("#file-name").text(this.files[0].name);
                        $("#FileUpload_Preview img").attr("src", "/Images/Common/pdf.jpg");

                    }
                }
                else {
                    //alert(2)
                    alert('Unsupported file type!');
                    return false;
                }
            }
        });
    }


    var SaveData = function (formData, FBList) {
        $.ajax({
            url: '/Event/EventRegistration/InsertUpdateEventRegistration?Data=' + JSON.stringify(FBList),
            type: 'Post',
            data: formData,
            dataType: 'json',
            //contentType: false,
            processData: false,
            //contentType: "application/json;charset=utf-8",
            success: function (data) {
                if (data > 0) {
                    data = 1;
                }
                ToggleData(data);

            },
            error: function (errResponse) {
                console.log(errResponse);
            }
        })
    }

    var ToggleData = function (data) {
        var value = parseInt(data);
        switch (value) {
            case -1:
                $("#StrmMsg").html("Registration Already Done For Event!");
                $("#divAlter").addClass("myAlert-fullscreen alert alert-warning");
                $(".myAlert-fullscreen").show();
                setTimeout(function () { $(".myAlert-fullscreen").hide(); }, 5000);
                break;
            case 2:
                $("#StrmMsg").html("Record Updated Successfully!");
                $("#divAlter").addClass("myAlert-fullscreen alert alert-warning");
                $(".myAlert-fullscreen").show();
                setTimeout(function () { $(".myAlert-fullscreen").hide(); }, 5000);
                break;
            case 1:
                window.location.href = "/Event/Payment/Index";
                $("#StrmMsg").html("Registration For Event Done Successfully!");
                $("#divAlter").addClass("myAlert-fullscreen alert alert-success");
                $(".myAlert-fullscreen").show();
                setTimeout(function () { $(".myAlert-fullscreen").hide(); }, 5000);
                break;
        }
        Clear();
        BindEventData();
    };

    var Clear = function () {

        $("#txtFirstName").val("");
        $("#txtMiddleName").val("");
        $("#txtLastName").val("");
        $("#txtEmail").val("");
        $("#txtMobile").val("");
        $("#hdnEventMasterId").val(0);
        $("#pnlEventDetails").css("display", "none");
        $("#divRegistration").css('display', 'none');
        $("#divCert").css('display', 'block');
        $("#lblEventName").text("");
        $("#lblEventType").text("");
        $("#lblEventDate").text("");
        $("#lblEvenTime").text("");
        $("#lblVenue").text("");
        $("#lblRegistrationFee").text("");
        $('#listDiv').empty();
        $("#image1").val('');
    }

    var BindEventData = function () {
        $.ajax({
            url: '/Event/EventRegistration/GetEventData/',
            type: 'POST',
            contentType: "application/json;charset=utf-8",
            success: function (data) {
                BindData(data);
            }
        });
    };

    var BindData = function (data) {
        $('#TimeTableBody').empty();
        var html = '';
        $.each(data, function (key, item) {
            html += '<tr>';
            html += '<td style="width: 30%;" class="text-left">' + item.EventName + '</td>';
            html += '<td style="width: 20%;" class="text-left">' + item.OrganiserName + '</td>';
            html += '<td style="width: 20%;" class="text-left">' + item.EventFromDate + '-' + item.EventToDate + '</td>';

            if (item.FilePath != null && item.FilePath != '') {
                var url = item.FilePath;
                //html += '<a href="' + val.StoragePath + '/' + StorageContainer + '/' + val.StudentApplicationReportName + '" download="' + val.StudentApplicationReportName + '" type="application/jpeg" target="_blank"><i class="fa fa-eye" style="color:green;"></i></a></td>';
                html += '<td style="text-align:center;"><a title="View Image" style="color:green;cursor: pointer;" class="fa fa-eye" id="aviewApp' + item.EventMasterId + '"  onclick=\'(viewApplication("' + url + '"))\'></a></td>'; /// 
            } else {
                html += '<td></td>';
            }
            html += '<td style="width: 20%;" class="text-center"><button id="btnSubmit" class="btn btn-primary" title="Click here to Register" onclick="return ApplyData(' + item.EventMasterId + ')"><span>Register</span></button></td>';
            html += '<td style="width: 20%;" class="text-center"><button id="btnSubmit" class="btn btn-success" title="Click here to view Details" onclick="return GetDetailsData(' + item.EventMasterId + ')"><span>View Details</span></button></td>';
            html += '<td style="width: 20%;" class="text-center"><button id="btnSubmit" class="btn btn-info" title="Click here to view Details" onclick="return GetRequeryData(' + item.EventMasterId + ')"><span>Requery</span></button></td>';
            html += '</tr>';
        });
        $('#TimeTableBody').append(html);
        $('#divCert').show();
    };


    var getQuestionAnswer = function (id) {
        $.ajax({
            url: '/Event/EventRegistration/GetQuestionAndAnswerById',
            type: 'Post',
            data: { EventMasterId: id },
            success: function (data) {
                if (data != 0) {

                    var count = 1;
                    $.each(data, function (key, item) {
                        var html = '';
                        var Acount = 1;
                        html += '<div class="form-group"><div class="col-md-1 col-xs-1 col-sm-1" style="text-align:right"><label>Q.' + count + '<span style="color: #FF0000; font-weight: bold;">*</span></label></div><div class="col-md-11 col-xs-11 col-sm-11"><label id="lblQ' + count + '">' + item.QuestionDescription + '</label><input type="hidden" id="hdnQ_Id' + item.QuestionId + '" class="QuesClass" value="' + item.QuestionId + '"/></div>';
                        $.each(data[key].lstAns, function (r, j) {

                            if (item.IsMultiSelect == false) {
                                html += '<div class="col-md-1 col-sm-1 col-xs-1" style="text-align:right"><input  id="rdbQ' + Acount + item.QuestionId + '" type="radio" class="RCClass" name="' + item.QuestionId + '"  title="' + j.AnswerId + '" value="' + j.AnswerId + '"/></div><div class="col-md-11 col-sm-11 col-xs-11"><label for="rdbQ' + Acount + item.QuestionId + '" style="font-weight:400">' + j.AnswerDescription + '</label></div>';
                            } else {
                                html += '<div class="col-md-1 col-sm-1 col-xs-1" style="text-align:right"><input  id="chkQ' + Acount + item.QuestionId + '" type="checkbox" class="RCClass' + item.QuestionId + '" name="' + item.QuestionId + '" title="' + j.AnswerId + '" value="' + j.AnswerId + '" /></div><div class="col-md-11 col-sm-11 col-xs-11"><label for="chkQ' + Acount + item.QuestionId + '" style="font-weight:400">' + j.AnswerDescription + '</label></div>';
                            }
                            Acount += 1;
                        });

                        if (item.IsDescriptive == true) {
                            html += '<div class="col-md-6 col-sm-6 col-xs-6" style="text-align:center"><textarea id="txt' + item.QuestionId + '" type="text" rows="2" class="form-control required" name="' + item.QuestionId + '" style="margin-left: 50px; width: 494px; height: 51px;" required/></div>';
                        }

                        html += '</div>';
                        $('#listDiv').append(html);
                        count += 1;
                    });

                    //$('.displayImg').css('display', 'none');
                }
            }
        })
    }

    return {
        Init: init,
        GetQuestionAnswer: getQuestionAnswer
    }
}();