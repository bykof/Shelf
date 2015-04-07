angular
    .module("shelfModule", ['ngRoute', 'restangular', 'angularUtils.directives.dirPagination', 'angularFileUpload'])
    .config(function(paginationTemplateProvider) {
        paginationTemplateProvider.setPath('templates/dirPagination.tpl.html');
    });