from pydoc import locate

# Run input via process pipeline.
def process(pipeline, input):
    # For each token in pipeline
    for token in pipeline[::1]:
        # Find the processing class
        processorClass = locate('synopsys.pesti.' + token)
        # Transform the input
        input = processorClass.transform(input)

    # Return the processed input as output.
    return input
