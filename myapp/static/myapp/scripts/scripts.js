$("#id_category").change(function () {
    var url = $("#createItemForm").attr("data-sub_category-url");  
    var categoryId = $(this).val();  

    $.ajax({                       
    url: url,                    
    data: {
        'category': categoryId      
    },
    success: function (data) {   
        $("#id_sub_category").html(data);  
    }
    });

});


