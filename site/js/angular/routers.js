var module = angular.module("shelfModule");

module.config(['$routeProvider', '$locationProvider',
    function($routeProvider, $locationProvider) {
        $routeProvider
            .when('/', {
                templateUrl: 'templates/home.html'
            })
            .when('/orders', {
                templateUrl: 'order-templates/index.html'
            })
            .when('/invoices', {
                templateUrl: 'invoice-templates/index.html'
            })
            .when('/articles', {
                templateUrl: 'article-templates/index.html'
            }).otherwise( {
                redirectTo: '/'
            });
        $locationProvider.html5Mode(true);
    }
]);