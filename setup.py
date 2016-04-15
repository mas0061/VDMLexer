from setuptools import setup

setup(
        name = "pygments_plugin_vdm_lexer",
        version = "1.0",
        author = "mas0061",
        author_email = "github@mas0061.net",
        description = "Pygments lexer for VDM",
        license = "MIT",
        keywords = "pygments lexer vdm",
        url = "https://github.com/mas0061/VDMLexer",
        package_dir = {"pygments_plugin": "", 
                       "pygments_plugin.lexers": "lexers",
                       "pygments_plugin.styles": "styles"},
        packages = ["pygments_plugin",
                    "pygments_plugin.lexers",
                    "pygments_plugin.styles"],
        entry_points = """ 
        [pygments.lexers]
        vdmlexer = pygments_plugin.lexers.vdm:VDMLexer
        [pygments.styles]
        vdmstyle = pygments_plugin.styles.colorful:ColorfulStyle
        """
     ) 
