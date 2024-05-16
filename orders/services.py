
class ScreenshotService:
    @staticmethod
    def capture_screenshot_script(element_id):
        return f"""
        html2canvas(document.getElementById('{element_id}')).then(function(canvas) {{
            var a = document.createElement('a');
            a.href = canvas.toDataURL('image/png');
            a.download = 'screenshot.png';
            a.click();
        }});
        """

