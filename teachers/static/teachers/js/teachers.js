function removeCourse(id){
    $.ajax({
    type: 'post' ,
    url: `/teachers/courses/manage/delete/${id}/`,
    data: {
        csrfmiddlewaretoken: WindowCSRF
    },
    success:function(){
    $(`#card-item-${id}`).remove();
    console.log("Success!" +  "and token" + `${WindowCSRF}`);
  }
    });
};





$('form[id="update-course-form"]').submit(function(event) {
  event.preventDefault(); // Prevent the form from being submitted

  $.ajax({
    url: $(this).attr('action'),
    type: 'POST',
    data: $(this).serialize(),
    success: function(response) {
    console.log("AJAX update succesfully");

    }
  });
});

