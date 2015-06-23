var app = angular.module('siteListsApp', []);

app.service('queryLists', function () {
    return function (siteUrl, success, error) {
        var clientContext = SP.ClientContext.get_current();
        var appContextSite = new SP.AppContextSite(clientContext, siteUrl);
        var web = appContextSite.get_web();
        var lists = web.get_lists();

        clientContext.load(lists);
        clientContext.executeQueryAsync(function (sender, args) {
            var listsArray = [];
            var enumerator = lists.getEnumerator();

            while (enumerator.moveNext()) {
                listsArray.push(enumerator.get_current());
            }

            success(listsArray);
        }, function (sender, args) {
            var message = args.get_message();

            error(message);
        });
    };
});

app.controller('mainController', function ($scope, queryLists) {
    $scope.siteUrl = '';
    $scope.lists = [];

    $scope.queryLists = function () {
        queryLists($scope.siteUrl, function (lists) {
            $scope.lists = lists;
            $scope.$apply();
        }, function (error) {
            alert(error);
        });
    };
});