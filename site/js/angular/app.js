angular
    .module("shelfModule", ['ngRoute', 'restangular', 'angularUtils.directives.dirPagination'])
    .config(function(RestangularProvider) {
    RestangularProvider.setBaseUrl('http://127.0.0.1:8000/api');
    RestangularProvider.setRequestSuffix('/');
    })
    .config(function(paginationTemplateProvider) {
        paginationTemplateProvider.setPath('templates/dirPagination.tpl.html');
    });