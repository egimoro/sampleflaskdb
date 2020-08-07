$(function () {
  $("#flask").submit( function (e) {
  
      e.preventDefault(e);

      var formData = {firstName: $("#firstName").val(),
      lastName: $("#lastName").val() }

      $.ajax({
          url: "/process",
          type: "POST",
          data: formData,
          success: function (data) {
                      console.log(data);
                      alert("Entry added!");

                   },
          error: function (errorThrown) {
                        console.log(errorThrown);

                 }

      });
      
      
});
  $("#getprocess").on("click", function () {
           
            $.ajax({
                
                url: "/process",
                type: "GET",
                success: function (data) {
                        
                        
                      var fullName = $("#output tbody");
                      
                      fullName.empty();
                      $(data).each(function (index, full) {
                      
                          fullName.append( `<tr><td>` + full.id +`</td><td>`
                            + full.firstName + `</td><td>` +
                           full.lastName + `</td></tr>`
                          )
                               
                             });
                        
                                        
                           
                         },
                         
                         error: function (errorThrown) {
                         
                                  alert(errorThrown);
                                }
                         
                         
            
            });
            
            
            
                           
                         });
  
  
  });
