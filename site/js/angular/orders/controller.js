var module = angular.module("shelfModule");
var searchTimer = false;

function initDatePicker() {
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
        scrollInput:false,
        format:'d.m.Y'
    });
}

function closeModal(modalId) {
    $('#' + modalId).modal("hide");
}

function openModal(modalId) {
    $('#' + modalId).modal(
        {
            closable  : false,
            onApprove : function() {
                return false;
            }
        }
    ).modal("show");
}

module.controller("OrderListController", function($rootScope, $scope, $timeout, Restangular, loaderTexts) {
    getOrders();

    $scope.clearOrderSearch = function() {
        $scope.orderSearch = "";
    };

    function getOrders() {
        var listLoader = $("#list-loader");
        $scope.loaderText = loaderTexts.getRandomText();
        listLoader.addClass("active");
        if ($scope.orderSearch != "" || $scope.orderSearch.length >= 3) {
            Restangular.one("orders").get({"search": $scope.orderSearch}).then( function(response) {
                $scope.totalOrders = response.length;
                $scope.orders = response;
                listLoader.removeClass("active");
            }, function (response) {
            });
        } else {
            Restangular.one("orders").get().then( function(response) {
                $scope.totalOrders = response.length;
                $scope.orders = response;
                listLoader.removeClass("active");
            });
        }

    };
});

module.controller(
    "CreateOrderController",
    function($rootScope, $scope, Restangular, $timeout, $location, $upload, GlobalService) {

        $scope.$on('$viewContentLoaded', function(){
            $scope.newOrder = {
                "bought_on": moment().format("DD.MM.YYYY"),
                "invoice_documents": []
            };

            initDatePicker();
            $('select.dropdown').dropdown();
            $('.ui.accordion').accordion();
            fillChoices();
        });

        Restangular.one("users").get({"search": $.cookie("djangocookie_username")}).then( function(response) {
            $timeout( function(){
                $scope.newOrder.bought_by = response[0].id;
                $('.dropdown').dropdown("set selected");
            }, 100);
        });

        $rootScope.$on("newDataCreated", function() {
            fillChoices();
        });

        $scope.back = function() {
            $location.path("/orders/list");
        };

        $scope.createArticle = function() {
            openModal("createArticleModal");
        };

        $scope.createCategory = function() {
            openModal("createCategoryModal");
        };

        $scope.createSupplier = function() {
            openModal("createSupplierModal");
        };

        $scope.createPaymentMethod = function() {
            openModal("createPaymentMethodModal");
        };

        $scope.createNewOrder = function () {
            var newOrder = $scope.newOrder;
            formatTime(true);

            if (!newOrder.tags) {
                newOrder.tags = [];
            }

            var files = $scope.newOrder.invoice_documents;
            delete $scope.newOrder["invoice_documents"];

            if (files && files.length > 0) {
                openModal("uploadProgressBarModal");
            }

            $upload.upload({
                url: GlobalService.apiServer + "/create-or-update-order-with-documents/",
                file: files,
                method: "POST",
                headers: {"Authorization": "Token " + $.cookie("djangocookie")},
                data: newOrder
            }).progress(function(evt) {
                $("#upload-progress").progress({
                    percent: parseInt(100.0 * evt.loaded / evt.total)
                });
            }).success(function(data, status, headers, config) {
                closeModal("uploadProgressBarModal");
                $rootScope.addMessage("Order successfully created! Have a great day!");
                $scope.back();
            }).error( function( response) {
                closeModal("uploadProgressBarModal");
                $scope.error_messages = response;
                $timeout( function() {
                    $("div[data-content]").popup("show", {"movePopup": false});
                });
                formatTime(false);
                $scope.newOrder["invoice_documents"] = files;
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

        function fillChoices () {
            Restangular.one("orders").options().then( function (response) {
                $scope.postActions = response.actions.POST;
            });
            $('select.dropdown').dropdown("set selected");
        }
    }
);

module.controller("CreateArticleController", function($rootScope, $scope, Restangular) {
    $scope.save = function() {
        Restangular.one("articles").post('', $scope.newArticle).then( function(response) {
            $rootScope.addMessage("Article '" + $scope.newArticle.name + "' successfully saved!");
            $('#createArticleModal').modal("hide");
            $rootScope.$broadcast("newDataCreated", response);
        }, function(response) {
            $scope.errors = response.data;
        });
    }
});

module.controller("CreateCategoryController", function($rootScope, $scope, Restangular) {
    $scope.save = function() {
        Restangular.one("order-categories").post('', $scope.newCategory).then( function(response) {
            $rootScope.addMessage("Category '" + $scope.newCategory.name + "' successfully saved!");
            $('#createCategoryModal').modal("hide");
            $rootScope.$broadcast("newDataCreated", response);
        }, function(response) {
            $scope.errors = response.data;
        });
    }
});

module.controller("CreateSupplierController", function($rootScope, $scope, Restangular) {
    $scope.save = function() {
        Restangular.one("suppliers").post('', $scope.newSupplier).then( function(response) {
            $rootScope.addMessage("Supplier '" + $scope.newSupplier.name + "' successfully saved!");
            $('#createSupplierModal').modal("hide");
            $rootScope.$broadcast("newDataCreated", response);
        }, function(response) {
            $scope.errors = response.data;
        });
    }
});

module.controller("CreatePaymentMethodController", function($rootScope, $scope, Restangular) {
    $scope.save = function() {
        Restangular.one("payment-methods").post('', $scope.newPaymentMethod).then( function(response) {
            $rootScope.addMessage("Payment Method '" + $scope.newPaymentMethod.name + "' successfully saved!");
            $('#createPaymentMethodModal').modal("hide");
            $rootScope.$broadcast("newDataCreated", response);
        }, function(response) {
            $scope.errors = response.data;
        });
    }
});

module.controller(
    "DetailOrderController",
    function($rootScope, $scope, Restangular, $routeParams, $timeout, $location, $upload, GlobalService) {

        Restangular.one("orders").one($routeParams.orderId).get().then( function(response) {
            $scope.order = response;
            formatTime(false);
            $timeout( function(){
                $('.dropdown').dropdown("set selected");
            }, 50);
        });

        $rootScope.$on("newDataCreated", function() {
            fillChoices();
        });

        $scope.back = function() {
            $location.path("/orders/list");
        };

        $scope.$on('$viewContentLoaded', function(){
            fillChoices();
            initDatePicker();
        });

        $scope.createArticle = function() {
            openModal("createArticleModal");
        };

        $scope.createCategory = function() {
            openModal("createCategoryModal");
        };

        $scope.createSupplier = function() {
            openModal("createSupplierModal");
        };

        $scope.createPaymentMethod = function() {
            openModal("createPaymentMethodModal");
        };

        function formatTime(to_server) {
            var order = $scope.order;

            if (to_server) {
                order.bought_on = moment(order.bought_on, "DD.MM.YYYY").format();
            } else{
                $scope.order.bought_on = moment($scope.order.bought_on).format("DD.MM.YYYY");
            }


            if (order.delivery_received_on) {
                if (to_server) {
                    order.delivery_received_on = moment(order.delivery_received_on, "DD.MM.YYYY").format();
                } else {
                    order.delivery_received_on = moment(order.delivery_received_on).format("DD.MM.YYYY");
                }
            }
        }

        function fillChoices () {
            Restangular.one("orders").options().then( function (response) {
                $scope.postActions = response.actions.POST;
                $('.dropdown').dropdown("refresh");
            });
        }

        $scope.saveOrder = function () {
            var order = $scope.order;
            formatTime(true);

            if (!order.tags) {
                order.tags = [];
            }

            var files = $scope.order.new_invoice_documents;
            delete $scope.order["new_invoice_documents"];

            if (files && files.length > 0) {
                openModal("uploadProgressBarModal");
            }

            $upload.upload({
                url: GlobalService.apiServer + "/create-or-update-order-with-documents/",
                file: files,
                method: "POST",
                headers: {"Authorization": "Token " + $.cookie("djangocookie")},
                data: order
            }).progress(function(evt) {
                $("#upload-progress").progress({
                    percent: parseInt(100.0 * evt.loaded / evt.total)
                });
            }).success(function(data, status, headers, config) {
                closeModal("uploadProgressBarModal");
                $rootScope.addMessage("Order successfully updated! Have a great day!");
                $scope.back();
            }).error( function( response) {
                closeModal("uploadProgressBarModal");
                $scope.error_messages = response;
                $timeout( function() {
                    $("div[data-content]").popup("show", {"movePopup": false});
                });
                formatTime(false);
                $scope.order["new_invoice_documents"] = files;
            });
        };
});