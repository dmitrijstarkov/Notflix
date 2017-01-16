docker run -it --rm --name dashit \
    -v $PWD/local/videofiles/todo_dashify/:/todo_dashify \
    -v todo-python:/todo_python \
        dashifying:3 \
        /bin/bash -c \
        'python /usr/bin/group-dash.py'