from models import lstm_bidirectional
from helpers import checkpoint

# Get the review summary file
review_summary_file = 'extracted_data/review_summary.csv'

# Initialize Checkpointer to ensure checkpointing
checkpointer = checkpoint.Checkpointer('bidirectional','lstm','Attention')
checkpointer.steps_per_checkpoint(500)

# Do using GRU cell - without attention mechanism
out_file = 'result/bidirectional/lstm/attention.csv'
lstm_net = lstm_bidirectional.NeuralNet(review_summary_file, checkpointer,attention=True)
lstm_net.set_parameters(batch_size=15, memory_dim=15,learning_rate=0.05)
lstm_net.begin_session()
lstm_net.form_model_graph()
lstm_net.fit()
lstm_net.predict()
lstm_net.store_test_predictions(out_file)
lstm_net.close_session()
