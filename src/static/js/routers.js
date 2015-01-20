var shelfModule = angular.module("shelf");
var static_url = "/static/";
var booking_static_url = static_url + "booking/";

shelfModule.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: static_url + "home.html",
        controller: "HomeController"
      }).
      when('/orders', {
        templateUrl: booking_static_url + "orders.html",
        controller: "HomeController"
      }).
      otherwise({
        redirectTo: '/'
      });
}]);