var module = angular.module("shelfModule");

module.config(['$routeProvider', '$locationProvider',
    function($routeProvider, $locationProvider) {
        $routeProvider
            .when('/', {
                templateUrl: 'templates/home.html'
            })
            // ORDERS
            .when('/orders', {
                redirectTo: '/orders/list'
            })
            .when('/orders/list', {
                templateUrl: 'order-templates/list.html'
            })
            .when('/orders/detail/:orderId', {
                templateUrl: 'order-templates/detail.html',
                controller: "DetailOrderController"
            })
            .when('/orders/create', {
                templateUrl: 'order-templates/create.html',
                controller: "CreateOrderController"
            })
            .when('/invoices', {
                templateUrl: 'invoice-templates/list.html'
            })
            .when('/articles', {
                templateUrl: 'article-templates/list.html'
            }).otherwise( {
                redirectTo: '/'
            });
        $locationProvider.html5Mode(true);
    }
]);