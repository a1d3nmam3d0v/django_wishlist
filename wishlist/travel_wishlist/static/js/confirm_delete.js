var deleteButtons = document.querySelectorAll('.delete');
deleteButtons.forEach(function (button) {
    button.addEventListener('click', function (ev) {
        // show a confirm dialog
        var okToDelete = confirm('Delete place - Are you sure?');

        // if user presses no, prevent the form submit
        if (!okToDelete) {
            ev.preventDefault(); // prevent the click event propagating
        }
    });
});
