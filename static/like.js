$(document).ready(function () {
    $('.like').on('click', function (l) {
        l.preventDefault();
        let post_pk = l.target.id;
        console.log(post_pk)
        url = `http://localhost:8000/api/posts${post_pk}/like/`
        fetch(url)
            .then((response) => {
                img = document.getElementById(post_pk)
                img.setAttribute('src', '/static/img/like.png');
                $(this).removeClass('like').addClass('unlike')
                return response
            })
    });
    $('.unlike').on('click', function (l) {
        l.preventDefault();
        let post_pk = l.target.id;
        url = `http://localhost:8000/api/posts${post_pk}/like/`
        fetch(url)
            .then((response) => {
                img = document.getElementById(post_pk)
                img.setAttribute('src', '/static/img/liked.png');
                $(this).removeClass('unlike').addClass('like')
                return response
            })
    });
})