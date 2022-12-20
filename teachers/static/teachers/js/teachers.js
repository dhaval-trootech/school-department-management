const element = document.getElementById("");

$(document).ready(function(){
  $("#delete-course-1").click(function() {
        $.get("{% url 'course_delete' 7 %}", function(){
        });
  });



});