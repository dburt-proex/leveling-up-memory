from opportunity_engine import load_state, generate_opportunities

def run_loop():
    state = load_state()
    
    options = generate_opportunities(state)
    
    print("\nTOP 3 MOVES:\n")
    for i, opt in enumerate(options):
        print(f"{i+1}. {opt['title']} ({opt['leverage']})")

    choice = int(input("\nSelect option: ")) - 1
    
    selected = options[choice]
    
    print(f"\nExecuting: {selected['title']}")
    
    # Hook into your operator system here
    # execute_task(selected)

if __name__ == "__main__":
    run_loop()
