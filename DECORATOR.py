# Decorator to format the report output
def format_report(func):
    def wrapper(report):
        print("=" * 50)
        print("              REPORT")
        print("=" * 50)
        print(func(report))
        print("=" * 50)

    return wrapper


class Report:
    # Class variable to store available templates
    templates = {
        "simple": "Simple Report",
        "detailed": "Detailed Report",
        "summary": "Summary Report"
    }

    def __init__(self, title, content, template):
        self.title = title
        self.content = content
        self.template = template

    # Magic method
    def __str__(self):
        return (
            f"Title    : {self.title}\n"
            f"Content  : {self.content}\n"
            f"Template : {self.template}"
        )

    # Class method to add a new template
    @classmethod
    def add_template(cls, name, description):
        cls.templates[name] = description

    # Class method to display all templates
    @classmethod
    def show_templates(cls):
        print("Available Report Templates:")
        for name, description in cls.templates.items():
            print(f"{name} : {description}")


# Using the decorator
@format_report
def generate_report(report):
    return str(report)


# Main program
Report.show_templates()

print("\nAdding a new template...\n")

# Add a new template using class method
Report.add_template("professional", "Professional Business Report")

Report.show_templates()

print("\nGenerating Report...\n")

# Create a Report object
report1 = Report(
    "Monthly Sales Report",
    "Sales increased by 20% this month.",
    "Professional Business Report"
)

# Generate and display the report
generate_report(report1)
