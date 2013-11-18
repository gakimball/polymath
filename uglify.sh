#!/bin/bash
cd polymath/static/js/src
uglifyjs jquery-ui-1.10.3.custom.js jquery-scrollto.js history.js ajaxify.js script.js > ../script.min.js