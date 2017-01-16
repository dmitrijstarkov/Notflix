docker run -it --rm --name dataget \
    --link video-rest:rest \
    -v todo-python:/todo_python \
    -v encoded-video:/encoded_video \
    data-get:alp3 \
        /bin/ash -c \
        'python /py_scripts/process_video_files.py'