import streamlit as st

# Function to generate the blog post
def generate_blog_post():
    title = "Why Top Companies Rely on Linux: Power, Performance, and Freedom"
    intro = (
        "Linux has become the backbone of modern computing infrastructure. "
        "From tech giants to financial institutions, companies across industries are leveraging Linux "
        "for its stability, scalability, and open-source flexibility. In this post, we explore some of the "
        "leading companies using Linux and the reasons behind their choice."
    )

    companies = [
        {
            "name": "Google",
            "reason": "Google’s massive infrastructure runs on a customized version of Linux called gLinux.",
            "benefits": [
                "High scalability for data centers",
                "Customizability for internal tools",
                "Cost-effective and open-source"
            ]
        },
        {
            "name": "Amazon (AWS)",
            "reason": "AWS offers Amazon Linux as a secure, stable, and high-performance execution environment.",
            "benefits": [
                "Optimized for cloud workloads",
                "Security and performance tuning",
                "Deep integration with AWS services"
            ]
        },
        {
            "name": "Facebook (Meta)",
            "reason": "Facebook uses Linux to power its servers and internal development environments.",
            "benefits": [
                "Efficient resource management",
                "Ability to modify the kernel for performance",
                "Strong community and internal support"
            ]
        },
        {
            "name": "NASA",
            "reason": "NASA uses Linux for mission-critical systems, including the International Space Station.",
            "benefits": [
                "Reliability in extreme environments",
                "Open-source transparency",
                "Long-term support and customization"
            ]
        },
        {
            "name": "Netflix",
            "reason": "Netflix uses Linux to run its content delivery network (CDN) and backend services.",
            "benefits": [
                "High throughput and low latency",
                "Efficient streaming infrastructure",
                "Robust monitoring and debugging tools"
            ]
        }
    ]

    conclusion = (
        "Linux continues to be the operating system of choice for companies that demand performance, "
        "security, and flexibility. Its open-source nature empowers organizations to innovate without "
        "vendor lock-in, making it a cornerstone of modern enterprise computing."
    )

    blog = f"# {title}\n\n{intro}\n\n"
    for company in companies:
        blog += f"## {company['name']}\n"
        blog += f"**Why they use Linux:** {company['reason']}\n\n"
        blog += "**Benefits:**\n"
        for benefit in company["benefits"]:
            blog += f"- {benefit}\n"
        blog += "\n"
    blog += f"### Conclusion\n{conclusion}"
    return blog

# Streamlit UI
st.set_page_config(page_title="Linux Blog Generator", layout="centered")
st.title("📝 Linux Blog Post Generator")
st.write("Click the button below to generate a blog post about companies using Linux.")

if st.button("Generate Blog Post"):
    blog_content = generate_blog_post()
    st.markdown(blog_content)

    # Option to download the blog post
    st.download_button(
        label="📥 Download as Markdown",
        data=blog_content,
        file_name="linux_blog_post.md",
        mime="text/markdown"
    )
