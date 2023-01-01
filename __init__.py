import json


def send_keys_coordinates(driver, x, y, text):
    # https://stackoverflow.com/a/73339766/15096247
    try:
        text = json.dumps(str(text).encode("utf-8").decode("utf-8"), ensure_ascii=True)
    except Exception as fda:
        print(fda)

    texttowrite = text.strip('"')
    resas = driver.execute_script(fr"""

    var theButton = document.elementFromPoint({x}, {y});

    DoCustomEvent(`{texttowrite}`, theButton);



    function DoCustomEvent(ct, elem){{
    var key;
    var pressEvent = document.createEvent("CustomEvent");
    pressEvent.initCustomEvent("keypress", true, false);

    for (var i =0; i < ct.length; ++i)
    {{
        key                     = ct.charCodeAt(i);
        pressEvent.bubbles      = true;
        pressEvent.cancelBubble = false;
        pressEvent.returnValue  = true;
        pressEvent.key          = ct.charAt(i);
        pressEvent.keyCode      = key;
        pressEvent.which        = key;
        pressEvent.charCode     = key;
        pressEvent.shiftKey     = false;
        pressEvent.ctrlKey      = false;
        pressEvent.metaKey      = false;

        elem.focus;

        //keypress //beforeinput //input //sendkeys //select
        setTimeout(function() {{
            var e = new window.KeyboardEvent('keypress', pressEvent);
            document.activeElement.dispatchEvent(e);
            e = new window.KeyboardEvent('input', pressEvent);
            document.activeElement.dispatchEvent(e);

        }}, 0);

        elem.value = elem.value + ct.charAt(i);
    }}}};return theButton;""", )
    print(resas, type(resas))
    return resas