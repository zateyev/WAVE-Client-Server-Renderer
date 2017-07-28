$("#message").draggable();
$("#orientation").draggable();
$("#settings").draggable();


function setMessage(bheader, bcontent) {
    //console.log("Creating message");
    var timeNow = new Date();
    var hours   = timeNow.getHours();
    var minutes = timeNow.getMinutes();
    var seconds = timeNow.getSeconds();
    //var timeString = "" + ((minutes > 12) ? - 12 : hours);
    var timeString  = ((minutes < 10) ? "0" : "") + minutes;
    timeString  += ((seconds < 10) ? ":0" : ":") + seconds;

    var html = "<div><span class='bar-hl'>";
    //html += timeString;
    html += bheader;
    html += "</span><span class='bar-info'>";
    html += bcontent;
    html += "</span></div>";

    console.log(html);
    $(".bar-message > .bar-wrapper").append(html);
    $('.bar-message > .bar-wrapper').scrollTop($('.bar-message > .bar-wrapper')[0].scrollHeight);
}

$(".bar-dropdown").click(function() {
    console.log($(this).parent().parent().attr('id'));
    var _id = $(this).parent().parent().attr('id');
    if (parseInt($(".bar-"+ _id).css("height")) > 0) {
        $(".bar-dropdown", "#"+_id).css("transform", "rotate(180deg)");
        $(".bar-"+ _id + "> .bar-wrapper").hide();
        $(".bar-"+ _id).css("height", 0);
        $("#"+_id).css("height", 36);
    } else {
        $(".bar-dropdown", "#"+_id).css("transform", "rotate(0deg)");
        if (_id == "settings") {
            $(".bar-"+ _id).css("height", 400);
            $("#"+_id).css("height", 436);
        } else {
            $(".bar-"+ _id).css("height", 200);
            $("#"+_id).css("height", 236);
        }
        $(".bar-"+ _id + "> .bar-wrapper").show();
    }
});

// master hide all elements on screen
$("#toggleGUI").click(function() {
    $(".window-item").toggle();
});

$("#showTabs").hover(
    function() {
        $("#window-tab").show();
    }, function() {
        $("#window-tab").hide();
    }
);

$("#window-tab").hover(
    function() {
        $("#window-tab").show();
    }, function() {
        $("#window-tab").hide();
    }
);

$("#offMessage").click(function() {
    if ($("#message").is(":visible")) {
        $("#message").removeClass("window-item");
        $("#message").hide();
    } else {
        $("#message").addClass("window-item");
        $("#message").show();
    }
});

$("#offOrientation").click(function() {
    if ($("#orientation").is(":visible")) {
        $("#orientation").removeClass("window-item");
        $("#orientation").hide();
    } else {
        $("#orientation").addClass("window-item");
        $("#orientation").show();
    }
});

$("#offSettings").click(function() {
    if ($("#settings").is(":visible")) {
        $("#settings").removeClass("window-item");
        $("#settings").hide();
    } else {
        $("#settings").addClass("window-item");
        $("#settings").show();
    }
});


function setMessage(bheader, bcontent) {
    console.log("Creating message");
    var timeNow = new Date();
    var hours   = timeNow.getHours();
    var minutes = timeNow.getMinutes();
    var seconds = timeNow.getSeconds();
    //var timeString = "" + ((minutes > 12) ? - 12 : hours);
    var timeString  = ((minutes < 10) ? "0" : "") + minutes;
    timeString  += ((seconds < 10) ? ":0" : ":") + seconds;

    var html = "<div><span class='bar-hl'>";
    //html += timeString;
    html += bheader;
    html += "</span><span class='bar-info'>";
    html += bcontent;
    html += "</span></div>";

    console.log(html);
    $(".bar-message > .bar-wrapper").append(html);
    $('.bar-message > .bar-wrapper').scrollTop($('.bar-message > .bar-wrapper')[0].scrollHeight);
}

$('#settings-box :checkbox').click(function() {
    var $this = $(this);
    // $this will contain a reference to the checkbox
    if ($this.is(':checked')) {
        if (this.name == "wireframe") {
            rcl2.addWireframe();
            setMessage("tomo", "Add cube wireframe.");
        }
        // the checkbox was checked
    } else {
        if (this.name == "wireframe") {
            rcl2.removeWireframe();
            setMessage("tomo", "Remove cube wireframe.");
        }
        // the checkbox was unchecked
    }
});

$('#viewIso :checkbox').click(function() {
    var $this = $(this);
    if ($this.is(':checked')) {
        rcl2.showISO();
        rcl2.hideLight();
        $('#viewVolren :checkbox').prop('checked', false);
    } else {
        rcl2.showVolren();
        $('#viewVolren :checkbox').prop('checked', true);
    }

});

$('#viewVolren :checkbox').click(function() {
    var $this = $(this);
    if ($this.is(':checked')) {
        console.log("Checked");
        rcl2.showVolren();
        $('#viewIso :checkbox').prop('checked', false);
    } else {
        console.log("Not Checked");
        rcl2.showISO();
        $('#viewIso :checkbox').prop('checked', true);
    }
});

$('#rotateLight :checkbox').click(function() {
    var $this = $(this);
    if ($this.is(':checked')) {
        rcl2.startLightRotation();
    } else {
        console.log("Not Checked");
        rcl2.stopLightRotation();
    }
});


$( "#bg-color" ).change(function() {
    console.log(this.value);
    rcl2.setBackgroundColor("#"+this.value);
    setMessage("tomo", "Set background color: #" + this.value);
});

$("#textLowerGray").change(function() {
    rcl2.setGrayMinValue(($("#textLowerGray").val()/255.0));
    $( "#slider-range" ).slider('values',0, ($("#textLowerGray").val()/255.0 * 100)  );
    $( "#slider-range" ).slider("refresh");
});

$("#textUpperGray").change(function() {
    rcl2.setGrayMaxValue(($("#textUpperGray").val()/255.0));
    $( "#slider-range" ).slider('values', 1, ($("#textUpperGray").val()/255.0 * 100)  );
    $( "#slider-range" ).slider("refresh");
});

$("#textLowerX").change(function() {
    rcl2.setGeometryMinX(($("#textLowerX").val()/255.0));
    $( "#slider-range-x" ).slider('values',0, ($("#textLowerX").val()/255.0 * 100)  );
    $( "#slider-range-x" ).slider("refresh");
});

$("#textUpperX").change(function() {
    rcl2.setGeometryMaxX(($("#textUpperX").val()/255.0));
    $( "#slider-range-x" ).slider('values', 1, ($("#textUpperX").val()/255.0 * 100)  );
    $( "#slider-range-x" ).slider("refresh");
});

$("#textLowerY").change(function() {
    rcl2.setGeometryMinY(($("#textLowerY").val()/255.0));
    $( "#slider-range-y" ).slider('values',0, ($("#textLowerY").val()/255.0 * 100)  );
    $( "#slider-range-y" ).slider("refresh");
});

$("#textUpperY").change(function() {
    rcl2.setGeometryMaxY(($("#textUpperY").val()/255.0));
    $( "#slider-range-y" ).slider('values', 1, ($("#textUpperY").val()/255.0 * 100)  );
    $( "#slider-range-y" ).slider("refresh");
});

$("#textLowerZ").change(function() {
    rcl2.setGeometryMinZ(($("#textLowerZ").val()/255.0));
    $( "#slider-range-z" ).slider('values',0, ($("#textLowerZ").val()/255.0 * 100)  );
    $( "#slider-range-z" ).slider("refresh");
});

$("#textUpperZ").change(function() {
    rcl2.setGeometryMaxZ(($("#textUpperZ").val()/255.0));
    $( "#slider-range-z" ).slider('values', 1, ($("#textUpperZ").val()/255.0 * 100)  );
    $( "#slider-range-z" ).slider("refresh");
});

$( document ).ready(function() {

    namespace = '';

    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

    socket.on('connect', function() {
      socket.emit('my_event', {
        data: 'I\'m connected!'
      });
    });

    socket.on('my_response', function(msg) {
        // $('#container-2').append('<br>' + $('<div/>').text('Quaternion #' + msg.count + ': ' + msg.data).html());
        $("#imageBox").html('<img src="static/img/scrshot.png?id=' + msg.id + '" />');
    });

    $('#container').mouseup(function() {
      // var quaternion_arr = rcl2._core._controls.getRotationParams();
      var camera_position = rcl2._core._camera.position.toArray();
      var camera_up = rcl2._core._camera.up.toArray();
      var camera = {"position": {"x": camera_position[0], "y": camera_position[1], "z": camera_position[2]},
                    "up": {"x": camera_up[0], "y": camera_up[1], "z": camera_up[2]}};
      // var quaternion = {"angle": quaternion_arr[3], "x": quaternion_arr[0], "y": quaternion_arr[1], "z": quaternion_arr[2]};
      // console.log("mouseup from container " + quaternion_arr);
      console.log("mouseup from container " + camera.position.x);
      socket.emit('my_broadcast_event', {
        data: camera
      });
    });


    setMessage("GUI", "Initialized.");
    setMessage("GUI", "After 5 seconds of idling, raycaster and light rotation will stop.");
    setMessage("GUI", "Click on scene to resume.");
    // Handler for .ready() called.
    $( "#slider-range" ).slider({
        range: true,
        min: 0,
        max: 100,
        values: [ 0, 100 ],
        slide: function( event, ui ) {
            console.log(ui.values);
            rcl2.setGrayMinValue(ui.values[0]/100.0);
            rcl2.setGrayMaxValue(ui.values[1]/100.0);
            $("#textLowerGray").val( parseInt(ui.values[0]/100*255) );
            $("#textUpperGray").val( parseInt(ui.values[1]/100*255) );
        }
    });

    $( "#slider-range-x" ).slider({
        range: true,
        min: 0,
        max: 100,
        values: [ 0, 100 ],
        slide: function( event, ui ) {
            console.log(ui.values);
            rcl2.setGeometryMinX(ui.values[0]/100.0)
            rcl2.setGeometryMaxX(ui.values[1]/100.0)
            $("#textLowerX").val( parseInt(ui.values[0]/100*255) );
            $("#textUpperX").val( parseInt(ui.values[1]/100*255) );
        }
    });

    $( "#slider-range-y" ).slider({
        range: true,
        min: 0,
        max: 100,
        values: [ 0, 100 ],
        slide: function( event, ui ) {
            console.log(ui.values);
            rcl2.setGeometryMinY(ui.values[0]/100.0)
            rcl2.setGeometryMaxY(ui.values[1]/100.0)
            $("#textLowerY").val( parseInt(ui.values[0]/100*255) );
            $("#textUpperY").val( parseInt(ui.values[1]/100*255) );
        }
    });

    $( "#slider-range-z" ).slider({
        range: true,
        min: 0,
        max: 100,
        values: [ 0, 100 ],
        slide: function( event, ui ) {
            console.log(ui.values);
            rcl2.setGeometryMinZ(ui.values[0]/100.0)
            rcl2.setGeometryMaxZ(ui.values[1]/100.0)
            $("#textLowerZ").val( parseInt(ui.values[0]/100*255) );
            $("#textUpperZ").val( parseInt(ui.values[1]/100*255) );
        }
    });
});

// $("#container").mouseup(function() {
//   console.log("lastlast" + rcl2._core._controls.getRotationParams());
// });
