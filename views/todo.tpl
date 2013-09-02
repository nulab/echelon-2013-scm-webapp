<!DOCTYPE html>
<html>
<head>
    <title>Todo</title>
    <meta charset="UTF-8">
    <link rel="stylesheet" type="text/css" media="all" href="/static/todo.css">
</head>
<body>

<div id="content">
    <h1>Todo</h1>
    <form data-bind="submit: addTodo">
        <input type="text" data-bind="value: todoSummary, valueUpdate: 'afterkeydown'" placeholder="todo"/>
        <input type="submit" value="add" data-bind="enable: canAddTodo"/>
    </form>

    <div id="todoList">
        <span class="counter"><!--ko text: todoList().length--><!--/ko--> items</span><span class="archive redLink" data-bind="click:archive">archive</span>

        <ul data-bind="foreach: {data:todoList, afterAdd: showTodo, beforeRemove: hideTodo}">
            <li class="todoItem" data-bind="css: {doneItem: done}">
                <input type="checkbox" data-bind="checked: done"/>
                <span class="summary" data-bind="text: summary"></span>
                <span class="delete redLink" data-bind="click: $root.deleteTodo">delete</span>
            </li>
        </ul>
    </div>
</div>
</body>
<script type="text/javascript" src="/static/jquery-2.0.2.min.js"></script>
<script type="text/javascript" src="/static/knockout-2.2.1.js"></script>
<script type="text/javascript" src="/static/todo.js"></script>
</html>