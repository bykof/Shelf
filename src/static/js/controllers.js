var shelfModule = angular.module("shelf");

shelfModule.controller("HomeController", ["$scope", function($scope) {
   $scope.name = "Michael";
}]);

shelfModule.controller(
    "OrderListController",
    ["$scope", "$dialogs", "$modal", "orderService",
    function($scope, $dialogs, $modal, orderService) {
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
            }, function () {
                console.log('Modal dismissed at: ' + new Date());
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
            }, function () {
                console.log('Modal dismissed at: ' + new Date());
            });
        };
}]);

shelfModule.controller('DeleteModalInstanceCtrl',["$scope", "$modalInstance", function ($scope, $modalInstance) {
    console.log($modalInstance.orderId);

    $scope.ok = function () {
        $modalInstance.close();
    };

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };
}]);


shelfModule.controller(
    "CreateModalInstanceCtrl",
    ["$scope", "$modalInstance", "orderService",
        function ($scope, $modalInstance, orderService) {
        orderService.getOptions().then( function(options) {
           angular.forEach(options.actions.POST, function(value, key) {
                $scope[key] = value;
            });
            $("select").select2({width: '100%'});
        });

        $scope.ok = function () {
            $modalInstance.close($scope.selected.item);
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
}]);

function refreshOrders(orderService, $scope) {
    orderService.getOrders().then( function(orders) {
        $scope.orders = orders;
        console.log(orders);
    });
}