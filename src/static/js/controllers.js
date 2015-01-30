var shelfModule = angular.module("shelf");

shelfModule.controller("HomeController", function($rootScope, $scope) {
    $scope.name = "Michael";
    $scope.notify = function(type) {
        if (type == "simple") {
            toast('I am a toast!', 4000);
        }

    };
});

shelfModule.controller("navbarController", function($rootScope, $scope, $location, loginService) {
    $scope.logout = function () {
        loginService.logout().then( function(data) {
            if (data == 200) {
                $rootScope.loggedIn = false;
                $location.path("/login");
            }
        });
    }
});

shelfModule.controller("newOrderController", function($scope) {
    $scope.name = "Hi";
});

shelfModule.controller("deleteOrderController", function($rootScope, $scope, orderService) {
    $rootScope.$on("deleteOrderOpened", function(event, args) {
        orderService.getOrder(args["orderId"]).then( function(order) {
            $scope.order = order;
        });
    });

    $scope.deleteOrder = function(orderId) {
        orderService.deleteOrder(orderId).then( function () {
            $('#deleteOrder').closeModal();
            $rootScope.$emit("refreshOrders");
            toast('Bestellung gelöscht!', 4000);
        });
    };
});

shelfModule.controller("OrderDetailController", function($scope, $routeParams, orderService) {
    orderService.getOrder($routeParams.orderId).then( function(order) {
        $scope.order = order;
    });
});

shelfModule.controller("OrderListController", function($rootScope, $scope, $location, orderService) {
    $rootScope.$emit("refreshOrders");
    $rootScope.$on("refreshOrders", function() {
        $scope.order_template = "/static/booking/progress.html";
        orderService.getOrders().then( function(orders) {
            $scope.orders = orders;
            $scope.order_template = "/static/booking/order-table.html";
        });
    });

    $scope.createNewOrder = function() {
       $('#createNewOrder').openModal();
    };

    $scope.deleteOrder = function(orderId) {
        $('#deleteOrder').openModal();
        var args = {'orderId': orderId};
        $rootScope.$emit("deleteOrderOpened", args);
    }
});

shelfModule.controller("LoginController", function($rootScope, $scope, $location, loginService) {
        $scope.login = function() {
            loginService.login($scope.loginModel).then(function(data) {
                if (data == 200) {
                    $rootScope.loggedIn = true;
                    $location.path("/");
                } else if (data == 401) {
                    $scope.errorMessage = "Dont have the permission";
                } else if (data == 403) {
                    $scope.errorMessage = "The credentials were not right. Please try again";
                }
            });
        }
    }
);