$(function(){
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
    var marker = new google.maps.Marker({
      position: location,
      map: map,
      dragable: true
    });

    google.maps.event.addListener(marker,'click', function(event){
      marker.setMap(null);
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
