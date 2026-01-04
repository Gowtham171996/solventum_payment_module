Solventum Utils (UPI Payment Declaration Module)

### Overview
This Frappe/ERPNext application provides a high-reliability UPI payment declaration workflow for the Customer Portal. It is designed to bridge the gap between customer UPI transfers and internal accounting verification by providing a real-time "I Have Paid" signaling mechanism.
Developed for: Solventum OPC Private Limited
Location: Bangalore, KA, India

### Installation
You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app solventum_utils
```

### Quantitative Impact & Logic
Response Time: Reduces internal notification latency from an average of ~4 hours (manual check) to < 30 seconds (automated alert).
Audit Integrity: Utilizes allow_on_submit logic to ensure that payment declarations are logged without compromising the legal "Submitted" state of the Quotation/Order.
Data Accuracy: Captures ISO-8601 timestamps and exact amounts, minimizing reconciliation errors in bank statement matching.

### Features
Portal Integration: Programmatically injects a payment declaration button into the standard ERPNext order.html template via template_overrides.
UI/UX: Premium CSS-animated confirmation area with Glassmorphism styling and auto-refresh logic.
Multi-Channel Alerting: - UI Alert: Immediate confirmation for the customer.
Document Timeline: Persistent server comment added for audit trails.
Email Dispatch: Automated SMTP relay to sales and finance teams.

### Installation
```bash
#Clone the repository:
bench get-app [https://github.com/gowtham171996/solventum_utils.git](https://github.com/gowtham171996/solventum_utils.git)


#Install on site:
bench --site [your-site-name] install-app solventum_utils


#Run Migration & Assets:
bench --site [your-site-name] migrate
bench build --app solventum_utils
```

Technical Configuration

Dependencies: erpnext (v14+)
Hooks: template_overrides for templates/pages/order.html.
Fixtures: - Custom Field: custom_payment_declared (Check) on Quotation.
Notification: Customer Payment Declaration Alert.
Asset Path: /assets/solventum_utils/images/solventum_qr.png

### Operational Support

For technical escalations or feature requests within the Solventum OPC Private Limited ecosystem:
Company: Solventum OPC Private Limited
Email: hello@solventumrnd.com
Primary Operations: Bangalore, Karnataka.

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/solventum_utils
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

MIT License

Copyright (c) 2025-2026 Solventum OPC Private Limited

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
