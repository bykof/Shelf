var shelfModule = angular.module("shelf");
var static_url = "/static/";
var is_logged_in_url = "/api/is-logged-in/";
var booking_static_url = static_url + "booking/";

//https://angularjs.de/artikel/angularjs-login-sicherheit

shelfModule.config(function($routeProvider) {
        $routeProvider.
        when('/', {
            templateUrl: static_url + "home.html",
            controller: "HomeController"
        }).
        when('/login', {
            templateUrl: static_url + "login.html",
            controller: "LoginController"
        }).
        when('/orders', {
            templateUrl: booking_static_url + "orders.html",
            controller: "OrderListController"
        }).
        when('/orders/:orderId', {
            templateUrl: booking_static_url + "order-detail.html",
            controller: "OrderDetailController"
        }).
        when('/booking', {
            redirectTo: '/orders'
        }).
        otherwise({
            redirectTo: '/'
        });
});

shelfModule.run(function ($rootScope, $location, loginService) {
    $rootScope.$on('$routeChangeStart', function (event) {
        loginService.isLoggedIn().then( function(loggedIn) {
            if (!loggedIn) {
                $rootScope.loggedIn = loggedIn;
                event.preventDefault();
                $location.path('/login');
            } else {
                $rootScope.loggedIn = loggedIn;
            }
        });

    });
});
