function main() {
    $('button').on('click', function () {
        $('.blue').toggleClass('changed');
    });
}

$(document).ready(main);