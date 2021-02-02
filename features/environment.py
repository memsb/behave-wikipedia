import os
import shutil

from behave.model_core import Status
from selenium import webdriver

BEHAVE_DEBUG_ON_ERROR = True
SCREENSHOT_FOLDER = 'screenshots'


def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


def before_all(context):
    setup_debug_on_error(context.config.userdata)
    options = webdriver.ChromeOptions()
    options.headless = True
    context.driver = webdriver.Chrome(options=options)
    empty_screenshots_folder(SCREENSHOT_FOLDER)


def empty_screenshots_folder(folder):
    if os.path.exists(folder):
        shutil.rmtree(folder)
    os.makedirs(folder)


def after_step(context, step):
    if step.status == Status.failed:
        destination_path = f"{SCREENSHOT_FOLDER}/{context.scenario.name}"
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)
        context.driver.save_screenshot(f"{destination_path}/{step.name}.png")

    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        # -- ENTER DEBUGGER: Zoom in on failure location.
        # NOTE: Use IPython debugger, same for pdb (basic python debugger).
        import ipdb
        ipdb.post_mortem(step.exc_traceback)


def after_all(context):
    context.driver.close()
