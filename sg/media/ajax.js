function comboDependiente(idComboPadre, idComboHijo, UrlPeticionAjax) {
  /*se establece el evento onchange del combo padre*/
  $('#'+idComboPadre).on('change', function() {
  	/*se obtiene el valor actual del select id del combo padre*/
  	var valor_combo_padre = this.value;
    /*se desactiva el combo padre para evitar request constantes*/
  	$('#'+idComboPadre).attr('disabled', true);
  	/*peticion http*/
  		$.ajax({
  			data: {'id':valor_combo_padre},
  			url: UrlPeticionAjax,
  			type: 'get',
  			success: function(datos_json){
  				var html = ""
          /*se verifica si la respuesta posee al menos 1 objeto*/
          if(datos_json.length > 0){
    				for (var i = 0 ; i<datos_json.length; i++) {
    					html += '<option value='+datos_json[i].pk+'>'+datos_json[i].fields.nombre+'</option>'
    				}
            $('#'+idComboHijo).attr('disabled', false);
          }else{
            /*caso de que no se encontraran objetos para el combo hijo*/
            html='<option value="">-------------</option>'
            $('#'+idComboHijo).attr('disabled', true);
          }
  				$('#'+idComboHijo).html(html);
  				$('#'+idComboPadre).attr('disabled', false);
  			},
        /*en caso de tener algun error con la peticion al servidor*/
  			error: function (codigo, opcionesAjax, error){
  				if(codigo.status==404){
  					$('#'+idComboHijo).html('<option value="">-------------</option>');
  					$('#'+idComboHijo).attr('disabled', true);
  					alert('[ERROR]: '+codigo.status+' - URL no existe');
  				}
  				$('#'+idComboPadre).attr('disabled', false);
  			}
  		});
  });
}