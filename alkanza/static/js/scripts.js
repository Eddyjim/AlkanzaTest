$(function(){

  var loc;
  var map;

  if(navigator.geolocation){
    navigator.geolocation.getCurrentPosition(getCords,getError);
  }else{
    initialize();
  }

  function getCords(position){
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    initialize(lat,lon);
  }

  function getError(error){
    initialize();
  }

  function initialize(){
    initialize(41.879535,-87.624333);
  }

  function initialize(lat, lon) {
    var latLng = new google.maps.LatLng(lat,lon);
    var mapSettings = {
      center: latLng,
      zoom:   15,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    }

    map = new google.maps.Map($('#map').get(0),mapSettings);

    google.maps.event.addListenerOnce(map,'click', function(event) {
      loc = event.latLng;
      addMarker(event.latLng, map,'https://maps.google.com/mapfiles/kml/shapes/info-i_maps.png');
    });
  }

  function addMarker(location, map, icon) {
    var marker = new google.maps.Marker({
      icon: icon,
      position: location,
      map: map,
      draggable: true
    });

    google.maps.event.addListener(marker,'click', function(event){
      marker.setMap(null);
    });
  }

  function getDistance(pointA, pointB){
    return google.maps.geometry.spherical.computeDistanceBetween(pointA , pointB);;
  }

  $("#evaluate").on('click',function(){
    $.ajaxSetup({
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     }
    });
    $.ajax({
      type: 'POST',
      url: 'evaluate',
      data:{
        latitude: loc.lat(),
        longitude: loc.lng(),
        radius: $("#radius").val()
      },success: function(response){
        var json = "[";
        $.each(response, function(i, obj) {

          var pointTmp = new google.maps.LatLng(obj.lat,obj.lng);
          addMarker(pointTmp,map, obj.icon);
          var distance = getDistance(loc, pointTmp);

          json += '{ "lat" : '+ obj.lat + " , ";
          json += ' "lng" : '+ obj.lng + " , ";
          json += '"name" : ""' + obj.name + '" , ';
          json += '"distance" : ' + distance +" },"
        });
        json = json.substring(0, json.length-1);
        json += "]";

        if(json == ']'){
          json = '[{"lat" : 45 , "lng" : 45, "name" : "test", "distance": 4},{"lat" : 85 , "lng" : 25, "name" : "test", "distance": 6}]';
        }


        console.log(json);
        //var points = JSON.parse('');
        var points = JSON.parse(json);
        console.log(points);

        calculate (loc,points);

      }, error: function(response){
        alert("Something went wrong!: "+response["status"]);
      }
    });
  });

  function calculate(pivot, points){

    $.ajaxSetup({
      beforeSend: function(xhr, settings) {
        function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
       }
    });
    $.ajax({
      type: 'POST',
      url: 'calculate',
      data:{
        lat: loc.lat(),
        lng: loc.lng(),
        radius: $("#radius").val(),
        points: JSON.stringify(points )
      },
      success: function(response){
        $("#coeficient").val(response.coeficient);
      }, error: function(response){
        alert("Something went wrong!: "+response["status"]);
      }
    });
  }

  /*
var marker;
var pointByID = {};
  $(document).ready(function () {
    function activatePoints() {
      $('.point').each(function () {
        $(this).click(function() {
          var point = pointByID[this.id];
          var center = new google.maps.LatLng(point.lat, point.lng);

          if (marker) marker.setMap();
            marker = new google.maps.Marker({map: map, position: center});
            map.panTo(center);
          }).hover(

          function () {this.className = this.className.replace('OFF', 'ON');},
          function () {this.className = this.className.replace('ON', 'OFF');}
        );
      });
    }activatePoints();
  });

  function loadPrevious(){
    {% for point in points %}
      pointByID[{{point.id}}] = {
          lat: {{point.latitude}},
          lng: {{point.longitude}}
      };
    {% endfor %}
  }*/
});
