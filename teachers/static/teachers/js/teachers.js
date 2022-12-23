function removeCourse(id){
    $.ajax({
    type: 'GET',
    url: `/teachers/courses/manage/delete/${id}/`,
    success:function(remove_course){
    $(`#card-item-${id}`).remove();
  }
    })
};