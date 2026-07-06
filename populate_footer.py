import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pindhni.settings')
django.setup()

from api.models import FooterSection, SocialLink, FooterMenu, FooterMenuItem

def populate_footer():
    print('Populating footer data...')
    # Clear all existing footer data
    FooterMenuItem.objects.all().delete()
    FooterMenu.objects.all().delete()
    SocialLink.objects.all().delete()
    FooterSection.objects.all().delete()

    # --- Section 1: Main Content ---
    footer_section = FooterSection.objects.create(
        newsletter_text="Perks include <strong>10% off</strong> your first online order. Be the first to know about new collections, store launches, sales, and much more!",
        copyright_line_1="© Pindhni •",
        copyright_line_2="Designed by Biz499 Marketing Agency"
    )

    SocialLink.objects.create(footer_section=footer_section, icon='Camera', link='https://instagram.com', order=1)
    SocialLink.objects.create(footer_section=footer_section, icon='Music', link='https://tiktok.com', order=2)
    SocialLink.objects.create(footer_section=footer_section, icon='MessageCircle', link='https://whatsapp.com', order=3)

    # --- Section 2: Menus ---
    
    # Menu 1: Our Policies
    policies_menu = FooterMenu.objects.create(title="Our Policies", order=1)
    policies_items = ["Search", "Privacy Policy", "Terms of Service", "Refund Policy"]
    for i, item in enumerate(policies_items):
        FooterMenuItem.objects.create(menu=policies_menu, title=item, link=f"/{item.lower().replace(' ', '-')}", order=i+1)

    # Menu 2: Quick Links
    quick_links_menu = FooterMenu.objects.create(title="Quick Links", order=2)
    quick_links_items = ["Home page", "About", "Contact", "Partners"]
    for i, item in enumerate(quick_links_items):
        FooterMenuItem.objects.create(menu=quick_links_menu, title=item, link=f"/{item.lower().replace(' ', '-')}", order=i+1)

    # Menu 3: Shop By Collection
    collections_menu = FooterMenu.objects.create(title="Shop By Collection", order=3)
    collections_items = ["Pindhni Women", "Pindhni Blings", "Pindhni Strings", "Pindhni Sole", "Pindhni Home"]
    for i, item in enumerate(collections_items):
        FooterMenuItem.objects.create(menu=collections_menu, title=item, link=f"/collections/{item.lower().replace(' ', '-')}", order=i+1)

    print('Successfully populated footer data.')

if __name__ == '__main__':
    populate_footer()
