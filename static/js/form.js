$(function () {

      $("#addProcess").bind("click", function () {

            $.getJSON($SCRIPT_ROOT + "/add_process", {

              firstName: $('input[name="firstName"]').val(),
              lastName: $('input[name="lastName"]').val()



            },
            function (data) {

             console.log(data)


            });
            return false;



                                     });
      $("#getProcess").bind("click", function () {
        $.getJSON($SCRIPT_ROOT + "/get_process",
            function (data) {

            $(data).each(function (i,full) {
                  $("#result").append(`<tr><td>` + full.id + `</td><td>` +
                      full.firstName + `</td><td>`+ full.lastName + `</td></tr>`)

                         })

            });

                                     })


  });
