function getCookieValue(cookieName) {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.indexOf(cookieName + '=') !== -1) {
        return cookie.substring(cookie.indexOf('=') + 1);
      }
    }
    return null;
  }
  
  function form_errors(data){
      var htmlContent = '<ul>';
      for(const [key_name, msg] of Object.entries(data)){
        var inputElement = document.querySelector('input[name="' + key_name + '"]');
        var inputId = inputElement.id;
        var labelElement = document.querySelector('label[for="' + inputId + '"]');
        var labelText = labelElement.textContent;
        htmlContent += '<li>' + labelText + ' - ' + msg + '</li>';
      }
      htmlContent += '</ul>';
      return htmlContent;
    }
  
  async function do_request(url, method, params = {}, csrf_token = "") {
      $(".has-danger").removeClass("has-danger");
      $(".pristine-error").remove();
      let result;
      var csrf = getCookieValue('csrftoken');
      params["csrfmiddlewaretoken"] = csrf;
      try{
        Pace.restart(100);
        result = await $.ajax({
          type: method,
          url: url,
          data: params,
        });
        Pace.stop();
        return result;
      } catch (error){
        Pace.stop();
        return false;
      }
    }