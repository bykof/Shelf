var module = angular.module("shelfModule");
var searchTimer = false;

module.controller("OrderListController", function($rootScope, $scope, $timeout, Restangular, loaderTexts) {
    if (!$.cookie("djangocookie")) {
        return
    }

    getOrdersByPage(1);

    $scope.pageChanged = function(newPageNumber) {
        getOrdersByPage(newPageNumber);
    };

    $scope.clearOrderSearch = function() {
        $scope.orderSearch = "";
    }

    $scope.$watch("orderSearch", function(newValue, oldValue) {
        if (newValue && newValue.length >= 3) {
            if(searchTimer){
                $timeout.cancel(searchTimer);
            }

            searchTimer = $timeout(function(){
                getOrdersByPage(1);
            }, 1000);

            $("#search-delete-icon").removeClass("search");
            $("#search-delete-icon").addClass("remove circle");
        } else {
            if(oldValue && oldValue.length >= 3 && newValue.length < oldValue.length) {
                getOrdersByPage(1)
            }
            $("#search-delete-icon").addClass("search");
            $("#search-delete-icon").removeClass("remove circle");
        }
    });

    function getOrdersByPage(pageNumber) {
        var listLoader = $("#list-loader");
        $scope.loaderText = loaderTexts.getRandomText();
        listLoader.addClass("active");
        if ($scope.orderSearch != "" || $scope.orderSearch.length >= 3) {
            Restangular.one("orders").get({"page": pageNumber, "search": $scope.orderSearch}).then( function(response) {
                $scope.totalOrders = response.count;
                $scope.orders = response.results;
                listLoader.removeClass("active");
            });
        } else {
            Restangular.one("orders").get({"page": pageNumber}).then( function(response) {
                $scope.totalOrders = response.count;
                $scope.orders = response.results;
                listLoader.removeClass("active");
            });
        }

    };
});

module.controller("CreateOrderController", function($rootScope, $scope, Restangular, $timeout, $location) {
    $scope.$on('$viewContentLoaded', function(){
        $scope.newOrder = {"bought_on": moment().format("DD.MM.YYYY")};
        $('.datetimepicker').datetimepicker({
            lang:'de',
            i18n:{
                de:{
                    months:[
                        'Januar','Februar','März','April',
                        'Mai','Juni','Juli','August',
                        'September','Oktober','November','Dezember',
                    ],
                    dayOfWeek:[
                        "So.", "Mo", "Di", "Mi",
                        "Do", "Fr", "Sa."
                    ]
                }
            },
            timepicker:false,
            format:'d.m.Y'
        });
        $('select.dropdown').dropdown();
        $('.ui.accordion').accordion();
    });

    $scope.back = function() {
        $location.path("/orders/list");
    };

    Restangular.one("orders").options().then( function (response) {
        $scope.postActions = response.actions.POST;
    });

    $scope.createNewOrder = function () {
        var newOrder = $scope.newOrder;
        formatTime(true);

        if (!newOrder.tags) {
            newOrder.tags = [];
        }

        Restangular.one("orders").post('', newOrder).then( function(response) {
            $rootScope.addMessage("Order successfully created! Have a great day!");
            $scope.back();
        }, function(response) {
            $scope.error_messages = null;
            $scope.error_messages = response.data;
            console.log($scope.error_messages);
            $timeout( function() {
                $("div[data-content]").each( function(index, element) {
                    $(element).popup("destroy");
                });
                $("div[data-content]").popup("show", {"movePopup": false});
            });
            formatTime(false);
        });
    };

    function formatTime(to_server) {
        var newOrder = $scope.newOrder;

        if (to_server) {
            newOrder.bought_on = moment(newOrder.bought_on, "DD.MM.YYYY").format();
        } else{
            $scope.newOrder.bought_on = moment($scope.newOrder.bought_on).format("DD.MM.YYYY");
        }


        if (newOrder.delivery_received_on) {
            if (to_server) {
                newOrder.delivery_received_on = moment(newOrder.delivery_received_on, "DD.MM.YYYY").format();
            } else {
                newOrder.delivery_received_on = moment(newOrder.delivery_received_on).format("DD.MM.YYYY");
            }
        }
    }
});