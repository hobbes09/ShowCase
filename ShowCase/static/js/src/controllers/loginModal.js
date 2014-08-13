var loginModalModule = angular.module('controller.loginModal', ['ui.bootstrap', 'security.service']);

loginModalModule.controller('loginModalCtrl', ['$scope', '$modalInstance', 'securityFactory', function ($scope, $modalInstance, securityFactory) {
    'use strict';
    
    $scope.authError = '';
    
    $scope.login = function (user) {
        $scope.authError = '';
        securityFactory.login(user.email, user.password).then(function (res) {
            if (res) {
                $modalInstance.close(res);
            } else {
                $scope.authError = 'Authentication failure';
            }
        }, function (res) {
            $scope.authError = 'Authentication failure';
        });
    };
    
    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };
}]);