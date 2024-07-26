import os
from whiskerAPI import whiskerlogic

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

app = whiskerlogic.get_app()

if __name__ == '__main__':
   app.run()
