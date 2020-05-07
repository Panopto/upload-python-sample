# UCS upload applicatoin

## Summary
This sample application demonstrates how you may upload a set of files organized by Universal Capture Specification (UCS) version 2.
Sample contents are included in the sub-directory.

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
9. The rest can be blank. Click Create Key.
10. Note the created Client ID and Client Secret.

## Determine the target folder ID
1. Navigate to the target folder on Panopto web site
2. Click gear icon at the top-right corner.
3. Select Manage tab
4. Find Folder ID and note it.

## Upload UCS content
Following command uploads the sample contents in primary-video-only folder.
```
python upload.py --server your.site.panopto.com --folder-id [Folder ID] --local-folder primary-video-only --client-id [Client ID] --client-secret [Client Secret]
```
Following command uploads the sample contents in primary-secondary-ppt-and-cuts folder.
```
python upload.py --server your.site.panopto.com --folder-id [Folder ID] --local-folder primary-secondary-ppt-and-cuts --client-id [Client ID] --client-secret [Client Secret]
```

Type ```python upload.py --help``` for more command line options.

## Notes

### Usage of upload API
Core part of this application uses the same logic as [the simplest upload sample](../simplest). See that application for technical detail of API usage.

### Warning
This sample application intentionally does not include error handling or retry logic to simplify the sample. As the best practice, you should have both proper error handling and reasonable retry logic in production code.

### Sample videos
The sample videos in this repository are provided by [Pixbay](https;//pixabya.com) under [Pixabay License](https://pixabay.com/service/license/). Panopto thanks the authors of these videos.

## References
- [Universal Content Library specification](https://github.com/Panopto/universal-content-library-specification): UCS XML definition, validation tool, and samples.
