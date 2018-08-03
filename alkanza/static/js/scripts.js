$(function(){

  var loc;

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

    var map = new google.maps.Map($('#map').get(0),mapSettings);

    google.maps.event.addListenerOnce(map,'click', function(event) {
      addMarker(event.latLng, map);
    });
  }

  function addMarker(location, map) {
    loc = location;
    var marker = new google.maps.Marker({
      position: location,
      map: map,
      draggable: true
    });

    google.maps.event.addListener(marker,'click', function(event){
      marker.setMap(null);
    });
  }

  function getDistance(pointA, pointB){
    return google.maps.geometry.spherical.computeDistanceBetween(pointA,pointB);
  }

  $("#evaluate").on('click',function(){
    alert(loc.lat());
    $.ajax({
      type: 'POST',
      url: 'evaluate',
      data:{
        latitude: loc.lat(),
        longitude: loc.lng(),
        radius: $("#radius").val()
      },success: function(response){
        alert(response);
      }, error: function(response){
        alert("Something went wrong!: "+response["status"]);
      }
    });
  });

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
