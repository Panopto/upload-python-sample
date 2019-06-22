#!python3
import argparse
from panopto_oauth2 import PanoptoOAuth2
from panopto_uploader import PanoptoUploader
import urllib3

def parse_argument():
    '''
    Argument definition and handling.
    '''
    parser = argparse.ArgumentParser(description='Upload a single video file to Panopto server')
    parser.add_argument('--server', dest='server', required=True, help='Server name as FQDN')
    parser.add_argument('--folder-id', dest='folder_id', required=True, help='ID of target Panopto folder')
    parser.add_argument('--upload-file', dest='upload_file', required=True, help='File to be uploaded')
    parser.add_argument('--client-id', dest='client_id', required=True, help='Client ID of OAuth2 client')
    parser.add_argument('--client-secret', dest='client_secret', required=True, help='Client Secret of OAuth2 client')
    parser.add_argument('--skip-verify', dest='skip_verify', action='store_true', required=False, help='Skip SSL certificate verification. (Never apply to the production code)')
    
    return parser.parse_args()

def main():
    '''
    Main method
    '''
    args = parse_argument()

    if args.skip_verify:
        # This line is needed to suppress annoying warning message.
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    oauth2 = PanoptoOAuth2(args.server, args.client_id, args.client_secret, not args.skip_verify)

    uploader = PanoptoUploader(args.server, not args.skip_verify, oauth2)
    uploader.upload_video(args.upload_file, args.folder_id)

if __name__ == '__main__':
    main()
