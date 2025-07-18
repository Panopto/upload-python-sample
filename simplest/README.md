# Simplest Panopto upload sample application

## Summary
This sample application demonstrates how you may upload a video file to Panopto by using Panopto Upload API and Panotpo OAuth2 authorization.

## Preparation
1. You need Panopto user account who can create a video on Panopto system. If you don't have it, ask your organization's Panopto administrator.
2. If you do not have Python 3 on your system, install the latest stable version from https://python.org
3. Install external modules for this application.
```
pip install requests oauthlib requests_oauthlib
pip install boto3
```

## Setup API Client on Panopto server
1. Sign in to Panopto web site
2. Click your name in right-upper corner, and clikc "User Settings"
3. Select "API Clients" tab
4. Click "Create new API Client" button
5. Enter arbitrary Client Name
6. Select Server-side Web Application type.
7. Enter ```https://localhost``` into CORS Origin URL.
8. Enter ```http://localhost:9127/redirect``` into Redirect URL.
9. The rest can be blank. Click "Create API Client" button.
10. Note the created Client ID and Client Secret.

### Configure S3 Client for Panopto Uploads
Panopto's upload process involves interacting with an S3-compatible service. To maintain compatibility with this upload flow, the S3 client used in `boto3` must explicitly be set to use the `s3v4` signing protocol. This is a required configuration for correctly uploading to Panopto's S3-compatible upload targets.

This configuration has already been implemented in the provided sample application, specifically in the `panopto_uploader.py` file. However, if you are encountering issues with upload failures, you should ensure that the S3 client is correctly initialized with the `Config(signature_version='s3v4')`.

For example:

s3 = boto3.session.Session().client(
    service_name='s3',
    endpoint_url=service_endpoint,  # Replace with your service endpoint
    verify=self.ssl_verify,        	# SSL verification configuration
    aws_access_key_id='dummy',     	# Dummy credentials
    aws_secret_access_key='dummy', 	# Dummy credentials
    config=boto3.session.Config(signature_version='s3v4')
)

## Determine the target folder ID
1. Navigate to the target folder on Panopto web site
2. Click gear icon at the top-right corner.
3. Select Manage tab
4. Find Folder ID and note it.

## Upload a single file 
Assuming you have test.mp4 in the current directly, type the following command.
```
python upload.py --server your.site.panopto.com --folder-id [Folder ID] --upload-file test.mp4 --client-id [Client ID] --client-secret [Client Secret]
```
You will see the sign-in screen on the browser for the first time. Go through sign in process. Once it's done, the file should be uploaded and the command monitors the progress until server side process is done.

If you run this script for the second time, you do not need to go to sign-in screen because this sample application has saved OAuth2 refresh token in *.cache file.

Type ```python upload.py --help``` for more command line options.

## Notes

### Warning
This sample application intentionally does not include error handling or retry logic in order to focus on the usage of API. As the best practice, you should have both proper error handling and reasonable retry logic in production code.

### Panopto Upload API and S3 Client Configuration
The sample application is already configured to use the `s3v4` signing protocol when interacting with Panopto's upload services (see "### Configure S3 Client for Panopto Uploads" section). If you encounter any issues with upload failures, revisit that section for further details on this configuration.

### Capture traffic
It is useful to capture the actual network traffic by the capture tool, like [Fiddler on Windows](https://www.telerik.com/fiddler) and [Charles on Mac](https://www.charlesproxy.com/), and examine it.

You should pass ```--skip-verify``` option for that purpose, so that the appliation ignore SSL ceritificate replaced by such tool and continue to run.

### UCS XML file
UCS XML file may provide various additional metadata to construct a complicated Panopto video session. You may find the full spec as [XSD file](https://github.com/Panopto/universal-content-library-specification/blob/master/schemas/universal-capture-2.0.xsd). You may modify upload_manifest_template.xml file in this example and experiment how it works.

## References
- Panopto support document: [How to Upload Files Using the API](https://support.panopto.com/s/article/Upload-API)
- Panopto support document: [Create OAuth2 Clients](https://support.panopto.com/s/article/oauth2-client-setup)
- [Universal Content Library specification](https://github.com/Panopto/universal-content-library-specification): UCS XML definition and samples.
- [Requests-OAuthlib](https://requests-oauthlib.readthedocs.io/): Python module to handle OAuth2 workflow on top of [OAuthlib library](https://github.com/oauthlib/oauthlib)
- [Requests](https://2.python-requests.org/): HTTP library for Python
