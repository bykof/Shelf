var shelfModule = angular.module("shelf");

shelfModule.controller("HomeController", function($rootScope, $scope) {
    $scope.name = "Michael";
    $scope.notify = function(type) {
        if (type == "simple") {
            toast('I am a toast!', 4000);
        }

    };
});

shelfModule.controller("navbarController", function($rootScope, $scope, $location, Restangular) {
    $scope.logout = function () {
        Restangular.one("logout/").get().then( function(data) {
            if (data == 200) {
                $rootScope.loggedIn = false;
                $location.path("/login");
            }
        });
    }
});

shelfModule.controller("newOrderController", function($scope, $location, Restangular) {
    Restangular.one("orders/").options().then(function(data) {
        angular.forEach(data.choices, function(value, key) {
            $scope[key] = value;
        });
        $("select").select2();
    });

    $scope.save = function() {
        Restangular.one("orders/").post("", $scope.formModel).then( function(data) {
            $location.path("/orders");
        }, function(error_data) {
            angular.forEach(error_data.data, function(value, key) {
                toast(key + ": " + value, 4000);
            });
        });
    };
});

shelfModule.controller("deleteOrderController", function($rootScope, $scope, Restangular) {
    $rootScope.$on("deleteOrderOpened", function(event, args) {
        Restangular.one('orders', args["orderId"]).get().then(function(order) {
            $scope.order = order;
        });
    });

    $scope.cancel = function() {
        $('#deleteOrder').closeModal();
        $scope.order = null;
    };

    $scope.deleteOrder = function(orderId) {
        Restangular.one('orders', orderId).remove().then(function() {
            $('#deleteOrder').closeModal();
            $rootScope.$emit("refreshOrders");
            toast('Bestellung gelöscht!', 4000);
        });
    };
});

shelfModule.controller("OrderDetailController", function($scope, $routeParams, Restangular) {
    Restangular.one('orders', $routeParams.orderId).get().then(function(order) {
        $scope.order = order;
    });
});

shelfModule.controller("OrderListController", function($rootScope, $scope, Restangular) {
    $rootScope.$emit("refreshOrders");
    $rootScope.$on("refreshOrders", function() {
        $scope.order_template = "/static/booking/progress.html";
        Restangular.all('orders-collapsed/').getList().then( function(orders) {
            $scope.orders = orders;
            $scope.order_template = "/static/booking/order-table.html";
        });
    });

    $scope.deleteOrder = function(orderId) {
        $('#deleteOrder').openModal();
        var args = {'orderId': orderId};
        $rootScope.$emit("deleteOrderOpened", args);
    }
});

shelfModule.controller("LoginController", function($rootScope, $scope, $location, Restangular) {
        $scope.login = function() {
            Restangular.one("login/").post("", $scope.loginModel).then( function(data) {
                console.log(data);
                if (data == 200) {
                    $rootScope.loggedIn = true;
                    $location.path("/");
                } else if (data == 401) {

                    toast('You don\'t have enough permission to login', 4000)
                } else if (data == 403) {
                    toast('The credentials were not right, please try again!', 4000)
                }
            });
        }
    }
);