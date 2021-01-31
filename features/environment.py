from selenium import webdriver

BEHAVE_DEBUG_ON_ERROR = True


def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        # -- ENTER DEBUGGER: Zoom in on failure location.
        # NOTE: Use IPython debugger, same for pdb (basic python debugger).
        import ipdb
        ipdb.post_mortem(step.exc_traceback)


def before_all(context):
    setup_debug_on_error(context.config.userdata)
    options = webdriver.ChromeOptions()
    options.headless = True
    context.driver = webdriver.Chrome(options=options)


def after_all(context):
    context.driver.close()
