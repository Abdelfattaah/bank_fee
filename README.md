## Job Application Assessment - Odoo Payment Handling with Bank Fee

### Description

This Odoo module extends the `account.payment` model to handle bank fees associated with payments. The module introduces the `bank_fee` field to capture the bank's fee and a `fee_included` selection to determine whether the fee is included or excluded from the payment amount. Based on the user's choice, it appropriately adjusts the journal entries to account for the bank fee in either scenario.

### (30 seconds) Demo video:

[Here](https://youtu.be/YenTcnSwLeE)

### The implementation was done on **Odoo 16** as I didn't have access to Odoo 15 Enterprise Edition at the time of the assessment.

### If I Had More Time

If I had more time, I would have focused on the following areas to further enhance the module:

- **Validation of Account Selection**: Currently, the `account_id` for the bank fee is hardcoded. A future improvement could be to dynamically select the correct account based on configuration or payment type.
- **Error Handling**: Adding more robust error handling and logging can help debug and ensure smooth operation in production environments.
- **Testing and Coverage**: Include comprehensive unit tests and ensure complete coverage for different scenarios, such as multiple payments or varying payment methods or editing an exsisting payment.
