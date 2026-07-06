import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pindhni.settings')
django.setup()

from api.models import Policy

def populate_policies():
    print('Populating policy data...')
    # Clear all existing policy data
    Policy.objects.all().delete()

    # Define standard policies with HTML content
    policies = [
        {
            "title": "Privacy Policy",
            "policy": """
                <p>At Pindhni, we respect your privacy and are committed to protecting your personal data. This Privacy Policy describes how we collect, use, and share your personal information when you visit our website, browse our catalog, save items in your wishlist, or purchase premium apparel.</p>
                
                <h3 style="margin-top: 1.5rem; margin-bottom: 0.5rem; font-weight: bold;">1. Information We Collect</h3>
                <p>We collect information that you provide directly to us when using our services. This includes contact information (name, email, phone, addresses) and order details.</p>
                
                <h3 style="margin-top: 1.5rem; margin-bottom: 0.5rem; font-weight: bold;">2. How We Use Your Data</h3>
                <p>We utilize the collected information to deliver a premium fashion shopping experience, including processing orders, notifying you of updates, and maintaining your active wishlist sessions.</p>
                
                <h3 style="margin-top: 1.5rem; margin-bottom: 0.5rem; font-weight: bold;">3. Contact Information</h3>
                <p>If you have any questions or concerns regarding this Privacy Policy, please feel free to reach out to our support team at privacy@pindhni.com.</p>
            """
        },
        {
            "title": "Terms of Service",
            "policy": """
                <p>By accessing, browsing, or using the Pindhni website, you acknowledge that you have read, understood, and agree to be bound by these Terms of Service. If you do not agree to these terms, please discontinue using this site.</p>
                
                <h3 style="margin-top: 1.5rem; margin-bottom: 0.5rem; font-weight: bold;">1. User Eligibility and Accounts</h3>
                <p>You must be at least 18 years old, or accessing the site under the supervision of a parent or guardian, to place orders.</p>
                
                <h3 style="margin-top: 1.5rem; margin-bottom: 0.5rem; font-weight: bold;">2. Products, Customizations, and Pricing</h3>
                <p>We strive to display our premium collection, garment details, colors, and textures as accurately as possible. Pindhni reserves the right to modify prices or catalog stock availability at any time without notice.</p>
                
                <h3 style="margin-top: 1.5rem; margin-bottom: 0.5rem; font-weight: bold;">3. Governing Law</h3>
                <p>These Terms of Service are governed by and construed in accordance with local regulations, without regard to conflict of law principles.</p>
            """
        },
        {
            "title": "Refund Policy",
            "policy": """
                <p>We want you to love your Pindhni garments. If you are not completely satisfied with your purchase, we accept returns and exchange requests within <strong>15 days</strong> of the delivery date.</p>
                
                <h3 style="margin-top: 1.5rem; margin-bottom: 0.5rem; font-weight: bold;">1. Return Eligibility Criteria</h3>
                <p>To qualify for a refund or size exchange, the items must be unworn, unwashed, and undamaged, with all original tags attached and packaging preserved.</p>
                
                <h3 style="margin-top: 1.5rem; margin-bottom: 0.5rem; font-weight: bold;">2. Refund Inspection Process</h3>
                <p>Once your returned package is received at our facility, it will undergo an inspection process. Approved refunds will be applied to your original payment method within 7 to 10 business days.</p>
            """
        }
    ]

    for p in policies:
        policy_obj = Policy.objects.create(
            title=p["title"],
            policy=p["policy"]
        )
        print(f"Successfully created policy: {policy_obj.title} (/{policy_obj.slug})")

    print('Successfully populated policy data.')

if __name__ == '__main__':
    populate_policies()
