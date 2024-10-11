tickets = {}
# Opening a new customer ticket
def openTicket(customer_name):
    problem_description = input(f"\nPlease give details regarding what {customer_name} is having issues with: ")
    ticket_id = len(tickets) + 1
    tickets[ticket_id] = {
        "customer_name": customer_name,
        "problem_description": problem_description,
        "status": "open"
    }
    print(f'Ticket {ticket_id} opened for {customer_name}.')

# Updating ticket status
def updateTicket(ticket_id, status):
    if ticket_id in tickets:
        tickets[ticket_id]["status"] = status
        print(f"\nTicket {ticket_id} updated to {status}")
    else:
        print(f'Ticket {ticket_id} not found.')

# Display or filter tickets
def see_or_filter():
    filter_question = input("\nDo you want to see 'open' tickets or 'closed' tickets? If you want to see all, enter 'both': ")
    for ticket_id, ticket in tickets.items():
        if filter_question.lower() == "open":
            if ticket['status'] == "open":
                print(f"\nTicket ID: {ticket_id}")
                print(f"Customer Name: {ticket['customer_name']}")
                print(f"Problem Description: {ticket['problem_description']}")
                print(f"Status: {ticket['status']}")

        elif filter_question.lower() == "closed":
            if ticket['status'] == "closed":
                print(f"\nTicket ID: {ticket_id}")
                print(f"Customer Name: {ticket['customer_name']}")
                print(f"Problem Description: {ticket['problem_description']}")
                print(f"Status: {ticket['status']}")

        elif filter_question.lower() == "both":
            print(f"\nTicket ID: {ticket_id}")
            print(f"Customer Name: {ticket['customer_name']}")
            print(f"Problem Description: {ticket['problem_description']}")
            print(f"Status: {ticket['status']}")

        else:
            print("Sorry, that is not a valid option.")