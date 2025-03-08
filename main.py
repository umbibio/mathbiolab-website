import os

def define_env(env):
    """Define custom macros for MkDocs."""
    
    @env.macro
    def get_research_images():
        image_folder = "docs/assets/research_images"
        try:
            images = sorted(
                [f for f in os.listdir(image_folder) if f.endswith((".png", ".jpg", ".jpeg"))]
            )
            html_content = ""
            for image in images:
                html_content += f"""
                <div class="swiper-slide">
                    <img src="/assets/research_images/{image}" />
                </div>
                """
            return html_content
        except FileNotFoundError:
            return "<p>No research images found.</p>"
