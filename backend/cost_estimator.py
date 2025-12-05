def estimate_monthly_cost(
    users=100,
    rewrites_per_user=3,
    input_tokens_per_request=2500,
    output_tokens_per_request=2500,
    price_input_per_million=30.0,
    price_output_per_million=60.0,
):
    """
    Estimate API costs for JobPilot.

    Returns:
        total_cost_usd
    """

    total_requests = users * rewrites_per_user

    total_input_tokens = total_requests * input_tokens_per_request
    total_output_tokens = total_requests * output_tokens_per_request

    cost_input = (total_input_tokens / 1_000_000) * price_input_per_million
    cost_output = (total_output_tokens / 1_000_000) * price_output_per_million

    total_cost = cost_input + cost_output

    return round(total_cost, 2)


# Example usage:
if __name__ == "__main__":
    cost = estimate_monthly_cost(
        users=100,
        rewrites_per_user=3,
        input_tokens_per_request=2500,
        output_tokens_per_request=2500,
    )
    print(f"Estimated monthly cost: ${cost}")
