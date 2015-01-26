var shelfModule = angular.module("shelf");

shelfModule.controller("HomeController", function($rootScope, $scope) {
    $scope.name = "Michael";
});

shelfModule.controller("navbarController", function($rootScope, $scope, $location, loginService) {
    $scope.logout = function () {
        loginService.logout().then( function(data) {
            if (data == 200) {
                $rootScope.loggedIn = false;
                $location.path("/");
            }
        });
    }
});

shelfModule.controller("OrderListController", function($scope, $dialogs, $modal, $location, orderService) {
    $.material.init();
    refreshOrders(orderService, $scope);

    $scope.deleteOrder = function (orderId, size) {
        var modalInstance = $modal.open({
            templateUrl: '/static/booking/deleteOrderModal.html',
            controller: 'DeleteModalInstanceCtrl',
            size: size
        });

        modalInstance.orderId = orderId;
        modalInstance.result.then(function () {
            orderService.deleteOrder(orderId).then( function(data) {
                refreshOrders(orderService, $scope);
            });
        });
    };

    $scope.createNewOrder = function (size) {
        var modalInstance = $modal.open({
            templateUrl: '/static/booking/createOrderModal.html',
            controller: 'CreateModalInstanceCtrl',
            size: size
        });

        modalInstance.result.then(function (selectedItem) {
            $scope.selected = selectedItem;
        });
    };
});

shelfModule.controller("DeleteModalInstanceCtrl", function ($scope, $modalInstance) {
    $scope.ok = function () {
        $modalInstance.close();
    };

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };
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


shelfModule.controller("CreateModalInstanceCtrl", function ($scope, $modalInstance, orderService) {
    orderService.getOptions().then( function(options) {
       angular.forEach(options.actions.POST, function(value, key) {
            $scope[key] = value;
        });
    });

    $scope.ok = function () {
        console.log($scope.article.selected);
        console.log($scope.bought_by.selected);
        $modalInstance.close();
    };

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };

    $scope.today = function() {
        $scope.dt = new Date();
    };

    $scope.today();

    $scope.clear = function () {
        $scope.dt = null;
    };

    $scope.toggleMin = function() {
        $scope.minDate = $scope.minDate ? null : new Date();
    };
    $scope.toggleMin();

    $scope.open = function($event) {
        $event.preventDefault();
        $event.stopPropagation();

        $scope.opened = true;
    };

    $scope.dateOptions = {
        formatYear: 'yy',
        startingDay: 1
    };

    $scope.format = 'dd.MM.yyyy';
});

function refreshOrders(orderService, $scope) {
    orderService.getOrders().then( function(orders) {
        $scope.orders = orders;
    });
}