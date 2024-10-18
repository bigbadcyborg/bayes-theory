def bayes_rule(prior_A, prob_B_given_A, prob_B):
    return (prob_B_given_A * prior_A) / prob_B

def main():
    print("Bayes Rule Probability Calculator")

    # User inputs
    event_A = input("Enter the name of event A: ")
    event_B = input("Enter the name of event B: ")
    prior_A = float(input(f"Enter the prior probability P({event_A}): "))
    prob_B_given_A = float(input(f"Enter the conditional probability P({event_B}|{event_A}): "))
    prob_B = float(input(f"Enter the marginal probability P({event_B}): "))

    # Calculate the posterior probability using Bayes' rule
    posterior_A_given_B = bayes_rule(prior_A, prob_B_given_A, prob_B)

    print(f"The probability of {event_A} given {event_B} (P({event_A}|{event_B})) is: {posterior_A_given_B:.4f}")

if __name__ == "__main__":
    main()
