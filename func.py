import io
import json
import response
import oci

{ "funcMode": "describeFunction"}

funcDefinition = {
    "status": {
        "returnCode": 0,
        "errorMessage": ""
    },
    "funcDescription": {
        "outputs": [
            {"name": "word_count", "dataType": "integer"}
        ],
        "parameters": [
            {"name": "textColumn", "displayName": "Text Column",
             "description": "Choose column to count words", "required": True,
             "value": {"type": "column"}}
        ],
        "bucketName": "bucket-OCI-FAAS",
        "isOutputJoinableWithInput": True
    }
}

def handler(ctx, data: io.BytesIO = None):
    response_data = ""
    try:
        body = json.loads(data.getvalue())
        funcMode = body.get("funcMode")
        if funcMode == 'describeFunction':
           response_data = json.dumps(funcDefinition)
    except (Exception, ValueError) as ex:
        response_data = json.dumps(
            {"error": "{0}".format(str(ex))})
    return response.Response(
        ctx, response_data,
        headers={"Content-Type": "application/json"}
    )

{ "funcMode": "executeFunction"}
	
{
    "args":
    {
        "textColumn": "Ename"
    },
    "funcMode": "executeFunction",
    "input":
    {
        "bucketName": "bucket-OCI-FAAS",
        "fileExtension": ".xlsx",
        "fileName": "Input_Test",
        "method": "xlsx",
        "rowID": "Eno"
    },
    "output":
    {
        "bucketName": "bucket-OCI-FAAS",
        "fileExtension": ".xlsx",
        "fileName": "Output_Test"
    }
}