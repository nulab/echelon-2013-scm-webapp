(function($){
    function Todo(summary, done) {
        this.summary = summary;
        this.done = ko.observable(done);
    }

    Todo.prototype.toPlainObject = function () {
        return {
            summary: this.summary,
            done: this.done()
        };
    };

    function Model() {
        var self = this;

        self.todoList = ko.observableArray();

        self.addTodo = function (summary, done) {
            self.todoList.push(new Todo(summary, done));
        };

        self.deleteTodo = function (todo) {
            self.todoList.remove(todo);
        };

        self.archive = function () {
            self.todoList.remove(function (todo) {
                return todo.done();
            });
        };

        self.save = function () {
            var list = ko.utils.arrayMap(self.todoList(), function (todo) {
                return todo.toPlainObject();
            });
            return $.ajax({
                url : '/todo/save',
                type : 'POST',
                data : {
                    todos : ko.utils.stringifyJson(list)
                }
            });
        };

        self.load = function () {

            return $.ajax({
                url : '/todo/list'
            }).done(function(data){
                self.todoList.removeAll();
                ko.utils.arrayForEach(data.todos, function (todo) {
                    self.addTodo(todo.summary, todo.done);
                });
            });
        };

        self.bind = function(){
            $(window).on('load', function(){
                self.load().complete(function(){
                    var subscr = self.todoList.subscribe(function(){
                        self.save();
                    },null,'change');
                });
            });
        };
    }


    function ViewModel(model) {
        var self = this;

        self.todoList = model.todoList;
        self.deleteTodo = model.deleteTodo;
        self.archive = model.archive;
        self.save = model.save;

        self.todoSummary = ko.observable('');
        self.addTodo = function () {
            if (self.canAddTodo()) {
                model.addTodo(self.todoSummary(), false);
                self.todoSummary('');
            }
        };

        self.canAddTodo = ko.computed(function () {
            return self.todoSummary().length > 0;
        });

        self.showTodo = function (elem) {
            if (elem.nodeType === 1) {
                $(elem).hide().slideDown();
            }
        };

        self.hideTodo = function (elem) {
            if (elem.nodeType === 1) {
                $(elem).slideUp(function () {
                    $(elem).remove();
                });
            }
        };
    }

    var model = new Model();
    model.bind();
    ko.applyBindings(new ViewModel(model));

})(jQuery);

