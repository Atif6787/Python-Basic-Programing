def retry_pyment():
    max_retry = 3
    retry_count = 0
    while retry_count < max_retry:
        payment_status = input("Enter payment status (success/failure): ")
        if payment_status.lower() == "success":
            print("Payment successful!")
            break
        else:
            retry_count += 1
            print(f"Payment failed. Retry {retry_count}/{max_retry}.")

    if retry_count == max_retry:
        print("Maximum retry limit reached. Payment failed.")
        print("Please contact support for assistance.")

print(retry_pyment())