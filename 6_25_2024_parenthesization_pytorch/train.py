import torch
def train_one_epoch(training_loader, model, loss_fn, optimizer):
    """
    Trains the model for one epoch using the given training data loader, model, loss function, and optimizer.
    
    Args:
        training_loader (torch.utils.data.DataLoader): The data loader for the training data.
        model (torch.nn.Module): The model to be trained.
        loss_fn (torch.nn.loss._Loss): The loss function used to compute the loss.
        optimizer (torch.optim.Optimizer): The optimizer used to update the model parameters.
        
    Returns:
        float: The total loss computed over the entire epoch.
    """
    running_loss = 0.
    last_loss = 0.

    # Here, we use enumerate(training_loader) instead of
    # iter(training_loader) so that we can track the batch
    # index and do some intra-epoch reporting
    for i, data in enumerate(training_loader):
        # Every data instance is an input + label pair
        inputs, labels = data

        # Zero your gradients for every batch!
        optimizer.zero_grad()

        # Make predictions for this batch
        outputs = model(inputs)

        # Compute the loss and its gradients
        loss = loss_fn(outputs, labels)
        loss.backward()

        # Adjust learning weights
        optimizer.step()

        # Gather data and report
        running_loss += loss.item()
        if i % 27 == 26:
            last_loss = running_loss / 1000 # loss per batch
            print('  batch {} loss: {}'.format(i + 1, last_loss))
            running_loss = 0.

    return last_loss

def evaluate_model(model, test_dataset):
    """
    Evaluates the model using the provided test dataset and returns the confusion matrix.

    Args:
        model (torch.nn.Module): The model to be evaluated.
        test_dataset (torch.utils.data.Dataset): The dataset used for evaluation.

    Returns:
        list: A 2x2 confusion matrix where rows represent true labels and columns represent predicted labels.
    """
    model.eval()

    with torch.no_grad():
        confusion_matrix = [[0, 0], [0, 0]]
        for data in test_dataset:
            inputs, labels = data
            outputs = model(inputs)
            prob = torch.nn.functional.softmax(outputs)
            _, predicted = torch.max(prob, dim=0)
            confusion_matrix[labels][predicted] += 1

        return confusion_matrix
