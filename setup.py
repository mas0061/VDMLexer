from setuptools import setup

setup(
        name = "pygments_plugin_vdm_lexer",
        version = "1.0",
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
