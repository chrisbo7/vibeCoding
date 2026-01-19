from crypto_leverage import calculate_stop_loss, calculate_take_profit

# Test scenario 1
current_price = 45000
stop_loss_pct = 5
sl = calculate_stop_loss(current_price, stop_loss_pct)
print(f"Stop loss: {sl}")
print(f"Expected: {45000 * 0.95}")
print(f"Match: {sl == 45000 * 0.95}")
print()

# Test scenario 2
tp = calculate_take_profit(45000, leverage=10)
print(f"Take profit: {tp}")
print(f"Expected: {45000 * 1.1}")
print(f"Match: {tp == 45000 * 1.1}")
