function removeCourse(id){
    $.ajax({
    type: 'DELETE' ,
    url: `/teachers/courses/manage/delete/${id}/`,
    headers: {
        "X-CSRFToken": WindowCSRF,
    },
    success:function(){
    $(`#card-item-${id}`).remove();
    console.log("Success!" +  "and token" + `${WindowCSRF}`);
  }
    });
};





$('form[id="update-course-form"]').submit(function(event) {
  event.preventDefault(); // Prevent the form from being submitted
  console.log("I am Serialize++", $(this).serialize())

  $.ajax({
    url: $(this).attr('action'),
    type: 'POST',
    data: $(this).serialize(),
    success: function(response) {
    console.log("AJAX update succesfully");
    location.reload();

    }
  });
});

