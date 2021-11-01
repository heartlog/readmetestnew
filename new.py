if __name__ == "__main__":
    readme = root / "README.md"
    
    rewritten = "Problem with the extra spaces and then send you the"
    
    readme.open("w").write(rewritten)
